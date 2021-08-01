from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from .models import clgdetails,clgdetails_forms,courses,courses_form,exams,exams_form,clg_link,clgadmi_form  #import all the models and modelform classes from the model.py program
from django.db.models import F
#from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login as demo_login, logout as demo_logout
from .forms import CreateUserForm

#chatbot
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#Creating a chatbot name Sweta
chatbot=ChatBot("Sweta")

trainer=ListTrainer(chatbot)

trainer.train([
    "Hello",
    "Hi, How can I help you?",
    "What is your name?",
    "My name is Sweta, I am your assistant to this website."
    "Do you know any good colleges for me?",
    "Yes, I do. My owner studies in ADAMAS University situated in northen West Bengal, India.  It is a good college to develop your career."
])

'''home page'''
def homepage(request):
    return render(request,"homepage.html")
'''end'''



def chatbotview(request):
    if request.method=="POST":
        val=request.POST.get("query")
        while True:
            ans=chatbot.get_response(val)
            return render(request,"chatbot.html",{"answer":ans,"ques":val})
    else:
        return render(request,"chatbot.html")
    return render(request,"chatbot.html")



# Create your views here.
def SignUp(request):
	if request.user.is_authenticated:
		return redirect('homepage')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'register.html', context)

def login(request):
	if request.user.is_authenticated:
		return redirect('homepage')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				demo_login(request, user)
				return redirect('homepage')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	demo_logout(request)
	return redirect('login')

'''
Working.... 


#Register new user
def SignUp(request):
    if request.method == 'POST':
        member = Member(username=request.POST['username'], password=request.POST['password'],  firstname=request.POST['firstname'], lastname=request.POST['lastname'])
        member.save()
        if member.save():
            name=request.POST.get("username")
        return redirect('/',{"user":name})
    else:
        return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')
'''

'''
#Signup
def SignUp(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('username')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,'Username Taken')
                return redirect("register.html")
            elif User.objects.filter(email=email).exists():
                messages.error(request,'Email Taken')
                return redirect("register.html")
            else:
                user=User.objects.create_user(username=username,password=password1,email=email,first_name=first_name,last_name=last_name)
                user.save();
                messages.success(request,'Account Created')
                return render(request,'login.html')
        else:
            messages.error(request,'Password donot match')
            return render(request,'register.html')
    else:
        return render(request,'register.html')
#end

#login
def login(request):
    if request.method=="POST":
        username=request.POST.get['username']
        password=request.POST.get['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("homepage.html")
        else:
            messages.error(request,"invalid credentials")
            return render(request,"login.html")
    else:
        return render(request,"login.html")
#end
'''


'''list of top colleges'''
def topclglist(request):
    topclgs=clgdetails.objects.filter(Ratings__gt=4)
    return render(request,"topclgpage.html",{'topclgs':topclgs})
'''end'''

'''list of top courses'''
def topcourse(request):
    course_list=courses.objects.all()
    return render(request,"topcoursepage.html",{'topcourse':course_list})
'''end'''

'''list of top exams'''
def topexam(request):
    exam_list=exams.objects.all()
    return render(request,"topexamspage.html",{'topexams':exam_list})
'''end'''

'''list of colleges'''
def clglist(request):
    details=clgdetails.objects.all()
    return render(request,"clglistpage.html",{'allclgs':details})
"""end"""

"""college search"""
def clgsearch(request):
    details=clgdetails.objects.all()
    if request.method=="GET":
        item=request.GET.get("clgsearch")
        if item:
            match=clgdetails.objects.filter(Name__contains=item)
            if match:
                return render(request,"clglistpage.html",{'searchdata':match})
            else:
                messages.success(request,"Invalid Search Request!!!")
                return render(request,"clglistpage.html",{'allclgs':details})
        else:
            messages.success(request,"Invalid Search Request!!!")
            return render(request,"clglistpage.html",{'allclgs':details})
    return render(request,"clglistpage.html",{'allclgs':details})

"""college details"""
def clgdetailspage(request,pk):
    item=get_object_or_404(clgdetails,pk=pk)
    value=getattr(item,"College_ID")
    match=clgdetails.objects.filter(College_ID__exact=value)
    course_match=courses.objects.filter(College_ID__exact=value)
    return render(request,"clgdetailspage.html",{'clgdata':match,'course':course_match})
"""end"""

#course details
def coursedetailspage(request,pk):
    item=get_object_or_404(courses,pk=pk)
    value=getattr(item,"Course_ID")
    match=courses.objects.filter(Course_ID__exact=value)
    return render(request,"coursedetailspage.html",{'coursedesc':match})

#exam details
def examdetailspage(request,pk):
    item=get_object_or_404(exams,pk=pk)
    value=getattr(item,"Exam_ID")
    match=exams.objects.filter(Exam_ID__exact=value)
    return render(request,"examsdetailspage.html",{'examsdesc':match})

"""college details form"""
def clgdetails_save(request):
    if request.method=="POST":
        form=clgdetails(request.POST)
        if form.is_valid():
            form.save()
            clgid=clgdetails.objects.latest("College_ID")
            messages.success(request,"Records saved!!!! College ID:")
            return render(request,"clgdetails_form.html",{'clgid':clgid})
        else:
            messages.MessageFailure(request,"Invalid Input!!!")
    return render(request,"clgdetails_form.html")
"""end"""

#Admissions
def admission(request):
    admi_list=clg_link.objects.all()
    return render(request,"admission.html",{'admi':admi_list})