# import sqlalchemy as sq
# from sqlalchemy.orm import declarative_base,sessionmaker
from databases import Database
import asyncio
import asyncpg


async def create():
    database = Database('postgresql://postgres:9785@localhost:5432/postgres')
    try:
        await database.connect()
        print('Connected to Database')
        query = """create table "user" (id varchar(200) primary key, name varchar(40))"""
        print('Created Table user Successfully')
        await database.execute(query=query)

        await database.disconnect()
        print('Disconnecting from Database')
    except:
        print('Connection to Database Failed')

asyncio.run(create())



