# Feather DataFrame CLI

A command-line interface tool for reading and displaying Feather data format files. This tool provides easy access to view and analyze data stored in the Feather format, which is a fast and efficient file format for storing DataFrames.

## Features

- Display file metadata (number of rows, columns, etc.)
- View schema information
- Count total records
- View data with customizable output formats (table, markdown, csv)
- Support for viewing both head and tail of the data

## Installation

You can install the package using pip:

```bash
pip install feather-df-cli
```

## Usage

After installation, you can use the `feather-cli` command to interact with Feather files:

### Display Metadata
```bash
feather-cli <input_file>
```

### View Schema
```bash
feather-cli <input_file> --schema
```

### Count Records
```bash
feather-cli <input_file> --count
```

### View First N Rows
```bash
feather-cli <input_file> --head N --format [table|markdown|csv]
```

### View Last N Rows
```bash
feather-cli <input_file> --tail N --format [table|markdown|csv]
```

## Development

### Prerequisites

- Python 3.6 or higher
- pip

### Setting up Development Environment

1. Clone the repository:
```bash
git clone https://github.com/villadora/feather-df-cli.git
cd feather-df-cli
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
```

3. Install development dependencies:
```bash
pip install -r requirements.txt
```

### Building from Source

To build the package:

```bash
python setup.py build
```

To install in development mode:

```bash
pip install -e .
```

## License

This project is licensed under the MIT License.

### Running Tests

The project uses pytest for testing. To run the tests:

1. Make sure you have installed development dependencies:
```bash
pip install -r requirements.txt
```

2. Run the tests:
```bash
pytest
```

Test options are configured in `pytest.ini`:
- Tests are located in the `tests` directory
- Test files must match `test_*.py`
- Test classes must match `Test*`
- Test functions must match `test_*`
- Verbose output and short traceback are enabled by default

To run specific tests:
```bash
pytest tests/test_cli.py  # Run tests in a specific file
pytest tests/test_cli.py::test_view_schema  # Run a specific test function
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
