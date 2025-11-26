from fastapi import Request

def get_con(req:Request):
    return req.app.state.con