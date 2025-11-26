from fastapi import Request

async def get_con(req:Request):
    return req.app.state.con