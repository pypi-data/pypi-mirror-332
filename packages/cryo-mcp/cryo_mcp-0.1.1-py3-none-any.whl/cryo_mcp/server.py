# cryo_mcp/server.py
"""
Cryo MCP - A Model Completion Protocol server for the Cryo blockchain data extraction tool.

This module provides a server that exposes Cryo's functionality through the MCP protocol,
allowing blockchain data querying through an API interface geared at usage by LLMs.
"""
import json
import os
import subprocess
import requests
import argparse
import sys
from pathlib import Path
from typing import List, Optional, Dict, Any
from mcp.server.fastmcp import FastMCP

# Get the default RPC URL from environment or use fallback
DEFAULT_RPC_URL = "http://localhost:8545"

# Create an MCP server
mcp = FastMCP("Cryo Data Server")

def get_latest_block_number() -> Optional[int]:
    """Get the latest block number from the Ethereum node"""
    rpc_url = os.environ.get("ETH_RPC_URL", DEFAULT_RPC_URL)
    
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_blockNumber",
        "params": [],
        "id": 1
    }
    
    try:
        response = requests.post(rpc_url, json=payload)
        response_data = response.json()
        
        if 'result' in response_data:
            # Convert hex to int
            latest_block = int(response_data['result'], 16)
            print(f"Latest block number: {latest_block}")
            return latest_block
        else:
            print(f"Error fetching latest block: {response_data.get('error', 'Unknown error')}")
            return None
    except Exception as e:
        print(f"Exception when fetching latest block: {e}")
        return None

@mcp.tool()
def list_datasets() -> List[str]:
    """Return a list of all available cryo datasets"""
    # Ensure we have the RPC URL
    rpc_url = os.environ.get("ETH_RPC_URL", DEFAULT_RPC_URL)
    
    result = subprocess.run(
        ["cryo", "help", "datasets", "-r", rpc_url],
        capture_output=True,
        text=True
    )

    # Parse the output to extract dataset names
    lines = result.stdout.split('\n')
    datasets = []

    for line in lines:
        if line.startswith('- ') and not line.startswith('- blocks_and_transactions:'):
            # Extract dataset name, removing any aliases
            dataset = line[2:].split(' (alias')[0].strip()
            datasets.append(dataset)
        if line == 'dataset group names':
            break

    return datasets

@mcp.tool()
def query_dataset(
    dataset: str,
    blocks: Optional[str] = None,
    start_block: Optional[int] = None,
    end_block: Optional[int] = None,
    use_latest: bool = False,
    blocks_from_latest: Optional[int] = None,
    contract: Optional[str] = None,
    output_format: str = "json",
    include_columns: Optional[List[str]] = None,
    exclude_columns: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Query a cryo dataset and return the results

    Args:
        dataset: The name of the dataset to query (e.g., 'logs', 'transactions')
        blocks: Block range specification as a string (e.g., '1000:1010')
        start_block: Start block number as integer (alternative to blocks)
        end_block: End block number as integer (alternative to blocks)
        use_latest: If True, query the latest block
        blocks_from_latest: Number of blocks before the latest to include (e.g., 10 = latest-10 to latest)
        contract: Contract address to filter by
        output_format: Output format (json, csv, parquet)
        include_columns: Columns to include alongside the defaults
        exclude_columns: Columns to exclude from the defaults

    Returns:
        The dataset results
    """
    # Ensure we have the RPC URL
    rpc_url = os.environ.get("ETH_RPC_URL", DEFAULT_RPC_URL)
    
    # Build the cryo command
    cmd = ["cryo", dataset, "-r", rpc_url]

    # Handle block range (priority: blocks > use_latest > start/end_block > default)
    if blocks:
        # Use specified block range string directly
        cmd.extend(["-b", blocks])
    elif use_latest or blocks_from_latest is not None:
        # Get the latest block number
        latest_block = get_latest_block_number()
        
        if latest_block is None:
            return {"error": "Failed to get the latest block number from the RPC endpoint"}
        
        if blocks_from_latest is not None:
            # Use a range of blocks up to the latest
            start = latest_block - blocks_from_latest
            block_range = f"{start}:{latest_block+1}"  # +1 to make it inclusive
        else:
            # Just the latest block
            block_range = f"{latest_block}:{latest_block+1}"  # +1 to make it inclusive
        
        print(f"Using latest block range: {block_range}")
        cmd.extend(["-b", block_range])
    elif start_block is not None:
        # Convert integer block numbers to string range
        if end_block is not None:
            # Note: cryo uses [start:end) range (inclusive start, exclusive end)
            # Add 1 to end_block to include it in the range
            block_range = f"{start_block}:{end_block+1}"
        else:
            # If only start_block is provided, get 10 blocks starting from there
            block_range = f"{start_block}:{start_block+10}"
        
        print(f"Using block range: {block_range}")
        cmd.extend(["-b", block_range])
    else:
        # Default to a reasonable block range if none specified
        cmd.extend(["-b", "1000:1010"])

    if contract:
        cmd.extend(["--contract", contract])

    if output_format == "json":
        cmd.append("--json")
    elif output_format == "csv":
        cmd.append("--csv")

    if include_columns:
        cmd.append("--include-columns")
        cmd.extend(include_columns)

    if exclude_columns:
        cmd.append("--exclude-columns")
        cmd.extend(exclude_columns)

    # Create a temporary directory for output
    temp_dir = Path("/tmp/cryo_output")
    temp_dir.mkdir(exist_ok=True)

    cmd.extend(["-o", str(temp_dir)])

    # Print the command for debugging
    print(f"Running query command: {' '.join(cmd)}")
    
    # Execute the command
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode != 0:
        return {
            "error": result.stderr,
            "stdout": result.stdout,
            "command": " ".join(cmd)
        }

    # Find the output file(s)
    output_files = list(temp_dir.glob(f"*{dataset}*.{output_format}"))
    print(f"Output files found: {output_files}")

    if not output_files:
        return {"error": "No output files generated", "command": " ".join(cmd)}

    # Read and return the data
    if output_format == "json":
        with open(output_files[0], 'r') as f:
            data = json.load(f)
            return {
                "data": data,
                "count": len(data) if isinstance(data, list) else 1,
            }
    else:
        # For other formats, just return the file path
        return {"file_path": str(output_files[0])}

@mcp.resource("dataset://{name}")
def get_dataset_info(name: str) -> Dict[str, Any]:
    """Get information about a specific dataset"""
    # Ensure we have the RPC URL
    rpc_url = os.environ.get("ETH_RPC_URL", DEFAULT_RPC_URL)
    
    result = subprocess.run(
        ["cryo", "help", name, "-r", rpc_url],
        capture_output=True,
        text=True
    )

    # Get the latest block number for examples
    latest_block = get_latest_block_number()
    latest_example = ""
    
    if latest_block:
        latest_example = f"query_dataset('{name}', blocks_from_latest=10)  # Gets latest-10 to latest blocks"
    
    return {
        "name": name,
        "description": result.stdout,
        "example_queries": [
            f"query_dataset('{name}', blocks='1000:1010')",
            f"query_dataset('{name}', start_block=1000, end_block=1009)",
            f"query_dataset('{name}', use_latest=True)  # Gets just the latest block",
            latest_example
        ],
        "notes": [
            "Block ranges are inclusive for start_block and end_block when using integer parameters.",
            "Use 'use_latest=True' to query only the latest block.",
            "Use 'blocks_from_latest=N' to query the latest N blocks."
        ]
    }

@mcp.tool()
def lookup_dataset(
    name: str,
    sample_start_block: Optional[int] = None,
    sample_end_block: Optional[int] = None,
    use_latest_sample: bool = False,
    sample_blocks_from_latest: Optional[int] = None
) -> Dict[str, Any]:
    """
    Look up a specific dataset and return detailed information about it
    
    Args:
        name: The name of the dataset to look up
        sample_start_block: Optional start block for sample data (integer)
        sample_end_block: Optional end block for sample data (integer)
        use_latest_sample: If True, use the latest block for sample data
        sample_blocks_from_latest: Number of blocks before the latest to include in sample
        
    Returns:
        Detailed information about the dataset including schema and available fields
    """
    # Get basic dataset info
    info = get_dataset_info(name)
    
    # Ensure we have the RPC URL
    rpc_url = os.environ.get("ETH_RPC_URL", DEFAULT_RPC_URL)
    
    # Get schema information by running the dataset with --dry-run
    schema_result = subprocess.run(
        ["cryo", name, "--dry-run", "-r", rpc_url],
        capture_output=True,
        text=True
    )
    
    if schema_result.returncode == 0:
        info["schema"] = schema_result.stdout
    else:
        info["schema_error"] = schema_result.stderr
    
    # Try to get a sample of the dataset (first 5 records)
    try:
        temp_dir = Path("/tmp/cryo_samples")
        temp_dir.mkdir(exist_ok=True)
        
        # Determine block range for sample (priority: latest > specified blocks > default)
        if use_latest_sample or sample_blocks_from_latest is not None:
            # Get the latest block number
            latest_block = get_latest_block_number()
            
            if latest_block is None:
                info["sample_error"] = "Failed to get the latest block number from the RPC endpoint"
                return info
            
            if sample_blocks_from_latest is not None:
                # Use a range of blocks from latest-n to latest
                block_range = f"{latest_block - sample_blocks_from_latest}:{latest_block+1}"
            else:
                # Just the latest 5 blocks
                block_range = f"{latest_block-4}:{latest_block+1}"
            
            info["sample_block_range"] = block_range
        elif sample_start_block is not None:
            if sample_end_block is not None:
                # Note: cryo uses [start:end) range (inclusive start, exclusive end)
                # Add 1 to end_block to include it in the range
                block_range = f"{sample_start_block}:{sample_end_block+1}"
            else:
                # Use start block and get 5 blocks
                block_range = f"{sample_start_block}:{sample_start_block+5}"
        else:
            # Default to a known good block range
            block_range = "1000:1005"
            
        # Use the block range for the sample
        sample_cmd = [
            "cryo", name, 
            "-b", block_range,
            "-r", rpc_url,
            "--json", 
            "-o", str(temp_dir)
        ]
        
        print(f"Running sample command: {' '.join(sample_cmd)}")
        sample_result = subprocess.run(
            sample_cmd,
            capture_output=True,
            text=True,
            timeout=30  # Add timeout to prevent hanging
        )
        
        if sample_result.returncode == 0:
            # Find the output file
            output_files = list(temp_dir.glob(f"*{name}*.json"))
            print(f"Output files found: {output_files}")
            
            if output_files:
                with open(output_files[0], 'r') as f:
                    data = json.load(f)
                    # Only include a few records as a sample
                    info["sample_data"] = data[:5] if isinstance(data, list) else data
            else:
                info["sample_error"] = "No output files generated"
        else:
            info["sample_error"] = sample_result.stderr
            info["sample_stdout"] = sample_result.stdout  # Include stdout for debugging
    except (subprocess.TimeoutExpired, Exception) as e:
        info["sample_error"] = str(e)
    
    return info

@mcp.tool()
def get_transaction_by_hash(
    tx_hash: str
) -> Dict[str, Any]:
    """
    Get detailed information about a transaction by its hash
    
    Args:
        tx_hash: The transaction hash to look up
        
    Returns:
        Detailed information about the transaction
    """
    # Ensure we have the RPC URL
    rpc_url = os.environ.get("ETH_RPC_URL", DEFAULT_RPC_URL)
    
    # Use RPC directly to get the transaction
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getTransactionByHash",
        "params": [tx_hash],
        "id": 1
    }
    
    try:
        response = requests.post(rpc_url, json=payload)
        response_data = response.json()
        
        if 'result' in response_data and response_data['result']:
            tx_data = response_data['result']
            
            # Get the receipt as well for additional information (gas used, status)
            receipt_payload = {
                "jsonrpc": "2.0",
                "method": "eth_getTransactionReceipt",
                "params": [tx_hash],
                "id": 2
            }
            
            receipt_response = requests.post(rpc_url, json=receipt_payload)
            receipt_data = receipt_response.json()
            
            if 'result' in receipt_data and receipt_data['result']:
                receipt = receipt_data['result']
                
                # Combine transaction and receipt data
                result = {
                    "transaction_hash": tx_hash,
                    "block_number": int(tx_data.get("blockNumber", "0x0"), 16),
                    "block_hash": tx_data.get("blockHash"),
                    "from_address": tx_data.get("from"),
                    "to_address": tx_data.get("to"),
                    "value": tx_data.get("value"),
                    "value_decimal": int(tx_data.get("value", "0x0"), 16),
                    "gas_limit": int(tx_data.get("gas", "0x0"), 16),
                    "gas_price": int(tx_data.get("gasPrice", "0x0"), 16),
                    "nonce": int(tx_data.get("nonce", "0x0"), 16),
                    "input": tx_data.get("input"),
                    "transaction_index": int(tx_data.get("transactionIndex", "0x0"), 16),
                    "gas_used": int(receipt.get("gasUsed", "0x0"), 16),
                    "status": int(receipt.get("status", "0x0"), 16),
                    "logs_count": len(receipt.get("logs", [])),
                    "contract_address": receipt.get("contractAddress")
                }
                
                # Handle EIP-1559 transactions
                if "maxFeePerGas" in tx_data:
                    result["max_fee_per_gas"] = int(tx_data.get("maxFeePerGas", "0x0"), 16)
                    result["max_priority_fee_per_gas"] = int(tx_data.get("maxPriorityFeePerGas", "0x0"), 16)
                    result["transaction_type"] = int(tx_data.get("type", "0x0"), 16)
                
                return result
            else:
                # Return just the transaction data if receipt is not available
                return {
                    "transaction_hash": tx_hash,
                    "block_number": int(tx_data.get("blockNumber", "0x0"), 16),
                    "block_hash": tx_data.get("blockHash"),
                    "from_address": tx_data.get("from"),
                    "to_address": tx_data.get("to"),
                    "value": tx_data.get("value"),
                    "value_decimal": int(tx_data.get("value", "0x0"), 16),
                    "gas_limit": int(tx_data.get("gas", "0x0"), 16),
                    "gas_price": int(tx_data.get("gasPrice", "0x0"), 16),
                    "nonce": int(tx_data.get("nonce", "0x0"), 16),
                    "input": tx_data.get("input"),
                    "transaction_index": int(tx_data.get("transactionIndex", "0x0"), 16),
                    "error": "Failed to retrieve transaction receipt"
                }
        else:
            return {"error": f"Transaction not found: {tx_hash}"}
    except Exception as e:
        return {"error": f"Exception when fetching transaction: {e}"}

@mcp.tool()
def get_latest_ethereum_block() -> Dict[str, Any]:
    """
    Get information about the latest Ethereum block
    
    Returns:
        Information about the latest block including block number
    """
    latest_block = get_latest_block_number()
    
    if latest_block is None:
        return {"error": "Failed to get the latest block number from the RPC endpoint"}
    
    # Get block data using cryo
    rpc_url = os.environ.get("ETH_RPC_URL", DEFAULT_RPC_URL)
    block_range = f"{latest_block}:{latest_block+1}"  # +1 to make it inclusive
    
    temp_dir = Path("/tmp/cryo_latest")
    temp_dir.mkdir(exist_ok=True)
    
    cmd = [
        "cryo", "blocks", 
        "-b", block_range,
        "-r", rpc_url,
        "--json", 
        "-o", str(temp_dir)
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        return {
            "block_number": latest_block,
            "error": "Failed to get detailed block data",
            "stderr": result.stderr
        }
    
    # Find the output file
    output_files = list(temp_dir.glob("*blocks*.json"))
    
    if not output_files:
        return {
            "block_number": latest_block,
            "error": "No output files generated"
        }
    
    # Read the block data
    with open(output_files[0], 'r') as f:
        data = json.load(f)
        if data and len(data) > 0:
            block_data = data[0]
            return {
                "block_number": latest_block,
                "timestamp": block_data.get("timestamp"),
                "hash": block_data.get("block_hash"),
                "author": block_data.get("author"),
                "gas_used": block_data.get("gas_used"),
                "base_fee_per_gas": block_data.get("base_fee_per_gas")
            }
        else:
            return {
                "block_number": latest_block,
                "error": "Empty block data"
            }

def parse_args(args=None):
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="Cryo Data Server")
    parser.add_argument(
        "--rpc-url", 
        type=str, 
        help="Ethereum RPC URL to use for requests"
    )
    return parser.parse_args(args)

def main():
    """Main entry point for the command-line script"""
    args = parse_args()
    
    # Set RPC URL with priority: command line > environment variable > default
    if args.rpc_url:
        rpc_url = args.rpc_url
        os.environ["ETH_RPC_URL"] = rpc_url
        print(f"Using RPC URL from command line: {rpc_url}")
    elif os.environ.get("ETH_RPC_URL"):
        rpc_url = os.environ["ETH_RPC_URL"]
        print(f"Using RPC URL from environment: {rpc_url}")
    else:
        rpc_url = DEFAULT_RPC_URL
        os.environ["ETH_RPC_URL"] = rpc_url
        print(f"Using default RPC URL: {rpc_url}")
    
    mcp.run()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
