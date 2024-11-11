# Documentación

## Ejercicio práctico

### Creación de un servidor web para docs


#### Instalación

En este ejercicio utilizaremos `mkdocs` para crear un servidor web que muestre la documentación de nuestro proyecto.

1. Asegurate de tener `python` o `python3` instalado, si no lo tienes, puedes instalarlo con `sudo apt install python3`.
2. Asegúrate de tener `pip` instalado, si no lo tienes, puedes instalarlo con `sudo apt install python3-pip`.
3. Instala `mkdocs`:

```bash
pip install mkdocs
```

Si después de instalar `mkdocs` aun no puedes lanzarlo, puedes intentar con:

```bash
sudo apt install mkdocs
```

#### Creación de un proyecto

Lanza el comando mkdocs new proyecto-prueba para crear un nuevo proyecto de documentación.

Este comando te creará una carpeta llamada `mkdocs-prueba` con la siguiente estructura:

```bash
.
├── docs
│   └── index.md
└── mkdocs.yml
```

- `docs`: es la carpeta donde se encuentran los archivos `.md` que contienen la documentación, es decir, lo que se mostrará en la página web.
- `mkdocs.yml`: es el archivo de configuración de `mkdocs`, aqui puedes cambiar el nombre del proyecto, la url de la página, el tema, y alterar la estructura de la página.
- `index.md`: es el archivo principal de la documentación, cuando entras a la página web, este archivo es el que se muestra por defecto.

#### Lanzar el servidor web

Situandote en la raiz de la carpeta `mkdocs-prueba`, lanza el comando `mkdocs serve` para lanzar el servidor web.

Por defecto, el servidor web se lanza en `127.0.0.1:8000`, abre tu navegador y entra a esa dirección.

#### Exponer servidor localmente

Si queremos que otros dispositivos de la red local puedan acceder a nuestro servidor, podemos lanzar el comando `mkdocs serve --dev-addr=0.0.0.0:8000` para exponer el servidor usando la dirección IP de la máquina.

Asegúrate de abrir el puerto 8000 en el firewall de tu máquina. Por ejemplo, con ufw:

```bash
sudo ufw allow 8000
```

Cuando quieras dejar de exponer el servidor, puedes cerrar el puerto con:

```bash
sudo ufw delete allow 8000
```

#### Modificar `index.md`

Modifica el archivo `index.md` para editar la página principal de la documentación.

#### Crear documentación

1. Crea un archivo `hola.md` en la carpeta `docs` con el siguiente contenido:

```markdown
# Hola mundo

Este es un ejemplo de un archivo markdown.
```

Si has seguido los pasos correctamente, al entrar a la web deberías ver un enlace a `Hola mundo` desde cualquier dispositivo de la red local.

2. Descarga el siguiente documento: https://raw.githubusercontent.com/lifeparticle/Markdown-Cheatsheet/refs/heads/main/README.md y añadelo a la carpeta `docs` con el nombre `cheatsheet.md`.do

Al reiniciar el servidor, verás dos warnings y un error, lee las advertencias, entiende por qué aparecen y corrige los errores.

Descarga los archivos `*.md` adjuntos con el ejercicio y añadelos a la carpeta `docs`.

#### Modificando el titulo de la web

Modifica el archivo `mkdocs.yml` para cambiar el título de la web por uno personalizado.

#### Cambiando el tema

Lanza el siguiente comando con la terminal: `pip install mkdocs-material` para instalar el tema `material` de `mkdocs`.

> Si estás usando pip3, lanza `pip3 install mkdocs-material`.

Modifica el archivo `mkdocs.yml` para cambiar el tema de la web por el tema `material` con el siguiente bloque:

```yaml
# Configuration
theme:
  name: material
  features:
    - announce.dismiss
    - content.action.edit
    - content.action.view
    - content.code.annotate
    - content.code.copy
    # - content.code.select
    # - content.footnote.tooltips
    # - content.tabs.link
    - content.tooltips
    # - header.autohide
    # - navigation.expand
    - navigation.footer
    - navigation.indexes
    # - navigation.instant
    # - navigation.instant.prefetch
    # - navigation.instant.progress
    # - navigation.prune
    - navigation.sections
    - navigation.tabs
    # - navigation.tabs.sticky
    - navigation.top
    - navigation.tracking
    - search.highlight
    - search.share
    - search.suggest
    - toc.follow
    # - toc.integrate
  palette:
    - media: "(prefers-color-scheme)"
      toggle:
        icon: material/link
        name: Switch to light mode
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/toggle-switch
        name: Switch to dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: black
      accent: indigo
      toggle:
        icon: material/toggle-switch-off
        name: Switch to system preference
  font:
    text: Roboto
    code: Roboto Mono
  favicon: assets/favicon.png
  icon:
    logo: logo

# Plugins
plugins:
  - blog
  - search:
      separator: '[\s\u200b\-_,:!=\[\]()"`/]+|\.(?!\d)|&[lg]t;|(?!\b)(?=[A-Z][a-z])'
```

#### Cambiando la estructura del contenido

Modifica el archivo `mkdocs.yml` para cambiar la estructura de la página web.

```yaml
nav:
  - Home: index.md
  - Ejemplos:
    - Hola mundo: hola.md
    - Ejemplo markdown: cheatsheet.md
  - Cheatsheets:
    - Unix: linux.md
    - Git: git.md
    - Documentación: docs.md
    - Docker: docker.md
```

En este ejemplo, hemos dejado un enlace a la página principal, una sección de ejemplos con dos enlaces, y una sección de cheatsheets con cuatro enlaces.

Deberás asegurarte de que los archivos `linux.md`, `git.md`, `docs.md` y `docker.md` existan en la carpeta `docs` y apuntemos correctamente a ellos.

En `mkdocs.ym` puedes alterar la estructura del contenido como quieras, podrías tener todos tus `.md` en `docs` y luego crear las secciones en `mkdocs.yml` para organizarlos.

Sin embargo, si tienes muchos archivos `.md`, lo ideal es organizarlos por carpetas, luego puedes reestructurar este contenido en `mkdocs.yml` como prefieras.

#### Sincronizar tus notas

Idealmente, tendrás tus notas en otra carpeta de más fácil acceso, como `~/Documentos/Notas`.

Esto nos crea un problema, ya que si modificamos un archivo en `~/Documentos/Notas`, no se verá reflejado en `mkdocs-prueba/docs`. Deberíamos copiar y sobreescribir el archivo en `mkdocs-prueba/docs` cada vez que hagamos un cambio y esto es tedioso.

Vamos a solucionar esto utilizando `ln -s`.

1. Situate en la carpeta `mkdocs-prueba/docs` y lanza el siguiente comando:

```bash
ln -s /ruta/a/tus/archivos/md ruta/a/mkdocs-prueba/docs
```

Deberías ver un enlace simbólico en la carpeta `mkdocs-prueba/docs` que apunta a tus archivos `.md`.

Puedes tratar esta carpeta como un acceso directo a tus archivos `.md`, cualquier cambio que hagas en `~/Documentos/Notas` se verá reflejado en `mkdocs-prueba/docs`, y viceversa.

