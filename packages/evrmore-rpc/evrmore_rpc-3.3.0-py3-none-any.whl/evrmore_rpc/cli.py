#!/usr/bin/env python3
"""
Evrmore RPC CLI Tool

A command-line interface for interacting with the Evrmore blockchain via RPC.
"""

import argparse
import json
import sys
import os
import textwrap
from typing import Any, Dict, List, Optional, Union
import asyncio
from rich.console import Console
from rich.table import Table
from rich.progress import Progress
from rich.panel import Panel
from rich.syntax import Syntax
from datetime import datetime

from evrmore_rpc import EvrmoreClient, EvrmoreConfig, EvrmoreRPCError

console = Console()

def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Evrmore RPC CLI Tool - A command-line interface for the Evrmore blockchain"
    )
    
    # Connection options
    conn_group = parser.add_argument_group("Connection options")
    conn_group.add_argument(
        "--host", 
        help="RPC host (default: localhost)", 
        default=os.environ.get("EVRMORE_RPC_HOST", "localhost")
    )
    conn_group.add_argument(
        "--port", 
        type=int, 
        help="RPC port (default: 8819)", 
        default=int(os.environ.get("EVRMORE_RPC_PORT", "8819"))
    )
    conn_group.add_argument(
        "--user", 
        help="RPC username", 
        default=os.environ.get("EVRMORE_RPC_USER", "")
    )
    conn_group.add_argument(
        "--password", 
        help="RPC password", 
        default=os.environ.get("EVRMORE_RPC_PASSWORD", "")
    )
    conn_group.add_argument(
        "--timeout", 
        type=int, 
        help="Request timeout in seconds (default: 30)", 
        default=30
    )
    
    # Output options
    output_group = parser.add_argument_group("Output options")
    output_group.add_argument(
        "--json", 
        action="store_true", 
        help="Output as raw JSON"
    )
    output_group.add_argument(
        "--pretty", 
        action="store_true", 
        help="Pretty-print the output"
    )
    output_group.add_argument(
        "--quiet", 
        action="store_true", 
        help="Suppress informational output"
    )
    
    # Command options
    subparsers = parser.add_subparsers(dest="command", help="RPC command to execute")
    
    # Blockchain info command
    info_parser = subparsers.add_parser("info", help="Get blockchain information")
    
    # Block commands
    block_parser = subparsers.add_parser("block", help="Block-related commands")
    block_subparsers = block_parser.add_subparsers(dest="subcommand", help="Block subcommand")
    
    # getblock subcommand
    getblock_parser = block_subparsers.add_parser("get", help="Get block information")
    getblock_parser.add_argument("blockhash", help="Block hash")
    getblock_parser.add_argument(
        "--verbosity", 
        type=int, 
        choices=[0, 1, 2], 
        default=1, 
        help="Verbosity level (0=hex, 1=decoded, 2=decoded with tx data)"
    )
    
    # getblockcount subcommand
    block_subparsers.add_parser("count", help="Get the current block count")
    
    # getblockhash subcommand
    getblockhash_parser = block_subparsers.add_parser("hash", help="Get block hash by height")
    getblockhash_parser.add_argument("height", type=int, help="Block height")
    
    # Transaction commands
    tx_parser = subparsers.add_parser("tx", help="Transaction-related commands")
    tx_subparsers = tx_parser.add_subparsers(dest="subcommand", help="Transaction subcommand")
    
    # getrawtransaction subcommand
    getrawtx_parser = tx_subparsers.add_parser("get", help="Get transaction information")
    getrawtx_parser.add_argument("txid", help="Transaction ID")
    getrawtx_parser.add_argument(
        "--verbose", 
        action="store_true", 
        help="Show detailed transaction information"
    )
    
    # sendrawtransaction subcommand
    sendrawtx_parser = tx_subparsers.add_parser("send", help="Send raw transaction")
    sendrawtx_parser.add_argument("hexstring", help="Transaction data hexadecimal string")
    
    # Asset commands
    asset_parser = subparsers.add_parser("asset", help="Asset-related commands")
    asset_subparsers = asset_parser.add_subparsers(dest="subcommand", help="Asset subcommand")
    
    # listassets subcommand
    listassets_parser = asset_subparsers.add_parser("list", help="List assets")
    listassets_parser.add_argument(
        "--asset", 
        help="Asset name filter with wildcard support", 
        default="*"
    )
    listassets_parser.add_argument(
        "--count", 
        type=int, 
        help="Number of results to return", 
        default=100
    )
    
    # getassetdata subcommand
    getassetdata_parser = asset_subparsers.add_parser("info", help="Get asset information")
    getassetdata_parser.add_argument("asset_name", help="Asset name")
    
    # Wallet commands
    wallet_parser = subparsers.add_parser("wallet", help="Wallet-related commands")
    wallet_subparsers = wallet_parser.add_subparsers(dest="subcommand", help="Wallet subcommand")
    
    # getbalance subcommand
    wallet_subparsers.add_parser("balance", help="Get wallet balance")
    
    # listunspent subcommand
    listunspent_parser = wallet_subparsers.add_parser("unspent", help="List unspent transaction outputs")
    listunspent_parser.add_argument(
        "--minconf", 
        type=int, 
        help="Minimum confirmations", 
        default=1
    )
    listunspent_parser.add_argument(
        "--maxconf", 
        type=int, 
        help="Maximum confirmations", 
        default=9999999
    )
    
    # Network commands
    network_parser = subparsers.add_parser("network", help="Network-related commands")
    network_subparsers = network_parser.add_subparsers(dest="subcommand", help="Network subcommand")
    
    # getnetworkinfo subcommand
    network_subparsers.add_parser("info", help="Get network information")
    
    # getpeerinfo subcommand
    network_subparsers.add_parser("peers", help="Get peer information")
    
    # Raw command for any RPC method
    raw_parser = subparsers.add_parser("raw", help="Execute a raw RPC command")
    raw_parser.add_argument("method", help="RPC method name")
    raw_parser.add_argument("params", nargs="*", help="RPC method parameters")
    
    return parser.parse_args()

def format_output(data: Any, json_output: bool = False, pretty: bool = False) -> str:
    """Format the output data.
    
    Args:
        data: The data to format
        json_output: Whether to output as raw JSON
        pretty: Whether to pretty-print the output
        
    Returns:
        The formatted output string
    """
    if json_output:
        if pretty:
            return json.dumps(data, indent=2)
        return json.dumps(data)
    
    if isinstance(data, (dict, list)) and pretty:
        return json.dumps(data, indent=2)
    
    return str(data)

def print_result(data: Any, args):
    """Print the result to the console.
    
    Args:
        data: The data to print
        args: Command-line arguments
    """
    if args.json:
        console.print(format_output(data, json_output=True, pretty=args.pretty))
        return
    
    # Handle different output formats based on the command
    if args.command == "info":
        print_blockchain_info(data)
    elif args.command == "block":
        if args.subcommand == "get":
            print_block_info(data, args.verbosity)
        elif args.subcommand == "count":
            console.print(f"Current block height: [bold]{data}[/bold]")
        elif args.subcommand == "hash":
            console.print(f"Block hash: [bold]{data}[/bold]")
    elif args.command == "tx":
        if args.subcommand == "get":
            print_transaction_info(data, args.verbose)
        elif args.subcommand == "send":
            console.print(f"Transaction sent: [bold]{data}[/bold]")
    elif args.command == "asset":
        if args.subcommand == "list":
            print_asset_list(data)
        elif args.subcommand == "info":
            print_asset_info(data)
    elif args.command == "wallet":
        if args.subcommand == "balance":
            console.print(f"Wallet balance: [bold]{data}[/bold] EVR")
        elif args.subcommand == "unspent":
            print_unspent_outputs(data)
    elif args.command == "network":
        if args.subcommand == "info":
            print_network_info(data)
        elif args.subcommand == "peers":
            print_peer_info(data)
    else:
        # Default to pretty-printing the data
        console.print(format_output(data, pretty=args.pretty))

def print_blockchain_info(info: Dict[str, Any]):
    """Print blockchain information in a formatted table."""
    table = Table(title="Blockchain Information")
    table.add_column("Property", style="cyan")
    table.add_column("Value", style="green")
    
    for key, value in info.items():
        if isinstance(value, dict):
            value = json.dumps(value)
        table.add_row(key, str(value))
    
    console.print(table)

def print_block_info(block: Dict[str, Any], verbosity: int):
    """Print block information in a formatted panel."""
    if verbosity == 0:
        console.print(f"Block (hex): [bold]{block}[/bold]")
        return
    
    # For verbosity level 1 or 2
    panel = Panel(
        f"""[bold]Block Hash:[/bold] {block.get('hash', 'Unknown')}
[bold]Height:[/bold] {block.get('height', 'Unknown')}
[bold]Time:[/bold] {datetime.fromtimestamp(block.get('time', 0)).strftime('%Y-%m-%d %H:%M:%S')}
[bold]Transactions:[/bold] {len(block.get('tx', []))}
[bold]Size:[/bold] {block.get('size', 'Unknown')} bytes
[bold]Weight:[/bold] {block.get('weight', 'Unknown')}
[bold]Version:[/bold] {block.get('version', 'Unknown')}
[bold]Merkle Root:[/bold] {block.get('merkleroot', 'Unknown')}
[bold]Difficulty:[/bold] {block.get('difficulty', 'Unknown')}
[bold]Nonce:[/bold] {block.get('nonce', 'Unknown')}
[bold]Bits:[/bold] {block.get('bits', 'Unknown')}
[bold]Previous Block:[/bold] {block.get('previousblockhash', 'None')}
[bold]Next Block:[/bold] {block.get('nextblockhash', 'None')}""",
        title=f"Block {block.get('height', 'Unknown')}",
        expand=False
    )
    console.print(panel)
    
    # Print transaction list for verbosity level 1
    if verbosity == 1 and 'tx' in block:
        tx_table = Table(title="Transactions")
        tx_table.add_column("Transaction ID", style="cyan")
        
        for tx in block['tx']:
            if isinstance(tx, dict) and 'txid' in tx:
                tx_table.add_row(tx['txid'])
            else:
                tx_table.add_row(str(tx))
        
        console.print(tx_table)
    
    # Print detailed transaction info for verbosity level 2
    if verbosity == 2 and 'tx' in block and block['tx'] and isinstance(block['tx'][0], dict):
        console.print("\n[bold]Transaction Details:[/bold]")
        for i, tx in enumerate(block['tx']):
            if i > 9:  # Limit to first 10 transactions to avoid overwhelming output
                console.print(f"\n... and {len(block['tx']) - 10} more transactions")
                break
            
            print_transaction_info(tx, verbose=True)

def print_transaction_info(tx: Dict[str, Any], verbose: bool):
    """Print transaction information in a formatted panel."""
    if not verbose and isinstance(tx, str):
        console.print(f"Transaction (hex): [bold]{tx}[/bold]")
        return
    
    panel = Panel(
        f"""[bold]Transaction ID:[/bold] {tx.get('txid', 'Unknown')}
[bold]Version:[/bold] {tx.get('version', 'Unknown')}
[bold]Size:[/bold] {tx.get('size', 'Unknown')} bytes
[bold]VSize:[/bold] {tx.get('vsize', 'Unknown')} virtual bytes
[bold]Weight:[/bold] {tx.get('weight', 'Unknown')}
[bold]Locktime:[/bold] {tx.get('locktime', 'Unknown')}
[bold]Block Hash:[/bold] {tx.get('blockhash', 'Not confirmed')}
[bold]Time:[/bold] {datetime.fromtimestamp(tx.get('time', 0)).strftime('%Y-%m-%d %H:%M:%S') if tx.get('time') else 'Unknown'}
[bold]Confirmations:[/bold] {tx.get('confirmations', 0)}""",
        title="Transaction Details",
        expand=False
    )
    console.print(panel)
    
    # Print inputs
    if 'vin' in tx:
        vin_table = Table(title="Inputs")
        vin_table.add_column("Txid", style="cyan")
        vin_table.add_column("Vout", style="green")
        vin_table.add_column("ScriptSig", style="magenta")
        vin_table.add_column("Sequence", style="blue")
        
        for vin in tx['vin']:
            script = vin.get('scriptSig', {}).get('asm', 'No script')
            if len(script) > 30:
                script = script[:27] + "..."
            vin_table.add_row(
                vin.get('txid', 'Coinbase' if 'coinbase' in vin else 'Unknown'),
                str(vin.get('vout', 'N/A')),
                script,
                str(vin.get('sequence', 'Unknown'))
            )
        
        console.print(vin_table)
    
    # Print outputs
    if 'vout' in tx:
        vout_table = Table(title="Outputs")
        vout_table.add_column("n", style="cyan")
        vout_table.add_column("Value", style="green")
        vout_table.add_column("Address", style="magenta")
        vout_table.add_column("Type", style="blue")
        
        for vout in tx['vout']:
            addresses = []
            script_type = 'Unknown'
            
            if 'scriptPubKey' in vout:
                script = vout['scriptPubKey']
                script_type = script.get('type', 'Unknown')
                
                if 'addresses' in script:
                    addresses = script['addresses']
                elif 'address' in script:
                    addresses = [script['address']]
            
            address_str = ", ".join(addresses) if addresses else 'No address'
            if len(address_str) > 30:
                address_str = address_str[:27] + "..."
            
            vout_table.add_row(
                str(vout.get('n', 'Unknown')),
                str(vout.get('value', 'Unknown')),
                address_str,
                script_type
            )
        
        console.print(vout_table)

def print_asset_list(assets: Dict[str, Dict[str, Any]]):
    """Print asset list in a formatted table."""
    table = Table(title="Assets")
    table.add_column("Name", style="cyan")
    table.add_column("Amount", style="green")
    table.add_column("Units", style="blue")
    table.add_column("Reissuable", style="magenta")
    table.add_column("Has IPFS", style="yellow")
    
    for name, data in assets.items():
        table.add_row(
            name,
            str(data.get('amount', 'Unknown')),
            str(data.get('units', 'Unknown')),
            "Yes" if data.get('reissuable', False) else "No",
            "Yes" if data.get('has_ipfs', False) else "No"
        )
    
    console.print(table)

def print_asset_info(asset: Dict[str, Any]):
    """Print asset information in a formatted panel."""
    panel = Panel(
        f"""[bold]Name:[/bold] {asset.get('name', 'Unknown')}
[bold]Amount:[/bold] {asset.get('amount', 'Unknown')}
[bold]Units:[/bold] {asset.get('units', 'Unknown')}
[bold]Reissuable:[/bold] {'Yes' if asset.get('reissuable', False) else 'No'}
[bold]Has IPFS:[/bold] {'Yes' if asset.get('has_ipfs', False) else 'No'}
[bold]IPFS Hash:[/bold] {asset.get('ipfs_hash', 'None')}
[bold]Txid:[/bold] {asset.get('txid', 'Unknown')}
[bold]Verifier String:[/bold] {asset.get('verifier_string', 'None')}""",
        title=f"Asset: {asset.get('name', 'Unknown')}",
        expand=False
    )
    console.print(panel)

def print_unspent_outputs(utxos: List[Dict[str, Any]]):
    """Print unspent transaction outputs in a formatted table."""
    table = Table(title="Unspent Transaction Outputs")
    table.add_column("Txid", style="cyan")
    table.add_column("Vout", style="green")
    table.add_column("Address", style="magenta")
    table.add_column("Amount", style="blue")
    table.add_column("Confirmations", style="yellow")
    
    for utxo in utxos:
        txid = utxo.get('txid', 'Unknown')
        if len(txid) > 20:
            txid = txid[:17] + "..."
        
        table.add_row(
            txid,
            str(utxo.get('vout', 'Unknown')),
            utxo.get('address', 'Unknown'),
            str(utxo.get('amount', 'Unknown')),
            str(utxo.get('confirmations', 'Unknown'))
        )
    
    console.print(table)

def print_network_info(info: Dict[str, Any]):
    """Print network information in a formatted table."""
    table = Table(title="Network Information")
    table.add_column("Property", style="cyan")
    table.add_column("Value", style="green")
    
    for key, value in info.items():
        if isinstance(value, (dict, list)):
            value = json.dumps(value)
        table.add_row(key, str(value))
    
    console.print(table)

def print_peer_info(peers: List[Dict[str, Any]]):
    """Print peer information in a formatted table."""
    table = Table(title="Peer Information")
    table.add_column("Address", style="cyan")
    table.add_column("ID", style="green")
    table.add_column("Version", style="magenta")
    table.add_column("Subver", style="blue")
    table.add_column("Ping (ms)", style="yellow")
    table.add_column("Connected", style="cyan")
    
    for peer in peers:
        table.add_row(
            peer.get('addr', 'Unknown'),
            str(peer.get('id', 'Unknown')),
            str(peer.get('version', 'Unknown')),
            peer.get('subver', 'Unknown'),
            str(peer.get('pingtime', 'Unknown')),
            str(peer.get('conntime', 'Unknown'))
        )
    
    console.print(table)

async def main():
    """Main entry point for the CLI tool."""
    args = parse_args()
    
    if not args.command:
        console.print("[bold red]Error:[/bold red] No command specified")
        return 1
    
    # Create client with provided connection details
    client = EvrmoreClient(
        rpcuser=args.user,
        rpcpassword=args.password,
        rpchost=args.host,
        rpcport=args.port,
        timeout=args.timeout
    )
    
    try:
        # Execute the appropriate command
        if args.command == "info":
            result = await client.getblockchaininfo()
        elif args.command == "block":
            if args.subcommand == "get":
                result = await client.getblock(args.blockhash, args.verbosity)
            elif args.subcommand == "count":
                result = await client.getblockcount()
            elif args.subcommand == "hash":
                result = await client.getblockhash(args.height)
            else:
                console.print("[bold red]Error:[/bold red] Unknown block subcommand")
                return 1
        elif args.command == "tx":
            if args.subcommand == "get":
                result = await client.getrawtransaction(args.txid, args.verbose)
            elif args.subcommand == "send":
                result = await client.sendrawtransaction(args.hexstring)
            else:
                console.print("[bold red]Error:[/bold red] Unknown transaction subcommand")
                return 1
        elif args.command == "asset":
            if args.subcommand == "list":
                result = await client.listassets(args.asset, False, args.count)
            elif args.subcommand == "info":
                result = await client.getassetdata(args.asset_name)
            else:
                console.print("[bold red]Error:[/bold red] Unknown asset subcommand")
                return 1
        elif args.command == "wallet":
            if args.subcommand == "balance":
                result = await client.getbalance()
            elif args.subcommand == "unspent":
                result = await client.listunspent(args.minconf, args.maxconf)
            else:
                console.print("[bold red]Error:[/bold red] Unknown wallet subcommand")
                return 1
        elif args.command == "network":
            if args.subcommand == "info":
                result = await client.getnetworkinfo()
            elif args.subcommand == "peers":
                result = await client.getpeerinfo()
            else:
                console.print("[bold red]Error:[/bold red] Unknown network subcommand")
                return 1
        elif args.command == "raw":
            # Parse the parameters (convert string numbers to actual numbers)
            params = []
            for param in args.params:
                try:
                    if param.isdigit():
                        params.append(int(param))
                    elif param.replace(".", "", 1).isdigit():
                        params.append(float(param))
                    elif param.lower() in ("true", "false"):
                        params.append(param.lower() == "true")
                    else:
                        params.append(param)
                except (ValueError, AttributeError):
                    params.append(param)
            
            # Execute the raw command
            result = await client.call(args.method, *params)
        else:
            console.print(f"[bold red]Error:[/bold red] Unknown command: {args.command}")
            return 1
        
        # Print the result
        print_result(result, args)
    
    except EvrmoreRPCError as e:
        console.print(f"[bold red]RPC Error:[/bold red] {e}")
        return 1
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        return 1
    finally:
        # Close the client
        await client.close()
    
    return 0

def cli_main():
    """Entry point for the CLI tool when run as a script."""
    try:
        sys.exit(asyncio.run(main()))
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Operation cancelled by user[/bold yellow]")
        sys.exit(130)

if __name__ == "__main__":
    cli_main() 