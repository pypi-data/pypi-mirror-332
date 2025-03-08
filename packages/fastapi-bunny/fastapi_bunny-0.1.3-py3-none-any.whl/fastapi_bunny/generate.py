import os
import subprocess  

BOILERPLATE = """\
from fastapi import FastAPI
from pymongo import MongoClient
from pydantic import BaseModel
from typing import List
from bson import ObjectId

app = FastAPI()

# MongoDB Connection
db = MongoClient("mongodb://localhost:27017")["{db_name}"]["{collection}"]

# Pydantic Model
class {model}(BaseModel):
{fields}

# Create {model}
@app.post("/{collection}/")
def create_{collection}_entry(entry: {model}):
    result = db.insert_one(entry.model_dump())
    return {{"id": str(result.inserted_id), **entry.model_dump()}}  #   Fixed syntax

# Get All {collection}
@app.get("/{collection}/", response_model=List[{model}]) 
def get_all_{collection}():
    return list(db.find({{}}, {{"_id": 0}}))  #   Fixed escaping `{}`

# Get {model} by ID
@app.get("/{collection}/{{id}}", response_model={model})
def get_{collection}_by_id(id: str):
    return db.find_one({{"_id": ObjectId(id)}}, {{"_id": 0}})  #   Fixed escaping `{}`

# Update {model} by ID
@app.put("/{collection}/{{id}}")
def update_{collection}_entry(id: str, entry: {model}):
    db.update_one({{"_id": ObjectId(id)}}, {{"$set": entry.model_dump()}})  #   Fixed escaping `{}` 
    return {{"message": "{model} updated successfully"}}

# Delete {model} by ID
@app.delete("/{collection}/{{id}}")
def delete_{collection}_entry(id: str):
    db.delete_one({{"_id": ObjectId(id)}})  #   Fixed escaping `{}` 
    return {{"message": "{model} deleted successfully"}}
"""

def create_boilerplate():
    # Get user input
    project_name = input("Enter your project name: ").strip().lower().replace(" ", "_")
    db_name = input("Enter your Database name: ").strip().lower().replace(" ", "_")
    collection = input("Enter your Collection name: ").strip().lower().replace(" ", "_")
   # Get dynamic fields for the Pydantic model
    fields = []
    print("Enter fields for your Pydantic model (type 'done' to finish):")
    
    while True:
        field_name = input("Field name: ").strip()
        if field_name.lower() == "done":
            break
        field_type = input("Field type (str/int/float/bool): ").strip()
        
        # Validate field type
        if field_type not in ["str", "int", "float", "bool"]:
            print("Invalid type! Use one of: str, int, float, bool")
            continue
        
        fields.append(f"    {field_name}: {field_type}")

    fields_str = "\n".join(fields)
    # Define project directory
    project_dir = os.path.join(os.getcwd(), project_name)

    # Prevent overwriting existing directories
    if os.path.exists(project_dir):
        print(f"  Error: Directory '{project_name}' already exists.")
        return
    
    os.makedirs(project_dir)
    boilerplate_code = BOILERPLATE.replace("{db_name}", db_name) \
                              .replace("{collection}", collection) \
                              .replace("{fields}", fields_str) \
                              .replace("{model}", project_name.capitalize())

    with open(os.path.join(project_dir, "main.py"), "w") as f:
        f.write(boilerplate_code)
    print(f"  Boilerplate project '{project_name}' created successfully!")

    run_now = input("Do you want to run the server now? (y/n): ").strip().lower()

    if run_now == "y":
    # Change to the new project directory
        os.chdir(project_dir)

    # Run the FastAPI server
        subprocess.run(["uvicorn", "main:app", "--reload"])
    else:
        print("\nYou can start the server later by running:")
        print(f"    cd {project_name}")
        print("    uvicorn main:app --reload")

