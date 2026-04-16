from pydantic import BaseModel

class Film(BaseModel):
    title: str
    description: str
    genre: str
    year: int
    
class CreateFilmResponseModel(BaseModel):
    message: str
    id: str
    
class ListFilmResponseModel(BaseModel):
    films: object
    length: int