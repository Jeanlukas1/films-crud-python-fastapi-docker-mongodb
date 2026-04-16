from fastapi import APIRouter
from services.film_service import *
from schemas.film_schema import *

router = APIRouter()

@router.post("/filmes", status_code=201, response_model=CreateFilmResponseModel)
def create_film(film: Film):
    return create_service()
    
@router.get("/filmes", status_code=200, response_model=ListFilmResponseModel)
def list_films():
    return list_service()

@router.put("/filmes/{_id}", status_code=200, response_model=UpdateFilmResponseModel)
def update_film(_id: str, film: Film):
    film_dict = film.model_dump(mode="json")
    result = film_collection.update_one(
        {"_id": ObjectId(_id)},
        {"$set": film_dict}
    )
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Film not found")
    return {"message": "Film updated succefully!"}

@router.delete("/filmes/{_id}", status_code=200)
def delete_film(_id: str):
    filter_object = {"_id": ObjectId(_id)}
    result = film_collection.delete_one(filter_object)
    
    if result.deleted_count == 0:
        raise HTTPException(status_code=404 , detail="Film not found!")
    return {"message": "Film deleted succefully!", "id": _id}