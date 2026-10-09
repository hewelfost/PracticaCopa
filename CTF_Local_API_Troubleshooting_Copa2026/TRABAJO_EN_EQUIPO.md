# Trabajo en equipo sugerido

Los cuatro trabajan sobre el mismo proyecto.

## Ramas

```text
main
├── reto1-http
├── reto2-auth
├── reto3-health
└── reto4-observabilidad
```

Cada integrante crea su rama.

Ejemplo:

```bash
git switch -c reto1-http
```

Al terminar:

```bash
git add .
git commit -m "fix: complete challenge 1 http contract"
git push -u origin reto1-http
```

Después integran mediante merge/PR.

## Regla

Antes de mergear:

1. `git status`
2. actualizar rama
3. ejecutar API
4. repetir las pruebas de SU reto
5. comprobar que `/health/live` sigue funcionando

Después de integrar los cuatro cambios, todo el equipo ejecuta la validación final.
