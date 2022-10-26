from fastapi import FastAPI

app = FastAPI()

class Library:
    def __init__(self, name, usage, link):
        self.name = name
        self.usage = usage
        self.link = link

libs = []
libs.append(Library("Numpy", "scientific computing", ""))
libs.append(Library("Pandas", "managing dataframes", ""))
libs.append(Library("Seaborn", "vizualising charts", ""))

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/libs/{name}")
async def usage(name):
    return next((x for x in libs if x.name == name), None)


@app.get("/name/{id}")
def name(id: int):
    return fun(id)


@app.get("/age")
def root():
    return "22"


def fun(id):
    if id == 1:
        return "amine"
    return "alami"
