from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional


class UserModel(BaseModel):
    name: str
    age: int = None
    email: EmailStr

    @field_validator("email")
    def validate_email(cls, value: EmailStr) -> EmailStr:
        if "@" not in value:
            raise ValueError("Email must contain '@' symbol.")
        if len(value) > 100:
            raise ValueError(
                "Email address must be less than or equal to 45 characters."
            )
        return value

    @field_validator("age")
    def validate_age(cls, value: Optional[int]) -> int:
        if value is not None:
            if not isinstance(value, int):
                raise ValueError("Age must be an integer.")
            if value < 0:
                raise ValueError("Age must be a positive integer.")
        return value

    @field_validator("name")
    def validate_name(cls, value: str) -> str:
        if not isinstance(value, str):
            raise ValueError("Name must be a string.")
        if len(value) > 45:
            raise ValueError("Name must be less than or equal to 45 characters.")
        if not value.isalpha():
            raise ValueError("Name must contain only alphabetic characters.")
        return value


class BookModel(BaseModel):
    title: str
    id_user: int
    description: str = None

    @field_validator("title")
    def validate_title(cls, value: str) -> str:
        if not isinstance(value, str):
            raise ValueError("Title must be a string.")
        if len(value) > 45:
            raise ValueError("Title must be less than or equal to 45 characters.")
        return value

    @field_validator("id_user")
    def validate_id_user(cls, value: int) -> int:
        if not isinstance(value, int):
            raise ValueError("User ID must be an integer.")
        if value < 0:
            raise ValueError("User ID must be a positive integer.")
        return value

    @field_validator("description")
    def validate_description(cls, value: Optional[str]) -> str:
        if value is not None:
            if not isinstance(value, str):
                raise ValueError("Description must be a string.")
            if len(value) > 300:
                raise ValueError(
                    "Description must be less than or equal to 300 characters."
                )
        return value
