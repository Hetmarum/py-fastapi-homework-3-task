from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserRegistrationRequestSchema(BaseModel):
    email: EmailStr = Field(example="user@example.com")
    password: str = Field(example="SecurePassword123!")


class UserRegistrationResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: EmailStr


class UserActivationRequestSchema(BaseModel):
    email: EmailStr = Field(example="user@example.com")
    token: str = Field(example="activation_token")


class PasswordResetRequestSchema(BaseModel):
    email: EmailStr = Field(example="user@example.com")


class PasswordResetCompleteRequestSchema(BaseModel):
    email: EmailStr = Field(example="user@example.com")
    token: str = Field(example="reset_token")
    password: str = Field(min_length=8, example="NewSecurePassword123!")


class UserLoginRequestSchema(BaseModel):
    email: EmailStr = Field(example="user@example.com")
    password: str = Field(example="UserPassword123!")


class UserLoginResponseSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class MessageResponseSchema(BaseModel):
    message: str = Field(example="Action completed successfully.")


class TokenRefreshRequestSchema(BaseModel):
    refresh_token: str = Field(example="refresh_token")


class TokenRefreshResponseSchema(BaseModel):
    access_token: str = Field(example="new_access_token_here")
    refresh_token: str = Field(example="new_refresh_token_here")
    token_type: str = Field(default="bearer", example="bearer")
