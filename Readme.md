# CORE

Este proyecto contiene todo lo necesario para trabajar en el desarrollo de CORE
que es un sistema para FUNCIONES.
Como base se utiliza el framework Django y el bundler Snowpack.
La base de datos a utilizar es PostgreSQL, tanto en el desarrollo local como en
producción.

## Instrucciones

Para correr el proyecto es necesario tener instalado make, Docker y Docker
Compose en el equipo.
Una vez cubiertos estos requisitos solo es necesario ejecutar el siguiente
comando:

```
make serve
```

De esta forma se levantará el servidor en el puerto 8000 de la computadora.
Para acceder al mismo basta con entrar a http://localhost:8000.
Una vez que se haya terminado de trabajar en él, se puede detener el servidor
utilizando las teclas `ctrl + c`.

## Testing

Para ejecutar las pruebas existen los comandos:

- `make python-test`
- `make python-test-watch`
- `make javascript-test`
- `make javascript-test-watch`

La diferencia es que el primero ejecuta las pruebas una sola vez, mientras que
el segundo se ejecuta de forma constante cada vez que se detecta un cambio en
los archivos de pruebas (al guardarlos).

### Functional testing

Las pruebas funcionales utilizan Cypress como base, lo cual requiere tener
instalado NodeJS de forma local.
Para ejecturlas es necesario utilizar el comando `./integration-server.sh` que
inicializa el servidor y abre Cypress para ejecutar las pruebas.

## Linting

Este proyecto está configurado para garantizar que se mantenga la consistencia
en el estilo utilizado para escribir código.
Para lograrlo se utiliza una serie de linters que verifican el estado del
código.
Los siguientes comandos permiten realizar las distintas revisiones:

```
make lint
make python-lint
make javascript-lint
```

Aunque no es posible corregir de forma automática todos los errores las
siguientes herramientas pueden tratar de corregirlos.

```
make lint-fix
make python-lint-fix
make javascript-lint-fix
```

## Consideraciones adicionales

Cuando las dependencias del proyecto cambien y se esté usando docker compose
para correrlo será necesario actualizar el contenedor de Docker.
Para esto solo se debe de volver a correr el proyecto con el siguiente comando

```
docker-compose up --build
```

Happy coding
