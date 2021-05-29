import pymongo,pandas

myclient = pymongo.MongoClient("mongodb://localhost:27017/") 

mydb = myclient["test"]

mycol = mydb["city"]
df = pandas.read_csv("alerts.csv")

id_list = list(df['_id'])
print(id_list,"csv ids")

db_records = mycol.find()
db_data = list(db_records)
# print(db_data[1],"db list")

filter_ids = []
for each in db_data:
    filter_ids.append(each['_id'])
print(filter_ids[:2],"fffff")

len_records = len(list(db_data))
# len_records =0
print(len_records,"total")

if not len_records:
    # print("---false")
    mycol.insert_many(df.to_dict("records"))
else:
    print("true")
    for each in id_list:
    #     print(each) 
        if each not in filter_ids:
            # result = id_list['_ids']
            # print(id_list['_ids'])