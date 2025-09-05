# Simple FastAPI Server

A simple FastAPI server with a single route `/kostya`.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

1. Run the server:
```bash
python main.py
```

Or using uvicorn directly:
```bash
uvicorn main:app --reload
```

2. The server will start on `http://localhost:8000`

## API Endpoints

- **GET** `/kostya` - Returns a greeting message

## Interactive API Documentation

Once the server is running, you can access:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
