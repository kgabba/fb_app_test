from fastapi import APIRouter, Depends
from app.deps_and_routes.user_deps import basic_authoriz, check_valid_roles_from_db

router_user = APIRouter(prefix='/user')

@router_user.get('/protected', dependencies=[Depends(basic_authoriz)])
async def protect_basic_auth():
    return {'message':'ok'}

@router_user.get('/for_admin', dependencies=[Depends(check_valid_roles_from_db(('admin')))])
async def protect_admin():
    return {'message':'ok ok'}