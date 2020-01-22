from django.shortcuts import render
def index(request):
    return render(request,'warehouse/index.html')
def reg(request):
    if request.method=='POST':
        data1 = request.POST.get('nm','')
        data2 = request.POST.get('em', '')
        data3 = request.POST.get('ph', '')
        data4 = request.POST.get('us', '')
        data5 = request.POST.get('ps', '')
        data6 = request.POST.get('dob', '')
        data7 = request.POST.get('cty', '')
        data8 = request.POST.get('st','')
        song_obj = signup(Name=data1, Email=data2, Phone=data3, Username=data4, Password=data5, DOB=data6, City=data7, State=data8)
        song_obj.save()
        return render(request, 'warehouse/index.html')
    else:
        return render(request, 'warehouse/index.html')
def login(request):
    if request.method == 'POST':
        Uss = request.POST['us']
        Pss = request.POST['ps']
        try:
            d1 = signup.objects.get(Username=Uss)
            d2 = signup.objects.get(Password=Pss)
        except signup.DoesNotExist:
            d1 = None
            d2 = None
            if (Uss == d1 and Pss == d2):
              return render(request, 'warehouse/index.html')
            else:
               return render(request, 'warehouse/index.html')
        else:
            if (Uss == d1.Username and Pss == d2.Password):
                request.session['uid'] = d1.id
                return render(request, 'warehouse/index.html')
            else:
                return render(request, 'warehouse/index.html')
    return render(request, 'warehouse/index.html')

def logout(request):
    auth.logout(request)
    try:
        del request.session['userid']
    except KeyError:
        pass
    return render(request,'warehouse/index.html')
# Create your views here.
def about(request):
    return render(request,'warehouse/about.html')
def blog(request):
    return render(request,'warehouse/blog.html')
def contact(request):
    return render(request,'warehouse/contact.html')
def elements(request):
    return render(request,'warehouse/elements.html')
def main(request):
    return render(request,'warehouse/main.html')
def Property(request):
    return render(request,'warehouse/Property.html')
def property_details(request):
    return render(request,'warehouse/property_details.html')
def single_blog(request):
    return render(request,'warehouse/single_blog.html')