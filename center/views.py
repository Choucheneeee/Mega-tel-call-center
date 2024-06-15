from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from .models import *
from datetime import timedelta
from django.utils import timezone
import random
from django.shortcuts import redirect
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import *






@login_required
def admin(request):
    user = request.user
    employee_count = User.objects.all().count()
    if employee_count >= 5:
        employee = random.sample(list(User.objects.all()), 5)
    else:
        employee = list(User.objects.all())
    project_count = Project.objects.all().count()
    if project_count >= 3:
        project = random.sample(list(Project.objects.all()), 3)
    else:
        project = list(Project.objects.all())
    today = timezone.now()
    # Calculate the first day of the current month
    first_day_of_current_month = today.replace(day=1)

    # Filter employees added this month
    new_employees_this_month = User.objects.filter(
        created_at__gte=first_day_of_current_month,
        created_at__lte=today
    ).count()
    employee_with_id_3 = user
    porcentage = round((new_employees_this_month * 100) / employee_count / 10) * 10
    print(porcentage)
    context = {'employee_count': employee_count,
               'project_count':project_count,
               'new_employees_this_month': new_employees_this_month,
               'porcentage':porcentage,
               'employee':employee,
               'project':project,
               'employee_with_id_3': employee_with_id_3,

               }
    print(employee_with_id_3.id)
    return render(request, "center/admin-dashboard.html", context)

@login_required
def logout_view(request):
    logout(request)
    user = request.user
    if user.is_authenticated:
        super.status = 'Inactive'
        super.save()
    return redirect('login')

def employee(request):
    user = request.user
    employee_with_id_3 = User.objects.get(id=request.user.id)
    context={
        'employee_with_id_3':employee_with_id_3
    }
    return render(request,"center/employee-dashboard.html",context)


@login_required
def creat(request):
    
    employee_with_id_3 = User.objects.get(id=request.user.id)
    missing_fields = []
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        status = request.POST.getlist("status")
        start_date = request.POST.get("start_date")
        end_date = request.POST.get("end_date")
        contact_name = request.POST.get("contact_name")
        contact_email = request.POST.get("contact_email")
        contact_phone = request.POST.get("contact_email")
        print(f"name: {name}")
        print(f"description: {description}")
        print(f"status: {status}")
        print(f"end_date: {end_date}")
        print(f"start_date: {start_date}")
        print(f"contact_name: {contact_name}")
        print(f"contact_email: {contact_email}")
        print(f"contact_phone: {contact_phone}")
        if not name:
            missing_fields.append("name")
        if not description:
            missing_fields.append("description")
        if not status:
            missing_fields.append("status")
        if not start_date:
            missing_fields.append("start_date")
        if not end_date:
            missing_fields.append("end_date")
        if not contact_name:
            missing_fields.append("contact_name")
        if not contact_email:
            missing_fields.append("contact_email")
        if not contact_phone:
            missing_fields.append("contact_phone")
        
        if missing_fields:
            return render(request, "center/project.html", {
                "message": f"Missing or invalid fields:/n {', '.join(missing_fields)}"
            })
        print(f"start_date{start_date}")
        print(f"end_date{end_date}")
        try:
            pr=Project.objects.create(
                name=name,
                description=description,
                end_date=end_date,
                contact_name = contact_name ,
                start_date=start_date,
                status=','.join(status),
                contact_email=contact_email,
                contact_phone=contact_phone,
            )
            pr.save()
            return redirect('project.html')
        except IntegrityError as e:
            print(f"IntegrityError: {e}")
            return render(request, "project.html", {
                "messages": "Listing valid."
            })
    employee_with_id_3 = User.objects.get(id=request.user.id)
    context={
        'employee_with_id_3':employee_with_id_3
    }
        
    return render(request,"center/project.html",context)
    

@login_required 
def calender(request):
    employee_with_id_3 = User.objects.get(id=request.user.id)
    print(employee_with_id_3)
    context={
        'employee_with_id_3':employee_with_id_3,
    }
    return render(request,"center/calender.html",context)

@login_required
def chat(request):
    chat_group = get_object_or_404(ChatGroup, group_name="public")
    chat_messages = chat_group.chat_messages.all()[:30]
    form=ChatmessageCreateForm()
    request.method="POST"
    employee_with_id_3 = User.objects.get(id=request.user.id)
    if request.method=="POST":
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid():
            print("valide")
        else:
            print("non valide",form.errors)    
        
        if form.is_valid():
            print("oui valide")
            message=form.save(commit=False)
            message.author=request.user
            message.group=chat_group
            message.save()
            context={
                'message':message,
                'user':request.user    
            }
            return render(request, "center/partials/chat_message_p.html", context)
        else:
            print("non valide")
    return render(request, "center/chat.html", {'chat_messages': chat_messages,'chat_group':chat_group,'employee_with_id_3':employee_with_id_3,'form': form,})




@login_required
def employ(request):
    
    employee_with_id_3 = User.objects.get(id=request.user.id)
    employee = User.objects.all()    
    context={
        'employee':employee,
        'employee_with_id_3':employee_with_id_3,
    }
    return render(request, "center/employees.html",context)


from django.shortcuts import render
import random
@login_required
def att(request):
    employee_with_id_3 = User.objects.get(id=request.user.id)
    employee_list = User.objects.all()
    for emp in employee_list:
        emp.random_numbers = [random.randint(0, 1) for _ in range(30)]
    context = {
        'employee_with_id_3':employee_with_id_3,
        'employee': employee_list,
    }
    return render(request, "center/attendance.html", context)


from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

def login_view(request):
    if request.method == "POST":
        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        print(f"username'{username}'")
        print(f"password'{password}'")
        user = authenticate(request, username=username, password=password)
        print(f"user'{user}'")
        # Check if authentication successful
        if user is not None:
            print("dkhalt f if loula") 
            login(request, user)
            return HttpResponseRedirect(reverse("admin"))
        else:
            print("maa mchech")
            return render(request,"center/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request,"center/login.html")


def contact(request):
    return render(request,"center/contact.html")

def contact_l(request):
    return render(request,"center/contact-list.html")

def index2(request):
    return render(request,"center/index.html")

def data(request):
    employee_with_id_3 = User.objects.get(id=request.user.id)
    return render(request,"center/data.html")

def about(request):
    employee_with_id_3 = User.objects.get(id=request.user.id)
    return render(request,"center/about.html")

@login_required
def project(request, id):
    # Retrieve the project
    project = get_object_or_404(Project, pk=id)

    project.total_hours = (project.end_date - project.start_date).total_seconds() / 3600
    # Get user information
    print(f"Project ID: {id}")
    print(f"Project start date: {project.start_date}")
    print(f"Project end date: {project.end_date}")
    print(project.total_hours)
    employee_with_id_3 = User.objects.get(id=request.user.id)

    context = {
        'project': project,
        'employee_with_id_3': employee_with_id_3,
    }
    return render(request, 'center/project-view.html', context)

@login_required
def allproject(request):
    employee_with_id_3 = User.objects.get(id=request.user.id)
    project =Project.objects.all()
    context={
        'employee_with_id_3':employee_with_id_3,
        'project':project,
    }
    return render(request, 'center/project.html',context)
@login_required
def profile(request,id):
    user = request.user
    employee_with_id_3 = user
    employe = get_object_or_404(User, pk=id)
    return render(request, 'center/profile.html',{
        'employe': employe,
        'employee_with_id_3': employee_with_id_3,                                          
        })
    
    
    
@login_required
def createmp(request):
    employee_with_id_3 = User.objects.get(id=request.user.id)
    context = {
    'employee_with_id_3': employee_with_id_3
}
    employee = User.objects.all()    
    print(employee_with_id_3.id)
    
    
    missing_fields = []
    if request.method == "POST":
        username = request.POST["username"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        telephone = request.POST.get("telephone")
        Password=request.POST["Password"]
        cPassword=request.POST.get("cPassword")
        Bank_name = request.POST.get("Bank name")
        Salair_type = request.POST.get("Salair type")

        Image = request.FILES.get('image')
        Adresse = request.POST.get("Adresse")
        Salair_month = request.POST.get("Salair month")
        Payment_type = request.POST.get("Payment type")
        Nationality = request.POST.get("Nationality")
        Email = request.POST.get("Email")
        City = request.POST.get("City")
        Passport = request.POST.get("Passport")
        Cin = request.POST.get("Cin")
        date_birthday = request.POST.get("date_birthday")
        Poste = request.POST.get("Poste")
        Status = "Active"
        Gender = request.POST.get("gender")
        #print(f"description: {description}")
        #print(f"start_date: {start_date}")
        #print(f"contact_name: {contact_name}")
        #print(f"contact_email: {contact_email}")
        #print(f"contact_phone: {contact_phone}")
        if not username:
            missing_fields.append("username")
        if not telephone:
            missing_fields.append("telephone")
        if not Bank_name:
            missing_fields.append("bank_name")
        if not Salair_type:
            missing_fields.append("salair_type")
        if not Image:
            missing_fields.append("image")
        if not Adresse :
            missing_fields.append("adresse")
        if not Salair_month:
            missing_fields.append("salair_month")
        if not Payment_type:
            missing_fields.append("payment_type")
        if not Nationality:
            missing_fields.append("nationality")
        if not Email:
            missing_fields.append("email")
        if not City:
            missing_fields.append("city")
        if not Passport:
            missing_fields.append("passport")
        if not Cin:
            missing_fields.append("cin")
        if not Poste:
            missing_fields.append("poste")
        if not Status :
            missing_fields.append("status")
        if not Gender :
            missing_fields.append("gender")
        if not Password :
            missing_fields.append("password")
        
        if missing_fields:
            mes = f"Missing or invalid fields: {', '.join(missing_fields)}"
            return render(request, "center/employees.html", {
                "employee_with_id_3": employee_with_id_3,    
                "message": mes,
                'employee':employee,
            
        })
            
            
        if missing_fields:
            mes = f"Missing or invalid fields: {', '.join(missing_fields)}"
            return render(request, "center/employees.html", {
                "employee_with_id_3": employee_with_id_3,    
                "message": mes,
                'employee':employee,
            
        })
        if Poste =="Admin":
            try:
                print("ahahahah")
                us = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                cin=Cin,
                telephone=telephone,
                adresse=Adresse,
                Payment_type=Payment_type,
                nationality=Nationality,
                email=Email,
                image=Image,
                Bank_name=Bank_name,
                city=City,
                date_birthday=date_birthday,
                salair_month=Salair_month,
                poste=Poste,
                passport=Passport,
                status=Status,
                password=Password,
                gender=Gender,
                is_superuser=True,
                is_staff=True, 
                    )
                print("mchet yaa chaa")
                return redirect('employees.html', context)
            except IntegrityError as e:
                print("maa mchetch ya chaaa")
                print(f"IntegrityError: {e}")
            return render(request, "employees.html", {
            "messages": "Listing valid."
        }, context)
    
            
        else:
            try:
                print("ahahahah")
                us = User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                cin=Cin,
                telephone=telephone,
                adresse=Adresse,
                Payment_type=Payment_type,
                nationality=Nationality,
                email=Email,
                image=Image,
                Bank_name=Bank_name,
                city=City,
                date_birthday=date_birthday,
                salair_month=Salair_month,
                poste=Poste,
                passport=Passport,
                status=Status,
                password=Password,
                gender=Gender,
    )
                print("mchet yaa chaa")
                return redirect('employees.html', context)
            except IntegrityError as e:
                print("maa mchetch ya chaaa")
                print(f"IntegrityError: {e}")
            return render(request, "employees.html", {
            "messages": "Listing valid."
        }, context)
    print(employee_with_id_3.id)
        
    return render(request,"center/employees.html",context)


def delete_profile(request, user_id):
    print("hahaahah")
    
    try:
        user = User.objects.get(id=user_id)
        print(user)
        user.delete()
        # Redirect to a success page or refresh the current page
        employee_with_id_3 = User.objects.get(id=request.user.id)
        employee = User.objects.all()    
        context={
        'employee':employee,
        'employee_with_id_3':employee_with_id_3,
    }
        return redirect('emply')

    except User.DoesNotExist:
        # Handle case where user doesn't exist
            employee_with_id_3 = User.objects.get(id=request.user.id)
            employee = User.objects.all()    
            context={
            'employee':employee,
            'employee_with_id_3':employee_with_id_3,
        }
            return redirect('emply')

@login_required
def vedio(request):
    return render(request,'center/vedio.html',{'name':request.user.username})

@login_required
def joinvedio(request):
    if request.method=="POST":
        roomID=request.POST['roomID']
        return redirect("/meeting?roomID=" + roomID)

    return render(request,'center/chat.html')



from django.shortcuts import render
from django.http import JsonResponse 
from center.models import Events 
 
# Create your views here.
def index(request):  
    all_events = Events.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'calender.html',context)
 
def all_events(request):                                                                                                 
    all_events = Events.objects.all()                                                                                    
    out = []                                                                                                             
    for event in all_events:                                                                                             
        out.append({                                                                                                     
            'title': event.name,                                                                                         
            'id': event.id,                                                                                              
            'start': event.start.strftime("%m/%d/%Y, %H:%M:%S"),                                                         
            'end': event.end.strftime("%m/%d/%Y, %H:%M:%S"),                                                             
        })                                                                                                               
                                                                                                                      
    return JsonResponse(out, safe=False) 
 
def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)
 
def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)
 
def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)