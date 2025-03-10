from pydantic import BaseModel


class IsEven(BaseModel):
    is_even: bool
