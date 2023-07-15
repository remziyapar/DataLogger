import pymongo


_MongoClient = pymongo.MongoClient("mongodb://localhost:27017/")
_Db = _MongoClient["RtmDataLogger"]

def InsertData(value,register,datetime):
    _DataCollection = _Db["Data"]
    _Dic = { "Register": register, "Value": value ,"DateTime":datetime}
    x = _DataCollection.insert_one(_Dic)