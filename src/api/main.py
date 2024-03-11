import fastapi

app = fastapi.FastAPI()

@app.get("/")
async def generate_name(starts_with: str = None):
    return {"Hello": "World!"}
