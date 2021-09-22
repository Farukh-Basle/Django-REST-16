
from django.shortcuts import render
from Serialize_App.models import Employee
from Serialize_App.forms import EmployeeModelForm
from django.http  import HttpResponse
import json
from django.views import View
from django.core.serializers import serialize

# Non_Id Based operations
class EmployeeListView(View):
    def get(self,request): # db --->> qs --->> dict --->> json ---> browser
        employee_list = Employee.objects.all()  # [{ }, { }, { },..]  or [ ]

        json_meta_data = serialize('json', employee_list)

        emp_dict = json.loads(json_meta_data)

        employee_list = []

        for emp in emp_dict:
            employee_list.append(emp['fields'])

        json_data = json.dumps(employee_list)

        return HttpResponse(json_data, content_type='application/json')



    def post(self,request):
        pass


# Id Based operations
class EmployeeDetailView(View):
    def get(self, request,id): # db---qs ---dict --- json --- browser
        try:
            employee = Employee.objects.get(eno=id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'message' : 'Requested resource not available to get.'})
            return HttpResponse(json_data,content_type='application/json')
        else:
            # emp_dict = {
            #     "eno" : employee.eno,
            #     "ename" : employee.ename,
            #     "salary" : employee.salary,
            #     "email" : employee.email,
            # }
            # json_data = json.dumps(emp_dict)
            json_meta_data = serialize('json',[employee])

            emp_dict = json.loads(json_meta_data)

            employee_list = []

            for emp in emp_dict:
                employee_list.append(emp['fields'])

            json_data = json.dumps(employee_list)

            return HttpResponse(json_data, content_type='application/json')




    def put(self, request,id):
        pass

    def delete(self, request,id):
        pass



