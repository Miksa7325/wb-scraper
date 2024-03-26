from beanie import Document


class Product(Document):
    brand: str | None
    name: str | None
    price: float | None
    currency: str | None
    url: str | None
    img_link: str | None
    description: str | None
    rating: float | None
    reviews: int | None

