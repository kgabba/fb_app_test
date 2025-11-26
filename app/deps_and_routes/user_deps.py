from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Depends, HTTPException
from schemas.model import User
from db_utils.db_deps import get_con


async def check_from_db(name, password, connect = Depends(get_con)) -> User:
    info_db = await connect.fetchrow('select * from users where name = $1', name)
    if not info_db:
        raise HTTPException(status_code=401, detail='incorrect login')
    if info_db['passw'] != password:
        raise HTTPException(status_code=401, detail='incorrect password')
    return User(username=info_db['name'], password=None, roles=info_db['roles'])


async def basic_authoriz(user: HTTPBasicCredentials = Depends(HTTPBasic())) -> User:
    return await check_from_db(user.username, user.password)

# async def check_valid_roles_from_db(need_roles: list[str]|None = None, user: HTTPBasicCredentials = Depends(HTTPBasic())) -> User:
#     user_from_db = await check_from_db(user.username, user.password)
#     return 

async def check_valid_roles_from_db(need_roles: set, user = Depends(basic_authoriz)) -> User:
    fact_roles = set(user.roles)
    if not need_roles.intersection(fact_roles):
        raise HTTPException(status_code=403, detail='accses error')
    return user