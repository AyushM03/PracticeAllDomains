# from fastapi import FastAPI
# from pydantic import BaseModel

# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
# app= FastAPI()

# @app.post("/items/")
# async def create_item(item: Item):
#     item_dict = item.dict()
#     if item.tax:
#         total_price = item.price + item.tax
#         item_dict.update({"total_price": total_price})
#     return item_dict


#------------------------------------------------------------

#we can work along with path parameters and query parameters
#  in the same path operation:
#also we can declare path parameters and query parameters
#  in the same path operation function, and FastAPI
#  will know which is which:
#same like we did in the previous study of path parameters and query parameters.
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
# app= FastAPI()

# @app.put("/items/{item_id}")
# async def create_item(item_id: int, item: Item, q: str | None = None):
#     result = {"item_id": item_id, **item.dict()}
#     if q:
#         result.update({"q": q})
#     return result



#---------------------------------------------------------------
#query parameters and string validations:
#validation using query and annotated types
#we can declare it as required or optional. using None

#Code

from typing import Annotated
from fastapi import FastAPI, Query

app=FastAPI()

@app.get("/items/")
async def read_items(q:Annotated[str | None, Query(max_length=50)]=None):
    results={"items":[{"items_id":"Foo","owner":"Bar"}]}
    if q:
        results.update({"q": q})
    return results

