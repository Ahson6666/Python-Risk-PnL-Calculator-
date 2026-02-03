from fastapi import APIRouter, HTTPException
from models import Position, Portfolio, AssetClass
import numpy as np

router = APIRouter()

# Mock HSBC portfolio
hsbc_portfolio = {
    "positions": [
        Position(
            symbol="0005.HK", 
            quantity=5000, 
            avg_price=65.50, 
            current_price=67.20,
            asset_class=AssetClass.EQUITY
        )
    ],
    "cash": 2500000.0
}

@router.get("/portfolio/health")
async def portfolio_health():
    return {"status": "Risk engine healthy", "ready": "HSBC calculations"}

@router.get("/risk/hsbc")
async def hsbc_risk():
    # Calculate PnL for HSBC position
    position = hsbc_portfolio["positions"][0]
    pnl = (position.current_price - position.avg_price) * position.quantity
    
    # Simple VaR (historical simulation mock)
    returns = np.array([0.01, -0.02, 0.015, -0.01, 0.008])
    var_95 = np.percentile(returns, 5) * position.quantity * position.current_price
    
    return {
        "symbol": "0005.HK (HSBC)",
        "exposure": position.quantity * position.current_price,
        "pnl": round(pnl, 2),
        "pnl_pct": round((pnl / (position.avg_price * position.quantity)) * 100, 2),
        "var_95": round(abs(var_95), 2),
        "var_pct": round(abs(var_95) / (position.quantity * position.current_price) * 100, 2)
    }

@router.post("/portfolio/analyze")
async def analyze_portfolio(portfolio: Portfolio):
    total_pnl = sum((p.current_price - p.avg_price) * p.quantity for p in portfolio.positions)
    total_exposure = sum(p.quantity * p.current_price for p in portfolio.positions)
    
    return {
        "total_exposure": total_exposure,
        "total_pnl": total_pnl,
        "pnl_pct": (total_pnl / (sum(p.avg_price * p.quantity for p in portfolio.positions))) * 100,
        "positions": len(portfolio.positions)
    }
