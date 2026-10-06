from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Track, Album
from app import schemas

router = APIRouter(prefix="/api/tracks", tags=["tracks"])


@router.get("/", response_model=list[schemas.TrackOut])
def list_tracks(genre: str | None = None, db: Session = Depends(get_db)):
    query = db.query(Track)
    if genre:
        query = query.filter(Track.genre == genre)
    return query.all()


@router.post("/", response_model=schemas.TrackOut, status_code=status.HTTP_201_CREATED)
def create_track(payload: schemas.TrackCreate, db: Session = Depends(get_db)):
    album = db.get(Album, payload.album_id)
    if not album:
        raise HTTPException(status_code=400, detail="Album not found")
    track = Track(**payload.model_dump())
    db.add(track)
    db.commit()
    db.refresh(track)
    return track


@router.get("/{track_id}", response_model=schemas.TrackOut)
def get_track(track_id: int, db: Session = Depends(get_db)):
    track = db.get(Track, track_id)
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")
    return track


@router.delete("/{track_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_track(track_id: int, db: Session = Depends(get_db)):
    track = db.get(Track, track_id)
    if not track:
        raise HTTPException(status_code=404, detail="Track not found")
    db.delete(track)
    db.commit()
    return None