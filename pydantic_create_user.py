from pydantic import BaseModel, EmailStr, Field, UUID4


class UserSchema(BaseModel):
    """
    Описание модели пользователя
    """

    id: UUID4
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """
    Описания модель запроса на создание пользователя
    """

    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserResponseSchema(BaseModel):
    """
    Описание модели ответа на создание пользователя
    """

    user: UserSchema
