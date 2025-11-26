from pydantic import BaseModel, Field

class Player(BaseModel):
    name: str
    position: str = Field(examples=['defendsman', 'forward', 'goalkeeper'])
    team: str|None = None
    rating: str = Field(ge=50, le=99)

class User(BaseModel):
    username: str
    password: str|None
    roles: list[str] = []
    session: str|None = None