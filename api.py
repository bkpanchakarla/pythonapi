from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Request model
class Item(BaseModel):
    name: str
    value: int

# Health check endpoint
@app.get("/health")
def health():
    return {"status": "ok"}

# Process endpoint
@app.post("/process")
def process_item(item: Item):
    if item.value < 0:
        raise HTTPException(status_code=400, detail="Value must be positive")

    result = {
        "message": f"Received {item.name}",
        "double_value": item.value * 2
    }
    return result
