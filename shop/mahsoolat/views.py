from django.shortcuts import render
import time,datetime
from .models import mahsoolat

def choose_device(device):
    if device == "phone":
        return "گوشی موبایل"
    if device == "tablet":
        return "تبلت"
    if device == "console":
        return "کنسول بازی"
    if device == "laptop":
        return "لپتاپ"
    if device == "accessory":
        return "لوازم جانبی"
    

def mahsoolatt(request,login=False):
    if login==True:
        print("comed mennnn")

    prod = mahsoolat.objects.all()

   
    time_in_now = datetime.datetime.now()
    day=3
    timee=23
    minn=59
    hour= time_in_now.strftime("%H")
    min= time_in_now.strftime("%M")


    if (timee)-(int(hour)) == 0:
        day-1
    return render(request,"Main_page/main_page.html",context={"prod":prod,"time":{"day":day,"h":(timee)-(int(hour)),"m":(minn)-(int(min))}})
def devices(request,id):
    print("salammmm")
    products= mahsoolat.objects.get(id=id)
    device= choose_device(products.product_type)
    return render(request,"Main_page/products.html",context={"product":products,"device":device})