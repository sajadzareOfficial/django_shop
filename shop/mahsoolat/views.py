from django.shortcuts import render,redirect
import time,datetime
from .models import mahsoolat

def choose_type_op_device(device):
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
    device= choose_type_op_device(products.product_type)
    price=  products.price - ((products.price * products.offer  ) /100)
    return render(request,"Main_page/products.html",context={"product":products,"device":device ,"after_offer":price})



    
def searching_products(request):
    product_name = request.GET.get("form-input-in-searching")
    print("product_name is : \t",f"{type(product_name)}\t",product_name)
    # return redirect("/products",mahsoolatt(request,id=product_name))
    # if id !=False:
    try:
        products= mahsoolat.objects.get(title=product_name)
        print("its worked we in filter :\n\t ",products.description)

            # prod = products
            # device= choose_type_op_device(products.product_type)
        time_in_now = datetime.datetime.now()
        day=3
        timee=23
        minn=59
        hour= time_in_now.strftime("%H")
        min= time_in_now.strftime("%M")
        return render(request,"Main_page/main2.html",context={"product":products,"time":{"day":day,"h":(timee)-(int(hour)),"m":(minn)-(int(min))}})
        # return mahsoolatt(request,id=product_name)
    except:
            return redirect("/products")