from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


class ArtistBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    country: str | None = Field(None, max_length=50)
    description: str | None = None


class ArtistCreate(ArtistBase):
    pass


class ArtistOut(ArtistBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class AlbumBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=150)
    year: int | None = Field(None, ge=1900, le=2100)
    artist_id: int


class AlbumCreate(AlbumBase):
    pass


class AlbumOut(AlbumBase):
    model_config = ConfigDict(from_attributes=True)
    id: int


class TrackBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=150)
    genre: str | None = Field(None, max_length=50)
    duration: int | None = Field(None, ge=0)
    album_id: int


class TrackCreate(TrackBase):
    pass


class TrackOut(TrackBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    created_at: datetime