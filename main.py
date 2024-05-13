# import FastAPI class from fastapi module
from fastapi import FastAPI

# create an instance of FastAPI class
app = FastAPI()

# use the instance to define a route that will be called when the root URL is accessed
@app.get("/")

# define a function that will be called when the route is accessed
async def root():
    # return a dictionary containing a message
    return {"message": "Hello World"}

# define a route that will be called when the /items/{item_id} URL is accessed
@app.get("/items/{item_id}")

# # define a function that will be called when the route is accessed who takes an item_id parameter
# async def read_item(item_id):
#     # return a dictionary containing the item_id parameter
#     return {"item_id": item_id}

# define a route that will be called when the /items/{item_id} URL is accessed but the item_id parameter is an integer
async def read_item(item_id: int):
    return {"item_id": item_id}