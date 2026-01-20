# 🏭 Industrial IoT Bridge: Integracja z Odoo MRP
**Architekt Systemu:** Volodymyr Shevchenko | CTO @ Fayna Digital

### 🌐 Opis Projektu
To repozytorium prezentuje profesjonalny most technologiczny (IoT Bridge) zbudowany w Pythonie, który łączy park maszynowy bezpośrednio z systemem **Odoo Enterprise MRP**. Rozwiązanie eliminuje błędy ludzkie і zapewnia pełną transparentność produkcji w czasie rzeczywistym.

### 🛠 Składniki Systemu
* **`config.py`**: Warstwa bezpiecznej abstrakcji dla poświadczeń API.
* **`machine_tester.py`**: Moduł diagnostyczny "Heartbeat" – weryfikacja dostępności maszyn w sieci lokalnej.
* **`main.py`**: Główny silnik synchronizacji danych produkcyjnych z ERP.

### 🚀 Wartość Biznesowa
* **Automatyzacja Raportowania:** Dane o nakładach trafiają bezpośrednio do Odoo bez udziału operatora.
* **Zgodność z RODO:** Bezpieczne przetwarzanie danych na lokalnych serwerach або AWS.
* **Skalowalność:** Architektura gotowa na integrację z dziesiątkami maszyn drukarskich.
