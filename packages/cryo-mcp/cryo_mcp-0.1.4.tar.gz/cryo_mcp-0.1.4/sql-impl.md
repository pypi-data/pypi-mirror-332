### I want to add some functionality to this repository, mainly adding the ability for running SQL queries against downloaded data using duckdb to run queries backed by parquet files. Help me plan the implementation of this


# SQL Query Functionality with DuckDB

DuckDB provides a powerful way to analyze blockchain data using SQL against parquet files.

## Implementation Details

### Table Resolution and Multi-File Handling

When executing SQL queries, there are two main ways to reference tables:

1. **Simple table names** (e.g., `SELECT * FROM blocks`): 
   - The system automatically maps table names to parquet files that include that name in the filename.
   - If multiple matching files are found, they are combined using a `UNION ALL` operation.
   - This is the recommended approach for simplicity.

2. **Direct file references** (e.g., `SELECT * FROM '/path/to/file.parquet'`):
   - You can directly reference a specific file by its path.
   - This allows more precise control over which files are being queried.

#### Multi-file Handling

When using simple table names and multiple matching files are found, the implementation:

1. Creates a temporary view that combines all matching files using `UNION ALL`
2. This effectively joins all rows from all matching files into a single virtual table
3. The query is then executed against this combined view

For example, with files:
- `/data/ethereum__blocks__1000_to_2000.parquet`
- `/data/ethereum__blocks__2001_to_3000.parquet`

A query like `SELECT * FROM blocks` will:
1. Find both matching files
2. Create a view: `CREATE VIEW blocks AS SELECT * FROM '/data/ethereum__blocks__1000_to_2000.parquet' UNION ALL SELECT * FROM '/data/ethereum__blocks__2001_to_3000.parquet'`
3. Execute the query against this combined view

#### File Matching Logic

Files are matched to table names using the following priority:

1. **Exact dataset name match**: Files with pattern `__tablename__` (e.g., `ethereum__blocks__`)
2. **Word boundary match**: Files with pattern `_tablename_` or `/tablename.`

This ensures that queries like `SELECT * FROM blocks` match files like `ethereum__blocks__1000_to_2000.parquet` but avoid false matches.

### Response Details

When SQL queries are executed, the response includes information about how files were used:

```json
{
  "success": true,
  "result": [...],
  "row_count": 123,
  "schema": {...},
  "files_used": [...],
  "used_direct_references": true,
  "table_mappings": {
    "blocks": {
      "files": ["/path/to/file1.parquet", "/path/to/file2.parquet"],
      "combined": true
    }
  }
}
```

The `table_mappings` field shows which files were used for each table name and whether they were combined.

### 2. Create a New Module for SQL Functionality

Create a new file `cryo_mcp/sql.py` to contain the SQL query functionality:

```python
"""SQL query functionality for Cryo MCP using DuckDB."""
import os
import json
from pathlib import Path
import duckdb
from typing import Dict, Any, List, Optional

# Default SQL query timeout in seconds
DEFAULT_QUERY_TIMEOUT = 30

def get_data_directory() -> Path:
    """Get the data directory where Cryo files are stored."""
    default_data_dir = str(Path.home() / ".cryo-mcp" / "data")
    return Path(os.environ.get("CRYO_DATA_DIR", default_data_dir))

def create_connection(read_only: bool = True) -> duckdb.DuckDBPyConnection:
    """Create a DuckDB connection with appropriate settings."""
    conn = duckdb.connect(database=":memory:", read_only=read_only)
    
    # Configure DuckDB settings as needed
    conn.execute("SET memory_limit='4GB'")
    conn.execute(f"SET max_expression_depth=10000")
    conn.execute(f"SET max_query_time={DEFAULT_QUERY_TIMEOUT}")
    
    return conn

def list_available_tables() -> List[Dict[str, Any]]:
    """List all available tables from downloaded data files."""
    data_dir = get_data_directory()
    
    # Find all parquet files in the data directory
    parquet_files = list(data_dir.glob("**/*.parquet"))
    
    tables = []
    for file_path in parquet_files:
        # Extract dataset name from filename
        name = file_path.stem.split("__")[0]
        
        # Get file stats
        stats = file_path.stat()
        
        tables.append({
            "name": name,
            "path": str(file_path),
            "size_bytes": stats.st_size,
            "modified": stats.st_mtime
        })
    
    return tables

def execute_sql_query(
    query: str,
    include_schema: bool = True
) -> Dict[str, Any]:
    """
    Execute a SQL query against downloaded Cryo data files.
    
    Args:
        query: SQL query to execute
        include_schema: Whether to include schema information in the result
        
    Returns:
        Dictionary with query results and metadata
    """
    data_dir = get_data_directory()
    conn = create_connection()
    
    try:
        # Register all parquet files as tables
        parquet_files = list(data_dir.glob("**/*.parquet"))
        for file_path in parquet_files:
            # Extract dataset name from filename for table name
            table_name = file_path.stem.split("__")[0]
            conn.execute(f"CREATE VIEW {table_name} AS SELECT * FROM read_parquet('{file_path}')")
        
        # Execute the query
        result = conn.execute(query).fetchdf()
        
        # Convert to records format for easier JSON serialization
        records = result.to_dict(orient="records")
        
        # Get schema information if requested
        schema_info = None
        if include_schema and not result.empty:
            schema_info = {
                "columns": list(result.columns),
                "dtypes": {col: str(dtype) for col, dtype in result.dtypes.items()}
            }
        
        return {
            "success": True,
            "result": records,
            "row_count": len(records),
            "schema": schema_info
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
    finally:
        conn.close()
```

### 3. Add MCP Tools in server.py

Add new tool functions to expose the SQL functionality through the MCP interface:

```python
@mcp.tool()
def query_sql(
    query: str,
    include_schema: bool = True
) -> Dict[str, Any]:
    """
    Run a SQL query against downloaded blockchain data
    
    Args:
        query: SQL query to execute
        include_schema: Whether to include schema information in the result
        
    Returns:
        Query results and metadata
    """
    from cryo_mcp.sql import execute_sql_query
    return execute_sql_query(query, include_schema)

@mcp.tool()
def list_available_sql_tables() -> List[Dict[str, Any]]:
    """
    List all available tables that can be queried with SQL
    
    Returns:
        List of available tables and their metadata
    """
    from cryo_mcp.sql import list_available_tables
    return list_available_tables()

@mcp.tool()
def get_sql_table_schema(table_name: str) -> Dict[str, Any]:
    """
    Get the schema for a specific table
    
    Args:
        table_name: Name of the table to get schema for
        
    Returns:
        Table schema information
    """
    from cryo_mcp.sql import create_connection
    
    try:
        conn = create_connection()
        # Find the parquet file for the table
        data_dir = Path(os.environ.get("CRYO_DATA_DIR", DEFAULT_DATA_DIR))
        parquet_files = list(data_dir.glob(f"**/{table_name}*.parquet"))
        
        if not parquet_files:
            return {"error": f"No parquet file found for table '{table_name}'"}
        
        # Use the first matching file
        file_path = parquet_files[0]
        
        # Register the table
        conn.execute(f"CREATE VIEW temp_view AS SELECT * FROM read_parquet('{file_path}')")
        
        # Get schema info
        schema_result = conn.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name='temp_view'").fetchdf()
        
        # Get sample data
        sample_data = conn.execute("SELECT * FROM temp_view LIMIT 5").fetchdf()
        
        return {
            "table_name": table_name,
            "file_path": str(file_path),
            "columns": schema_result.to_dict(orient="records"),
            "sample_data": sample_data.to_dict(orient="records")
        }
    except Exception as e:
        return {"error": str(e)}
    finally:
        conn.close()
```

### 4. Update Query Dataset to Support Parquet Output

Ensure the `query_dataset` function can output parquet files for SQL queries:

```python
# In query_dataset, ensure parquet output is supported
if output_format == "json":
    cmd.append("--json")
elif output_format == "csv":
    cmd.append("--csv")
```

### 5. Add SQL Examples and Documentation

Add some example SQL queries and documentation to help users:

```python
@mcp.tool()
def get_sql_examples() -> Dict[str, List[str]]:
    """
    Get example SQL queries for different blockchain datasets
    
    Returns:
        Dictionary of example queries categorized by dataset type
    """
    return {
        "transactions": [
            "SELECT * FROM transactions LIMIT 10",
            "SELECT block_number, COUNT(*) as tx_count FROM transactions GROUP BY block_number ORDER BY tx_count DESC LIMIT 10",
            "SELECT from_address, COUNT(*) as sent_count FROM transactions GROUP BY from_address ORDER BY sent_count DESC LIMIT 10",
            "SELECT to_address, SUM(value) as total_eth FROM transactions GROUP BY to_address ORDER BY total_eth DESC LIMIT 10"
        ],
        "blocks": [
            "SELECT * FROM blocks LIMIT 10",
            "SELECT block_number, gas_used, transaction_count FROM blocks ORDER BY gas_used DESC LIMIT 10",
            "SELECT AVG(gas_used) as avg_gas, AVG(transaction_count) as avg_txs FROM blocks"
        ],
        "logs": [
            "SELECT * FROM logs LIMIT 10",
            "SELECT address, COUNT(*) as event_count FROM logs GROUP BY address ORDER BY event_count DESC LIMIT 10",
            "SELECT topic0, COUNT(*) as event_count FROM logs GROUP BY topic0 ORDER BY event_count DESC LIMIT 10"
        ],
        "joins": [
            "SELECT t.block_number, COUNT(*) as tx_count, b.gas_used FROM transactions t JOIN blocks b ON t.block_number = b.block_number GROUP BY t.block_number, b.gas_used ORDER BY tx_count DESC LIMIT 10",
            "SELECT l.block_number, l.address, COUNT(*) as log_count FROM logs l GROUP BY l.block_number, l.address ORDER BY log_count DESC LIMIT 10"
        ]
    }
```

### 6. Add Test Cases

Create test files to verify the SQL functionality:

```python
# test_sql.py
#!/usr/bin/env python3
import os
from pathlib import Path
from cryo_mcp.sql import execute_sql_query, list_available_tables, create_connection

def test_sql_functionality():
    """Test the SQL query functionality"""
    print("\n=== Testing SQL Functionality ===")
    
    # First, ensure we have some data
    # This would typically be done by running a query_dataset first
    
    # List available tables
    tables = list_available_tables()
    print(f"Available tables: {tables}")
    
    if not tables:
        print("No tables available for testing. Download some data first.")
        return False
    
    # Execute a simple query
    table_name = tables[0]["name"]
    query = f"SELECT * FROM {table_name} LIMIT 5"
    
    print(f"Running query: {query}")
    result = execute_sql_query(query)
    
    if not result.get("success", False):
        print(f"Query failed: {result.get('error')}")
        return False
    
    print(f"Query returned {result.get('row_count')} rows")
    print(f"First row: {result.get('result')[0] if result.get('result') else 'No data'}")
    
    # Test schema information
    if "schema" in result:
        print(f"Schema columns: {result['schema']['columns']}")
    
    return True

if __name__ == "__main__":
    test_sql_functionality()
```

### 7. Update Requirements and Documentation

Ensure you update your requirements file to include the new dependencies:

```
duckdb>=0.9.2
```

And update your README to document the new SQL functionality.

## Implementation Considerations

1. **Data Format**: For SQL queries to work effectively, you should encourage users to output data in parquet format which is more efficient for SQL queries than JSON or CSV.

2. **Memory Management**: DuckDB runs in-memory, so for large datasets, you might need to configure memory limits or implement pagination.

3. **Table Naming**: Consider how to handle table naming when multiple files for the same dataset exist. You might need to include block ranges in table names.

4. **Query Timeout**: Implement timeouts for queries to prevent hanging the service.

5. **Error Handling**: Provide clear error messages when queries fail, especially for large or complex queries.

Would you like me to implement any specific part of this plan in more detail?

### would the flow then be to do a query that downloads data, and then a separate one for running sql against it? what if we could combine these steps?



# Integrated Query and SQL Execution Flow

That's an excellent point! We can definitely streamline the process by combining the data download and SQL query steps into a single operation. This would provide a much better user experience. Let's design an integrated approach:

## Integrated Query and SQL Flow

Here's how we can implement an integrated flow that:
1. Downloads the necessary data if it doesn't exist
2. Runs SQL queries directly against it
3. Optionally caches the data for future queries

### 1. Create a Combined Function

```python
@mcp.tool()
def query_blockchain_sql(
    sql_query: str,
    dataset: Optional[str] = None,
    blocks: Optional[str] = None,
    start_block: Optional[int] = None,
    end_block: Optional[int] = None,
    use_latest: bool = False,
    blocks_from_latest: Optional[int] = None,
    contract: Optional[str] = None,
    force_refresh: bool = False,
    include_schema: bool = True
) -> Dict[str, Any]:
    """
    Query blockchain data using SQL, automatically downloading any required data
    
    Args:
        sql_query: SQL query to execute
        dataset: The specific dataset to query (e.g., 'transactions', 'logs')
                 If None, will be extracted from the SQL query
        blocks: Block range specification as a string (e.g., '1000:1010')
        start_block: Start block number (alternative to blocks)
        end_block: End block number (alternative to blocks)
        use_latest: If True, query the latest block
        blocks_from_latest: Number of blocks before the latest to include
        contract: Contract address to filter by
        force_refresh: Force download of new data even if it exists
        include_schema: Include schema information in the result
        
    Returns:
        SQL query results and metadata
    """
    from cryo_mcp.sql import execute_sql_query, list_available_tables
    
    # 1. Parse the SQL query to identify datasets if not specified
    if dataset is None:
        dataset = extract_dataset_from_sql(sql_query)
        if dataset is None:
            return {
                "success": False,
                "error": "Could not determine dataset from SQL query. Please specify dataset parameter."
            }
    
    # 2. Determine if we need to download data
    data_dir = Path(os.environ.get("CRYO_DATA_DIR", DEFAULT_DATA_DIR))
    tables = list_available_tables()
    
    # Check if we have matching data already
    need_download = True
    block_range_str = ""
    
    if not force_refresh:
        if blocks:
            block_range_str = blocks
        elif start_block is not None and end_block is not None:
            block_range_str = f"{start_block}:{end_block+1}"
        
        # Look for existing data that matches our criteria
        for table in tables:
            if table["name"] == dataset:
                # Check if block range matches (if specified)
                if block_range_str and block_range_str in table["path"]:
                    need_download = False
                    break
                # If using latest, check if we have latest data
                elif (use_latest or blocks_from_latest is not None) and "latest" in table["path"]:
                    need_download = False
                    break
    
    # 3. Download data if needed
    if need_download:
        print(f"Downloading {dataset} data for SQL query...")
        download_result = query_dataset(
            dataset=dataset,
            blocks=blocks,
            start_block=start_block,
            end_block=end_block,
            use_latest=use_latest,
            blocks_from_latest=blocks_from_latest,
            contract=contract,
            output_format="parquet"  # Always use parquet for SQL
        )
        
        if "error" in download_result:
            return {
                "success": False,
                "error": f"Failed to download data: {download_result['error']}"
            }
        
        print(f"Downloaded data: {download_result}")
    else:
        print(f"Using existing {dataset} data for SQL query")
    
    # 4. Execute the SQL query
    result = execute_sql_query(sql_query, include_schema)
    
    # 5. Add download info to result
    if need_download:
        result["data_download"] = {
            "performed": True,
            "dataset": dataset,
            "block_range": block_range_str if block_range_str else "latest blocks"
        }
    else:
        result["data_download"] = {
            "performed": False,
            "used_existing": True
        }
    
    return result

def extract_dataset_from_sql(sql_query: str) -> Optional[str]:
    """
    Try to extract the dataset name from an SQL query.
    
    This is a simple heuristic that looks for FROM clauses in the query.
    
    Args:
        sql_query: The SQL query to parse
        
    Returns:
        The extracted dataset name or None if it couldn't be determined
    """
    import re
    
    # Simple regex to find table names after FROM or JOIN
    # This won't handle all SQL syntax but works for basic queries
    matches = re.findall(r'(?:FROM|JOIN)\s+([a-zA-Z_][a-zA-Z0-9_]*)', sql_query, re.IGNORECASE)
    
    if matches:
        # Return the first match that isn't a common SQL keyword
        for match in matches:
            if match.lower() not in ('where', 'select', 'group', 'order', 'having', 'limit', 'offset'):
                return match
    
    return None
```

### 2. Enhance the SQL Module

Update the SQL module to better support the integrated flow:

```python
def get_matching_parquet_files(
    dataset: str, 
    block_range: Optional[str] = None,
    latest: bool = False
) -> List[Path]:
    """
    Find parquet files matching the given dataset and block range criteria.
    
    Args:
        dataset: The dataset name to look for
        block_range: The block range string (e.g., '1000:1010')
        latest: Whether to look for the latest data
        
    Returns:
        List of matching parquet file paths
    """
    data_dir = get_data_directory()
    
    if latest:
        # Look in the latest directory first
        latest_dir = data_dir / "latest"
        if latest_dir.exists():
            latest_files = list(latest_dir.glob(f"*{dataset}*.parquet"))
            if latest_files:
                return latest_files
    
    # If block range is provided, look for files matching that range
    if block_range:
        # Try to find exact match
        block_files = list(data_dir.glob(f"*{dataset}*{block_range}*.parquet"))
        if block_files:
            return block_files
        
        # Otherwise parse block range and look for files that contain any portion of it
        try:
            start, end = map(int, block_range.split(':'))
            matching_files = []
            
            for file_path in data_dir.glob(f"*{dataset}*.parquet"):
                # Try to extract block range from filename
                file_blocks = re.search(r'blocks_(\d+)_to_(\d+)', file_path.stem)
                if file_blocks:
                    file_start = int(file_blocks.group(1))
                    file_end = int(file_blocks.group(2))
                    
                    # Check if file contains any part of the requested range
                    if (file_start <= start <= file_end) or (file_start <= end <= file_end) or (start <= file_start and end >= file_end):
                        matching_files.append(file_path)
            
            if matching_files:
                return matching_files
        except (ValueError, IndexError):
            pass
    
    # Fallback to any file for this dataset
    return list(data_dir.glob(f"*{dataset}*.parquet"))
```

### 3. Add a Function to Help with Complex Queries

For situations where users need to query across multiple datasets, we can add a helper function:

```python
@mcp.tool()
def query_multiple_datasets_sql(
    sql_query: str,
    datasets: List[str],
    blocks: Optional[str] = None,
    use_latest: bool = False,
    blocks_from_latest: Optional[int] = None,
    force_refresh: bool = False
) -> Dict[str, Any]:
    """
    Run an SQL query that combines multiple datasets, downloading them if needed
    
    Args:
        sql_query: SQL query to execute
        datasets: List of datasets needed for the query (e.g., ['transactions', 'logs'])
        blocks: Block range specification as a string (e.g., '1000:1010')
        use_latest: If True, query the latest block
        blocks_from_latest: Number of blocks before the latest to include
        force_refresh: Force download of new data even if it exists
        
    Returns:
        SQL query results and metadata
    """
    # Download each dataset if needed
    download_results = {}
    for dataset in datasets:
        download_result = query_dataset(
            dataset=dataset,
            blocks=blocks,
            use_latest=use_latest,
            blocks_from_latest=blocks_from_latest,
            output_format="parquet"
        )
        download_results[dataset] = download_result
        
        if "error" in download_result:
            return {
                "success": False,
                "error": f"Failed to download dataset '{dataset}': {download_result['error']}",
                "download_results": download_results
            }
    
    # Execute the SQL query now that all data is downloaded
    from cryo_mcp.sql import execute_sql_query
    result = execute_sql_query(sql_query)
    
    # Add download info
    result["downloads"] = download_results
    
    return result
```

### 4. Add Convenience Function for Common Query Patterns

Let's add some convenience functions for common query patterns:

```python
@mcp.tool()
def summarize_blocks(
    blocks: Optional[str] = None,
    use_latest: bool = False,
    blocks_from_latest: Optional[int] = None
) -> Dict[str, Any]:
    """
    Get a summary of blocks including transaction counts, gas stats, etc.
    
    Args:
        blocks: Block range specification as a string (e.g., '1000:1010')
        use_latest: If True, summarize the latest block
        blocks_from_latest: Number of blocks before the latest to include
        
    Returns:
        Summary statistics about the blocks
    """
    sql_query = """
    SELECT 
        COUNT(*) as block_count,
        MIN(block_number) as min_block,
        MAX(block_number) as max_block,
        AVG(transaction_count) as avg_txs_per_block,
        MAX(transaction_count) as max_txs,
        AVG(gas_used) as avg_gas_used,
        SUM(gas_used) as total_gas_used,
        AVG(gas_limit) as avg_gas_limit,
        AVG(timestamp) as avg_timestamp
    FROM blocks
    """
    
    return query_blockchain_sql(
        sql_query=sql_query,
        dataset="blocks",
        blocks=blocks,
        use_latest=use_latest,
        blocks_from_latest=blocks_from_latest
    )
```

## Example User Flows

With this integrated approach, users can have several convenient workflows:

### Basic Flow - Direct SQL Query:

```python
result = query_blockchain_sql(
    sql_query="SELECT * FROM transactions WHERE value > 1000000000000000000 LIMIT 10",
    blocks="15000000:15000100"
)
```

This will:
1. Download transaction data for blocks 15000000-15000100 if not already available
2. Run the SQL query against the downloaded data
3. Return the results

### Advanced Analytics Flow:

```python
# Get stats on top gas consumers
result = query_blockchain_sql(
    sql_query="""
    SELECT 
        to_address as contract, 
        COUNT(*) as tx_count,
        AVG(gas_used) as avg_gas,
        SUM(gas_used) as total_gas
    FROM transactions 
    GROUP BY to_address
    ORDER BY total_gas DESC
    LIMIT 20
    """,
    blocks_from_latest=1000
)
```

### Multi-Dataset Query Flow:

```python
result = query_multiple_datasets_sql(
    sql_query="""
    SELECT 
        t.block_number,
        t.transaction_hash,
        t.to_address as contract_address,
        COUNT(l.log_index) as event_count
    FROM transactions t
    LEFT JOIN logs l ON t.transaction_hash = l.transaction_hash
    GROUP BY t.block_number, t.transaction_hash, t.to_address
    ORDER BY event_count DESC
    LIMIT 20
    """,
    datasets=["transactions", "logs"],
    blocks_from_latest=100
)
```

## Implementation Benefits

This integrated approach offers several advantages:

1. **Simplified User Experience**: Users don't need to remember separate steps for downloading and querying.

2. **Automatic Data Management**: The system automatically handles data download only when needed.

3. **Efficient Caching**: Previously downloaded data is reused for future queries.

4. **SQL Power**: Users get the full power of SQL for blockchain data analysis without handling the data management themselves.

5. **Single Interface**: A unified function that handles all the complexity but is simple to use.

Would you like me to focus on any particular aspect of this implementation in more detail?

### Does this take into account the mcp server stuff? like will this make it possible for an MCP query to be made including SQL and specifying some blocks to run it on?



You're absolutely right to focus on the MCP integration aspect. Let me clarify how this functionality would work specifically through the MCP protocol interface, which is a key feature of your architecture.

# MCP-Specific SQL Query Implementation

The implementations I suggested need to be tailored to work seamlessly through MCP. Let's revise the approach to ensure it works properly as MCP tools:

## 1. Enhanced MCP Tool for SQL Queries

```python
@mcp.tool()
def query_blockchain_sql(
    sql_query: str,
    dataset: Optional[str] = None,
    blocks: Optional[str] = None,
    start_block: Optional[int] = None,
    end_block: Optional[int] = None,
    use_latest: bool = False,
    blocks_from_latest: Optional[int] = None,
    contract: Optional[str] = None,
    force_refresh: bool = False,
    include_schema: bool = True
) -> Dict[str, Any]:
    """
    Query blockchain data using SQL, automatically downloading any required data
    
    Args:
        sql_query: SQL query to execute
        dataset: The specific dataset to query (e.g., 'transactions', 'logs')
                 If None, will be extracted from the SQL query
        blocks: Block range specification as a string (e.g., '1000:1010')
        start_block: Start block number (alternative to blocks)
        end_block: End block number (alternative to blocks)
        use_latest: If True, query the latest block
        blocks_from_latest: Number of blocks before the latest to include
        contract: Contract address to filter by
        force_refresh: Force download of new data even if it exists
        include_schema: Include schema information in the result
        
    Returns:
        SQL query results and metadata
    """
    from cryo_mcp.sql import execute_sql_query, list_available_tables, extract_dataset_from_sql
    
    # Try to determine dataset if not provided
    if dataset is None:
        dataset = extract_dataset_from_sql(sql_query)
        if dataset is None:
            return {
                "success": False,
                "error": "Could not determine dataset from SQL query. Please specify dataset parameter."
            }
    
    # First, ensure we have the data by running a query_dataset operation
    # This makes use of your existing MCP tool function
    download_result = query_dataset(
        dataset=dataset,
        blocks=blocks,
        start_block=start_block,
        end_block=end_block,
        use_latest=use_latest,
        blocks_from_latest=blocks_from_latest,
        contract=contract,
        output_format="parquet"  # Use parquet for optimal SQL performance
    )
    
    if "error" in download_result:
        return {
            "success": False,
            "error": f"Failed to download data: {download_result['error']}",
            "download_details": download_result
        }
    
    # Now execute the SQL query against the downloaded data
    sql_result = execute_sql_query(sql_query, include_schema)
    
    # Combine results to provide context
    result = {
        "sql_result": sql_result,
        "data_source": {
            "dataset": dataset,
            "files": download_result.get("files", []),
            "block_range": blocks or f"{start_block}:{end_block}" if start_block and end_block else "latest blocks" 
                           if use_latest or blocks_from_latest else "default range"
        }
    }
    
    # Include success/error at the top level for consistency
    if sql_result.get("success", False):
        result["success"] = True
        result["row_count"] = sql_result.get("row_count", 0)
        result["result"] = sql_result.get("result", [])
        if include_schema:
            result["schema"] = sql_result.get("schema")
    else:
        result["success"] = False
        result["error"] = sql_result.get("error", "Unknown SQL execution error")
    
    return result
```

## 2. Ensure SQL Module is MCP-Compatible

Here's the revised `sql.py` module to ensure it works properly with MCP:

```python
"""SQL query functionality for Cryo MCP using DuckDB."""
import os
import re
import json
from pathlib import Path
import duckdb
from typing import Dict, Any, List, Optional

# Default SQL query timeout in seconds
DEFAULT_QUERY_TIMEOUT = 30

def get_data_directory() -> Path:
    """Get the data directory where Cryo files are stored."""
    default_data_dir = str(Path.home() / ".cryo-mcp" / "data")
    return Path(os.environ.get("CRYO_DATA_DIR", default_data_dir))

def create_connection(read_only: bool = True) -> duckdb.DuckDBPyConnection:
    """Create a DuckDB connection with appropriate settings."""
    conn = duckdb.connect(database=":memory:", read_only=read_only)
    
    # Configure DuckDB settings for performance and safety
    conn.execute("SET memory_limit='4GB'")
    conn.execute(f"SET max_expression_depth=10000")
    conn.execute(f"SET max_query_time={DEFAULT_QUERY_TIMEOUT}")
    
    return conn

def list_available_tables() -> List[Dict[str, Any]]:
    """List all available tables from downloaded data files."""
    data_dir = get_data_directory()
    
    # Find all parquet files in the data directory (including the latest subdirectory)
    parquet_files = list(data_dir.glob("**/*.parquet"))
    
    tables = []
    for file_path in parquet_files:
        # Extract dataset name from filename
        name = file_path.stem.split("__")[0]
        if "__" in file_path.stem:
            name = file_path.stem.split("__")[0]
        else:
            # Try to extract from other naming patterns
            name_match = re.match(r'([a-z_]+)_', file_path.stem)
            if name_match:
                name = name_match.group(1)
            else:
                name = file_path.stem
        
        # Get file stats
        stats = file_path.stat()
        
        # Try to extract block range from filename
        block_range = ""
        blocks_match = re.search(r'blocks_(\d+)_to_(\d+)', str(file_path))
        if blocks_match:
            block_range = f"{blocks_match.group(1)}:{blocks_match.group(2)}"
        
        tables.append({
            "name": name,
            "path": str(file_path),
            "size_bytes": stats.st_size,
            "modified": stats.st_mtime,
            "block_range": block_range,
            "is_latest": "latest" in str(file_path)
        })
    
    return tables

def extract_dataset_from_sql(sql_query: str) -> Optional[str]:
    """
    Try to extract the dataset name from an SQL query.
    
    This is a simple heuristic that looks for FROM clauses in the query.
    
    Args:
        sql_query: The SQL query to parse
        
    Returns:
        The extracted dataset name or None if it couldn't be determined
    """
    # Simple regex to find table names after FROM or JOIN
    # This won't handle all SQL syntax but works for basic queries
    matches = re.findall(r'(?:FROM|JOIN)\s+([a-zA-Z_][a-zA-Z0-9_]*)', sql_query, re.IGNORECASE)
    
    if matches:
        # Return the first match that isn't a common SQL keyword
        for match in matches:
            if match.lower() not in ('where', 'select', 'group', 'order', 'having', 'limit', 'offset'):
                return match
    
    return None

def execute_sql_query(
    query: str,
    include_schema: bool = True
) -> Dict[str, Any]:
    """
    Execute a SQL query against downloaded Cryo data files.
    
    Args:
        query: SQL query to execute
        include_schema: Whether to include schema information in the result
        
    Returns:
        Dictionary with query results and metadata
    """
    data_dir = get_data_directory()
    conn = create_connection()
    
    try:
        # Register all parquet files as tables
        parquet_files = list(data_dir.glob("**/*.parquet"))
        
        # Track registered tables for the response
        registered_tables = {}
        
        for file_path in parquet_files:
            # Extract dataset name from filename for table name
            if "__" in file_path.stem:
                table_name = file_path.stem.split("__")[0]
            else:
                # Try to extract from other naming patterns
                name_match = re.match(r'([a-z_]+)_', file_path.stem)
                if name_match:
                    table_name = name_match.group(1)
                else:
                    table_name = file_path.stem
            
            # For multiple files of same dataset, use the path in latest directory if available
            if table_name in registered_tables and "latest" not in str(file_path):
                # Skip if we already have this table from a "latest" directory
                if "latest" in registered_tables[table_name]:
                    continue
            
            # Register or re-register the table
            try:
                # Drop the view if it exists
                conn.execute(f"DROP VIEW IF EXISTS {table_name}")
                conn.execute(f"CREATE VIEW {table_name} AS SELECT * FROM read_parquet('{file_path}')")
                registered_tables[table_name] = str(file_path)
            except Exception as e:
                print(f"Warning: Could not register table {table_name} from {file_path}: {e}")
        
        if not registered_tables:
            return {
                "success": False,
                "error": "No data files available. Run query_dataset first to download blockchain data."
            }
        
        # Execute the query with a timeout
        result = conn.execute(query).fetchdf()
        
        # Convert to records format for easier JSON serialization
        records = result.to_dict(orient="records")
        
        # Get schema information if requested
        schema_info = None
        if include_schema and not result.empty:
            schema_info = {
                "columns": list(result.columns),
                "dtypes": {col: str(dtype) for col, dtype in result.dtypes.items()}
            }
        
        return {
            "success": True,
            "result": records,
            "row_count": len(records),
            "schema": schema_info,
            "tables_used": registered_tables
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
    finally:
        conn.close()
```

## 3. Additional MCP Tools for SQL Query Support

Let's add a few more MCP tools to provide a complete SQL querying experience:

```python
@mcp.tool()
def get_sql_table_info() -> Dict[str, Any]:
    """
    Get information about available SQL tables with their schemas
    
    Returns:
        Detailed information about available tables for SQL queries
    """
    from cryo_mcp.sql import list_available_tables, create_connection
    
    tables = list_available_tables()
    if not tables:
        return {
            "success": False,
            "error": "No data files available. Run query_dataset first to download blockchain data."
        }
    
    # Get schema information for each table
    conn = create_connection()
    table_info = {}
    
    try:
        for table in tables:
            table_name = table["name"]
            file_path = table["path"]
            
            if table_name not in table_info:
                # Register the table
                try:
                    conn.execute(f"DROP VIEW IF EXISTS temp_view")
                    conn.execute(f"CREATE VIEW temp_view AS SELECT * FROM read_parquet('{file_path}')")
                    
                    # Get column info
                    column_info = conn.execute(
                        "SELECT column_name, data_type FROM information_schema.columns WHERE table_name='temp_view'"
                    ).fetchdf().to_dict(orient="records")
                    
                    # Count rows
                    row_count = conn.execute("SELECT COUNT(*) as count FROM temp_view").fetchone()[0]
                    
                    # Add to table info
                    table_info[table_name] = {
                        "columns": column_info,
                        "row_count": row_count,
                        "file_path": file_path,
                        "block_range": table.get("block_range", ""),
                        "is_latest": table.get("is_latest", False)
                    }
                except Exception as e:
                    print(f"Error getting schema for {table_name}: {e}")
        
        return {
            "success": True,
            "tables": table_info
        }
    finally:
        conn.close()

@mcp.tool()
def query_blockchain_sql_latest(
    sql_query: str,
    dataset: str,
    blocks_from_latest: int = 10,
    include_schema: bool = True
) -> Dict[str, Any]:
    """
    Query the latest blockchain data using SQL
    
    This is a convenience function for the common case of querying recent blocks.
    
    Args:
        sql_query: SQL query to execute
        dataset: The dataset to query (e.g., 'transactions', 'logs')
        blocks_from_latest: Number of blocks before the latest to include
        include_schema: Whether to include schema information in the result
        
    Returns:
        SQL query results and metadata
    """
    return query_blockchain_sql(
        sql_query=sql_query,
        dataset=dataset,
        blocks_from_latest=blocks_from_latest,
        include_schema=include_schema
    )

@mcp.tool()
def get_sql_examples() -> Dict[str, List[str]]:
    """
    Get example SQL queries for common blockchain analysis tasks
    
    Returns:
        Dictionary of example queries categorized by task
    """
    return {
        "basic_queries": [
            "SELECT * FROM transactions LIMIT 10",
            "SELECT * FROM blocks ORDER BY block_number DESC LIMIT 5",
            "SELECT * FROM logs WHERE address = '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48' LIMIT 10"
        ],
        "transaction_analysis": [
            "SELECT block_number, COUNT(*) as tx_count FROM transactions GROUP BY block_number ORDER BY tx_count DESC LIMIT 10",
            "SELECT from_address, COUNT(*) as sent_count FROM transactions GROUP BY from_address ORDER BY sent_count DESC LIMIT 10",
            "SELECT to_address, SUM(value) as total_eth FROM transactions GROUP BY to_address ORDER BY total_eth DESC LIMIT 10",
            "SELECT AVG(gas_used) as avg_gas FROM transactions"
        ],
        "contract_interactions": [
            "SELECT to_address as contract, COUNT(*) as interactions FROM transactions WHERE to_address IS NOT NULL GROUP BY contract ORDER BY interactions DESC LIMIT 20",
            "SELECT block_number, COUNT(*) as contract_txs FROM transactions WHERE to_address = '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48' GROUP BY block_number"
        ],
        "event_logs": [
            "SELECT address, COUNT(*) as event_count FROM logs GROUP BY address ORDER BY event_count DESC LIMIT 10",
            "SELECT topic0, COUNT(*) as event_count FROM logs GROUP BY topic0 ORDER BY event_count DESC LIMIT 10"
        ],
        "combined_queries": [
            "-- This requires both transactions and blocks datasets\nSELECT t.block_number, COUNT(*) as tx_count, b.timestamp FROM transactions t JOIN blocks b ON t.block_number = b.block_number GROUP BY t.block_number, b.timestamp ORDER BY tx_count DESC LIMIT 10"
        ]
    }
```

## Example MCP Queries with SQL

These functions can now be used directly through MCP. Here are some example interactions a user might have with these tools:

### Example 1: Querying Latest Transactions with SQL

**User Request:**
```
Show me a summary of the transactions from the last 10 blocks
```

**MCP Response:**
```
I'll get that information for you by running an SQL query on the latest transaction data.

```python
result = query_blockchain_sql(
    sql_query="""
    SELECT 
        block_number,
        COUNT(*) as tx_count,
        AVG(gas_used) as avg_gas,
        SUM(value) / 1e18 as total_eth_transferred
    FROM transactions
    GROUP BY block_number
    ORDER BY block_number DESC
    """,
    dataset="transactions",
    blocks_from_latest=10,
    include_schema=True
)
```

This will download transaction data for the 10 most recent blocks and then run the SQL query to analyze it.

The results show:
[summary of results would appear here]
```

### Example 2: Analyzing Contract Activity

**User Request:**
```
Find the most active contracts based on transaction count in blocks 15000000 to 15000100
```

**MCP Response:**
```
I'll analyze contract activity in the specified block range by using SQL on transaction data.

```python
result = query_blockchain_sql(
    sql_query="""
    SELECT 
        to_address as contract_address, 
        COUNT(*) as transaction_count,
        SUM(gas_used) as total_gas_used,
        COUNT(DISTINCT from_address) as unique_callers
    FROM transactions
    WHERE to_address IS NOT NULL
    GROUP BY to_address
    ORDER BY transaction_count DESC
    LIMIT 20
    """,
    dataset="transactions",
    blocks="15000000:15000100",
    include_schema=True
)
```

This query will:
1. Download transaction data for blocks 15000000 to 15000100
2. Run an SQL query to identify the most active contracts
3. Return details including transaction count, gas usage, and unique callers

The top active contracts are:
[results would appear here]
```

## Benefits of This Approach for MCP

1. **Complete Integration with MCP Protocol**: The tools are designed as MCP functions that can be called directly by LLMs.

2. **Single Query Flow**: Users can express their intent in natural language, and the LLM can translate that into a single call that handles both data fetching and SQL querying.

3. **Simplified Interface**: Despite the complexity behind the scenes, the interface remains simple and focused on what the user wants to know.

4. **Flexibility**: The implementation supports both:
   - Simple single-dataset queries
   - Complex multi-dataset analysis 
   - Latest block queries
   - Historical block range queries

5. **Discoverability**: Additional helper functions like `get_sql_examples()` and `get_sql_table_info()` make it easier for users to understand what's possible.

This implementation allows an MCP query to specify SQL to be run on blockchain data, with the system handling all the details of fetching the necessary data, preparing it for SQL querying, and returning the results in a structured format suitable for further processing or presentation to the user.

### 

<!-- Local Variables: -->
<!-- gptel-model: claude-3-7-sonnet-20250219 -->
<!-- gptel--backend-name: "Claude" -->
<!-- gptel-max-tokens: 20000 -->
<!-- gptel--bounds: ((227 . 10955) (11112 . 24090) (24264 . 42762)) -->
<!-- End: -->
