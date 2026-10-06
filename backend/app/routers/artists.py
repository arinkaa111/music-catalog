from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Artist
from app import schemas

router = APIRouter(prefix="/api/artists", tags=["artists"])


@router.get("/", response_model=list[schemas.ArtistOut])
def list_artists(db: Session = Depends(get_db)):
    return db.query(Artist).all()


@router.post("/", response_model=schemas.ArtistOut, status_code=status.HTTP_201_CREATED)
def create_artist(payload: schemas.ArtistCreate, db: Session = Depends(get_db)):
    artist = Artist(**payload.model_dump())
    db.add(artist)
    db.commit()
    db.refresh(artist)
    return artist


@router.get("/{artist_id}", response_model=schemas.ArtistOut)
def get_artist(artist_id: int, db: Session = Depends(get_db)):
    artist = db.get(Artist, artist_id)
    if not artist:
        raise HTTPException(status_code=404, detail="Artist not found")
    return artist