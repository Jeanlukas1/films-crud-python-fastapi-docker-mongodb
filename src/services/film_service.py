from fastapi import HTTPException
from bson import ObjectId
from src.schemas.film_schema import *
from src.repositories.film_repository import *

def format_id(film):
    film["_id"] = str(film["_id"])
    return film

def film_dict(film):
    return film.model_dump(mode="json")

def create_service(film: Film):
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

def get_by_id_service(_id):
    try:
        product = get_by_id_repository(_id)
        if product:
            format_id(product)
            return product
        else:
            raise HTTPException(status_code=404 ,detail="Product not found")
    except:
       raise HTTPException(status_code=404, detail="Invalid ID")
    
def list_service():
    try:
        films = [format_id(film) for film in list_repository()]
        
        length = len(films)
        
        return {
            "films": films, 
            "length": length
        }
    
    except HTTPException:
        raise
        
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