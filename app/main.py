from fastapi import FastAPI

app = FastAPI(title="Car Rental API")

@app.get("/")
def health():
    return {"status": "ok"}
