from django.db import models

# Create your models here.

class TBLKhoa(models.Model):
    makhoa = models.CharField(max_length=10,primary_key=True, blank=True)
    tenkhoa = models.CharField(max_length=30, blank=True)
    dienthoai = models.CharField(max_length=10,null=False, blank=True)
    class Meta:       
        db_table='tbl_khoa'
        
class TBLGiangVien(models.Model):
    magv = models.IntegerField(primary_key = True)
    hotengv = models.CharField(max_length=30,null=False)
    luong = models.DecimalField(max_digits=5,decimal_places=2)
    makhoa= models.ForeignKey(TBLKhoa, on_delete=models.CASCADE)
    class Meta:     
        db_table='tbl_giang_vien'
       
class TBLSinhVien(models.Model):
    masv = models.IntegerField(primary_key = True)
    hoten = models.CharField(max_length=30,null=False)
    makhoa = models.ForeignKey(TBLKhoa, on_delete=models.CASCADE)
    namsinh = models.IntegerField()
    quequan = models.CharField(max_length=30,null=False)
    class Meta:      
        db_table='tbl_sinh_vien'
        
class TBLDetai(models.Model):
    madt= models.CharField(primary_key=True,max_length=10)
    tendt = models.CharField(max_length=30,null=False)
    kinhphi = models.IntegerField()
    noithuctap = models.CharField(max_length=30,null=False)
    class Meta:     
        db_table='tbl_de_tai'
        

class TBLHuongDan(models.Model):
    masv = models.IntegerField(primary_key = True)
    magv = models.ForeignKey(TBLGiangVien, on_delete=models.CASCADE)
    madt= models.ForeignKey(TBLDetai, on_delete=models.CASCADE)
    ketqua = models.DecimalField(max_digits=5,decimal_places=2)
    class Meta:     
        db_table='tbl_huong_dan'
        
    