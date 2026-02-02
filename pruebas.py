prueba = {'success': True, 'timestamp': 1769623147, 'base': 'EUR', 'date': '2026-01-28', 'rates': {'USD': 1.193889, 'MXN': 20.566374, 'BTC': 1.3252656e-05}}

print(prueba.get("rates"))
rates = prueba["rates"]
print(f"USD - {rates["USD"]}")
print(f"MXN - {rates["MXN"]}")
print(f"BTC - {rates["BTC"]}")

USD: 1.18755
MXN: 20.664212
BTC: 1.4308459e-05