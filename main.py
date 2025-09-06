from fastapi import FastAPI
import uvicorn
import logging
logger = logging.getLogger(__name__)

app = FastAPI(title="Simple FastAPI Server", version="1.0.0")

@app.get("/")
async def kostya_route():
    logger.info("kostya_route endpoint was called")
    response = {"message": "Hello Kostya! Welcome to FastAPI!", "status": "success"}
    logger.info(f"kostya_route response: {response}")
    return response

@app.get("/health")
async def kostya_route_health():
    logger.info("kostya_route endpoint was called")
    response = {"message": "Server is live", "status": "success"}
    logger.info(f"kostya_route response: {response}")
    return response


if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)
