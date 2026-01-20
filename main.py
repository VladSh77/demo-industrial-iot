from machine_tester import MachineTester
import time

def run_fayna_bridge():
    print("🚀 FAYNA DIGITAL: Industrial IoT Bridge Started")
    tester = MachineTester()
    
    # Список машин у друкарні
    machines = ["Heidelberg-Offset-01", "HP-Indigo-7k"]
    
    for m in machines:
        if tester.check_status(m):
            print(f"⚙️ Syncing {m} production data with Odoo MRP...")
            # Тут викликається Odoo Connector
    
    print("🏁 Sync Cycle Completed.")

if __name__ == "__main__":
    run_fayna_bridge()
