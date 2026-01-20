# Fayna Digital Industrial Bridge | Core Orchestrator
from machine_tester import MachineTester
import config

def initialize_bridge():
    """Starts the synchronization process between Factory Floor and ERP"""
    print("--- FAYNA DIGITAL: Industrial IoT Bridge v1.0 ---")
    
    # Instance of the connectivity tester
    tester = MachineTester()
    
    # List of monitored assets in the printing house
    assets = ["Heidelberg-XL-106", "HP-Indigo-6k"]
    
    for asset_id in assets:
        print(f"🔄 Checking status for: {asset_id}")
        if tester.check_status(asset_id):
            # Logic for Odoo API call would be placed here
            print(f"📊 {asset_id}: Data stream active. Syncing with Odoo MRP...")
        else:
            print(f"🚨 {asset_id}: Critical Error. Machine unreachable.")

if __name__ == "__main__":
    initialize_bridge()
