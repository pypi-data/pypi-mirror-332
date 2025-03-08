import sys
import argparse
from typing import Optional, List

import pyarrow.feather as feather
from tabulate import tabulate
from feather_df_cli import __version__

def read_metadata(file_path: str) -> None:
    """Display metadata information about a Feather file.

    This function reads a Feather file and displays its basic metadata including
    the number of columns, number of rows, and schema information for each field.

    Args:
        file_path (str): Path to the Feather file to read

    Raises:
        FileNotFoundError: If the specified file does not exist
        Exception: If there is an error reading the file
    """
    try:
        table = feather.read_table(file_path)
        schema = table.schema
        print(f"Number of columns: {len(schema)}")
        print(f"Number of rows: {table.num_rows}")
        print("\nSchema:")
        for field in schema:
            print(f"{field.name}: {field.type}")
    except Exception as e:
        print(f"Error reading metadata: {str(e)}", file=sys.stderr)
        sys.exit(1)

def read_schema(file_path: str) -> None:
    """Display the schema of a Feather file.

    This function reads a Feather file and displays its schema information,
    showing the name and data type of each field in the file.

    Args:
        file_path (str): Path to the Feather file to read

    Raises:
        FileNotFoundError: If the specified file does not exist
        Exception: If there is an error reading the file
    """
    try:
        table = feather.read_table(file_path)
        schema = table.schema
        for field in schema:
            print(f"{field.name}: {field.type}")
    except Exception as e:
        print(f"Error reading schema: {str(e)}", file=sys.stderr)
        sys.exit(1)

def count_records(file_path: str) -> None:
    """Count the total number of records in a Feather file.

    This function reads a Feather file and displays the total number of rows
    contained in the file.

    Args:
        file_path (str): Path to the Feather file to read

    Raises:
        FileNotFoundError: If the specified file does not exist
        Exception: If there is an error reading the file
    """
    try:
        table = feather.read_table(file_path)
        print(f"Total records: {table.num_rows}")
    except Exception as e:
        print(f"Error counting records: {str(e)}", file=sys.stderr)
        sys.exit(1)

def format_data(data: List[List], headers: List[str], format_type: str) -> str:
    """Format tabular data into a string representation.

    This function takes a list of data rows and headers and formats them according
    to the specified format type (csv, table, or markdown).

    Args:
        data (List[List]): List of rows, where each row is a list of values
        headers (List[str]): List of column headers
        format_type (str): Output format ('csv', 'table', or 'markdown')

    Returns:
        str: Formatted string representation of the data
    """
    if format_type == 'csv':
        result = ','.join(headers) + '\n'
        result += '\n'.join(','.join(str(cell) for cell in row) for row in data)
        return result
    else:
        tablefmt = 'grid' if format_type == 'table' else 'pipe'
        return tabulate(data, headers=headers, tablefmt=tablefmt)

def display_data(file_path: str, n: int, format_type: str = 'table', tail: bool = False) -> None:
    """Display a subset of rows from a Feather file.

    This function reads a Feather file and displays either the first or last N rows
    of data in the specified format.

    Args:
        file_path (str): Path to the Feather file to read
        n (int): Number of rows to display
        format_type (str, optional): Output format ('table', 'markdown', or 'csv'). Defaults to 'table'
        tail (bool, optional): If True, display last N rows; if False, display first N rows. Defaults to False

    Raises:
        FileNotFoundError: If the specified file does not exist
        Exception: If there is an error reading or displaying the file
    """
    try:
        table = feather.read_table(file_path)
        headers = [field.name for field in table.schema]
        
        if tail:
            data = table.slice(max(0, table.num_rows - n)).to_pylist()
        else:
            data = table.slice(0, n).to_pylist()
            
        # Convert data to list of lists for tabulate
        rows = [[row.get(col) for col in headers] for row in data]
        print(format_data(rows, headers, format_type))
    except Exception as e:
        print(f"Error displaying data: {str(e)}", file=sys.stderr)
        sys.exit(1)

def main() -> None:
    """Main entry point for the Feather DataFrame CLI tool.

    This function parses command line arguments and executes the appropriate
    function based on the provided arguments. It supports displaying metadata,
    schema information, record counts, and viewing data in various formats.

    Command line arguments:
        file: Input Feather file path
        --schema: Display schema information
        --count: Display total number of records
        --head N: Display first N rows
        --tail N: Display last N rows
        --format {table,markdown,csv}: Output format for data display
    """
    parser = argparse.ArgumentParser(description='CLI tool for reading and displaying Feather data format files')
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
    parser.add_argument('file', help='Path to the Feather file')
    parser.add_argument('--schema', action='store_true', help='Display schema information')
    parser.add_argument('--count', action='store_true', help='Display total number of records')
    parser.add_argument('--head', type=int, help='Display first N rows')
    parser.add_argument('--tail', type=int, help='Display last N rows')
    parser.add_argument('--format', choices=['table', 'markdown', 'csv'], default='table',
                        help='Output format (default: table)')

    args = parser.parse_args()

    try:
        if args.schema:
            read_schema(args.file)
        elif args.count:
            count_records(args.file)
        elif args.head is not None:
            display_data(args.file, args.head, args.format)
        elif args.tail is not None:
            display_data(args.file, args.tail, args.format, tail=True)
        else:
            read_metadata(args.file)
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()