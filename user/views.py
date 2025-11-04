from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    return render(request,"home.html")
def login(request):
    return render(request,"loginpage.html")
def appointment(request):
    global Dr
    Dr=request.GET.get("Drname")
    return render(request,"appointment.html",{"Drname":Dr})
def slip(request):
    patientname=request.POST.get("your_name")
    Adress=request.POST.get("your_adress")
    Cellno=request.POST.get("your_number")
    Dr_Name=request.POST.get("Drname")
    
    showslip={
        "alert": True,
        "patient": patientname,
        "doctor": Dr_Name,
        "Adress": Adress,
        "Cellno": Cellno,
        "Drname":Dr,
    }
    if Dr=="Dr Hamid":
        try:
            store = Drsadia(petient_name=patientname, Adress=Adress,Cell_no=Cellno,Dr_name=Dr)
            store.save()
        except:
          pass
          print("naqi")
    return render(request,"appointment.html",showslip)
def userpage(request):
    return render(request , "userpage.html")
def Drlist(request):
    return render(request , "Drlist.html")