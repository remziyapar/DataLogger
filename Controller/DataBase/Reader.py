import pymongo


_MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
_Db = _MongoClient["RtmDataLogger"]


def GetClients():
    _DataCollection=_Db["Clients"]
    return list(_DataCollection.find({"Enable":True},{"_id":False}))
    

def GetParameters():
    _DataCollection=_Db["Parameters"]
    return list(_DataCollection.find())


class Clnt:
    pass