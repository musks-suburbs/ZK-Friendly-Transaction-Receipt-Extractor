# app.py
from web3 import Web3
import sys
import time

RPC_URL = "https://mainnet.infura.io/v3/your_api_key"

def get_transaction_receipt(tx_hash):
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not w3.is_connected():
        print("❌ RPC connection failed")
        sys.exit(1)

    receipt = w3.eth.get_transaction_receipt(tx_hash)
    return receipt

def extract_zk_relevant_data(receipt):
    return {
        "status": receipt.status,
        "gas_used": receipt.gasUsed,
        "contract_address": receipt.contractAddress,
        "logs_bloom": receipt.logsBloom.hex(),
    }

if __name__ == "__main__":
    print("🔍 Extracting ZK-relevant receipt info for soundness checks...")
    time.sleep(0.2)

    if len(sys.argv) < 2:
        print("Usage: python3 app.py <tx_hash>")
        sys.exit(1)

    tx_hash = sys.argv[1]

    print(f"Fetching receipt for: {tx_hash}")
    receipt = get_transaction_receipt(tx_hash)
    data = extract_zk_relevant_data(receipt)

    print("Transaction status:", data["status"])
    print("Gas used:", data["gas_used"])
    print("Contract address:", data["contract_address"])
    print("Logs bloom:", data["logs_bloom"])
    print("✅ Receipt extracted — ready for ZK circuit inputs or soundness verification.")
