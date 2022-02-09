# Created By  : Galileo Garibaldi, Simón López
# Created Date: 25/01/2022 
# Modified Date: -
# version ='1.0'

"""
Run
------
Archivo de tipo main, para correrlo, sólo es necesario correr en la terminal lo siguiente
    $ python3 run.py

"""
from api3 import app
from os import environ
if __name__ == "__main__":
    app.run(host = "0.0.0.0",port=int(environ.get("PORT", 8080)),debug =True)
