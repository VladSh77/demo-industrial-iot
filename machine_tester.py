import random

class MachineTester:
    """Тест перевірки зв'язку з промисловим обладнанням"""
    def check_status(self, machine_id):
        status = random.choice([True, True, False]) # Імітація перевірки
        if status:
            print(f"✅ Machine {machine_id}: CONNECTION STABLE (HTTP 200)")
        else:
            print(f"⚠️ Machine {machine_id}: TIMEOUT. Checking logs...")
        return status
