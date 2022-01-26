# Created By  : Galileo Garibaldi, Simón López
# Created Date: 25/01/2022 
# Modified Date: -
# version ='1.0'

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
    
category_view = ControllerStudent.as_view('category_view')
app.add_url_rule('/api/student/',view_func=category_view,methods = ['GET', 'POST','PUT'])

app.add_url_rule('/api/student/<int:id>',view_func=category_view,methods = ['GET', 'POST','DELETE'])
