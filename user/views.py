from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    return render(request,"home.html")
def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check if user already exists
        if Employee.objects.filter(email=email).exists():
            return render(request, "signup.html", {
                "error": "Email already registered"
            })

        # Save employee
        Employee.objects.create(
            name=name,
            email=email,
            password=password
        )

        return render(request, "loginpage.html")

    return render(request, "signup.html")
def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Check user in Employee table
        try:
            user = Employee.objects.get(email=email, password=password)
            # Login success → open dashboard
            return render(request, "userpage.html")

        except Employee.DoesNotExist:
            # Login failed
            return render(request, "loginpage.html", {
                "error": "Invalid email or password. Please sign in!"
            })


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
def DrRecords(request):
    Dr_r=request.GET.get("Drname")
    if Dr_r=="Dr Sadia Awan":
        try:
            #store = Drsadia(petient_name=patientname, Adress=Adress,Cell_no=Cellno,Dr_name=Dr)
            #store.save()
            record=Drsadia.objects.all()
            display={'record':record}
            print(display)
            return render(request , "Dr01records.html", display )
        except: 
          pass
          print("naqi")
    #Dr Hamid portion 02
    elif Dr_r=="Dr Hamid Khan":
        try:
            #store = DrHamid(petient_name=patientname, Adress=Adress,Cell_no=Cellno,Dr_name=Dr)
           # store.save()
            record=DrHamid.objects.all()
            display={'record':record}
            print(display)
            return render(request , "Dr01records.html", display )
           
        except:
          pass
          print("naqi")
    elif Dr_r=="Dr Nadia Hussain":
        try:
            #store = DrNadia(petient_name=patientname, Adress=Adress,Cell_no=Cellno,Dr_name=Dr)
            #store.save()
            record=DrNadia.objects.all()
            display={'record':record}
            print(display)
            return render(request , "Dr01records.html", display )
        except:
          pass
          print("naqi")
    #Dr Ahmed 04
    elif Dr_r=="Dr Ahmed Khan":
        try:
            record=DrAhmed.objects.all()
            display={'record':record}
            print(display)
            return render(request , "Dr01records.html", display )
        except:
          pass
          print("naqi")
    # Sara hussain 05
    elif Dr_r=="Dr Sara Hussain":
        try:
            record=DrSara.objects.all()
            display={'record':record}
            print(display)
            return render(request , "Dr01records.html", display )
        except:
          pass
          print("naqi")
    # Dr Imran Qureshi 06
    elif Dr_r=="Dr Imran Qureshi":
        try:
            
            record=DrImran.objects.all()
            display={'record':record}
            print(display)
            return render(request , "Dr01records.html", display )
        except:
          pass
          print("naqi")
    #Dr Ahmed 07
    elif Dr_r=="Dr Salman Tariq":
        try:
            
            record=DrSalman.objects.all()
            display={'record':record}
            print(display)
            return render(request , "Dr01records.html", display )
        except:
          pass
          print("naqi")
    # Faraz 08
    elif Dr_r=="Dr Faraz Sheikh":
        try:
            
            record=DrFaraz.objects.all()
            display={'record':record}
            print(display)
            return render(request , "Dr01records.html", display )
        except:
          pass
          print("naqi")
    
    #return render(request , "Dr01records.html",display)
#lab section
def lab(request):
    global test_name
    test_name=request.GET.get("Testname")
    return render(request, "lab.html",{"test_name":test_name})
def lab_appointment(request):
    if request.method == "POST":
        patient_name = request.POST.get("patient_name")
        address = request.POST.get("address")
        cell_no = request.POST.get("cell_no")
        test_name = request.POST.get("test_name")

        # Save to database
        LabAppointment.objects.create(
            patient_name=patient_name,
            address=address,
            cell_no=cell_no,
            test_name=test_name
        )

        return render(request, "home.html")  # redirect to success page

    return render(request, "lab.html")