import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['firedb2']
db = mydb["sample1"]

winter = [
        {'$match':
                    {'$and':
                        [
                            {"Month": {"$in": ["Dec","Jan","Feb"]}}
                        ]
                    }
        },
        {'$group':
            {
                "_id" : "$Problem", "val": {"$sum":1}   
            }
        },
        {
            '$sort' : {"val": -1}
        }
    ]

summer = [
        {'$match':
                    {'$and':
                        [
                            {"Month": {"$in": ["Jun","Jul","Aug"]}}
                        ]
                    }
        },
        {'$group':
            {
                "_id" : "$Problem", "val": {"$sum":1}   
            }
        },
        {
            '$sort' : {"val": -1}
        }
    ]

spring = [
        {'$match':
                    {'$and':
                        [
                            {"Month": {"$in": ["Mar","Apr","May"]}}
                        ]
                    }
        },
        {'$group':
            {
                "_id" : "$Problem", "val": {"$sum":1}   
            }
        },
        {
            '$sort' : {"val": -1}
        }
    ]

fall = [
        {'$match':
                    {'$and':
                        [
                            {"Month": {"$in": ["Sep","Oct","Nov"]}}
                        ]
                    }
        },
        {'$group':
            {
                "_id" : "$Problem", "val": {"$sum":1}   
            }
        },
        {
            '$sort' : {"val": -1}
        }
    ]

winter_= db.aggregate(winter)
spring_= db.aggregate(spring)
summer_= db.aggregate(summer)
fall_= db.aggregate(fall)

global winter_trash, winter_grass, winter_auto, winter_elec, winter_dump
global fall_trash, fall_grass, fall_auto, fall_elec, fall_dump
global spring_trash, spring_grass, spring_auto, spring_elec, spring_dump
global summer_trash, summer_grass, summer_auto, summer_elec, summer_dump

for x in winter_:    
    if(x.get('_id')=="TRASH - Trash Fire"):winter_trash =(x.get('val'))
    if(x.get('_id')=="ELEC - Electrical Fire"): winter_elec =(x.get('val'))
    if(x.get('_id')=="AUTO - Auto Fire"): winter_auto =(x.get('val'))
    if(x.get('_id')=="GRASS - Small Grass Fire"): winter_grass =(x.get('val'))
    if(x.get('_id')=="DUMP - Dumpster Fire"): winter_dump =(x.get('val'))

for x in spring_:    
    if(x.get('_id')=="TRASH - Trash Fire"):spring_trash =(x.get('val'))
    if(x.get('_id')=="ELEC - Electrical Fire"): spring_elec =(x.get('val'))
    if(x.get('_id')=="AUTO - Auto Fire"): spring_auto =(x.get('val'))
    if(x.get('_id')=="GRASS - Small Grass Fire"): spring_grass =(x.get('val'))
    if(x.get('_id')=="DUMP - Dumpster Fire"): spring_dump =(x.get('val'))

for x in summer_:    
    if(x.get('_id')=="TRASH - Trash Fire"):summer_trash =(x.get('val'))
    if(x.get('_id')=="ELEC - Electrical Fire"): summer_elec =(x.get('val'))
    if(x.get('_id')=="AUTO - Auto Fire"): summer_auto =(x.get('val'))
    if(x.get('_id')=="GRASS - Small Grass Fire"): summer_grass =(x.get('val'))
    if(x.get('_id')=="DUMP - Dumpster Fire"): summer_dump =(x.get('val'))

for x in fall_:    
    if(x.get('_id')=="TRASH - Trash Fire"):fall_trash =(x.get('val'))
    if(x.get('_id')=="ELEC - Electrical Fire"): fall_elec =(x.get('val'))
    if(x.get('_id')=="AUTO - Auto Fire"): fall_auto =(x.get('val'))
    if(x.get('_id')=="GRASS - Small Grass Fire"): fall_grass =(x.get('val'))
    if(x.get('_id')=="DUMP - Dumpster Fire"): fall_dump =(x.get('val'))
    
print("         TRASH   ELEC    AUTO    GRASS   DUMPSTER")
print("WINTER   ",winter_trash,"  ",winter_elec,"   ",winter_auto,"   ",winter_grass,"  ",winter_dump)
print("SPRING   ",spring_trash,"  ",spring_elec,"   ",spring_auto,"   ",spring_grass,"  ",spring_dump)
print("SUMMER   ",summer_trash,"  ",summer_elec,"   ",summer_auto,"   ",summer_grass,"  ",summer_dump)
print("FALL     ",fall_trash,"  ",fall_elec,"   ",fall_auto,"   ",fall_grass,"  ",fall_dump)