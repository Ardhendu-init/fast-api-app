from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import datetime, timezone


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    score: int = Field(ge=0, le=100)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    @field_validator("name")
    @classmethod
    def validate_name(cls, value):
        stripped_value = value.strip()
        if not stripped_value:
            raise ValueError("Name can not be empty")
        if len(stripped_value) > 200:
            raise ValueError("Name cannot exceed 200 characters")
        return stripped_value