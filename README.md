# Autofillingoogleforms

Automatización diligenciamiento Google Forms.

Requerimientos:

* **Python 3.8 o superior**

* **Paquetes**:

  Usa pip o pip3 para installar los paquetes. 
  
  Si tienes problemas durante la instalación, usa el comando sudo.
  
  > sudo pip3 install packageName

  -  gspread

  -  oauth2client

  -  selenium

  -  pyunitreport


* **Google Cloud - Free Account**

  -  Habilita el recurso Google Sheets API
   
  -  Habilita el recurso Google Drive API
  
  -  En la configuración de Google Sheets crea una credencial - Cuenta de Servicio - Crea una key o llave JWT - Descarga el archivo .json y añadelo dentro de la carpeta creds



### Recomendación:
Crea un entorno virtual de python. Usa el siguiente comando dentro de la carpeta en la cual vas a clonar el repositorio.
> python3 -m venv venv 



### Ejecución

- Clona el repositorio.
- Instala los 4 paquetes requeridos con el comando pip o pi3
- Descarga el archivo json de Google Cloud - Ver instrucciones -
- Una vez dentro de la carpeta de la app, ejecuta el siguiente comando en la terminal.

> python3 app.py



### Créditos

* Jhon Aldana
* Javier Bedoya
* Wilson Fino
* Ramón Castaño
* Miguel Sánchez
