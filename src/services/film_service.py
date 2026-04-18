from fastapi import HTTPException
from bson import ObjectId
from src.schemas.film_schema import *
from src.repositories.film_repository import *

def format_id(film: dict) -> dict:
    film["_id"] = str(film["_id"])
    return film

def validate_object_id(_id: str) -> ObjectId:
    if not ObjectId.is_valid(_id):
        raise HTTPException(status_code=400, detail="Invalid id format")
    return ObjectId(_id)

def film_dict(film: Film) -> dict:
    return film.model_dump(mode="json")

def create_service(film: Film) -> dict:
    try:
        data = film_dict(film)
        result = create_repository(data)
        
        return {
            "message": "Film Created",
            "id": str(result.inserted_id)
        }
        
    except HTTPException:
        raise
    
    except Exception as e:
        print("error: ", e)
        raise HTTPException(
            status_code= 500,
            detail= "Internal server error"
        )

def get_by_id_service(_id: str) -> dict:
    try:
        object_id = validate_object_id(_id)
        film = get_by_id_repository(object_id)
        if film:
            format_id(film)
            return film
        else:
            raise HTTPException(status_code=404 ,detail="Film not found")
    
    except HTTPException:
        raise
    
    except Exception as e:
        print("error: ", e)
        raise HTTPException(
            status_code=500, 
            detail="Internal server error"
        )
    
def list_service() -> dict:
    try:
        films = [format_id(film) for film in list_repository()]
        
        return {
            "films": films, 
            "length": len(films)
        }
    
    except HTTPException:
        raise
    
    except Exception as e:
        print("error: ", e)
        raise HTTPException(
            status_code= 500,
            detail= "Internal server error"
        )
        
def update_service(_id: str, film: Film) -> dict:
    try:
        object_id = validate_object_id(_id)
        data = film_dict(film)
        result = update_repository(object_id, data)
        
        if result.matched_count == 0:
            raise HTTPException(status_code=404, detail="Film not found")
        return {"message": "Film updated successfully!"}
    
    except HTTPException:
        raise 
    
    except Exception as e:
        print("error: ", e)
        raise HTTPException(
            status_code= 500,
            detail= "Internal server error"
        )
    
def delete_service(_id: str):
    try:
        object_id = validate_object_id(_id)
        result = delete_repository(object_id)

        if result.deleted_count == 0:
            raise HTTPException(status_code=404 , detail="Film not found!")
        return {
            "message": "Film deleted successfully!", 
            "id": _id
        }
    
    except HTTPException:
        raise
    
    except Exception as e:
        print("error: ", e)
        raise HTTPException(
            status_code= 500,
            detail= "Internal server error"
        )