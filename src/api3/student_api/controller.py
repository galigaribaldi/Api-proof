from api3.student_api.models.Student import Student
from api3 import db

def convertToJson(student: Student):
    return {
       "id":student.id,
       "name":student.name,
       "age":student.age,
       "status":student.status
    }
    
def insert_student(json_data):
    s = Student(name=json_data["name"], age=json_data["age"], status=json_data["status"])
    db.session.add(s)
    db.session.commit()
    return json_data

def select_all_student():
    student = Student.query.all()
    res =[convertToJson(p) for p in student]
    return res

def select_student_by_id(id):
    return convertToJson(student=Student.query.get(id))

def delete_student(id):
    student=Student.query.get(id)
    if not student:
        return None
    db.session.delete(student)
    db.session.commit()
    return "Sucess"