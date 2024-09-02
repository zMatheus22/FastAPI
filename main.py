from fastapi import FastAPI # type: ignore
from json_db import JsonDB
from releases import Release 

app = FastAPI()

releaseDB = JsonDB(path="./data/releases.json")

@app.get("/entradas")
def get_Entry():
    readEntry = releaseDB.read_Json()

    readEntry = [x for x in readEntry if x["type"] == "entrada"]
    return readEntry


@app.get("/saidas")
def get_Exit():
    readExit = releaseDB.read_Json()

    readExit = [x for x in readExit if x["type"] == "saída"]
    return readExit


@app.post("/lancamentos")
def post_lancamentos(release: Release):
    releaseDB.insert(release)
    return {"Status": "OK"}
