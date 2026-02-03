from pydantic import BaseModel
from typing import List, Optional
from enum import Enum

class AssetClass(str, Enum):
    EQUITY = "EQUITY"
    FX = "FX"
    BOND = "BOND"

class Position(BaseModel):
    symbol: str  # "0005.HK" (HSBC)
    quantity: float
    avg_price: float
    current_price: float
    asset_class: AssetClass

class Portfolio(BaseModel):
    positions: List[Position]
    cash: float = 0.0
    total_exposure: Optional[float] = None
    total_pnl: Optional[float] = None
    var_95: Optional[float] = None
