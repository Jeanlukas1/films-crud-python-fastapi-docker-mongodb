from bson import ObjectId
from src.services.film_service import *
from src.db.film_db import film_collection

def create_repository(film_dict):
    film_collection.insert_one(film_dict)
    
def list_repository():
    return film_collection.find()