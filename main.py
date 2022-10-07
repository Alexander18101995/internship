from fastapi import FastAPI
from pydantic import BaseModel
from databases import Database
import asyncio
import asyncpg
#uvicorn main:app --reload


class Useradd(BaseModel):
    name: str

class Userdelete(BaseModel):
    name: str

class Userupdate(BaseModel):
    id: int
    name: str

app = FastAPI()

@app.post("/add")
async def insert_records(parameters: Useradd):
    database = Database('postgresql://postgres:9785@localhost:5432/postgres')
    try:
        await database.connect()
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write('Connected to Database\n')
        import uuid
        uuid = uuid.uuid4()
        query = """INSERT INTO "user" (id,name) VALUES (:id ,:name)"""
        values = [{"id": f'{uuid}', "name": parameters.name}]
        await database.execute_many(query=query, values=values)
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write(f"""Inserted values in user Table\nid-{uuid}\nname-{parameters.name} Successfully\n""")
        await database.disconnect()
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write('Disconnecting from Database\n')
    except:
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write('Connection to Database Failed\n')


@app.delete("/delete")
async def user_delete(parameters: Userdelete):
    database = Database('postgresql://postgres:9785@localhost:5432/postgres')
    try:
        await database.connect()
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write('Connected to Database\n')
        query = """delete from "user" where name = :name"""
        values = [{"name": parameters.name}]
        await database.execute_many(query=query, values=values)
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write(f"""Delete values in user Table\nname-{parameters.name} Successfully\n""")
        await database.disconnect()
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write('Disconnecting from Database\n')
    except:
        with open('log.txt', 'a', encoding='utf-8') as file:
            file.write('Connection to Database Failed\n')

@app.post("/update")
async def user_update(parameters: Userupdate):
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