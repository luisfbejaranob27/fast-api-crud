import logging.config

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)

logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/", tags=["Home"])
async def docs():
	return RedirectResponse("/docs")
