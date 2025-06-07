# Programación para la Ciencia de datos - PEC4

 Este repositorio está dedicado a la solución de la **Práctica 4** de la asignatura **Programación para la Ciencia de datos** del **Máster de Ciencia de Datos de la UOC**.
 
## Contenido del repositorio:
- **main.py**: es el script principal con los 5 apartados del ejercicio a realizar resueltos.
- **data**: contiene el dataset de embalses catalanes que hemos utilizado.
- **doc**: contiene la documentacion en formato HTML de todas las funciones.
- **embassaments**: es un modulo que contiene a su vez submodulos con todas las funciones auxiliares necesarias para ejecutar el script main.
- **img**: contiene dos imagenes, resultado de los apartados 3 y 4 del ejercicio.
- **test**: contiene algunos test para asegurar que las funciones devuelvan los resultados correctos.
- **screeshots**: contiene las capturas de pantalla requeridas por el profesor.
- **.gitignore**: archivo que excluye algunos archivos a la hora de subir a GitHub.
- **LICENSE**: licencia seleccionada, en nuestro caso MIT adecuada para fines académicos.
- **requirements.txt**: archivo necesario para recrear el entorno virtual.
- **README.md**: archivo que estas leyendo ahora mismo.


## Como podemos ejecutar el script?

1. Creamos un entorno virtual e instalamos las dependencias necesarias

   - Linux/macOS
    ```bash
    python3 -m venv venv --system-site-packages

    source venv/bin/activate
    ```

   - Windows
    ```cmd
    python3 -m venv venv

    venv\Scripts\activate
    ```

   - Actualizar pip
    ```bash
    python -m pip install --upgrade pip
    ```
    - Instalar requirements
    ```bash
    pip install -r requirements.txt
    ```

2. Una vez instalado y activado el entorno virtual procedemos a hacer los tests
    ```bash
    python -m unittest discover -s tests -v
    ```

3. También podemos comprobar el coverage
    ```bash
    coverage run -m unittest discover -s tests -v
    coverage report
    ```

4. Si los resultados han sido exitosos podemos proceder a ejecutar el script main:
    ```bash
    python main.py
    ```
    también podemos ejecutar hasta el ejercicio que deseemos (por ejemplo el 3) usando el siguiente parámetro:
    ```bash
    python main.py -ex 3
    ```

## Extras

Para crear la documentación simplemente basta con ejecutar en la terminal:
```bash
pdoc embassaments -o doc
```

Para comprobar el linting ejecutamos en la terminal:
```bash
pylint embassaments main.py
```

---

*Autor: Pablo Perez Verdugo*
