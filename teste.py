import pymongo
from bson import ObjectId

myclient = pymongo.MongoClient("mongodb+srv://julio:senha@cluster0.pn3vb.mongodb.net/kivyapp?retryWrites=true&w=majority")
db = myclient["kivyapp"]
col_lv = db["lvs"]

get_ids = col_lv.count_documents({})

print(get_ids)
