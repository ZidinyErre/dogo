
import os
from typing import Union
from dotenv import load_dotenv, dotenv_values
# from fastapi import FastAPI

load_dotenv()

print(os.getenv("MY_KEY"))
# app = FastAPI()

# @app.get("")


# def read_root():
#     return{"Hello": "World"}

# @app.get("/items/{item_id}")

# def read_item(item_id: int, q: Union[str, None] = None):
#     return { "item_id" : item_id, "q" : q}