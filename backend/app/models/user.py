from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    """Docstring para saber como vai aparecer no Swagger"""

    __tablename__ = "users"
    id: int = Field(
        primary_key=True, description="Descrição para saber como vai aparecer no Swagger"
    )
    name: str
    email: str
    password_hash: str
    is_admin: bool
    group_id: int = Field(foreign_key="group.id", nullable=True, default=None)
