# Fayna Digital: Industrial Machine Simulator
from pymodbus.server import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext
import logging

# Налаштування логів (щоб бачити, хто підключається)
logging.basicConfig()
log = logging.getLogger()
log.setLevel(logging.INFO)

def run_simulator():
    # Створюємо блоки даних (регістри)
    # Регістр 0: Статус (1 - працює), Регістр 1: Швидкість, Регістр 2: Лічильник
    store = ModbusSlaveContext(
        hr=ModbusSequentialDataBlock(0, [1, 12000, 5500] + [0]*97)
    )
    context = ModbusServerContext(slaves=store, single=True)

    print("🏗️ FAYNA SIMULATOR: Machine Heidelberg-XL-106 is ONLINE")
    print("📍 Local IP: 127.0.0.1 (Port: 5020)")
    
    # Запуск сервера на локальній адресі
    StartTcpServer(context=context, address=("127.0.0.1", 5020))

if __name__ == "__main__":
    run_simulator()
