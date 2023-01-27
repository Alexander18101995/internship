from databases import Database
import asyncio
import asyncpg


async def create():
    database = Database('postgresql://postgres:9785@localhost:5432/postgres')
    try:
        await database.connect()
        print('Connected to Database')
        create = """create table user_api (id int, name varchar(10), gender varchar(10))"""
        print('Created Table user Successfully')
        await database.execute(query=create)
        insert = """insert into user_api (id,name,gender)
                     values
                    (1,'Alex','Male'),
                    (2,'Ekaterina','Female'),
                    (3,'Oleg','Male'),
                    (4,'Anna','Female')"""
        await database.execute(query=insert)
        await database.disconnect()
        print('Disconnecting from Database')

    except:
        print('Connection to Database Failed')

asyncio.run(create())

