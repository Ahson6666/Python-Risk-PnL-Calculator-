```python
from fastapi import FastAPI
from api import router as api_router

app = FastAPI(
    title="Risk & PnL Calculator", 
    version="1.0.0",
    description="Investment bank risk engine for HK markets"
)

app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Risk & PnL Calculator running! HSBC ready."}

@app.get("/api/portfolio/health")
async def health():
    return {"status": "healthy", "service": "Risk engine operational"}
