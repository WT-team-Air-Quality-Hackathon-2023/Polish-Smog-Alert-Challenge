import asyncio
import os
from models.air_pollution import AirPollutionRequest
from services.air_pollution_service import AirPollutionService

from dotenv import load_dotenv
from fastapi import FastAPI
from hypercorn import Config
from hypercorn.asyncio import serve
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles


app = FastAPI()

load_dotenv()

index = os.getenv('INDEX_PATH', '../frontend/dist/index.html')
assets = os.getenv('ASSETS_PATH', '../frontend/dist')
CONFIG_LOCAL_APP_ADDRESS = "127.0.0.1:80"


@app.get('/')
async def read_index():
    return FileResponse(index)


@app.post('/api/pollution')
async def fetch_pollution(air_pollution_request: AirPollutionRequest):
    pollution_data = AirPollutionService().get_air_pollution(
        air_pollution_request.latitude, 
        air_pollution_request.longitude
    )
    return pollution_data


app.mount('/assets', StaticFiles(directory=assets), name='assets')

if __name__ == "__main__":
    config = Config()
    config.bind = CONFIG_LOCAL_APP_ADDRESS
    asyncio.run(serve(app, config))
