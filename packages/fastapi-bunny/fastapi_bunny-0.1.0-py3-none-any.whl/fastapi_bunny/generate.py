import os

BOILERPLATE = """
from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List
from bson import ObjectId

app = FastAPI()

# MongoDB Connection
db = MongoClient("mongodb://localhost:27017").{dbname}.{collection}

# Pydantic Model
class {model}(BaseModel):
    name: str
    subject: str
    experience: int

# Create {model}
@app.post("/{collection}/")
def create_{collection}({collection}: {model}):
    result = db.insert_one({collection}.model_dump())
    return {{"id": str(result.inserted_id), **{collection}.model_dump()}}

# Get All {collection}
@app.get("/{collection}/", response_model=List[{model}]) 
def get_{collection}():
    return list(db.find({}, {{"_id": 0}}))

# Get {model} by ID
@app.get("/{collection}/{{id}}", response_model={model})
def get_{collection}(id: str):
    return db.find_one({{"_id": ObjectId(id)}}, {{"_id": 0}})

# Update {model} by ID
@app.put("/{collection}/{{id}}")
def update_{collection}(id: str, {collection}: {model}):
    db.update_one({{"_id": ObjectId(id)}}, {{"$set": {collection}.model_dump()}})
    return {{"message": "{model} updated successfully"}}

# Delete {model} by ID
@app.delete("/{collection}/{{id}}")
def delete_{collection}(id: str):
    db.delete_one({{"_id": ObjectId(id)}})
    return {{"message": "{model} deleted successfully"}}
"""

def create_boilerplate():
    project_name = input("Enter your project name: ")
    project_dir = os.path.join(os.getcwd(), project_name)
    
    if os.path.exists(project_dir):
        print(f"Error: Directory {project_name} already exists.")
        return
    
    os.makedirs(project_dir)

    with open(os.path.join(project_dir, "main.py"), "w") as f:
        f.write(BOILERPLATE.format(dbname=project_name + "DB", collection=project_name, model=project_name.capitalize()))

    print(f"Boilerplate project '{project_name}' created successfully!")
