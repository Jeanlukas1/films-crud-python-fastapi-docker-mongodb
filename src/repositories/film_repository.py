from bson import ObjectId
from src.services.film_service import *
from src.db.film_db import film_collection

def create_repository(film_dict):
    return film_collection.insert_one(film_dict)
    
def list_repository():
    return film_collection.find()

def update_repository(_id, film):
    return film_collection.update_one(
        {"_id": ObjectId(_id)},
        {"$set": film_dict(film)}
        )