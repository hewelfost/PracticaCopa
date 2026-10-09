# Primera practica
Se debe reconocer una serie de parámetros para el entendimiento y verificación del código.

## Parámetro 1: Lenguaje y framework
Viendo el tipo de archivo .py, podemos identificar que el lenguaje de programación utilizado es Python. Viendo la línea 5 del archivo main.py, podemos inferir que el framework de backend utilizado es FastAPI.

## Parámetro 2 y 6: Archivo de arranque
Todo servicio, programa o código de Python debe ser ejecutado desde el archivo main.py. Pero se está usando FastAPI como framework, por lo que el comando para la ejecución sería:
```
uvicorn main:api --reload
```
Siendo main la referencia al archivo main.py.

### Nuevo cambio
Pero es una buena práctica de programación siempre agregar el punto de inicio en el archivo main.py de la siguiente forma al final:
```
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:api", host="127.0.0.1", port=8000, reload=True)
```
De este modo, se puede ejecutar el archivo main.py desde un entorno de Python con el siguiente comando:
```
python main.py
```

## Parámetro 3: Endpoints   
Los endpoints para este proyecto son los siguientes:
1. GET "/"
2. GET "/health/live"
3. GET "/health/ready"
4. GET "/api/version"

## Parámetro 4: Variables de entorno y dependencias externas
Estas son las siguientes variables de entorno utilizadas, las cuales son llamadas en los archivos config.py y database.py:
1. APP_NAME
2. DB_HOST
3. DB_PORT
4. DB_NAME
5. DB_USER
6. DB_PASSWORD
Y estas variables ayudan a conectar con la base de datos externa PostgreSQL, que en este caso sería la dependencia externa.

## Parámetro 5: Endpoint que demuestra liveness
El endpoint GET /health/live, de no encontrar ningún problema, devolverá que el status de la API es alive, y se localiza en la línea 13 del archivo main.py:

if stats = good -> retrn = alive

## Parámetro 6: Dependencia que condiciona readiness
En la línea 16 se encuentra el endpoint ready. Este endpoint devolverá healthy de tener conexión con la base de datos, o de haber algún error, capturará la excepción y devolverá un error 503.

Entregables:
[x] Diagrama simple.
[x] Lista de variables.
[x] Comando de ejecución.
[x] Lista de endpoints.
[x] Explicación de liveness vs readiness.