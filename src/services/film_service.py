from fastapi import HTTPException
from bson import ObjectId
from routes.film_route import *
from schemas.film_schema import *
from repositories.film_repository import *

def create_service(film: Film):
    film_dict = film.model_dump(mode="json")
    result = create_repository(film_dict)
    
    return {
        "message": "Film Created",
        "id": str(result.inserted_id)
    }

def list_service():
    films = []
    
    for film in list_repository():
        film["_id"] = str(film["_id"])
        films.append(film)
    
    length = len(films)
    
    return {
        "films": films, 
        "length": length
    }