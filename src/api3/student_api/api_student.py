from api3 import app
from flask.views import MethodView
from flask import request
import api3.student_api.controller as controller
from api3.helper.convert_data import sendResJson

class ControllerStudent(MethodView):
    def get(self, id=None):
        if id:
            student = controller.select_student_by_id(id)
        else: 
            student = controller.select_all_student()
        return sendResJson(student, code=200)
    
    def post(self):
        d = controller.insert_student(request.json)
        return d
    
    def delete(self, id):
        student = controller.delete_student(id)
        print(student)
        if student:
            return sendResJson(code=200, data="Sucess")
        else:
            return sendResJson(code=404,data="")
    
    def put(self):
        return {"debug":"Not implemented"}
    
category_view = ControllerStudent.as_view('category_view')

app.add_url_rule(
    '/api/student/',
    view_func=category_view,
    methods = ['GET', 'POST','PUT']
    )

app.add_url_rule(
    '/api/student/<int:id>',
    view_func=category_view,
    methods = ['GET', 'POST','DELETE']
    )
