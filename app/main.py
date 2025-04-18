from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware 
from app.indicators import scrape_indicators
from app.netGrowth import scrape_netGrowth

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/scrape/indicators/{stock_code}")
async def scrape_indicators_endpoint(stock_code: str):
    if not stock_code:
        raise HTTPException(status_code=400, detail="stock_code is required")

    try:
        indicators_data = scrape_indicators(stock_code)

        response_data = {
            "indicators": indicators_data,
        }

        return JSONResponse(content=response_data, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/scrape/netGrowth/{stock_code}")
async def scrape_netGrowth_endpoint(stock_code: str):
    if not stock_code:
        raise HTTPException(status_code=400, detail="stock_code is required")

    try:
        net_growth_data = scrape_netGrowth(stock_code)
        
        response_data = {
            "net_growth": net_growth_data
        }
        
        return JSONResponse(content=response_data, status_code=200)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
