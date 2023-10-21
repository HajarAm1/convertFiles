import os
import sys

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

# Create your views here.

from django.http import HttpResponse


def hi(request):
    return render(request, 'CONVERTERAPP/hi.html')


# def home(request):
#     return render(request, 'index.htm', {'what':'Django File Upload'})


def upload(request):
    if request.method == 'post':
        handle_dir()
        uploaded_file = request.Files['document']
        sys.stdout.write(" file name is : " + uploaded_file.name)
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)
    return render(request, 'hi.html')


def handle_dir():
    if not os.path.isdir(rf'CONVERTERAPP/static/media'):
        os.makedirs(rf'CONVERTERAPP/static/media')


def read_uploaded_file(file, filename):
    pass
