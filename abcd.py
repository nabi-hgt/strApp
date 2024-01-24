from  fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pymongo import MongoClient

app = FastAPI()

mongoclient = MongoClient("mongodb://mongodbserver:27017")
db = mongoclient["str4"]
files_collection = db["files"]

@app.get("/",response_class=JSONResponse)
def index(request:Request):
    filelist = list(files_collection.find({}))
    return JSONResponse({"Hello":filelist})

if __name__=="__main__":
    filelist = list(files_collection.find({}))
    print(filelist)