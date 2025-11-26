from fastapi import APIRouter, Depends
from deps_and_routes.user_deps import basic_authoriz, check_valid_roles_from_db
from schemas.model import User
from functools import partial

router_user = APIRouter(prefix='/user')

@router_user.get('/protected', dependencies=[Depends(basic_authoriz)])
async def protect_basic_auth():
    return {'message':'ok'}

@router_user.get('/for_admin')
async def protect_admin(user:User = Depends(partial(check_valid_roles_from_db, need_roles={"admin"}))):
    return {'message':'ok ok'}