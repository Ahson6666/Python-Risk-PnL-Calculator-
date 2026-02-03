# Risk & PnL Calculator (Python)

**Investment bank risk engine: portfolio PnL, exposure, VaR calculations.**  
*FastAPI Python portfolio for HK investment bank junior developer roles.*

## ✨ Features
- Portfolio PnL calculations (mark-to-market)
- Risk exposure by symbol/sector (HSBC, HSI)
- Basic Value-at-Risk (VaR) metrics
- REST APIs for risk reports
- NumPy financial calculations

## 🛠 Tech Stack
FastAPI - Python 3.11 - Pydantic - NumPy - pytest - GitHub Actions CI


## 🚀 Quick Start
```bash
pip install -r requirements.txt
uvicorn main:app --reload

Live API: http://localhost:8000/docs (Swagger)

##  Skills Demonstrated
FastAPI REST APIs
NumPy financial math (PnL, VaR)
Pydantic data validation
pytest + GitHub Actions CI/CD
HK banking domain

Files Structure (8 total):
Risk-pnl-python
├── requirements.txt
├── .gitignore
├── .github/workflows/ci.yml
├── README.md
├── main.py
├── models.py
├── api.py
└── test_pnl.py
