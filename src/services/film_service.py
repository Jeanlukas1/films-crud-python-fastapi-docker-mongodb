from fastapi import HTTPException
from bson import ObjectId
from src.schemas.film_schema import *
from src.repositories.film_repository import *

def format_id(film):
    film["_id"] = str(film["_id"])
    return film

def film_dict(film):
    film.model_dump(mode="json")
    return film

def create_service(film: Film):
    film_dict(film)
    result = create_repository(film_dict)
    
    return {
        "message": "Film Created",
        "id": str(result.inserted_id)
    }
    
def list_service():
    films = [format_id(film) for film in list_repository()]
    
    length = len(films)
    
    return {
        "films": films, 
        "length": length
    }
    
def update_service():
    result = update_repository()
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Film not found")
    return {"message": "Film updated succefully!"}
