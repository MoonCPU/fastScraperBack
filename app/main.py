from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from .indicators import scrape_indicators
from .netGrowth import scrape_netGrowth

app = FastAPI()

@app.post("/scrape/{stock_code}")
async def scrape_and_return_data(stock_code: str):
    if not stock_code:
        raise HTTPException(status_code=400, detail="stock_code is required")

    try:
        indicators_data = scrape_indicators(stock_code)

        net_growth_data = scrape_netGrowth(stock_code)
        
        response_data = {
            "indicators": indicators_data,
            "net_growth": net_growth_data
        }

        return JSONResponse(content=response_data, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))