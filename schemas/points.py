def pointEntity(db_item)-> dict:
    return {
        "id": str(db_item["_id"]),
        "point_time": str(db_item["time"]),
        "point_value": str(db_item["value"])
    }

def listOfPointEntity(db_item_list)-> dict:
    list_stud_entity=[]    
    for item in db_item_list:
        list_stud_entity.append(pointEntity(item))
    return list_stud_entity