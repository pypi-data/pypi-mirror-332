from IPython.core.magic import Magics, magics_class, line_cell_magic
from IPython.core.magic_arguments import magic_arguments, argument, parse_argstring
from IPython import get_ipython

from .connection import SQLConnection
from .parser import SQLParser
from .executor import SQLExecutor

@magics_class
class SQLCmdMagic(Magics):
    """IPython magic for SQLCMD execution."""
    
    def __init__(self, shell):
        super().__init__(shell)
        self.connection = SQLConnection()
        self.parser = SQLParser(self.connection)
        self.executor = SQLExecutor(self.connection, self.parser)

    @line_cell_magic
    @magic_arguments()
    @argument('connection', nargs='?', help='Connection string')
    @argument('--debug', action='store_true', help='Enable debug mode to print verbose output')
    def sqlcmd(self, line, cell=None):
        """
        Magic that works as both line and cell magic.
        
        Usage as line magic:
            %sqlcmd connection_string
            
        Usage as cell magic:
            %%sqlcmd [--debug]
            SQL code here
        """
        args = parse_argstring(self.sqlcmd, line) if line else None
        debug = getattr(args, "debug", False) if args else False

        if cell is None:
            # Line magic mode - set connection string
            if not args or not args.connection:
                print("Error: Connection string is empty.")
                return

            success = self.connection.set_connection_string(args.connection)
            if success:
                print(f"Connection string set: {self.connection.connection_string}")
                print(f"Parsed sqlcmd connection info: {self.connection.connection_info}")
            else:
                print("Error: Invalid connection string format. Use 'mssql+sqlcmd:///?odbc_connect=...'")
        else:
            # Cell magic mode - execute SQL
            if not self.connection.connection_info:
                print("Error: No connection information provided. Use %sqlcmd to set the connection string.")
                return
            
            self.executor.execute_sql(cell, debug)


def load_ipython_extension(ipython):
    """
    Load the extension in IPython.
    """
    ipython.register_magics(SQLCmdMagic)