from pydantic import BaseModel

from schema.rating import RatingSchema


class ProductSchema(BaseModel):
    id: int
    title: str
    price: float
    description: str
    category: str
    image: str
    rating: RatingSchema