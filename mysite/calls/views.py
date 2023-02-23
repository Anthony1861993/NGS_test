# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views import generic
import datetime
from django.shortcuts import render, get_object_or_404
from .models import Call

def index(request):
    callList = Call.objects.all()

    # filter by ThoiGian
    myFrom = request.GET.get('myFrom')
    if myFrom:
        #print "INFO: ", type(myFrom), myFrom
        callList = callList.filter(ThoiGian__gte=datetime.datetime.strptime(myFrom, "%Y-%m-%dT%H:%M"))
    myTo = request.GET.get('myTo')
    if myTo:
        callList = callList.filter(ThoiGian__lte=datetime.datetime.strptime(myTo, "%Y-%m-%dT%H:%M"))


    # filter by NguoiGoi
    myNguoiGoi = request.GET.get('myNguoiGoi')
    if myNguoiGoi:
        #print "INFO: ", type(myNguoiGoi), myNguoiGoi
        callList = callList.filter(NguoiGoi=myNguoiGoi)

    # filter by NguoiNhan
    myNguoiNhan = request.GET.get('myNguoiNhan')
    if myNguoiNhan:
        callList = callList.filter(NguoiNhan=myNguoiNhan)

    # filter by TrangThai
    myTrangThai = request.GET.get('myTrangThai')
    if myTrangThai == "Tra Loi":
        callList = callList.filter(TrangThai="Trả lời")
    elif myTrangThai == "Khong Tra Loi":
        callList = callList.filter(TrangThai="Không trả lời")
    elif myTrangThai == "Agent Tat May":
        callList = callList.filter(TrangThai="Agent tắt máy trước")

    # filter by ChieuGoi
    myChieuGoi = request.GET.get('myChieuGoi')
    if myChieuGoi == "Goi Ra":
        callList = callList.filter(ChieuGoi="Gọi ra")
    elif myChieuGoi == "Goi Vao":
        callList = callList.filter(ChieuGoi="Gọi vào")
    elif myChieuGoi == "Goi Noi Bo":
        callList = callList.filter(ChieuGoi="Gọi nội bộ")

    # filter by DoChuong
    # callList = callList.exclude(DoChuong=None)
    myDoChuongTuGio = request.GET.get('myDoChuongTuGio')
    myDoChuongTuPhut = request.GET.get('myDoChuongTuPhut')
    myDoChuongTuGiay = request.GET.get('myDoChuongTuGiay')
    myDoChuongDenGio = request.GET.get('myDoChuongDenGio')
    myDoChuongDenPhut = request.GET.get('myDoChuongDenPhut')
    myDoChuongDenGiay = request.GET.get('myDoChuongDenGiay')
    if myDoChuongTuGio and myDoChuongTuPhut and myDoChuongTuGiay:
        callList = callList.filter(
            DoChuong__gte=datetime.time(int(myDoChuongTuGio), int(myDoChuongTuPhut), int(myDoChuongTuGiay)))
    if myDoChuongDenGio and myDoChuongDenPhut and myDoChuongDenGiay:
        callList = callList.filter(
            DoChuong__lte=datetime.time(int(myDoChuongDenGio), int(myDoChuongDenPhut), int(myDoChuongDenGiay)))

    # filter by DamThoai
    #callList = callList.exclude(DamThoai=None) nhung ma chac ko can
    myDamThoaiTuGio = request.GET.get('myDamThoaiTuGio')
    myDamThoaiTuPhut = request.GET.get('myDamThoaiTuPhut')
    myDamThoaiTuGiay = request.GET.get('myDamThoaiTuGiay')
    myDamThoaiDenGio = request.GET.get('myDamThoaiDenGio')
    myDamThoaiDenPhut = request.GET.get('myDamThoaiDenPhut')
    myDamThoaiDenGiay = request.GET.get('myDamThoaiDenGiay')
    if myDamThoaiTuGio and myDamThoaiTuPhut and myDamThoaiTuGiay:
        callList = callList.filter(
            DamThoai__gte=datetime.time(int(myDamThoaiTuGio), int(myDamThoaiTuPhut), int(myDamThoaiTuGiay)))
    if myDamThoaiDenGio and myDamThoaiDenPhut and myDamThoaiDenGiay:
        callList = callList.filter(
            DamThoai__lte=datetime.time(int(myDamThoaiDenGio), int(myDamThoaiDenPhut), int(myDamThoaiDenGiay)))

    ChuongTuGio = int(myDoChuongTuGio) if myDoChuongTuGio else 0
    ChuongTuPhut = int(myDoChuongTuPhut) if myDoChuongTuPhut else 0
    ChuongTuGiay = int(myDoChuongTuGiay) if myDoChuongTuGiay else 0
    ChuongDenGio = int(myDoChuongDenGio) if myDoChuongDenGio else 0
    ChuongDenPhut = int(myDoChuongDenPhut) if myDoChuongDenPhut else 0
    ChuongDenGiay = int(myDoChuongDenGiay) if myDoChuongDenGiay else 0

    DamTuGio = int(myDamThoaiTuGio) if myDamThoaiTuGio else 0
    DamTuPhut = int(myDamThoaiTuPhut) if myDamThoaiTuPhut else 0
    DamTuGiay = int(myDamThoaiTuGiay) if myDamThoaiTuGiay else 0
    DamDenGio = int(myDamThoaiDenGio) if myDamThoaiDenGio else 0
    DamDenPhut = int(myDamThoaiDenPhut) if myDamThoaiDenPhut else 0
    DamDenGiay = int(myDamThoaiDenGiay) if myDamThoaiDenGiay else 0

    # Get TrangThai-count list
    trangThaiList = []
    trangThaiList.append(["Tra loi", callList.filter(TrangThai="Trả lời").count()])
    trangThaiList.append(["Khong tra loi", callList.filter(TrangThai="Không trả lời").count()])
    trangThaiList.append(["Agent tat may", callList.filter(TrangThai="Agent tắt máy trước").count()])
    # print "HERE: ", trangThaiList

    # Get ChieuGoi-count list
    chieuGoiList = []
    chieuGoiList.append(["Goi ra", callList.filter(ChieuGoi="Gọi ra").count()])
    chieuGoiList.append(["Goi vao", callList.filter(ChieuGoi="Gọi vào").count()])
    chieuGoiList.append(["Goi noi bo", callList.filter(ChieuGoi="Gọi nội bộ").count()])
    # print "HERE:", chieuGoiList

    context = {
        'myFrom': myFrom,
        'myTo': myTo,
        'myNguoiGoi': myNguoiGoi,
        'myNguoiNhan': myNguoiNhan,
        'myTrangThai': myTrangThai,
        'myChieuGoi': myChieuGoi,
        'myDoChuong': [ChuongTuGio, ChuongTuPhut, ChuongTuGiay, ChuongDenGio, ChuongDenPhut, ChuongDenGiay],
        'myDamThoai': [DamTuGio, DamTuPhut, DamTuGiay, DamDenGio, DamDenPhut, DamDenGiay],
        'trangThaiList': trangThaiList,
        'chieuGoiList': chieuGoiList,
        'callList': callList
    }
    return render(request, 'calls/index.html', context)

