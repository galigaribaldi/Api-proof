#from my_app import app
from flask import Blueprint
###
from app import db
from models import Task

task = Blueprint('task',__name__)

def get_by_status(status):
    tasks = db.session.query(Task).filter(Task.status == status)
    return tasks

def get_by_description(description):
    search = "%{}%".format(description)
    tasks = db.session.query(Task).filter(Task.description.like(search)).all()
    return tasks

def insert(description,duration,time_registred,status):
    t = Task(description=description, duration=duration,time_registred=time_registred, status=status)
    db.session.add(t)
    db.session.commit()
    return t

def update(description,duration,time_registred,status,id):
    t = db.session.query(Task).filter(Task.id == id).first()
    if(t.status):
        return "No puede ser actualizada debido a que ya ha sido completada"
    else:
        t.description = description
        t.duration = duration
        t.time_registred = time_registred
        t.status = status
        db.session.add(t)
        db.session.commit()
        return t

def delete(id):
    tasks = db.session.query(Task).filter(Task.id == id).delete()
    db.session.commit()
    return "Eliminado con exito"