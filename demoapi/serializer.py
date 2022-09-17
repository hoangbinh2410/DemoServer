from dataclasses import field
from rest_framework import serializers

from demoapi.models import *
from django.db.models import Q
    
class TeacherSerializer(serializers.ModelSerializer):

    class Meta: 
        model = TBLGiangVien
        fields = ('magv', 'hotengv', 'luong','makhoa')

class StudentReqestSerializer(serializers.Serializer):  
    name = serializers.CharField()
    id = serializers.IntegerField()
    
    class Meta:
        fields =('id', 'name')

class StudentSerializer(serializers.ModelSerializer):

    class Meta: 
        model = TBLSinhVien
        fields = ('masv', 'hoten', 'makhoa','namsinh')
    def get_is_validated(seft,obj):
        query = TBLSinhVien.objects.all()
        if query is None:
            return []
        else: 
            return query
class BomSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    number_material = serializers.IntegerField()
    limit_material = serializers.IntegerField()
    class Meta:
        fields = ('number_material','id',  'limit_material')

            