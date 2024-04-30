from django.shortcuts import render
from accounts.models import Student
from rest_framework.renderers import JSONResponse
from accounts.serializers import StudentSerializer
# Create your views here.

def student_details(request):
    stu = Student.objects.get(id=1)
    serializer = StudentSerializer(stu)
    json_data = JSONResponse().render(serializer.data)

