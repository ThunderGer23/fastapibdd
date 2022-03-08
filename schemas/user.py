def userEntity(item) -> dict:
    return {
        "id": item.get("id"),
        "name": item.get("name"),
        "email": item.get("email"),
        "password": item.get("password")
    }