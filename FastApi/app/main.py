from fastapi import FastAPI
from pydantic import BaseModel
import redis

app = FastAPI()
redis = redis.Redis(host='redis', port=6379)

class Library(BaseModel):
    name : str
    usage : str
    link : str = None
"""     def __init__(self, name, usage, link):
        self.name = name
        self.usage = usage
        self.link = link 

libs = []
libs.append(Library("Numpy", "scientific computing", ""))
libs.append(Library("Pandas", "managing dataframes", ""))
libs.append(Library("Seaborn", "vizualising charts", ""))
libs2 = []
libs2.append(Library("Junit", "Testing", ""))
libs2.append(Library("Log4j", "loging", ""))
libs2.append(Library("JAXB", "Xml parsing", ""))
"""
# ############### GET ###############
@app.get("/")
async def root():
    redis.incr('hits')
    return ' - - - This basic web page has been viewed {} time(s) - - -'.format(redis.get('hits'))

@app.get("/libs/{lang}")
def usage(name, lang):
    if lang.lower() == "java" :
        return next((x for x in libs2 if x.name.lower() == name.lower()), None)
    elif lang.lower() == "python" :
        return next((x for x in libs if x.name.lower() == name.lower()), None)
    else :
        return "not supported"

@app.get("/name/{id}")
def name(id: int):
    if id == 1:
        return "amine"
    return "alami"

@app.get("/age")
def root():
    return "22"

# ###################################

# ############### POST ##############
@app.post("/libs/")
async def createLibrary(lib: Library):
    return lib.name +" -> "+ lib.usage
# ###################################