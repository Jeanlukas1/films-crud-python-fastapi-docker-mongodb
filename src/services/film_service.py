from fastapi import HTTPException
from bson import ObjectId
from src.schemas.film_schema import *
from src.repositories.film_repository import *

def create_service(film: Film):
    film_dict = film.model_dump(mode="json")
    result = create_repository(film_dict)
    
    return {
        "message": "Film Created",
        "id": str(result.inserted_id)
    }

def format_id(film):
    film["_id"] = str(film["_id"])
    return film

def list_service():
    films = [format_id(film) for film in list_repository()]
    
    length = len(films)
    
    return {
        "films": films, 
        "length": length
    }