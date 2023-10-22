import http.client

import paramiko
from django.db.migrations import serializer
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import response
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from scp import SCPClient

from download.models import DownLoad
from download.serializers import DownLoadSerializer


@csrf_exempt
def getfile(request):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('10.50.99.242', port=10011, username='gpuadmin', password='tlqkftorl1')

    with SCPClient(ssh.get_transport()) as scp:
        scp.get('/txt/share/summed.txt', './media/result/share.txt')
        scp.get('/txt/share/background.png', './media/')
        scp.get('/txt/share/color.png', './media/')

    ssh.close()

    return Response(serializer.models.Model)
