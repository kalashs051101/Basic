from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apicrud.models import *
from apicrud.serializers import *
from rest_framework.views import APIView
from django.contrib.auth.models import User


# Create your views here.
@api_view(['GET'])
def api_page(request):
    data=api_student.objects.all()
    serializer = student_serializer(data,many=True)
    return Response({'data':serializer.data ,'msg' : 'this is done'})


@api_view(['GET'])
def api_single(request,id):
    data=api_student.objects.get(id=id)
    serializer = student_serializer(data)
    return Response({'data':serializer.data ,'msg' : 'this is done'})

@api_view(['POST'])
def create_data(request):
    data = request.data
    serializer =student_serializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response({'data':serializer.data,'msg':'data fetch'})
    return Response({'error':'error occured'})

@api_view(['DELETE'])
def deletee(request,id):
    data = api_student.objects.get(id=id)
    serializer = student_serializer(data=data)

    if data is not None:
        data.delete()
        return Response({'msg':'data deleted'})
    return Response({'data':serializer.data,'msg':'msg delete succesfully'})



# @api_view(['PATCH'])
# def update_single(request,id):
#     obj=api_student.objects.get(id=id)
#     data=request.data

#     serializer=student_serializer(instance=obj,data=data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response({'data':serializer.data,"msg":'obj saved'})
#     return Response({'error':'error occured'})


@api_view(['PUT'])
def update_all(request,id):

    obj=api_student.objects.get(id=id)
    data=request.data

    serializer=student_serializer(instance=obj,data=data,partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({'data':serializer.data,"msg":'obj saved'})
    return Response({'error':'error occured'})


class studentapi(APIView):
    def get(self,request,id=None):
        if id is not None:
            # id = request.data['id']
            data=api_student.objects.get(id=id)
            serializer=student_serializer(data)
            return Response({'data':serializer.data,'msg':'data fetch bro'})

        else:
            data=api_student.objects.all()
            serializer=student_serializer(data,many=True)
            return Response({'data':serializer.data,'msg':'data fetch bro'})
        # return Response({'data':serializer.data ,'msg' : 'this is done'})
    
    def post(self,request):
        data = request.data
        serializer =student_serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,'msg':'data fetch'})
        
        return Response({'error':'error occured'})

    def put(self,request,id):
        obj=api_student.objects.get(id=id)
        data=request.data

        serializer=student_serializer(instance=obj,data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,"msg":'obj saved'})
        return Response({'error':'error occured'}) 
    
    def patch(self,request,id):
        obj=api_student.objects.get(id=id)
        data=request.data

        serializer=student_serializer(instance=obj,data=data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,"msg":'obj saved'})
        return Response({'error':'error occured'})
           
    def delete(self,request,id):
        data = api_student.objects.get(id=id)
        serializer = student_serializer(data=data)

        if data is not None:
            data.delete()
            return Response({'msg':'data deleted'})
        return Response({'error':'error occured'})


#BY THE CUSTOM VALIDATION OF TOKEN MANUALLY
from rest_framework.authtoken.models import Token       
class Registeruser(APIView):
    def post(self,request):
        serializer = userserializer(data=request.data)

        if not serializer.is_valid():
            return Response({'error':'error occured','errors':serializer.errors})
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        # token_obj,_= Token.objects.get_or_create(user=user)
        return Response({'data':serializer.data,
                        #'token': str(token_obj),
                        'msg':'data fetch',
                        'refresh': str(refresh),
                        'access': str(refresh.access_token)})
        




from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

class studentapitokenchecking(APIView):

    # authentication_classes = [TokenAuthentication]
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,id=None):
        if id is not None:
            # id = request.data['id']
            data=api_student.objects.get(id=id)
            serializer=student_serializer(data)
            return Response({'data':serializer.data,'msg':'data fetch bro'})

        else:
            data=api_student.objects.all()
            serializer=student_serializer(data,many=True)
            print(request.user)
            return Response({'data':serializer.data,'msg':'data fetch bro'})
        # return Response({'data':serializer.data ,'msg' : 'this is done'})
    
    def post(self,request):
        data = request.data
        serializer =student_serializer(data=data)

        if serializer.is_valid():
            serializer.save()

            return Response({'data':serializer.data,'msg':'data fetch'})
        
        return Response({'error':'error occured'})

    def put(self,request,id):
        obj=api_student.objects.get(id=id)
        data=request.data

        serializer=student_serializer(instance=obj,data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,"msg":'obj saved'})
        return Response({'error':'error occured'}) 
    
    def patch(self,request,id):
        obj=api_student.objects.get(id=id)
        data=request.data

        serializer=student_serializer(instance=obj,data=data,partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'data':serializer.data,"msg":'obj saved'})
        return Response({'error':'error occured'})
           
    def delete(self,request,id):
        data = api_student.objects.get(id=id)
        serializer = student_serializer(data=data)

        if data is not None:
            data.delete()
            return Response({'msg':'data deleted'})
        return Response({'error':'error occured'})


from django.conf import settings
import pandas as pd
import os
import uuid
class excelimportexport(APIView):
    def get(self,request):
        data = api_student.objects.all()
        serializer = student_serializer(data,many=True)
        df = pd.DataFrame(serializer.data)


        directory = 'apicrud/static/excel/'
        file_name = f'{uuid.uuid4()}.csv'
        file_path = os.path.join(directory, file_name)


        print(df)
        if not os.path.exists(directory):
            os.makedirs(directory)

# Save the DataFrame to a CSV file
        df.to_csv(file_path, encoding='UTF-8')
        # df.to_csv(f'apicrud/static/{uuid.uuid4}.csv',encoding= 'UTF-8')
        # df.to_csv(f'apicrud/static/excel/{uuid.uuid4}.csv',encoding= 'UTF-8')

        # pass
        # print(file_path)
        return Response({'msg':'success','data':serializer.data})


    # def post(self,request):
    #     upload_obj=Excelupload.objects.create(excel_file_upload=request.FILES['files'])
    #     df =pd.read_csv(f'{settings.BASE_DIR}/apicrud/static/{upload_obj.excel_file_upload}')

    #     # pass
    #     return Response({'msg':'success'})



    def post(self, request):
    # Check if 'file' key is in the request
        # if 'file' not in request.FILES:
        #     return Response({'error': 'No file provided'}, status=400)
        
        # Save the uploaded file
        upload_obj = Excelupload.objects.create(excel_file_upload=request.FILES['file'])
        
        # Get the path of the uploaded file
        uploaded_file_path = upload_obj.excel_file_upload.path
        
        # Read the Excel file
        try:
            df = pd.read_csv(uploaded_file_path)
            # Process the DataFrame (e.g., print, analyze, etc.)
            print(df)
        except Exception as e:
            return Response({'error': str(e)}, status=500)
        
        return Response({'msg': 'success'}, status=201)