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

#  from typing import Annotated
#  from fastapi import FastAPI, Query

# app=FastAPI()

# @app.get("/items/")
# async def read_items(q:Annotated[str | None, Query(max_length=50)]=None):
#     results={"items":[{"items_id":"Foo","owner":"Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

#multivalues using query parameters and Query decorator and annotated types

#Code

# @app.get("/items/")
# async def read_items(q: Annotated[list | None, Query()]=["Foo", "Bar"]):
#     results={"items":[{"items_id":"Foo","owner":"Bar"}]}
#     if q:
#         results.update({"q": q})
#     return results

#---------------------------------------------------------

#custom validations using pydantic afterValidator decorator inside annotated types

# from fastapi import FastAPI, Query
# from typing import Annotated
# from pydantic import AfterValidator


# app=FastAPI()

# data = {
#     "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
#     "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
#     "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
# }

# def check_values(id:str):
#     if not id.startswith(("isbn-", "imdb-")):
#         raise ValueError("id invalid value")
#     return id

# @app.get("/items/")
# async def read_items(id:Annotated[str | None, AfterValidator(check_values)]=None):
#     if id:
#         item=data.get(id)
#     else:
#         id,item=random.choice(list(data.items()))
#     return {"id": id, "item": item}


#------------------------------------------------------------

#you can declare the same type of validations and metadata for path parameters with Path.

# from typing import Annotated
# from fastapi import FastAPI, Query, Path

# app=FastAPI()

# @app.get("/items/{item_id}")
# async def read_items(
#     item_id:Annotated[int,Path(title="The ID of the item ")],
#     q: Annotated[str | None, Query(alias="item-query")] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

#-------------------------------------------------------------------
from typing import Annotated, Literal
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Field
app=FastAPI()

class FilterParams(BaseModel):
    limit: int = Field(100, ge=0,le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []

@app.get("/items/")
async def read_items(
    filters_query: Annotated[FilterParams, Query()]
):
    return filters_query
