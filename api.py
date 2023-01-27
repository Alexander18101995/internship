from fastapi import FastAPI
from pydantic import BaseModel
from databases import Database
import asyncio
import asyncpg
#uvicorn api:app --reload

database = Database('postgresql://postgres:9785@localhost:5432/postgres')


class Usergender(BaseModel):
    gender: str
    limit: int

class Useradd(BaseModel):
    id: int
    name: str
    gender: str

class Updateuser(BaseModel):
    name: str
    gender: str


class Deleteuser(BaseModel):
    name: str



app = FastAPI()




@app.get("/select")
async def user_select():
    await database.connect()
    query = """select * from user_api order by id"""
    results = await database.fetch_all(query=query)
    return results


@app.get("/gender-limit/")
async def user_filter(gender: str, limit: int):
    await database.connect()
    query = f"""select * from user_api where gender = '{gender}' order by id limit {limit}"""
    result =  await database.fetch_all(query=query)
    return result

# @app.get("/gender-limit/{gender}")
# async def user_filter(param: Usergender):
#     await database.connect()
#     query = f"""select * from user_api where gender = :gender"""
#     values = [{"gender":param.gender}]
#     result =  await database.execute_many(query=query,values=values)
#     return result


@app.post("/post/")
async def user_create(param: Useradd):
    await database.connect()
    query = """insert into user_api (id,name,gender) values (:id, :name,:gender)"""
    values = [{"id": param.id,"name": param.name, "gender": param.gender}]
    await database.execute_many(query=query, values=values)


# @app.patch("/update/")
# async def user_update(param: Updateuser):
#     await database.connect()
#     query = """update  user_api set gender = :gender where name = :name"""
#     values = [{"gender": param.gender,"name": param.name}]
#     await database.execute_many(query=query, values=values)
#
# @app.delete("/delete/")
# async def user_delete(param: Deleteuser):
#     await database.connect()
#     query = """delete from  user_api  where name = :name"""
#     values = [{"name": param.name}]
#     await database.execute_many(query=query, values=values)






