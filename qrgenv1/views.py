from django.http import HttpResponse
from django.shortcuts import render
from qrcode import *
# data = None
import os
#import cv2
import numpy as np
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import webbrowser
# def home(request):
#     global data
#     if request.method == 'POST':
#         data = request.POST['data']
        
#         img = make(data)
#         img.save('static/image/test.png')
#     else:
#         pass
#     return render(request,'home.html',{'data':data})
    
# def home(request):
#     if request.method == 'POST':
#         data = request.POST['data']
#         if not os.path.exists('static/image'):
#             os.makedirs('static/image')
#         img = make(data)
#         img.save('static/image/qr_code.png')
#         return render(request, 'home.html', {'data': data},{"message":"Record Submitted Successfully  now click on List icon at top right "})
#     else:
#         return render(request, 'home.html', {})


def home(request):
    if request.method == 'POST':
        data = request.POST['data']
        if not os.path.exists('static/image'):
            os.makedirs('static/image')
        img = make(data)
        img.save('static/image/qr_code.png')
        message = "Qr Created successfully"
        return render(request, 'home.html', {'data': data, 'message': message})
    else:
        return render(request, 'home.html', {})
    
def scan(request):
    return render(request, 'qrreader.html')
 
    



def handler404(request,exception=None):
   return render(request,'404.html',{})

def custom404(request,exception=None):
   return JsonResponse({
      'status_code':404,
      'error':'The resource was not found'
   })
handler404 = handler404
