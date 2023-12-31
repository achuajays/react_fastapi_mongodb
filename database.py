from model import B
import motor.motor_asyncio

c = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
d = c.crud
collection =d.cr_li

async def fetch(title):
    document = await collection.find_one({'title':title})
    return document

async def fetch_all():
    todos = []
    cursor = collection.find({})
    async for d in cursor:
        todos.append(B(**d))
    return todos


async def create_t(todo):
    document = todo
    result = await collection.insert_one(document)
    return result


async def up(title , des):
    await collection.update_one({'title':title},{'$set':{
        'dis' : des 
    }})
    document = await collection.find_one({'title':title})
    return document


async def d(title):
    await collection.delete_one({'title':title})
    return True



async def de():
    await collection.delete_many({})
    return True

