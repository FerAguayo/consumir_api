# Currency Exchange Rate API Client

Python application to fetch currency exchange rates (EUR/USD) from ExchangeRatesAPI.

## Features
- MVC architecture
- Unit tests with pytest
- Environment configuration with API key

## Installation

1. Get your API key at https://api.exchangeratesapi.io
2. Rename `config_template.py` to `config.py`
3. Add your API key:
```python
API_KEY="your_api_key_here"
```

## Setup

Create virtual environment:
```bash
python -m venv venv
```

Activate it:
```bash
# Windows
.\venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## Run Tests
```bash
pytest
```
