# Documentación con Flask y Sphinx

Ésta rama se centra en la doccumentación de una sencilla API. Éste contiene 2 carpetas:

- **docs:** Carpeta donde se encuentra la documentación del proyecto en formato html y pdf
- **src:** Carpeta donde se encuentra el código del proyecto.

A continuación se explicará como generar la documentación del proyecto, mientras que el funcionamiento del mismo, se dejará explicaco con ayuda de la documentación.

## Sphinx

1. Instalar las librerías necesarios con **pip** o **pip3**

   1. ```bash
      pip3 install sphinx
      ## o bien
      pip install -U Sphinx
      ```

2. Comenzar la estructura del proyecto con el comando quickstart

   1. ```bash
      sphinx-quickstart docs
      ```

3. A continuación se presentarán opciones para comenzar el proyecto, se recomienda seguir los pasos

   1. ```bash
      > Separar directorios fuente y compilado (y/n) [n]: n
      > Nombre de proyecto: Api-Proof (cambiar al tuyo)
      > Autor(es): Galileo Garibaldi
      > Liberación del proyecto []: 1.0 (Versión)
      > Lenguaje del proyecto [en]: en
      ```

4. Una vez concluido los pasos de arriba, se generará una estructura similar a la siguiente

   ![path1](/ASSETS/img/path1.png)

5. A continuación se modificarán los sigueintes archivos

   1. **conf.py:** Éste archivo contiene las configuraciones de ruta, extensiones y temas

      ```python
      # -- Path setup --------------------------------------------------------------
      
      # If extensions (or modules to document with autodoc) are in another directory,
      # add these directories to sys.path here. If the directory is relative to the
      # documentation root, use os.path.abspath to make it absolute, like shown here.
      # Añadir el path de los archivos
      import os
      import sys
      sys.path.insert(0, os.path.abspath('..')) ##Subir un nivel en los archivos
      sys.path.insert(0, os.path.abspath('../src')) ##Carpeta donde contienen los archivos
      ##Alguna otra Carpeta donde se encuentre el código
      #############
      #############
      #############
      #############			Configuraciones del documento
      #############
      #############
      #############
      
      # Add any Sphinx extension module names here, as strings. They can be
      # extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
      # ones.
      ###Extensiones
      extensions = ['sphinx.ext.todo', 'sphinx.ext.viewcode', 'sphinx.ext.autodoc']
      
      # Add any paths that contain templates here, relative to this directory.
      templates_path = ['_templates']
      
      # List of patterns, relative to source directory, that match files and
      # directories to ignore when looking for source files.
      # This pattern also affects html_static_path and html_extra_path.
      exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
      ```

   2. **index.rst:** Éste archivo contiene el índice de archivos y árbol jerárquico de los archivos, si no se modifica, no aparecerá nada en la documentación

      ```rst
      .. Api Proof documentation master file
      
      Welcome to Api Proof's documentation!
      =====================================
      ---Archivos en los cuales se encuentra el código
      ---Colocar los nombres sin la extensión
      .. auomodule:: run
         :members:
      ---Archivos en los cuales se encuentra el código pero en otra ruta
      ---Para especificar un archivo dentro de otra ruta, es importante ponerle
      --- un punto(.)
      .. automodule:: api3.student_api.api_student
         :members:
      ```

6. Una vez teniendo éstos archivos, se dan algunas recomendaciones generales:

   1. Se recomienda usar el estilo de documentación de pandas, ya que es el mas claro, sin emabrgo puedes usar la configuración de google u otro estándar, para visualizar otro tipo de documentación, se recomienda ver la bibliografía
   2. Se recomienda usar la extensión de VSCode, **AI Python Docstring Generator** para documentar cada parte![AIDoc](/ASSETS/img/AIDoc.png)

7. Una vez teniendo éstos archivos, se procedrá a documentar el el archivo **api_student.py** y **run.py**

   1. **run.py**

      ```python
      """
      Run
      ------
      Archivo de tipo main, para correrlo, sólo es necesario correr en la terminal lo siguiente
          $ python3 run.py
      
      """
      from api3 import app
      ###Se recomienda comentar el archivo de acción, ya que cuando se construyen los archivos, se corre también el interprete de python
      #app.run()
      ```

   1. **api_student.py**

      ```python
      """
      Api Student
      ------------
      Archivo encargado de definir las rutas y los parámetros a funcionar dentor de cada de
      endpoint con los protocolos Web (POST, GET, DELETE, PUT)
      
      Notes
      -----
      Ruta en la que se pone la API: **/api/student/**
      """
      from api3 import app
      from flask.views import MethodView
      from flask import request
      import api3.student_api.controller as controller
      from api3.helper.convert_data import sendResJson
      
      class ControllerStudent(MethodView):
          """Clase encargada de definir los protocolos Web Get, Post, Delete, Put.
      
          Parameters
          ----------
          MethodView : class
              Clase heredada de la biblioteca de Flask (flask.views)
          """
          def get(self, id=None):
              """Método Get para traer los datos de Estudiantes
      
              Parameters
              ----------
              id : int, optional
                  ID del estudiante a encontrar, by default None
      
              Returns
              -------
              JSON
                  JSON con la estructura mencionada en **sendResJson**
              """
              if id:
                  student = controller.select_student_by_id(id)
              else: 
                  student = controller.select_all_student()
              return sendResJson(student, code=200)
          
          def post(self):
              """Método para publicar un nuevo estudiante
              
              Notes
              -----
              Se describe el Json que se manda para publicar un estudiante::
                  $ { "age":2, "name":"Nombre", "status":1 }
              
              Returns
              -------
              JSON
                  JSON con la estructura mencionada en **sendResJson**
              """
              d = controller.insert_student(request.json)
              return d
          
          def delete(self, id):
              """Método encargado de eliminar registros
      
              Parameters
              ----------
              id : int
                  ID del Estudiante a eliminar
      
              Returns
              -------
              JSON
                  JSON con la estructura mencionada en **sendResJson**
              """
              student = controller.delete_student(id)
              print(student)
              if student:
                  return sendResJson(code=200, data="Sucess")
              else:
                  return sendResJson(code=404,data="")
          
          def put(self):
              """Método encargado de modificar los registros
      
              Returns
              -------
              JSON
                  JSON con la estructura mencionada en **sendResJson**
              """
              return {"debug":"Not implemented"}
       
      ###Al igual que en el caso anterior, se recomienda comentar los archivos de acción.
      #category_view = ControllerStudent.as_view('category_view')
      #app.add_url_rule('/api/student/',view_func=category_view,methods = ['GET', 'POST','PUT'])
      
      #app.add_url_rule('/api/student/<int:id>',view_func=category_view,methods = ['GET', 'POST','DELETE'])
      
      ```

8. Finalmente teniendo todos los archivos comentados, se procede a construir la documentación:

   1. Asegurarse estar dentro de la carpeta **docs**

   2. Ejecutar los comandos: **make html** para construir una documentación de tipo html

   3. Ésto generará en la carpeta **_build** la carpeta **html**, dentro de la misma, encontraremos el archivo **index.html**

      ![tree](/ASSETS/img/tree.png)

9. Como camino alternativo se puede generar un archivo **.pdf** a través de generarlo con **látex**

   1. Asegurarse estar dentro de la carpeta **docs**

   2. Agregar al archivo **conf.py**, las líneas siguientes

      ```python
      ####Latex Extension
      latex_engine = 'pdflatex'
      latex_elements = {
          'papersize': 'a4paper',
          'pointsize': '10pt',
          }
      ```

   3. Ejecutar el comando **make latexpdf**, sin embargo para poder ejecutar este comando, previamennte se debe tener instalado **látex**

   4. Pasarán algunos segundos - Minutos, dependiendo de que tan largo sea el proyecto, una vez terminada la ejecución del mismo, se producirá una nueva carpeta a la misma altura que **html**, pero con el nombre **latex**, dentro del mismo estarán todas las extensiones de látex y los archivos propios de éstos archivos, al igaual que, el archivo **apiproof.pdf**

   ![LatexFiles](/ASSETS/img/LatexFiles.png)

## Bibliografía

[Documentación oficial de Sphinx](https://www.sphinx-doc.org/es/master/index.html)

[Docstring Google](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

[Docstirng Numpy](https://numpydoc.readthedocs.io/en/latest/format.html)

[Docstring Python](https://docs.hektorprofe.net/python/documentacion-y-pruebas/docstrings/)

