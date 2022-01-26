# Created By  : Galileo Garibaldi, Simón López
# Created Date: 25/01/2022 
# Modified Date: -
# version ='1.0'

"""
Controller
----------
Archivo encargado de hacer las operaciones de DDL en SQL, es decir, agregar, seleccionar y eliminar
"""
from api3.student_api.models.Student import Student
from api3 import db

def convertToJson(student: Student):
    """Convertir el objeto de tipo **Student**

    Parameters
    ----------
    student : Student
        Objeto de tipo **Student**, el cual tiene como parámetros: id, name, age, state

    Returns
    -------
    JSON
        json con el formato de los tipos de dato
    """
    return {
       "id":student.id,
       "name":student.name,
       "age":student.age,
       "status":student.status
    }
    
def insert_student(json_data):
    """Insertar datos al json de Estudiante

    Parameters
    ----------
    json_data : json
        Json con el formato: { "age":2, "name":"Nombre", "status":1 }

    Returns
    -------
    Json
        json con el formato de los tipos de dato
    """
    s = Student(name=json_data["name"], age=json_data["age"], status=json_data["status"])
    db.session.add(s)
    db.session.commit()
    return json_data

def select_all_student():
    """Seleccionar todos los registros de los estudiantes

    Returns
    -------
    Json
        json con el formato de los tipos de dato
    """
    student = Student.query.all()
    res =[convertToJson(p) for p in student]
    return res

def select_student_by_id(id):
    """Seleccionar registros de estudiantes por su ID

    Parameters
    ----------
    id : int
        Id del estudiante (PK)

    Returns
    -------
    Json
        json con el formato de los tipos de dato
    """
    return convertToJson(student=Student.query.get(id))

def delete_student(id):
    """Eliminar un registro de el estudiante por su ID

    Parameters
    ----------
    id : int
        ID del estudiante (PK)

    Returns
    -------
    Json
        json con el formato de los tipos de dato
    """
    student=Student.query.get(id)
    if not student:
        return None
    db.session.delete(student)
    db.session.commit()
    return "Sucess"