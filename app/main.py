from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"Hello World !!"}

@app.get("/item")
async def item():
    return {"item_id": 8475289}
