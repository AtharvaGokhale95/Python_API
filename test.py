from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class AvailableCuisine(str, Enum):
    indian = "indian"
    italian = "italian"
    american = "american"

# This dictionary maps the Enum members to their respective dishes. By using Enums, we can ensure that only valid cuisine types are accepted, and FastAPI will automatically generate documentation for the available options.
Cuisine = {
    AvailableCuisine.indian: ["Butter Chicken", "Naan", "Biryani"],
    AvailableCuisine.italian: ["Pizza", "Pasta", "Tiramisu"],
    AvailableCuisine.american: ["Hamburger", "Fries", "Apple Pie"]
}

# The following dictionary is a simple mapping of cuisine types to their respective dishes. However, it does not leverage the benefits of using Enums for validation and documentation in FastAPI.
# food_items = {
#     "indian": ["Butter Chicken", "Naan", "Biryani"],
#     "italian": ["Pizza", "Pasta", "Tiramisu"],
#     "american": ["Hamburger", "Fries", "Apple Pie"]
# }   

# This function is for demonstrating the advantage of FastAPI's automatic validation and documentation generation when using Enums.
# @app.get("/get_items/{cuisine}")
# async def get_items(cuisine):
#     return food_items.get(cuisine, "Cuisine not found")
# We get only the values for defined cuisines, and if we try to access an undefined cuisine, we get a "Cuisine not found" message. However, this approach does not provide automatic validation or documentation for the available cuisines.


# @app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvailableCuisine): # The parameter 'cuisine' is of type 'AvailableCuisine', which is an Enum (fixed set of constant values). FastAPI will automatically validate the input against the Enum values.
    return {"cuisine": cuisine.value, # The 'value' attribute of the Enum member will give the actual string value (e.g., "indian", "italian", "american") instead of the Enum member name (e.g., AvailableCuisine.indian).
        "dishes": Cuisine[cuisine]}

# This dictionary is a simple mapping of coupon codes to their respective discounts
coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%'
}
@app.get("/get_discount/{code}")
async def get_discount(code: int):
    return {"code": code,
            "discount": coupon_code.get(code, "Invalid code")}


