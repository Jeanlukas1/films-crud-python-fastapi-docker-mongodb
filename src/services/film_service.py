from fastapi import HTTPException
from bson import ObjectId
from src.schemas.film_schema import *
from src.repositories.film_repository import *

def filter_object(_id):
    return ObjectId(_id)

def format_id(film):
    film["_id"] = str(film["_id"])
    return film

def film_dict(film):
    return film.model_dump(mode="json")

def create_service(film: Film):
    data = film_dict(film)
    result = create_repository(data)
    
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
    
def update_service(_id, film):
    data = film_dict(film)
    result = update_repository(_id, data)
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Film not found")
    return {"message": "Film updated succefully!"}

def delete_service(_id):
    result = delete_repository(_id)

    if result.deleted_count == 0:
        raise HTTPException(status_code=404 , detail="Film not found!")
    return {"message": "Film deleted succefully!", "id": _id}