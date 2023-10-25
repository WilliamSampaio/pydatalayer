from pydatalayer.schema import BaseSchema
from pydatalayer.tinydb import BaseModel


class UserModel(BaseModel):
    def __init__(self, env: str, data: BaseSchema) -> None:
        super().__init__(
            entity='user',
            required=['name','email','active'],
            env=env)
        self.data
