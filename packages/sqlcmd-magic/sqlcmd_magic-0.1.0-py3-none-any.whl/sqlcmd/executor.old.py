import subprocess
import sys
import time
from pathlib import Path
from typing import List, Optional

from .exceptions import SQLExecutionError
from .parser import handle_sql_error, split_sql_batches

# Global directory for caching session output
CACHE_DIR = Path(Path.home(), "sqlcmd_magic_cache")
CACHE_DIR.mkdir(parents=True, exist_ok=True)

class SQLExecutor:
    """Class to handle SQL execution."""
    
    def __init__(self, connection, parser):
        self.connection = connection
        self.parser = parser
    
    def execute_sql(self, sql_content: str, debug: bool = False) -> None:
        """
        Execute SQL content.
        
        Args:
            sql_content: SQL script content
            debug: Whether to enable debug mode
        """
        start_time = time.time()
        modified_content = self.parser.substitute_variables(sql_content)
        modified_content = self.parser.transform_sql(modified_content)

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
                command = self.connection.get_sqlcmd_command(batch_file)

                print_flag = True
                error_print_flag = True
                if debug:
                    print(command)

                with subprocess.Popen(
                    command, 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.PIPE, 
                    text=True, 
                    encoding="latin-1",
                ) as proc:

                    if debug:
                        print(f"Command executed: {command}")
                    
                    # Process stdout and stderr live
                    for line in proc.stdout:
                        out = line.strip()
                        if out == "/*":
                            print_flag = False
                        if print_flag:
                            print(out)
                        if out == "*/": 
                            print_flag = True
                    for error_line in proc.stderr:
                        out = error_line.strip()
                        if out == "/*":
                            error_print_flag = False
                        if error_print_flag:
                            print(out, file=sys.stderr)
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