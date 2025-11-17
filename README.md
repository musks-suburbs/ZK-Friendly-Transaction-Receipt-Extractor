# README.md
# ZK-Friendly Transaction Receipt Extractor

## Overview
This repository provides a utility that extracts zero-knowledge–friendly fields from an Ethereum transaction receipt. These fields can be used as public inputs to ZK circuits, soundness verifiers, rollup logic, and systems involving cryptographic correctness guarantees such as Aztec, Zama, and other proof-based frameworks.

## Files
1. app.py — the main script.
2. README.md — instructions and documentation.

## Installation
1. Install Python 3.10+  
2. Install dependencies:  
   pip install web3  
3. Insert your own RPC endpoint into the RPC_URL variable.

## Usage
Run the script with a transaction hash:  
   python3 app.py 0xYourTxHash

## What the Script Does
The script connects to an Ethereum RPC provider and retrieves the transaction receipt for the provided hash. It extracts fields commonly used in ZK proving systems:
- Transaction status  
- Gas used  
- Contract creation address (if applicable)  
- Logs bloom filter  

These values can serve as public inputs for ZK circuits or as checkpoints for soundness verification in proof systems.

## Expected Output
You will see:
- Status of the transaction  
- Gas used  
- Contract address (if created)  
- Logs bloom (hex-encoded)  
- Confirmation that the extraction succeeded  

## Notes
- The tool works with any EVM-compatible RPC by modifying RPC_URL.  
- Useful for ZK rollups, proof aggregation systems, and soundness checks requiring deterministic receipt fields.  
- Ensure your RPC provider supports archive mode if you plan to query very old transactions.  
