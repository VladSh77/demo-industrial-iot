# 🏭 Industrial IoT Bridge: Odoo MRP Integration
**System Architect:** Volodymyr Shevchenko | CTO @ Fayna Digital

### 📊 System Architecture
```text
[ Printing Machine ] ----( API / Heartbeat )----> [ Python IoT Bridge ]
                                                         |
                                                 ( XML-RPC / JSON )
                                                         |
                                                 v       v       v
                                               [  Odoo MRP System  ]
