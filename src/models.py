import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    loginName = Column(String, nullable=False)
    password = Column(String, nullable=False)
    loginStatus = Column(String, nullable=False)
    registerDate = Column(String, nullable=False)

class Favorites(Base):
    __tablename__ = 'Favorites'
    id = Column(Integer, primary_key=True)
    peopleId = Column(Integer, ForeignKey('People.id'))
    planetsId = Column(Integer, ForeignKey('Planets.id'))
    userId = Column(Integer, ForeignKey('User.id'))



class People(Base):
    __tablename__ = 'People'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    mass =  Column(Integer, nullable=False)
    hair_color =  Column(String, nullable=False)
    skin_color =  Column(String, nullable=False)
    eye_color =  Column(String, nullable=False)
    birth_year =  Column(String, nullable=False)
    gender =  Column(String, nullable=False)


class Planets(Base):
    __tablename__ = 'Planets'
    Id = Column(Integer, primary_key=True)
    name =  Column(String, nullable=False)
    rotation_period =  Column(Integer, nullable=False)
    orbital_period =  Column(Integer, nullable=False)
    diameter =  Column(Integer, nullable=False)
    climate =  Column(String, nullable=False)
    gravity =  Column(String, nullable=False)
    terrain =  Column(String, nullable=False)
    surface_water =  Column(Integer, nullable=False)
    population =  Column(Integer, nullable=False)
    residents =  Column(Integer, nullable=False)
    created =  Column(String, nullable=False)
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

  ##   comandos para correr esta gitpod
   ##  pipenv shell
    ## pipenv install
   ##  python src/models.py


