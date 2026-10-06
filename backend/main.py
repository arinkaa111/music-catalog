from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import artists, tracks

app = FastAPI(title="Music Catalog API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(artists.router)
app.include_router(tracks.router)


@app.get("/")
def read_root():
    return {"message": "Hello, Music Catalog!"}


@app.get("/health")
def health_check():
    return {"status": "ok"}