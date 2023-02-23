# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Call(models.Model):
    MaCuocGoi = models.IntegerField()
    ThoiGian = models.DateTimeField(null=True, blank=True)
    NguoiGoi = models.CharField(max_length=10, null=True, blank=True)
    NguoiNhan = models.CharField(max_length=10, null=True, blank=True)
    TrangThai = models.CharField(max_length=50, null=True, blank=True)
    DoChuong = models.TimeField(null=True, blank=True)
    DamThoai = models.TimeField(null=True, blank=True)
    ChieuGoi = models.CharField(max_length=20, null=True, blank=True)
    Record = models.CharField(max_length=200, null=True, blank=True)
    NgatMay = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.id)
