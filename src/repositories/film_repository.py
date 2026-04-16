from bson import ObjectId
from services.film_service import *
from db.film_db import film_collection

def create_repository(film_dict):
    film_collection.insert_one(film_dict)
    
def list_repository():
    film_collection.find()