from urllib import request
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from django.shortcuts import render
from schoolapp.models import login
from .forms import studdetailsform
from .models import Course,Detailsmodel
from django.http import JsonResponse
# Create your views here.
def index(request):
   return render(request,'index.html')
def login(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username, password=password)
      if user is not None:
         auth.login(request,user)
         return redirect('detailsform')
      else:
         messages.info(request,'invalid')
         return redirect('login')
   return render(request,'login.html')
def register(request):
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      cpassword = request.POST['cpassword']
      if password==cpassword:
         if User.objects.filter(username=username).exists():
            messages.info(request,'username alreadyhave')
            return redirect('register')
         else:
            user=User.objects.create_user(username=username,password=password)
            user.save();
            return redirect('login')
      else:
         messages.info(request,"password not matched")
         return redirect('register')
      #return redirect('/')
      return render(request,'login.html')
   return render(request,'register.html')
# def details(request):
#     return render(request,'detailsform.html')

# def detailsform(request):
#    if request.method == "POST":
#       first_name=request.POST.get('first_name')
#       last_name = request.POST.get('last_name')
#       birthday = request.POST.get('birthday')
#       age = request.POST.get('age')
#       Gender_choice = request.POST.get('Gender-choice')
#       phone = request.POST.get('phone')
#       email = request.POST.get('email')
#       address = request.POST.get('address')
#       #materials = request.POST.get('materials')
#       #purpose=request.POST.get('purpose')
#       detls=Detailsmodel(firstname=first_name,lastname=last_name,dob=birthday,age=age,gender=Gender_choice,phone=phone,email=email,address=address)
#       detls.save()
#    #deptcontext = studentdepartment.objects.all()
#    #coursecontext = Detailsmodel.objects.all()
#    #return render(request,"detailsform.html",{"studentdepartment":deptcontext,"Detailsmodel":coursecontext})
#    return render(request,"detailsform.html")

def detailsform(request):
   form = studdetailsform()
   if request.method == 'POST':
      form = studdetailsform(request.POST)
      if form.is_valid():
         form.save()
         return redirect('detailsform')
   return render(request, 'detailsform.html', {'form': form})

# AJAX
def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    return render(request, 'course_dropdown_list_options.html', {'courses': courses})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
def logout(request):
   auth.logout(request)
   return render("/")