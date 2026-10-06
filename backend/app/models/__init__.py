from datetime import datetime
from sqlalchemy import String, Integer, ForeignKey, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base


class Artist(Base):
    __tablename__ = "artists"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    country: Mapped[str | None] = mapped_column(String(50))
    description: Mapped[str | None] = mapped_column(Text)

    albums: Mapped[list["Album"]] = relationship(
        back_populates="artist", cascade="all, delete-orphan"
    )


class Album(Base):
    __tablename__ = "albums"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
    year: Mapped[int | None] = mapped_column(Integer)
    artist_id: Mapped[int] = mapped_column(
        ForeignKey("artists.id", ondelete="CASCADE"), nullable=False
    )

    artist: Mapped["Artist"] = relationship(back_populates="albums")
    tracks: Mapped[list["Track"]] = relationship(
        back_populates="album", cascade="all, delete-orphan"
    )


class Track(Base):
    __tablename__ = "tracks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False, index=True)
    genre: Mapped[str | None] = mapped_column(String(50), index=True)
    duration: Mapped[int | None] = mapped_column(Integer)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    album_id: Mapped[int] = mapped_column(
        ForeignKey("albums.id", ondelete="CASCADE"), nullable=False
    )

    album: Mapped["Album"] = relationship(back_populates="tracks")