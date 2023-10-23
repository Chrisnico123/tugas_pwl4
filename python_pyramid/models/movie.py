from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=False)
    year = Column(Integer, nullable=False)
    director = Column(Text, nullable=False)
    genre = Column(Text, nullable=False)
    
    def to_dict(self):
        """ Return a dictionary representation of a Movie object. """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'year': self.year,
            'director': self.director,
            'genre': self.genre,
        }


# Index('my_index', Movies.name, unique=True, mysql_length=255)
