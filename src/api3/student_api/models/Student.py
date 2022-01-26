"""
Student
-------
Modelo de la tabla Student, la cual se mapea a la base de datos con la ayuda de la bilbioteca
SQLAlchemy
"""
from api3 import db
class Student(db.Model):
    """Mapeado de Student

    Parameters
    ----------
    db : Class
        Clase heredada de SQLAlchemy, **NO MODIFICABLE**.
        Se describen los parámetros que tiene la tabla Student:
            | 1.- ID: Entero (Llave primaria)
            | 2.- Name: Cadena
            | 3.- Age: Entero 
            | 4.- Status: Bool
    
    Returns
    -------
    tuple
        Tupla con el siguiente formato: "Task Id, Name, Duracion"
    """
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    status = db.Column(db.Boolean)
    
    def __init__(self, name, age, status):
        self.name = name
        self.age = age
        self.status = status
    def __repr__(self):
        return 'Task Id: %d, NAme: %s, Duracion: %d' % (self.id, self.name, self.age)