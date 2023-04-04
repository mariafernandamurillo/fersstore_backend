import pymongo
import certifi

con_str = "mongodb+srv://fersstore:Fersstore101@cluster0.ttfvjxw.mongodb.net/?retryWrites=true&w=majority"
#mongodb+srv://fersstore:<password>@cluster0.ttfvjxw.mongodb.net/?retryWrites=true&w=majority

#Create a client
client = pymongo.MongoClient(con_str, tlsCAFile=certifi.where())
db = client.get_database("onlinestore_ch35")