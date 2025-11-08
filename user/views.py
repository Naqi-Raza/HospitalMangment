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
    #Dr sadia portion 01
    if Dr=="Dr Sadia Awan":
        try:
            store = Drsadia(petient_name=patientname, Adress=Adress,Cell_no=Cellno,Dr_name=Dr)
            store.save()
        except:
          pass
          print("naqi")
    #Dr Hamid portion 02
    elif Dr=="Dr Hamid Khan":
        try:
            store = DrHamid(petient_name=patientname, Adress=Adress,Cell_no=Cellno,Dr_name=Dr)
            store.save()
        except:
          pass
          print("naqi")
    # Nadia Hssain 03
    elif Dr=="Dr Nadia Hussain":
        try:
            store = DrNadia(petient_name=patientname, Adress=Adress,Cell_no=Cellno,Dr_name=Dr)
            store.save()
        except:
          pass
          print("naqi")
    #Dr Ahmed 04
    elif Dr=="Dr Ahmed Khan":
        try:
            store = DrAhmed(petient_name=patientname, Adress=Adress,Cell_no=Cellno,Dr_name=Dr)
            store.save()
        except:
          pass
          print("naqi")
    # Sara hussain 05
    elif Dr=="Dr Sara Hussain":
        try:
            store = DrSara(petient_name=patientname, Adress=Adress,Cell_no=Cellno,Dr_name=Dr)
            store.save()
        except:
          pass
          print("naqi")
    # Dr Imran Qureshi 06
    elif Dr=="Dr Imran Qureshi":
        try:
            store = DrImran(petient_name=patientname, Adress=Adress,Cell_no=Cellno,Dr_name=Dr)
            store.save()
        except:
          pass
          print("naqi")
    #Dr Ahmed 07
    elif Dr=="Dr Salman Tariq":
        try:
            store = DrSalman(petient_name=patientname, Adress=Adress,Cell_no=Cellno,Dr_name=Dr)
            store.save()
        except:
          pass
          print("naqi")
    # Faraz 08
    elif Dr=="Dr Faraz Sheikh":
        try:
            store = DrFaraz(petient_name=patientname, Adress=Adress,Cell_no=Cellno,Dr_name=Dr)
            store.save()
        except:
          pass
          print("naqi")
    
    return render(request,"appointment.html",showslip)




def userpage(request):
    return render(request , "userpage.html")
def Drlist(request):
    return render(request , "Drlist.html")