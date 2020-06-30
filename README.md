# Pruebas de aceptación

Este repositorio contiene las pruebas de aceptación de Chotuve.

## Convenciones al escribir las pruebas de aceptación

Las pruebas de aceptación mantienen un contexto entre paso y paso con la 
información relevante a la característica que se desea probar. Para mantener la
consistencia entre pasos, se definen algunas convenciones sobre nombres de 
atributos dentro del contexto:
- `context.yo`: Instancia de `ChotuveAppClient` que refiere a la primera persona
de las pruebas. Se carga en los pasos del estilo "inicié sesión".
- `context.yo.last_response`: Última respuesta obtenida del app server. No es
necesario verificar que las respuestas devuelvan 200/201/etc. en caso de que no
fuera así se lanzará una excepción.
- `context.error`: Si se espera que una solicitud falle (no devuelva 2**) la 
**excepción** generada por la instancia de `ChotuveAppClient` se debe atrapar y 
almacenar en este atributo.
- `context.data`: Si se espera que una solicitud devuelva datos, los datos 
recibidos se deben almacenar en este atributo.


## Correr las pruebas (local)
Existen 5 scripts para correr las pruebas:
- `run-acceptance-tests.sh`: El script por defecto para integración continua.
- `run-tests-url.sh`: Permite correr las pruebas indicando la URL de cada 
   servicio.
- `dev-run-acceptance-tests-url.sh`: Para correr las pruebas localmente con las
   URL por defecto apuntando a `localhost` y su respectivo puerto.
- `behave-local-url-dev.sh`: Igual al anterior pero corre `behave` localmente
   en lugar de correrlo dentro de una imagen de Docker.
- `dev-run-acceptance-tests-repo.sh`: Para correr las pruebas localmente 
   levantando la imagen desde la carpeta con el repositorio de cada servidor,
   ubicada en `../chotuve-*-server`.

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
