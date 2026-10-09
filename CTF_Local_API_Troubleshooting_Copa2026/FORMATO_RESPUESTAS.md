# Formato de respuestas / evidencias

Este archivo indica **cómo presentar una respuesta correcta**, pero NO contiene las soluciones.

---

## Reto 1

### Hallazgo
`<describir comportamiento observado>`

### Request usado
```bash
<curl o request de Postman>
```

### Respuesta ANTES
```text
HTTP/1.1 <código observado>
<body observado>
```

### Causa raíz
`<explicación técnica breve>`

### Archivo modificado
`<ruta del archivo>`

### Respuesta DESPUÉS
```text
HTTP/1.1 <código exigido por el contrato>
<body coherente con el endpoint>
```

---

## Reto 2

### Caso probado
`<header ausente / incorrecto / correcto / JSON inválido>`

### Request
```text
<método + URL + headers/body usados>
```

### Resultado esperado según el enunciado
```text
HTTP <código>
```

### Evidencia observada
```text
<status + body>
```

### Diagnóstico
`<causa raíz>`

### Validación final
`<evidencia>`

---

## Reto 3

### `/health/live`
```text
HTTP <código>
<body>
```

### `/health/ready`
```text
HTTP <código>
<body>
```

### Prueba de dependencia
```text
<comando/herramienta utilizada>
```

### Hipótesis
`<qué componente sospechan y por qué>`

### Causa raíz
`<causa real encontrada>`

### Validación
```text
/live  -> <código>
/ready -> <código>
```

---

## Reto 4

### Request que reproduce el fallo
```bash
<comando>
```

### Resultado
```text
HTTP 500
```

### Evidencia de logs
```text
<solo las líneas relevantes>
```

### Causa raíz
`<explicación>`

### Cambio mínimo
`<archivo y objetivo del cambio>`

### Validación final
```text
HTTP <código correcto>
```

### CORS
```text
Origin probado: http://localhost:3000
Header CORS observado: <valor>
```

---

# Regla de respuesta CTF

Una respuesta sólida debe contener:

**Síntoma → Evidencia → Causa raíz → Cambio mínimo → Validación**

No basta con decir:

> “Ya funciona”.
