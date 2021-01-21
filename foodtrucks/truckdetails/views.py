from django.shortcuts import render, HttpResponseRedirect
from .forms import AddShowTruck
from .models import Truck
import json
from datetime import datetime

#Show and Retrieve truck details
def add_show(request):
    if request.method == 'POST':
        form = AddShowTruck(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['name']
            loc = form.cleaned_data['location']
            opentime = form.cleaned_data['opentime']
            closetime = form.cleaned_data['closetime']
            register = Truck(name=nm, location=loc, opentime=opentime, closetime=closetime)
            register.save()
            form = AddShowTruck() 
    else:
        form = AddShowTruck()  
    truck = Truck.objects.all()    
    return render(request, 'truckdetails/addandshow.html', {'form': form, 'truck': truck})

#Update truck details
def update_data(request,id):
    if request.method == 'POST':
     pi = Truck.objects.get(pk=id)
     form =  AddShowTruck(request.POST, instance=pi)
     if form.is_valid():
        form.save()
    else:
        pi = Truck.objects.get(pk=id)
        form =  AddShowTruck(instance=pi)
    return render(request, 'truckdetails/update.html',{'form': form})

#Delete truck details
def delete_data(request,id):
    if request.method == 'POST':
        pi = Truck.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


#Map details
def map_details(request):
    truck = Truck.objects.all()
    ls = []
    t= datetime.now().strftime('%H:%M')
    print("mjjjjjjjjjjj",t)
    for i in truck:
        loc = i.location
        ls.append(loc)
    data = json.dumps(ls)
    return render(request, 'truckdetails/map.html',{'truck': data,'t':t})