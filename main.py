from fastapi import FastAPI
from pydantic import BaseModel
from databases import Database
import asyncio
import asyncpg

class User_add(BaseModel):
    name: str

class User_delete(BaseModel):
    name: str

class User_update(BaseModel):
    id: int
    name: str

app = FastAPI()

@app.get("/")
async def root():
    return 'User'

@app.post("/add")
async def insert_records(parameters: User_add):
    database = Database('postgresql://postgres:9785@localhost:5432/postgres')
    try:
        await database.connect()
        print('Connected to Database')
        import uuid
        uuid = uuid.uuid4()
        query = """INSERT INTO "user" (id,name) VALUES (:id ,:name)"""
        values = [{"id": f'{uuid}', "name": parameters.name}]
        await database.execute_many(query=query, values=values)
        print('Inserted values in user Table Successfully')
        await database.disconnect()
        print('Disconnecting from Database')
    except:
        print('Connection to Database Failed')


@app.post("/delete")
async def user_delete(parameters: User_delete):
    database = Database('postgresql://postgres:9785@localhost:5432/postgres')
    try:
        await database.connect()
        print('Connected to Database')
        query = """delete from "user" where name = :name"""
        values = [{"name": parameters.name}]
        await database.execute_many(query=query, values=values)
        print('Delete values in user Table Successfully')
        await database.disconnect()
        print('Disconnecting from Database')
    except:
        print('Connection to Database Failed')

@app.post("/update")
async def user_update(parameters: User_update):
    database = Database('postgresql://postgres:9785@localhost:5432/postgres')
    try:
        await database.connect()
        print('Connected to Database')
        query = """update "user" set name = :name where id = :id"""
        values = [{"id": parameters.id, "name": parameters.name}]
        await database.execute_many(query=query, values=values)
        print('Update values in user Table Successfully')
        await database.disconnect()
        print('Disconnecting from Database')
    except:
        print('Connection to Database Failed')

@app.post("/select")
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