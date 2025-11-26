from fastapi import FastAPI
from contextlib import asynccontextmanager
import asyncpg
from deps_and_routes.player_routes import router_player
from deps_and_routes.user_routes import router_user
import uvicorn
import os
DATABASE_URL = os.getenv('DATABASE_URL')


@asynccontextmanager
async def lifespan(api: FastAPI):
    # создаём одно соединение при старте
    api.state.conn = await asyncpg.connect(DATABASE_URL)
    print("БД подключена")

    yield   # приложение работает

    # закрываем при остановке
    await api.state.conn.close()
    print("БД закрыта")


api = FastAPI(lifespan=lifespan)

api.add_api_route(router_player)
api.add_api_route(router_user)

if __name__=='__main__':
    uvicorn.run("main:api", host="0.0.0.0", port=8000, reload=True)