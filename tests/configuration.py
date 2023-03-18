import os

mode = "local"
url = "http://127.0.0.1"
token = ""
base_path = f"{os.path.dirname(os.path.abspath(__file__))}/"


ACCESSED_CATALOG_ENUM = ["food", "phones", "furniture", "vehicle", "international_food"]
ROLE_ENUM = ["admin", "seller", "expert"]
Dimension = ["length", "width", "height"]


