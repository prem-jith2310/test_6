from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import tbl_school, tbl_teacher, tbl_student, tbl_staff

from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import authentication_classes
from rest_framework import *
from django.contrib.auth import authenticate


import json

def success_response(response, status_code=None):
    json_obj = {
        "hasError": False,
        "errorcode": -1,
        "message": "Success",
    }
    json_obj["response"] = response
    if status_code is None:
        return Response(json_obj, status=status.HTTP_200_OK)
    return Response(json_obj, status=status_code)


def failure_response(response, status_code=None, error_code=1001, message="Failure"):
    json_obj = {
        "hasError": True,
        "errorcode": error_code,
        "message": message,
    }
    json_obj["response"] = response
    if status_code is None:
        return Response(json_obj, status=status.HTTP_200_OK)
    return Response(json_obj, status_code)


class addSchool(APIView):
    def post(self, request):
        datas = {}
        response = {}

        try:
            school = tbl_school()
            school.name = request.POST['name']
            school.place = request.POST['place']
            school.district = request.POST['district']
            school.hmname = request.POST['hmname']
            school.typee = request.POST['typee']
            school.save()
            datas = {
                "Name": school.name,
                "Place": school.place,
                "District": school.district,
                "HM Name": school.hmname,
                "Type": school.typee
            }
        except Exception as e:
            return failure_response(response)
        
        response = {}
        response["isSuccess"] = True
        response["statusMessage"] = "successfully done"
        response["data"] = datas
        return success_response(response)
    


class addTeacher(APIView):
    def post(self, request):
        datas = {}
        response = {}

        try:
            tecaher = tbl_teacher()
            tecaher.name = request.POST['name']
            tecaher.age = request.POST['age']
            tecaher.qualification = request.POST['qualification']
            tecaher.experience = request.POST['experience']
            tecaher.salary = request.POST['salary']
            tecaher.save()
            datas = {
                "Name": tecaher.name,
                "Age": tecaher.age,
                "Qualification": tecaher.qualification,
                "Experience": tecaher.experience,
                "Salary": tecaher.salary,
            }

        except Exception as e:
            return failure_response(response)
        
        response = {}
        response["isSuccess"] = True
        response["statusMessage"] = "successfully done"
        response["data"] = datas
        return success_response(response)
    


class addStudent(APIView):
    def post(self, request):
        datas = {}
        response = {}

        try:
            student = tbl_student()
            student.name = request.POST['name']
            student.age = request.POST['age']
            student.school = request.POST['school']
            student.teacher = request.POST['teacher']
            student.save()
            datas = {
                "Name": student.name,
                "Age": student.age,
                "School": student.school,
                "Teacher": student.teacher
            }

        except Exception as e:
            return failure_response(response)
        
        response = {}
        response["isSuccess"] = True
        response["statusMessage"] = "successfully done"
        response["data"] = datas
        return success_response(response)
    


class addStaff(APIView):
    def post(self, request):
        datas = {}
        response = {}

        try:
            staff = tbl_staff()
            staff.name = request.POST['name']
            staff.designation = request.POST['designation']
            staff.experience = request.POST['experience']
            staff.salary = request.POST['salary']
            staff.save()
            datas = {
                "Name": staff.name,
                "Designation": staff.designation,
                "Experience": staff.experience,
                "Salary": staff.salary
            }

        except Exception as e:
            return failure_response(response)
        
        response = {}
        response["isSucess"] = True
        response["statusMessage"] = "successfully done"
        response["data"] = datas
        return success_response(response)



class viewSchool(APIView):
    def get(self, request):
        p = tbl_school.objects.all()
        a = []

        if p is not None:
            for x in p:
                data = {
                    "Name": x.name,
                    "Place": x.place,
                    "District": x.district,
                    "HM Name": x.hmname,
                    "Type": x.typee
                }
                a.append(data)
            response = {}
            response["isSuccess"] = True
            response["statusMessage"] = "successfully done"
            response["data"] = a
            return success_response(response)
        else:
            return failure_response(response)
        


class viewTecaher(APIView):
    def get(self, request):
        p = tbl_teacher.objects.all()
        a = []

        if p is not None:
            for x in p:
                data = {
                    "Name": x.name,
                    "Age": x.age,
                    "Qualification": x.qualification,
                    "Experience": x.experience,
                    "Salary": x.salary
                }
                a.append(data)
            response = {}
            response["isSuccess"] = True
            response["statusMessage"] = "successfully done"
            response["Data"] = a
            return success_response(response)
        else:
            return failure_response(response)
        

class viewStudent(APIView):
    def get(self, request):
        p = tbl_student.objects.all()
        a = []
        if p is not None:
            for x in p:
                data = {
                    "Name": x.name,
                    "Age": x.age,
                    "School": x.school,
                    "Teacher": x.teacher
                }
                a.append(data)
            response = {}
            response['isSuccess'] = True
            response['statusMessage'] = 'successfully done'
            response['Data'] = a
            return success_response(response)
        else:
            return failure_response(response)
        

class viewStaff(APIView):
    def get(self, request):
        p = tbl_staff.objects.all()
        a = []
        if p is not None:
            for x in p:
                data = {
                    "Name": x.name,
                    "Designation": x.designation,
                    "Experience": x.experience,
                    "Salary": x.salary
             }
                a.append(data)
            response = {}
            response['isSuccess'] = True
            response['statusMessage'] = 'successfully done'
            response['Data'] = a
            return success_response(response)
        else:
            return failure_response(response)
        

class deleteSchool(APIView):
    def post(self, request):
        data = {}
        response = {}
        user_id = request.data['school_id']

        try:
            p = tbl_school.objects.get(id = user_id)
            if p:
                p.delete()
            else:
                response['statusMessage'] = "user not found"
                return failure_response(response)
        except Exception as e:
            response['statusMessage'] = "user not found"
            return failure_response(response)
        
        response = {}
        response["isSuccess"] = True
        response["statusMessage"] = "successfully done"
        # response["data"] = data
        return success_response(response)
    

class deleteStudent(APIView):
        def post(self, request):
            data = {}
            response = {}
            user_id = request.data['student_id']

            try:
                p = tbl_student.objects.get(id = user_id)
                if p:
                    p.delete()
                else:
                    response['statusMessage'] = "user not found"
                    return failure_response(response)
                
            except Exception as e:
                response['statusMessage'] = "user not found"
                return failure_response(response)
            
            response = {}
            response["isSuccess"] = True
            response["statusMessage"] = "successfully done"
            return success_response(response)
        


class deleteTeacher(APIView):
    def post(self, request):
        data = {}
        response = {}
        user_id = request.data['teacher_id']
        
        try:
            p = tbl_teacher.objects.get(id = user_id)

            if p:
                p.delete()
            else:
                response['statusMeassage'] = 'usesr not found'
                return failure_response(response)
            
        except Exception as e:
            response['statusMeassage'] = 'user not found'
            return failure_response(response)
        
        response = {}
        response['isSuccess'] = True
        response["statusMeassage"] = 'successfully done'
        return success_response(response)
    


class deleteStaff(APIView):
    def post(self, request):
        data = {}
        response = {}
        user_id = request.data['staff_id']

        try:
            p = tbl_staff.objects.get(id = user_id)
            if p:
                p.delete()
            else:
                response['statusMessage'] = 'user not found'
                return failure_response(response)
            
        except Exception as e:
            response['statusMessage'] = 'user not found'
            return failure_response(response)
        
        response = {}
        response['isSuccess'] = True
        response["statusMeassage"] = 'successfully done'
        return success_response(response)
    


class updateSchool(APIView):
    def post(self, request):
        data = {}
        response = {}
        user_id = request.data['user_id']
        
        try:
            p = tbl_school.objects.get(id = user_id)
            if p is not None:
                p.name = request.data['Name']
                p.place = request.data['Place']
                p.district = request.data['District']
                p.hmname = request.data['HM Name']
                p.typee = request.data['Type']
                p.save()
                data = {
                    "Name": p.name,
                    "Place": p.place,
                    "District": p.district,
                    "HM Name": p.hmname,
                    "Type": p.typee
                }
            else:
                response['statusMessage'] = 'user not found'
                return failure_response(response)
        except Exception as e:
            response['statusMessage'] = 'user not found'
            return failure_response(response)
        
        response = {}
        response['isSuccess'] = True
        response["statusMessage"] = 'successfully done'
        response['data'] = data
        return success_response(response)
    


class updateTeacher(APIView):
    def post(self, request):
        data = {}
        response = {}
        user_id = request.data['user_id']

        try:
            p = tbl_teacher.objects.get(id = user_id)
            if p is not None:
                p.name = request.data['name']
                p.age = request.data['age']
                p.qualification = request.data['qualification']
                p.experience = request.data['experience']
                p.salary = request.data['salary']
                p.save()
                data = {
                    "Name": p.name,
                    "Age": p.age,
                    "Qualification": p.qualification,
                    "Experience": p.experience,
                    "Salary": p.salary
                }
            else:
                response['statusMessage'] = 'user not found'
                return failure_response(response)
            
        except Exception as e:
            response['statusMessage'] = 'user not found'
            return failure_response(response)
        
        response = {}
        response['isSuccess'] = True
        response["statusMessage"] = 'successfully done'
        response['data'] = data
        return success_response(response)



        


    

        


       

