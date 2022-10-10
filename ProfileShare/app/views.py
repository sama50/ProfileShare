from django.shortcuts import render , redirect ,HttpResponseRedirect
import uuid
from django.contrib.auth import logout
from app.forms import uploadimg , AddLink , AddProjectDetails , AddAchivement
from app.models import Details , LinkData , ProjectDetails , Achivement , Skill ,ShareDetails
 
def home(request):
    if request.user.is_authenticated:
        fm = uploadimg()
        detailsfm  = AddLink()
        projectfm = AddProjectDetails() 
        achivemtnfm = AddAchivement()
        imgdata = None
        linkdata = None
        projectis = None
        achimentis = None
        try:
            imgdata = Details.objects.get(user=request.user)
            linkdata = LinkData.objects.filter(user=request.user)
            projectis = ProjectDetails.objects.filter(user=request.user)
            achimentis = Achivement.objects.filter(user=request.user)
        except:
            pass
    
        return render(request,'index.html',{'fm':fm,'detailsfm':detailsfm,'imgdata':imgdata,'linkdata':linkdata,'projectfm':projectfm,'projectis':projectis,'achivemtnfm':achivemtnfm,'achimentis':achimentis})
    else:
        return HttpResponseRedirect('/login/')

def addprojectdetails(request):
    if request.method =='POST':
        data = AddProjectDetails(request.POST,request.FILES)
        if data.is_valid():
            projectname = data.cleaned_data['projectname']
            githublink = data.cleaned_data['githublink']
            image1 = data.cleaned_data['image1']
            image2 = data.cleaned_data['image2']
            desc = data.cleaned_data['desc']
             
            f = ProjectDetails(user=request.user,projectname=projectname,githublink=githublink,image1=image1,image2=image2,desc=desc)
            f.save()

    return redirect('/')

def addachimentdetails(request):
    if request.method == 'POST':
        data = AddAchivement(request.POST)
        if data.is_valid():
            nameofachivement = data.cleaned_data['nameofachivement']
            f = Achivement(user=request.user,nameofachivement=nameofachivement)
            f.save()

    return redirect('/')

def uploadurl(request):
    if request.method == 'POST':
        fm = uploadimg(request.POST,request.FILES)
        
        if fm.is_valid():
            name = fm.cleaned_data['name']
            eduaction = fm.cleaned_data['Education']
            email = fm.cleaned_data['email']
            image = fm.cleaned_data['image']
            f = Details(user=request.user,name=name,Education=eduaction,email=email,image=image)
            f.save()
    return redirect('/')

def shareprofile(request ,id):
    oid = ShareDetails.objects.get(nameid=id)
    detailsmodel = Details.objects.get(user=oid.user)
    linkdatamodel = LinkData.objects.filter(user=oid.user)
    projectDetailsmodel = ProjectDetails.objects.filter(user=oid.user)
    achimentModel = Achivement.objects.filter(user=oid.user)
    skillmodel = Skill.objects.filter(user=oid.user)
    return render(request,'profile.html',{'detailsmodel':detailsmodel,'linkdatamodel':linkdatamodel,'projectDetailsmodel':projectDetailsmodel,'achimentModel':achimentModel,'skillmodel':skillmodel})

def profileget(request):
    # detailuser = Details.objects.get(user=name)
    myid = None
    try:
        myid = ShareDetails.objects.get(user=request.user).nameid
    except:
        randomid = uuid.uuid4()
        f = ShareDetails(user=request.user,nameid=randomid)
        f.save()
        get = ShareDetails.objects.get(nameid=randomid)
        myid = randomid
    return redirect(str(myid)+'/')

def logoutby(request):
    logout(request)
    return HttpResponseRedirect('/login/')