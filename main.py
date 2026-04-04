from fastapi import FastAPI

app = FastAPI()


#we can also specify the type of the path parameter,
#  and FastAPI will validate and convert it for us.
#  In this example, we specify that items_id should be an integer.
#  If a client sends a request with a non-integer value for items_id,
#  FastAPI will return a 422 Unprocessable Entity error.

# @app.get("/items/{items_id}")
# async def read_items(items_id:int):
#     return {"items_id": items_id}

# ---------------------------------------------

# we can also specify a path parameter with different types but 
# when creating path parameters, oders matter.
#  In this example, we have two path parameters.
#Otherwise, the path for /users/{user_id} would match also for /users/me,
#  "thinking" that it's receiving a parameter user_id with a value of "me".

#code 
# @app.get("/users/me")
# async def read_user_me():
#     return {"user_id": "the current user"}

# @app.get("/users/{user_id}")
# async def read_user(user_id: str):
#     return {"user_id": user_id}

#Similarly, you cannot redefine a path operation:

#------------------------------------------------
# if u want a predefined values we can use Enum CLASS 


#Code
# from enum import Enum

# class ModelName(str, Enum):
#     alexnet = "alexnet"
#     resnet = "resnet"
#     lenet = "lenet"


# @app.get("/models/{model_name}")
# async def get_model(model_name: ModelName):
#     if model_name == ModelName.alexnet:
#         return {"model_name": model_name, "message": "Deep Learning FTW!"}

#     if model_name.value == "lenet":
#         return {"model_name": model_name, "message": "LeCNN all the images"}

#     return {"model_name": model_name, "message": "Have some residuals"}


#------------------------------------------------------------------------


#query parameters

#when we declare a parameter that is not part of the path,
#  it will be automatically interpreted as a "query" parameter.

# @app.get("/items/{items_id}")
# async def read_items(items_id:int, q:str=None):
#     if q:
#         return {"items_id": items_id, "q": "this is working"}
#     return {"items_id": items_id}


# @app.get("/items/{items_id}/users/{users_id}")
# async def read_items_users(items_id: int, users_id: str, q: str = None, short: bool = False):
#     result = {"items_id": items_id, "users_id": users_id}
#     if q:
#         result.update({"q": q})

#     if not short:
#         result.update(
#             {"description": "This is an amazing item that has a long description"}
#         )
#     return result


