# Skaner rejestrów Modbus dla Fayna Digital
from pymodbus.client import ModbusTcpClient

def scan_registers(ip, port=502):
    client = ModbusTcpClient(ip, port=port)
    if client.connect():
        print(f"🔍 Skanowanie maszyny {ip}...")
        # Czytamy pierwsze 100 rejestrów typu Holding Registers
        result = client.read_holding_registers(0, 100)
        if not result.isError():
            print("Stan rejestrów (0-99):", result.registers)
        client.close()
    else:
        print("❌ Brak połączenia z maszyną.")

if __name__ == "__main__":
    scan_registers("192.168.1.100") # Adres IP maszyny w drukarni
