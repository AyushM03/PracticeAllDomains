from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{items_id}")
async def read_items(items_id:int):
    return {"items_id": items_id}



