import time
from IPython import get_ipython
from io import StringIO
from IPython.core.magic import Magics, magics_class, line_cell_magic
from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring
import subprocess
import urllib.parse
import re
import sys
import pandas as pd
from pathlib import Path
import re
from typing import List, Tuple
from .exceptions import SQLExecutionError




def handle_sql_error(error_output: str, sql_script: str, model_name: str = "Unknown") -> SQLExecutionError:
    """Factory function to create appropriate SQL error instance"""
    print(SQLExecutionError(error_output, model_name, sql_script))
    raise 

# Global directory for caching session output
CACHE_DIR = Path(Path.home(), "sqlcmd_magic_cache")
CACHE_DIR.mkdir(parents=True, exist_ok=True)

def format_sql_output(stdout):
    """
    Format SQL output dynamically by reading columns as fixed-width with width=1 and eliminating unnecessary columns.

    Args:
        stdout (str): The raw SQL command output (from result.stdout).

    Returns:
        str: Formatted table as a string.
    """
    start_time = time.time()
    if not stdout.splitlines():
        return stdout
    longest_line = max(stdout.splitlines(), key=len)

    df = pd.read_fwf(StringIO(stdout), widths=[1] * len(longest_line), header=None, dtype=str)

    columns_to_remove = []
    for column in df.columns:
        column_data = df[column].fillna(" ").astype(str).str.strip()
        if (column_data == "-").sum() == 1 and (column_data.isin(["", "-"]).all()):
            columns_to_remove.append(column)

    cleaned_df = df.drop(columns=columns_to_remove, errors='ignore')
    cleaned_df = cleaned_df.fillna(" ").astype(str)
    cleaned_output = "\n".join(cleaned_df.apply(lambda row: "".join(row), axis=1))

    print(f"SQL output formatting completed in {time.time() - start_time:.2f} seconds")
    return cleaned_output


@magics_class
class SQLCmdMagic(Magics):
    def __init__(self, shell):
        super().__init__(shell)
        self.connection_string = None
        self.sqlcmd_connection_info = None

    def grant_file_permissions(self, file_path: Path):
        """Grants the SQL database permission to execute the script, in case the user is not logged in
        with the Windows user
        """
        file_path = str(file_path)
        commands = [
            fr'$folder = "{file_path}"',
            r'$acl = Get-Acl $folder',
            r'$sqlServiceAccount = "NT Service\MSSQLSERVER"',
            r'$accessRule = New-Object System.Security.AccessControl.FileSystemAccessRule($sqlServiceAccount, "Read", "Allow")',
            r'$acl.SetAccessRule($accessRule)',
            r'Set-Acl $folder $acl'
        ]
        powershell_command = "; ".join(commands)
        result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-Command", powershell_command], capture_output=True, text=True)

        print("Error:", result.stderr) if result.returncode != 0 else None


    def resolve_sql_file(self, sql_content: str) -> str:
        """
        Resolves EXECUTE_SQL_FILE commands by replacing them with the actual file contents.
        """
        pattern = r"EXECUTE_SQL_FILE\s+'([^']+)'|EXECUTE_SQL_FILE\s+\"([^\"]+)\""
        
        def create_command(file_path: str) -> str:
            resolved_path = file_path

            return (f"PRINT 'executing script at {resolved_path}';"
                    f"EXEC xp_cmdshell '{self.get_sqlcmd_command(resolved_path)}'")
        
        def wrap_content_for_config(sql_content: str):
            enable_xp_cmdshell = """
            PRINT '/*'
            EXEC sp_configure 'show advanced options', 1;
            RECONFIGURE;
            EXEC sp_configure 'xp_cmdshell', 1;
            RECONFIGURE;
            PRINT '*/'
            GO
            """

            disable_xp_cmdshell = """
            PRINT '/*'
            EXEC sp_configure 'show advanced options', 1;
            RECONFIGURE;
            EXEC sp_configure 'xp_cmdshell', 0;
            RECONFIGURE;
            PRINT '*/'
            GO
            """

            # Construct the full SQL content
            sql_content = f"""
            {enable_xp_cmdshell}
            {sql_content}
            GO
            {disable_xp_cmdshell}
            """
            return sql_content
        
        while True:
            match = re.search(pattern, sql_content)
            if not match:
                break
            
            full_match = match.group(0)
            file_path = match.group(1) or match.group(2)
            file_path = Path(file_path)
            file_path = (Path(Path.cwd(), file_path) if not file_path.is_absolute() else file_path)
            if not file_path.exists():
                raise FileNotFoundError(f"The file {str(file_path)} was not found!")
            self.grant_file_permissions(file_path)
            file_content = create_command(file_path)
            sql_content = sql_content.replace(full_match, file_content)
            sql_content = wrap_content_for_config(sql_content)
        
        return sql_content
    
    def substitute_variables(self, query):
        variable_pattern = re.compile(r"\$(\w+)")
        
        def replace_variable(match):
            var_name = match.group(1) 
            ipy = get_ipython()
            value = ipy.user_ns.get(var_name, None) 
            if value is None:
                raise ValueError(f"Variable '{var_name}' is not defined.")
            return str(value)  
        
        return variable_pattern.sub(replace_variable, query)


    def transform_sql(self, sql_content: str) -> str:
        """Main transformation function."""
        sql_content = sql_content.replace('%%sqlcmd', '').strip()
        sql_content = self.resolve_sql_file(sql_content)

        return sql_content.replace("GO", "")
    
    def get_sqlcmd_command(self, file_path: str):
        server = self.sqlcmd_connection_info["server"]
        database = self.sqlcmd_connection_info["database"]
        username = self.sqlcmd_connection_info["username"]
        password = self.sqlcmd_connection_info["password"]
        file_path = f'"{str(file_path)}"'
        return f"sqlcmd -S {server} -d {database} -U {username} -P {password} -b -i {file_path} -f 65001 -r 1 -W"

    @line_cell_magic
    @magic_arguments()
    @argument('connection', nargs='?', help='Connection string')
    @argument('--debug', action='store_true', help='Enable debug mode to print verbose output')
    def sqlcmd(self, line, cell=None):
        """Magic that works as both line and cell magic"""
        args = parse_argstring(self.sqlcmd, line) if line else None

        debug = getattr(args, "debug", False)

        if cell is None:
            if not args or not args.connection:
                print("Error: Connection string is empty.")
                return

            self.connection_string = args.connection.strip("'")
            print(f"Connection string set: {self.connection_string}")

            try:
                if "mssql+sqlcmd:///?odbc_connect=" in self.connection_string:
                    odbc_connect_part = urllib.parse.unquote(self.connection_string.split("odbc_connect=")[1])
                    params = dict(item.split("=") for item in odbc_connect_part.split(";") if "=" in item)
                    self.sqlcmd_connection_info = {
                        "server": params.get("SERVER", "localhost"),
                        "database": params.get("DATABASE", "master"),
                        "username": params.get("UID", ""),
                        "password": params.get("PWD", ""),
                    }
                    print(f"Parsed sqlcmd connection info: {self.sqlcmd_connection_info}")
                else:
                    print("Error: Invalid connection string format. Use 'mssql+sqlcmd:///?odbc_connect=...'")
            except Exception as e:
                print(f"Error parsing connection string: {e}")
        else:
            if not self.sqlcmd_connection_info:
                print("Error: No connection information provided. Use %sqlcmd to set the connection string.")
                return

            start_time = time.time()
            modified_content = self.substitute_variables(cell)
            modified_content = self.transform_sql(modified_content)

            # Split the SQL content into batches based on GO statements
            batches = split_sql_batches(modified_content)
            
            # Create a temporary directory for batch files
            temp_dir = CACHE_DIR / f"sql_batches_{int(time.time())}"
            temp_dir.mkdir(exist_ok=True)
            
            total_exec_duration = 0
            
            try:
                for i, batch in enumerate(batches):
                    if not batch.strip():  # Skip empty batches
                        continue
                        
                    batch_file = temp_dir / f"batch_{i}.sql"
                    with open(batch_file, 'w') as f:
                        f.write(batch)

                    if debug:
                        print(f"\nExecuting query {i+1}/{len(batches)}:")
                        print(f"Query file: {batch_file}")
                        print("SQL content:")
                        formatted_sql = "\n".join(f" |{line}" for line in batch.splitlines())
                        print(formatted_sql)

                    exec_start_time = time.time()
                    command = self.get_sqlcmd_command(batch_file)

                    print_flag = True
                    error_print_flag = True
                    print(command) if debug else None

                    with subprocess.Popen(
                        command, 
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE, 
                        text=True, 
                        encoding="latin-1",
                    ) as proc:

                        print(f"Command executed: {command}") if debug else None
                        
                        # Process stdout and stderr live
                        # TODO! might block
                        for line in proc.stdout:
                            out = line.strip()
                            if out == "/*":
                                print_flag = False
                            print(out) if print_flag else None
                            if out == "*/": 
                                print_flag = True
                        for error_line in proc.stderr:
                            out = error_line.strip()
                            if out == "/*":
                                error_print_flag = False
                            print(out, error_line.strip(), file=sys.stderr) if error_print_flag else None
                            if out == "*/": 
                                error_print_flag = True

                        proc.wait() 
                        exec_duration = time.time() - exec_start_time
                        total_exec_duration += exec_duration

                        if proc.returncode == 0:
                            if len(batches) == 1:
                                print(f"Command executed successfully in {exec_duration:.2f} seconds.")
                            else:
                                print(f"Batch {i+1} executed successfully in {exec_duration:.2f} seconds.")
                        else:
                            handle_sql_error(
                                error_output="See stderr above for error details.",
                                sql_script=batch,
                                model_name=f"Batch {i+1}"
                            )

            except Exception as e:
                print(f"Failed to execute SQL command: {e}")
                raise e
            finally:
                # Clean up batch files if not in debug mode
                if not debug:
                    for file in temp_dir.glob("*.sql"):
                        file.unlink()
                    temp_dir.rmdir()
                else:
                    print(f"\nBatch files preserved in: {temp_dir}")

            print(f"\nTotal execution time: {time.time() - start_time:.2f} seconds")
            print(f"SQL execution time: {total_exec_duration:.2f} seconds")

def split_sql_batches(sql_content):
    """Split SQL content into batches based on GO statements."""
    # Use regex to split on GO statements while preserving the original formatting
    batches = re.split(r'\bGO\b', sql_content, flags=re.IGNORECASE)
    
    # Remove empty batches and trim whitespace
    batches = [batch.strip() for batch in batches if batch.strip()]
    
    return batches


# Load the magic into the IPython environment
ip = get_ipython()
ip.register_magics(SQLCmdMagic)