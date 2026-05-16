from . import db
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime, timezone
from sqlalchemy import String, Text, DateTime, ForeignKey, Table, Column, Integer

note_tags = Table(
    'note_tags',
    db.metadata,
    Column('note_id', Integer, ForeignKey("notes.id"), primary_key=True),
    Column('tag_id', Integer, ForeignKey("tags.id"), primary_key=True)
)


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(200), nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

    notes: Mapped[list["Note"]] = relationship("Note", back_populates='owner')

    def __repr__(self):
        return f"<User {self.username}>"


class Note(db.Model):
    __tablename__ = 'notes'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), nullable=False)
    content: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)

    owner: Mapped["User"] = relationship("User", back_populates="notes")
    tags: Mapped[list["Tag"]] = relationship("Tag", secondary=note_tags, back_populates="notes")


class Tag(db.Model):
    __tablename__ = 'tags'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    notes: Mapped[list["Note"]] = relationship("Note", secondary=note_tags, back_populates="tags")


    