from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import os
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware  # Import CORSMiddleware
from app.indicators import scrape_indicators
from app.netGrowth import scrape_netGrowth
from mangum import Mangum

load_dotenv()

app = FastAPI()
handler = Mangum(app)


# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Temporarily allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/scrape/indicators/{stock_code}")
async def scrape_indicators_endpoint(stock_code: str):
    if not stock_code:
        raise HTTPException(status_code=400, detail="stock_code is required")

    try:
        # Call the asynchronous scraping function
        indicators_data = await scrape_indicators(stock_code)

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
        # Call the asynchronous scraping function
        net_growth_data = await scrape_netGrowth(stock_code)
        
        response_data = {
            "net_growth": net_growth_data
        }
        
        return JSONResponse(content=response_data, status_code=200)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))