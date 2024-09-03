def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "device_id": item["device_id"],
        "name": item["name"],
        "type": item["type"],
        "manufacturer": item.get("manufacturer"),
        "model": item.get("model"),
        "serial_number": item.get("serial_number"),
        "installed_at": item.get("installed_at")
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]



def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]