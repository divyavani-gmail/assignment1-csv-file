import pymongo,pandas

myclient = pymongo.MongoClient("mongodb://localhost:27017/") 

mydb = myclient["test"]

mycol = mydb["city"]
    
df = pandas.read_csv("alerts.csv")

mycol.insert_many(df.to_dict("records"))
total_rows = len(list(mycol.find()))
print("Total Rows of CSV:",total_rows)
event = (input("Please enter event name:"))
city_name = (input("Please enter city name:"))
city_count = mycol.find({"alert_1":event,"city":city_name}).count()

print("Alert count of",event,":",city_count)

print("Terms Of Percentage:",(city_count*100)/total_rows)