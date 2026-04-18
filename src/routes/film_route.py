from fastapi import APIRouter
from src.services.film_service import *
from src.schemas.film_schema import *

router = APIRouter()

@router.post("/filmes", status_code=201, response_model=CreateFilmResponseModel)
def create_film(film: Film):
    return create_service(film)

@router.get("/filmes/{_id}", response_model=Film)
def get_film(_id: str):
    return get_by_id_service(_id)
    
@router.get("/filmes", status_code=200, response_model=ListFilmResponseModel)
def list_films():
    return list_service()

@router.put("/filmes/{_id}", status_code=200, response_model=UpdateFilmRespondeModel)
def update_film(_id: str, film: Film):
    return update_service(_id, film)

@router.delete("/filmes/{_id}", status_code=200, response_model=DeleteFilmResponseModel)
def delete_film(_id: str):
    return delete_service(_id)
