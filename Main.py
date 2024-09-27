from fastapi import FastAPI
from fastapi.responses import RedirectResponse, JSONResponse
import Logging_config

logger = Logging_config.logger

app = FastAPI()

@app.get("/", tags=["Home"])
async def docs():
	return RedirectResponse("/docs")


@app.get("/test", tags=["Test"])
async def test():
	logger.info("Test")
	return JSONResponse("Test")
