from fastapi import APIRouter

user = APIRouter()

@user.get('/users')
def get_users():
    return "Hola ThunderGer"

@user.post('/users')
def create_user():
    return "Usuario creado"

@user.get('/users/{id}')
def find_user():
    return "Usuario encontrado"

@user.put('/users/{id}')
def update_user():
    return "Usuario modificado"

@user.delete('/users/{id}')
def delete_user():
    return "Usuario eliminado"