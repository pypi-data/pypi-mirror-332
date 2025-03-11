#!/usr/bin/env python3
"""
SQL Query Workflow Example for Cryo MCP

This example demonstrates the proper workflow for running SQL queries
against blockchain data using the Cryo MCP server.
"""
import os
import json
from typing import Dict, Any, List

# This assumes you have a client connected to a Cryo MCP server
# In a real scenario, you would use your MCP client's API
def mock_mcp_client():
    """Mock MCP client for demonstration purposes"""
    class MockClient:
        def query_dataset(self, **kwargs):
            print(f"MOCK: Downloading data with parameters: {kwargs}")
            # Return mock file paths
            return {
                "files": [
                    "/home/user/.cryo-mcp/data/ethereum__blocks__15000000_to_15001000.parquet",
                    "/home/user/.cryo-mcp/data/ethereum__transactions__15000000_to_15001000.parquet",
                ],
                "count": 2,
                "format": "parquet"
            }
        
        def get_sql_table_schema(self, file_path):
            print(f"MOCK: Getting schema for file: {file_path}")
            # Return mock schema
            return {
                "success": True,
                "file_path": file_path,
                "columns": [
                    {"column_name": "block_number", "data_type": "BIGINT"},
                    {"column_name": "block_hash", "data_type": "VARCHAR"},
                    {"column_name": "timestamp", "data_type": "TIMESTAMP"},
                    {"column_name": "gas_used", "data_type": "BIGINT"},
                    {"column_name": "transaction_count", "data_type": "INTEGER"},
                ],
                "sample_data": [
                    {"block_number": 15000000, "block_hash": "0x...", "timestamp": "2022-...", "gas_used": 12345678, "transaction_count": 123},
                    {"block_number": 15000001, "block_hash": "0x...", "timestamp": "2022-...", "gas_used": 23456789, "transaction_count": 234},
                ],
                "row_count": 1000
            }
        
        def query_sql(self, query, files=None, include_schema=True):
            print(f"MOCK: Executing SQL query: {query}")
            print(f"MOCK: Using files: {files}")
            # Return mock results
            return {
                "success": True,
                "result": [
                    {"block_number": 15000000, "gas_used": 12345678, "transaction_count": 123},
                    {"block_number": 15000001, "gas_used": 23456789, "transaction_count": 234},
                ],
                "row_count": 2,
                "files_used": files
            }
        
        def query_blockchain_sql(self, sql_query, dataset, **kwargs):
            print(f"MOCK: Executing combined query for dataset {dataset} with parameters: {kwargs}")
            print(f"MOCK: SQL Query: {sql_query}")
            # Return mock results
            return {
                "success": True,
                "result": [
                    {"block_number": 15000000, "gas_used": 12345678, "transaction_count": 123},
                    {"block_number": 15000001, "gas_used": 23456789, "transaction_count": 234},
                ],
                "row_count": 2,
                "data_source": {
                    "dataset": dataset,
                    "files": ["/home/user/.cryo-mcp/data/ethereum__blocks__15000000_to_15001000.parquet"],
                    "block_range": kwargs.get("blocks", "default range")
                }
            }
    
    return MockClient()

def main():
    """Main workflow example"""
    # Create a mock client
    client = mock_mcp_client()
    
    print("=== WORKFLOW 1: STEP-BY-STEP APPROACH (RECOMMENDED) ===")
    print("\nStep 1: Download blockchain data as parquet files")
    download_result = client.query_dataset(
        dataset="blocks",
        blocks="15000000:15001000",
        output_format="parquet"  # Always use parquet for SQL queries
    )
    
    # Get the file paths from the download result
    files = download_result.get("files", [])
    
    print("\nStep 2: Explore schema to understand available columns")
    # Inspect the schema of the first file
    schema = client.get_sql_table_schema(files[0])
    
    # Print column names and types to use in SQL
    print("\nAvailable columns:")
    for column in schema.get("columns", []):
        print(f"  - {column.get('column_name')}: {column.get('data_type')}")
    
    print("\nSample data:")
    for row in schema.get("sample_data", [])[:2]:
        print(f"  {row}")
    
    print("\nStep 3: Run SQL query against the downloaded files")
    # Option 1: Using simple table references (DuckDB matches the dataset name to files)
    sql_result = client.query_sql(
        query="""
        SELECT 
            block_number, 
            gas_used, 
            transaction_count,
            gas_used / transaction_count as avg_gas_per_tx
        FROM blocks
        WHERE transaction_count > 0
        ORDER BY avg_gas_per_tx DESC
        LIMIT 10
        """,
        files=files  # Pass the file paths from step 1
    )
    
    print("\nSQL query results (simple table reference):")
    for row in sql_result.get("result", [])[:2]:
        print(f"  {row}")
        
    # Option 2: Using explicit file path
    sql_result2 = client.query_sql(
        query=f"""
        SELECT 
            block_number, 
            gas_used, 
            transaction_count,
            gas_used / transaction_count as avg_gas_per_tx
        FROM '{files[0]}'
        WHERE transaction_count > 0
        ORDER BY avg_gas_per_tx DESC
        LIMIT 10
        """,
        files=files  # Pass the file paths from step 1
    )
    
    print("\nSQL query results (using explicit file path):")
    for row in sql_result2.get("result", [])[:2]:
        print(f"  {row}")
    
    print("\n=== WORKFLOW 2: COMBINED APPROACH ===")
    # Option 1: Combined approach with simple table name
    combined_result1 = client.query_blockchain_sql(
        sql_query="""
        SELECT 
            block_number, 
            gas_used, 
            transaction_count
        FROM blocks
        WHERE gas_used > 10000000
        ORDER BY gas_used DESC
        LIMIT 5
        """,
        dataset="blocks",  # Specify which dataset to download
        blocks="15000000:15001000"
    )
    
    print("\nCombined approach results (simple table reference):")
    for row in combined_result1.get("result", [])[:2]:
        print(f"  {row}")
        
    # Option 2: Combined approach with explicit file path
    combined_result2 = client.query_blockchain_sql(
        sql_query="""
        SELECT 
            block_number, 
            gas_used, 
            transaction_count
        FROM '/path/to/blocks.parquet'  -- Path doesn't matter, it will be replaced
        WHERE gas_used > 10000000
        ORDER BY gas_used DESC
        LIMIT 5
        """,
        dataset="blocks",  # Specify which dataset to download
        blocks="15000000:15001000"
    )
    
    print("\nCombined approach results (using explicit file path):")
    for row in combined_result2.get("result", [])[:2]:
        print(f"  {row}")
    
    print("\n=== BEST PRACTICES ===")
    print("1. Always use output_format='parquet' for best SQL performance")
    print("2. Use get_sql_table_schema() to understand available columns")
    print("3. You can use either:")
    print("   - Simple table references: FROM blocks")
    print("   - Or explicit file paths: FROM '/path/to/file.parquet'")
    print("4. For multiple files, you can join them in a single query")
    print("5. For complex analysis, the step-by-step approach gives more control")

if __name__ == "__main__":
    main()