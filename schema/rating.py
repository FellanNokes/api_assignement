from pydantic import BaseModel


class RatingSchema(BaseModel):
    rate: float
    count: int