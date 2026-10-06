from fastapi import FastAPI

app = FastAPI(title="Music Catalog API")

@app.get("/")
def read_root():
    return {"message": "Hello, Music Catalog!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}