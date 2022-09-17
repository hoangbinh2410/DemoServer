from typing import Generator
from unittest import result
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from demoapi.utils import custom_response
from django.http import JsonResponse
# Create your views here.
from .models import (
    TBLDetai,
    TBLGiangVien,
    TBLHuongDan,
    TBLKhoa,
    TBLSinhVien
)
from .serializer import *
from django.db import connection
from django.db.models import Q
from django.db.models.functions import Lower

from demoapi import serializer    
from celery import Celery
from celery.schedules import crontab
import logging

logger = logging.getLogger(__name__)
from django.http import HttpResponse

def home(request):
    return HttpResponse("Django")

#class Getlistteach(APIView):
    # truy vấn tất cả
    # def get(self, request):
    #     listteacher = TBLGiangVien.objects.all()
    #     print(connection.queries)
    #     data_serializer = TeacherSerializer(listteacher, many=True)
    #     return Response({ 
    #      'data': data_serializer.data  
    #     } 
    #     , status=status.HTTP_200_OK)

    #truy vấn dựa trên tìm kiếm
    # def get(self, request):
    #     listt = TBLGiangVien.objects.filter(hotengv__startswith='Thanh') | TBLGiangVien.objects.filter(hotengv__startswith='T')       
    #     data_serializer = TeacherSerializer(listt, many=True)
    #     return Response({
    #      'data': data_serializer.data  
    #     } 
    #     , status=status.HTTP_200_OK)

    # truy vấn ngoại trừ
    # def get(self, request):
    #     listt = TBLGiangVien.objects.filter(Q(hotengv__startswith='Thanh') & Q(makhoa='Geo'))     
    #     data_serializer = TeacherSerializer(listt, many=True)
    #     return Response({
    #      'data': data_serializer.data  
    #     } 
    #     , status=status.HTTP_200_OK)
    
    #onion :nhóm
    # def get(self, request):
    #     listt = TBLGiangVien.objects.all().values_list('hotengv').union(TBLSinhVien.objects.all().values_list('hoten'))  
    #     data_serializer = TeacherSerializer(listt, many=True)
    #     return Response({
    #      'data':  data_serializer.data  
    #     } 
    #     , status=status.HTTP_200_OK)

    # nhóm các trường khác kiểu dữ liệu ép về thằng thứ nhất
    # def get(self, request):
    #     listt = TBLGiangVien.objects.all().values('hotengv').union(TBLSinhVien.objects.all().values('quequan'))  
    #     data_serializer = TeacherSerializer(listt, many=True)
    #     return Response({
    #      'data': listt
    #     } 
    #     , status=status.HTTP_200_OK)

    #exclude :truy vấn ngoại trừ
    # def get(self, request):
    #     #listt = TBLGiangVien.objects.exclude(luong__lt=500)
    #      # giống cách viết dùng filter
    #     listt = TBLGiangVien.objects.filter(~Q(luong__lt=500)&~Q(hotengv='Thanh Xuan'))
    # #gt : 
    # #gte: 
    # #lt:
    # #lte
    #     data_serializer = TeacherSerializer(listt, many=True)
    #     return Response({
    #      'data': data_serializer.data 
    #     } 
    #     , status=status.HTTP_200_OK)

    #only : chỉ vs filter
    # def get(self, request):      
    #     listt = TBLGiangVien.objects.filter(luonggt=500).only('hotengv')
    #     print(listt)
    #     data_serializer = TeacherSerializer(listt, many=True)
    #     return Response({
    #      'data': data_serializer.data 
    #     } 
    #     , status=status.HTTP_200_OK)
    # raw : truy vấn bằng câu lệnh sql
    # def get(self, request):      
    #     listt = TBLGiangVien.objects.raw("SELECT * FROM tbl_giang_vien")       
    #     data_serializer = TeacherSerializer(listt, many=True)
    #     return Response({
    #      'data': data_serializer.data 
    #     } 
    #     , status=status.HTTP_200_OK)
    
    # lấy dữ liệu theo format
    # def dictfetchall(cursor):
    #     desc = cursor.get_view_description
    #     return[
    #         dict(zip([col[0] for col in desc], row )) for row in cursor   
    # truy vấn trực tiếp với db
    # def get(self, request):   
    #     cursor = connection.cursor()
    #     cursor.execute("SELECT * FROM tbl_giang_vien")      
    #     listt = dictfetchall(cursor)
    #     data_serializer = TeacherSerializer(listt, many=True)
    #     return Response({
    #      listt
    #     } 
    #     , status=status.HTTP_200_OK)

    # truy van voi releact

    # def get(self, request):
    #     query = TBLGiangVien.objects.select_related('makhoa').filter(hotengv__startswith='T')
    #     data_serializer = TeacherSerializer(query, many=True)
    #     lists = []
    #     for item in query:
    #         lists.append({'name': item.hotengv, 'tenkhoa': item.makhoa.tenkhoa})
    #     return Response({
    #      'data': lists
    #     } 
    #     , status=status.HTTP_200_OK)

    # truy van khong phan biet chu hoa chu thuong
    # def get(self, request,pk):
    #     query = TBLGiangVien.objects.order_by(Lower('hotengv'))
    #     data_serializer = TeacherSerializer(query, many=True)
    #     return Response({
    #      'data': data_serializer.data
    #     } 
    #     , status=status.HTTP_200_OK)
    #def get(sefl, request):
        # A = [{'id':1 ,'limit_material':10},
        # {'id':2, 'limit_material':7},
        # {'id':3, 'limit_material':4},
        # {'id':4, 'limit_material':7}
        # ]
        
        # B = [{'id':1, 'number_material':5},
        # {'id':2, 'number_material':4},
        # {'id':3, 'number_material':0},
        # {'id':4, 'number_material':11}
        # ]
        # C= list()
        # G = list()
        # for record in A: 
        #     id_A = record.get('id')          
        #     for item in B:         
        #         id_B = item.get('id')
        #         if id_A == id_B:
        #             D ={'id':id_A,
        #             'number_material':item.get('number_material'),
        #             'limit_material': record.get('limit_material') }                     
        #     C.append(D) 
        # # list_1 = C.filter(id = 1) 
        # for i in C:
            
        #     if i.get('number_material') <  i.get('limit_material'):
        #         G.append(i)
                         
        # return Response(custom_response(G, msg_display='Lấy dữ liệu thành công'),
        #                 status=status.HTTP_200_OK)

#class ListStuden(APIView):
    # def post(self, request):


    #     row = request.data
    #     serializer = StudentReqestSerializer(data = row)
    #     if serializer.is_valid():      
    #         data_serializer = StudentSerializer(serializer)
    #     return Response({
    #        'data': data_serializer.data       
    #     }, status= status.HTTP_200_OK)
#    def post(self, request, **kwargs):

#        row = request.data
#        serializer = BomSerializer(data=row)
#        return Response(custom_response(row, msg_display='Thông tin nhân viên hợp lệ'),
#                                 status=status.HTTP_200_OK)
    #    if serializer.is_valid():       
    #    return Response(custom_response(row, msg_display='Thông tin sai định dạng'), status=status.HTTP_200_OK)

