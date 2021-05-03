from django.shortcuts import render

from django.http import HttpResponse
import sys


def form(request):

     return render(request,'base.html')
def Goback(request):
     if request.method == 'POST':
          code_part = request.POST['code']
          input_part = request.POST['Input area']
          y = input_part
          input_part = input_part.replace("\n"," ").split(" ")
          def input():
               a =input_part[0]
               del input_part[0]
               return a
          try:
               orig_stdout = sys.stdout
               sys.stdout = open('file.txt','w')
               exec(code_part)
               sys.stdout.close()
               sys.stdout = orig_stdout
               output = open('file.txt','r').read()
          except Exception as e:
               sys.stdout.close()
               sys.stdout = orig_stdout
               output = e
          print(output)
     return  render(request, 'base.html',{'code':code_part,'Input':y,'Output':output})
          
