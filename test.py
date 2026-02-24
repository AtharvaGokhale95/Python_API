from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class AvailableCuisine(str, Enum):
    indian = "indian"
    italian = "italian"
    american = "american"
    
Cuisine = {
    AvailableCuisine.indian: ["Butter Chicken", "Naan", "Biryani"],
    AvailableCuisine.italian: ["Pizza", "Pasta", "Tiramisu"],
    AvailableCuisine.american: ["Hamburger", "Fries", "Apple Pie"]
}

food_items = {
    "indian": ["Butter Chicken", "Naan", "Biryani"],
    "italian": ["Pizza", "Pasta", "Tiramisu"],
    "american": ["Hamburger", "Fries", "Apple Pie"]
}   

# This function is for demonstrating the advantage of FastAPI's automatic validation and documentation generation when using Enums.
@app.get("/get_items/{cuisine}")
async def get_items(cuisine):
    return food_items.get(cuisine, "Cuisine not found")


# @app.get("/get_items/{cuisine}")
# async def get_items(cuisine: AvailableCuisine): # The parameter 'cuisine' is of type 'AvailableCuisine', which is an Enum (fixed set of constant values). FastAPI will automatically validate the input against the Enum values.
#     return {"cuisine": cuisine.value, # The 'value' attribute of the Enum member will give the actual string value (e.g., "indian", "italian", "american") instead of the Enum member name (e.g., AvailableCuisine.indian).
#         "dishes": Cuisine[cuisine]}

