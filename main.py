from fastapi import FastAPI

app = FastAPI(title="Simple FastAPI Server", version="1.0.0")

@app.get("/kostya")
async def kostya_route():
    """
    Simple route that returns a greeting message for Kostya
    """
    return {"message": "Hello Kostya! Welcome to FastAPI!", "status": "success"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
