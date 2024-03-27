import requests


response = requests.get("https://reqres.in/api/users")
if response.status_code // 100 == 2:
    users_data = response.json()
    print("Requerimiento 1: Información de usuarios")
    print(users_data)
else:
    print(f"Error en Requerimiento 1. Código de respuesta: {response.status_code}")


new_user = {
    "nombre": "Ignacio",
    "trabajo": "Profesor"
}
response = requests.post("https://reqres.in/api/users", data=new_user)
if response.status_code // 100 == 2:
    created_user = response.json()
    print("\nRequerimiento 2: Usuario creado")
    print(created_user)
else:
    print(f"Error en Requerimiento 2. Código de respuesta: {response.status_code}")


updated_data = {
    "residence": "zion"
}
response = requests.put("https://reqres.in/api/users/2", data=updated_data)  
if response.status_code // 100 == 2:
    updated_user = response.json()
    print("\nRequerimiento 3: Usuario actualizado")
    print(updated_user)
else:
    print(f"Error en Requerimiento 3. Código de respuesta: {response.status_code}")


response = requests.delete("https://reqres.in/api/users/3")  
print("\nRequerimiento 4: Código de respuesta al eliminar usuario")
print(response.status_code)
