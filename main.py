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


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

#Similarly, you cannot redefine a path operation:




