
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class CustomerCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: str | None = Field(default=None, max_length=150)
    phone: str | None = Field(default=None, max_length=20)


class CustomerUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    email: str | None = Field(default=None, max_length=150)
    phone: str | None = Field(default=None, max_length=20)


class CustomerResponse(BaseModel):
    id: int
    name: str
    email: str | None
    phone: str | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
