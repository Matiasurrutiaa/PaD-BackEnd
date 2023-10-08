# PaD-BackEnd
BackEnd del sistema de recuperacion de informacion Politica al Dia

## Contexto del proyecto
Para la realizacion del proyecto estaremos desarrollando una api rest con django y django rest framework haciendo uso de una base de datos noSQL (MongoDB) para el almacenamiento de archivos. 

## Carpeta raiz del proyecto
La carpeta raiz del proyecto corresponde a ```Politica Al Dia``` en esta se encuentran los archivos de configuracion relacionados al proyecto django. Algo importante a notar es el archivo Settings donde se encuentra las lineas de configuracion para la base de datos. 

## Creación del Virtualenv

Para mantener un entorno de desarrollo aislado, se recomienda el uso de un entorno virtual. Si no tienes `virtualenv` instalado, puedes hacerlo con el siguiente comando:

```bash
pip install virtualenv
```
Una vez ya instalado debemos de crear un entorno virtual con el siguiente comando

```bash
virtualenv venv
```
Ya teniendo creado el entorno virtual de trabajo podemos acceder con el siguiente comando

```bash
.\venv\Scripts\activate
```
En algunos casos es posible que se presente un mensaje de error relacionado a las politicas de ejecucion de scripts, por lo que en caso de presentarse este problema debemos introducir este comando en la misma terminal.

```bash
Set-ExecutionPolicy Unrestricted -Scope Process
```
Este comando nos permite ejecutar bypassear la seguridad unicamente dentro de la misma terminal, por lo que en situaciones futuras es necesario ingresar el comando nuevamente para ingresar al venv. Pero si se desea ingresar una sola vez simplemente remover ```-Scope Process```.

Ya una vez dentro del entorno virtual debería aparecer ``(venv)`` en la consola de comandos. Solo continuar en caso de que ese sea el caso.

## Instalación de librerías y paquetes necesarios para el desarrollo de la aplicacion*
En una consola de comandos, ejecutar:
```
pip install -r requirements.txt
```
Con esto ya tendriamos todo lo necesario para trabajar en el proyecto.

## Realizar las migraciones y correr el proyecto.
Para realizar las migraciones en una consola o terminal ingresar el siguiente comando:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
Con estos conmandos se crean los archivos que se van a migrar y finalmente se migran a la base de datos

## Correr el proyecto
Para correr el proyecto es necesario introducir lo siguiente en la terminal de comandos:
```
python manage.py runserver
```
Se le comunicara por la misma terminal la direccion local para ingresar.

## Urls
```/noticias/```
```/noticias/news```

URLs iniciales, por lo que una vez inciado y corriendo el proyecto es necesario añadir a la url esta direccion para acceder a la api.

## Anexos
Hay total libertad de experimentar y probar cosas mientras incorporen las funcionalidades requeridas para el proyecto asi que no se limiten unicamente a las tecnologias y librerias escogidas.
