
from fastapi import FastAPI


from schema.product import ProductSchema
from schema.rating import RatingSchema
ratingList:list[RatingSchema] = [
    RatingSchema(rate=4.3, count=4),
    RatingSchema(rate=4.1, count=3),
    RatingSchema(rate=4.0, count=2),
]
productList: list[ProductSchema] = [
    ProductSchema(id=1, title="Apple", price=6.99, description="Green apples from france", category="Fruit", image="apple.jpg", rating=ratingList[0]),
    ProductSchema(id=2, title="Flour", price=8.99, description="Local flour", category="Baking", image="flour.jpg", rating=ratingList[1]),
    ProductSchema(id=3, title="Coca Cola", price=9.99, description="Best drink in the world after beer", category="Beverage", image="coca.jpg", rating=ratingList[2]),
]
app = FastAPI(title="My Second API")
@app.get("/products")
def get_products() -> list[ProductSchema]:
    return productList

