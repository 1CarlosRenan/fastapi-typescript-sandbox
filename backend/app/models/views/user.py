from sqlmodel import SQLModel


class UserOut(SQLModel):
    """Docstring para ver como aparece no swagger"""

    id: int
    name: str
