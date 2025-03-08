import pytest
from unittest.mock import patch, MagicMock
from pathlib import Path
import pandas as pd
import pyarrow as pa
from feather_df_cli.cli import main

@pytest.fixture
def sample_df():
    """Create a sample DataFrame for testing."""
    return pd.DataFrame({
        'id': range(1, 6),
        'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'age': [25, 30, 35, 40, 45]
    })

@pytest.fixture
def feather_file(tmp_path, sample_df):
    """Create a temporary feather file for testing."""
    file_path = tmp_path / 'test.feather'
    sample_df.to_feather(str(file_path))
    return file_path

def test_display_metadata(feather_file, capsys):
    """Test displaying file metadata."""
    with patch('sys.argv', ['feather_cli', str(feather_file)]):
        main()
    captured = capsys.readouterr()
    assert 'Number of rows: 5' in captured.out
    assert 'Number of columns: 3' in captured.out

def test_view_schema(feather_file, capsys):
    """Test viewing schema information."""
    with patch('sys.argv', ['feather_cli', str(feather_file), '--schema']):
        main()
    captured = capsys.readouterr()
    assert 'id' in captured.out
    assert 'name' in captured.out
    assert 'age' in captured.out

def test_count_records(feather_file, capsys):
    """Test counting total records."""
    with patch('sys.argv', ['feather_cli', str(feather_file), '--count']):
        main()
    captured = capsys.readouterr()
    assert 'Total records: 5' in captured.out

def test_head_display(feather_file, capsys):
    """Test displaying first N rows."""
    with patch('sys.argv', ['feather_cli', str(feather_file), '--head', '3']):
        main()
    captured = capsys.readouterr()
    assert 'Alice' in captured.out
    assert 'Bob' in captured.out
    assert 'Charlie' in captured.out
    assert 'Eve' not in captured.out

def test_tail_display(feather_file, capsys):
    """Test displaying last N rows."""
    with patch('sys.argv', ['feather_cli', str(feather_file), '--tail', '2']):
        main()
    captured = capsys.readouterr()
    assert 'David' in captured.out
    assert 'Eve' in captured.out
    assert 'Alice' not in captured.out

def test_invalid_file():
    """Test handling of invalid file path."""
    with pytest.raises(SystemExit):
        with patch('sys.argv', ['feather_cli', 'nonexistent.feather']):
            main()

def test_format_options(feather_file, capsys):
    """Test different output format options."""
    formats = ['table', 'markdown', 'csv']
    for fmt in formats:
        with patch('sys.argv', ['feather_cli', str(feather_file), '--head', '1', '--format', fmt]):
            main()
        captured = capsys.readouterr()
        assert captured.out.strip() != ''
        if fmt == 'csv':
            assert ',' in captured.out
        elif fmt == 'markdown':
            assert '|' in captured.out