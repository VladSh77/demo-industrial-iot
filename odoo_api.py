import xmlrpc.client
import config # Używamy Twojego pliku config

class OdooAPI:
    def __init__(self):
        self.common = xmlrpc.client.ServerProxy(f'{config.ODOO_URL}/xmlrpc/2/common')
        self.uid = self.common.authenticate(config.ODOO_DB, config.ODOO_USER, config.ODOO_PASSWORD, {})
        self.models = xmlrpc.client.ServerProxy(f'{config.ODOO_URL}/xmlrpc/2/object')

    def push_log(self, machine_id, units, state):
        """Wysyła dane do tabeli fayna.iot.machine.log"""
        vals = {
            'workcenter_id': machine_id,
            'units_delta': units,
            'state': state,
        }
        # Wywołanie metody 'create' w Odoo
        return self.models.execute_kw(config.ODOO_DB, self.uid, config.ODOO_PASSWORD, 
                                     'fayna.iot.machine.log', 'create', [vals])
