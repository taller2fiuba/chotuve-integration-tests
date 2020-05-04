# Pruebas de aceptación

Este repositorio contiene las pruebas de aceptación de Chotuve.

Existen dos scripts para correr las pruebas:
- `run-acceptance-tests.sh`: El script por defecto para integración continua.
- `run-tests-url.sh`: Permite correr las pruebas indicando la URL de cada 
   servicio.

## Correr las pruebas (CI)
Para correr las pruebas en el servidor de integración continua o antes de agregar
cambios a un PR, se utiliza el script `run-acceptance-tests.sh`. 

Este script va a crear una red interna de Docker llamada "chotuve" o utilizar 
una ya existente, levantar una imagen productiva de cada servidor sobre esta
red con una base de datos vacía, y luego correr `behave` apuntándolo a estos
servicios.

Se soportan las siguientes opciones:
- `--chotuve-[app|auth|media]-repo=<directorio>`: Permite indicar donde está
clonado el repositorio para cada uno de los servidores. Si no se indica este
parámetro para algún servidor se lo clonará la rama master de su respectivo
repositorio en Github.
- `--no-docker-for-behave`: Por defecto `behave` se corre dentro de un 
contenedor de Docker para garantizar que la ejecución es siempre la misma y 
evitar ensuciar el sistema. Esto tiene la desventaja de que es un poco más lento,
con lo cual se puede pasar esta opción para correr `behave` directamente en la
máquina local. Require que se instale el archivo `requirements.txt` en la 
máquina previamente.

Ejemplo de uso descargando todos los repositorios:

```bash
$ ./run-acceptance-tests.sh
```

Ejemplo de uso descargando sólo los repositorios de App server y Media server:

```bash
$ ./run-acceptance-tests.sh --chotuve-auth-repo=../chotuve-auth-server
```

## Correr las pruebas (indicando URL)
Es posible correr las pruebas de aceptación sin levantar ningún servicio, 
indicándole a `behave` la URL de cada uno de los servidores. Esto se hace 
corriendo el script `run-tests-url.sh`.

Este script únicamente va a correr `behave` apuntándolo a las URL indicadas.

Se soportan las siguientes opciones:
- `--chotuve-[app|auth|media]-url=<URL>`: **Requerido**. Indica cuál es la URL
de cada servidor.
- `--no-docker-for-behave`: Al igual que en `run-acceptance-tests.sh`, permite
elegir correr `behave` en la máquina local.

Ejemplo de uso:

```bash
$ ./run-tests-url.sh --chotuve-media-url=http://localhost:27080 --chotuve-auth-url=http://localhost:26080 --chotuve-app-url=http://localhost:28080
```
