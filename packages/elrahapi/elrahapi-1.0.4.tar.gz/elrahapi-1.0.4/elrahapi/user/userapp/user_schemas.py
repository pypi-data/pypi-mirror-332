from elrahapi.user import  models
from myproject.settings import authentication
class UserBaseModel(models.UserBaseModel):
    pass

class UserCreateModel(models.UserCreateModel):
    pass

class UserUpdateModel(models.UserUpdateModel):
    pass

class UserPatchModel(models.UserPatchModel):
    pass

class UserPydanticModel(UserBaseModel):
    class Config :
        from_attributes=True

authentication.UserPydanticModel = UserPydanticModel
authentication.UserCreateModel = UserCreateModel
authentication.UserUpdateModel = UserUpdateModel
authentication.UserPatchModel = UserPatchModel


