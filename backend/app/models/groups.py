from sqlmodel import SQLModel, Field


class Group(SQLModel, table=True):
    __tablename__ = "groups"
    id: int = Field(primary_key=True)
    name: str = Field(nullable=False)
