"""Shipyard test app: Python + FastAPI, database through DB_* variables."""

import os

import pymysql
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
def home() -> str:
    return "Hello from Python on Shipyard"


@app.get("/db")
def database():
    try:
        connection = pymysql.connect(
            host=os.environ["DB_HOST"],
            port=int(os.environ["DB_PORT"]),
            user=os.environ["DB_USERNAME"],
            password=os.environ["DB_PASSWORD"],
            database=os.environ["DB_DATABASE"],
            connect_timeout=5,
        )
        with connection, connection.cursor() as cursor:
            cursor.execute("SELECT VERSION()")
            return {"ok": True, "version": cursor.fetchone()[0]}
    except (pymysql.MySQLError, KeyError) as error:
        return JSONResponse({"ok": False, "error": str(error)}, status_code=500)
