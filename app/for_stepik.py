# app/schemas.py
from pydantic import BaseModel, Field, ConfigDict


class Order(BaseModel):
    id: int
    user_id: int
    total_price: float
    status: str
    is_active: bool = True

    model_config = ConfigDict(from_attributes=True)


# Напишите в этот блок Pydantic модель OrderList
# в нужном для вывода формате.
class ProductList(BaseModel):
    """
    Список пагинации для товаров.
    """
    items: list[Order] = Field(description="Товары для текущей страницы")
    total: int = Field(ge=0, description="Общее количество")
    page: int = Field(ge=1, description="Номер текущей страницы")
    page_size: int = Field(ge=1, description="Количество элементов на странице")

# app/routers/orders.py
# Модернизируйте в этом блоке эндпоинт /orders/,
# принимающий GET запросы с именем функции get_all_orders,
# добавив в него пагинацию.