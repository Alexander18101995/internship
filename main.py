from fastapi import FastAPI
from pydantic import BaseModel
from databases import Database
import asyncio
import asyncpg
import logging
#uvicorn main:app --reload


class Useradd(BaseModel):
    name: str

class Userdelete(BaseModel):
    name: str

class Userupdate(BaseModel):
    id: str
    name: str

app = FastAPI()

logging.basicConfig(filename='app.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
@app.post("/add")
async def insert_records(parameters: Useradd):
    database = Database('postgresql://postgres:9785@localhost:5432/postgres')
    try:
        await database.connect()
        import uuid
        uuid = uuid.uuid4()
        query = """INSERT INTO "user" (id,name) VALUES (:id ,:name)"""
        values = [{"id": f'{uuid}', "name": parameters.name}]
        await database.execute_many(query=query, values=values)
        await database.disconnect()
    except:
          print('Connection to Database Failed')


@app.delete("/delete")
async def user_delete(parameters: Userdelete):
    database = Database('postgresql://postgres:9785@localhost:5432/postgres')
    try:
        await database.connect()
        query = """delete from "user" where name = :name"""
        values = [{"name": parameters.name}]
        await database.execute_many(query=query, values=values)
        await database.disconnect()
    except:
            print('Connection to Database Failed\n')

@app.post("/update")
async def user_update(parameters: Userupdate):
    database = Database('postgresql://postgres:9785@localhost:5432/postgres')
    try:
        await database.connect()
        print('Connected to Database')
        query = """update "user" set name = :ame where id = :id"""
        values = [{"id": parameters.id, "name": parameters.name}]
        await database.execute_many(query=query, values=values)
        print('Update values in user Table Successfully')
        await database.disconnect()
        print('Disconnecting from Database')
    except:
        print('Connection to Database Failed')

@app.get("/select")
async def user_select():
    database = Database('postgresql://postgres:9785@localhost:5432/postgres')
    try:
        await database.connect()
        print('Connected to Database')
        query = """select * from "user" """
        rows = await database.fetch_all(query=query)
        for r in rows:
          print(r['id'],r['name'])
        await database.disconnect()
        print('Disconnecting from Database')
    except:
        print('Connection to Database Failed')