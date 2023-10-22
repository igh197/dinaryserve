import scp
import requests
from django.db.migrations import serializer
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from scp import SCPClient, SCPException
from django.shortcuts import render, redirect
import os
import json
import paramiko
# Create your views here.
from django.views import View
from download.models import DownLoad as dL
from .forms import ShareForm
from .models import FileUpLoad


@csrf_exempt
def share(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        sh = open('./media/result/share.txt', 'w')
        sh.write(data.get('content'))

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('10.50.99.242', port=10011, username='gpuadmin', password='tlqkftorl1')

        with SCPClient(ssh.get_transport()) as scp:
            scp.put('./media/result/share.txt', './txt/share/', preserve_times=True)

        with SCPClient(ssh.get_transport()) as scp:
            scp.get('/txt/share/summed.txt', './media/result/share.txt')
            scp.get('/txt/share/background.png', './media/')
            scp.get('/txt/share/color.png', './media/')

        ssh.close()

        return Response(dL)
