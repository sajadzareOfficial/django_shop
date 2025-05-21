from django.shortcuts import render
from django import urls
from .models import User as user
from django.contrib import messages
from mahsoolat.views import mahsoolatt
from django.shortcuts import redirect

#def for adding user in db
def adding_user(Name, Email, Password1):
  
        User = user.objects.create(
            name=Name,
            email=Email,
            password=Password1)
        User.save()


  


# this def is said user can login or sign in              
def find_users(Name,Email,Password,for_login:bool,for_signin:bool):
  
  users=[]
  userrr= user.objects.all()
  for userr in userrr:
    users_data_dict={"name":userr.name,"email":userr.email,"password":userr.password}
    print("namee",Name,"email",Email)
    users.append(users_data_dict)
  
  if for_signin==True:
      for useree in users:
        if useree.get("name")== Name and useree.get("email")==Email:
          return False
      return True
    
  if for_login==True:
    for useree in users:
        if useree.get("name")== Name and useree.get("email")==Email and useree.get("password")==Password:
          return True
        if useree.get("name")== Name and useree.get("email")==Email and useree.get("password")!=Password:
          return "password Error"
        if useree.get("name") != Name or useree.get("email")!=Email :
          return "user not found"

    



def add_user(Name,Email,Password1,Password2):
  try:
        
      if Password1 == Password2 :
          if find_users(Name,Email,Password1,for_login=False,for_signin=True) ==True:
            
            adding_user(Name, Email, Password1)
            return True  
          else:
            return 
      else:
        return "passwords are not once"
        
  except Exception as e:
    return e




def sign_in(request):
  
  nam = request.GET.get("name")
  emai = request.GET.get("email")
  passwor = request.GET.get("password")
  passwor1 = request.GET.get("password_utent")
  print(nam,emai,passwor,passwor1)
  f=add_user(Name=nam,Email=emai,Password1=passwor,Password2=passwor1)
  print(f)

  if f==True:
    print("worked mennnnn")
    messages.error(request, "ثبت نام شدید!!!")

  if f=="passwords are not once":
     messages.error(request, "رمز عبور ها باید یکسان باشند")
  return render(request,"login/sign-in.html")


def logining(request):

  

  usernam=request.GET.get("username")
  emai=request.GET.get("email")
  passwor=request.GET.get("password")
  print(passwor,"\n",type(passwor))
  print("in logning \t",passwor , usernam,emai)
  if passwor !="" and usernam !="" and emai !="": 
    auth=find_users(Name=usernam,Email=emai,Password=passwor,for_login=True,for_signin=False)
    print("auth is",auth)
    if auth==None:
      messages.warning(request,"...please add user first")
    if auth==True:
      messages.success(request,"...welcome")


      url = "http://127.0.0.1:1040/products"
      data = {"login": True}
      # response = requests.post(url, json=data)

      # if response.status_code == 200:
      #     print("Data sent successfully!")
      #     return redirect(mahsoolatt)


    if auth=="password Error":
      messages.warning(request,"password not True ...")
    if auth=="user not found":
      messages.warning(request,"user not found")
    print(auth)
  return render(request,"login/login.html")