import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['firedb2']
db = mydb["sample1"]

def districts(dist_num):
    Dist_1 = [{'$match':{'$and':[{"CalendarYear": {"$in": ["2018","2021"]}},{"Council_District": dist_num}]}},
            {'$group':{"_id" :"$CalendarYear","val": {"$sum":1} }}]
    dt= db.aggregate(Dist_1)
    global m,n
    for i in dt:
        x = i.get("_id")
        if(x == "2018"):
            m = i.get("val")
        else:
            n =i.get("val")
    if(m/n) < 1:
        print("The number of Incidents in District", dist_num ,"has increased from",m,"to",n,"by",round(((n-m)/m)*100),"%")
    else:
        print("The number of Incidents in District", dist_num ,"has decreased from",m,"to",n,"by",round(((n-m)/m)*100),"%")
    
for i in range(1,11):
    districts(str(i))