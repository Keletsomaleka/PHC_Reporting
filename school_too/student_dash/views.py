
#from typing_extensions import dataclass_transform
from django.forms import forms
from django.shortcuts import render,redirect
from .forms import SignUpForm , StatsForm, FilterForm, ReportForm, FinancialForm
from django.contrib.auth.decorators import login_required
from .models import Church, ChurchLeader, Stats
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum



# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form=SignUpForm()
    return render(request, 'smart_dash/signup.html',{'form':form})

@login_required
def dash(request):
    if request.method == 'POST':
        form = StatsForm(request.POST)
        if form.is_valid():
            instance  = form.save()
            instance.username = request.user
            instance.save()
            return redirect('/')
    else:
        form = StatsForm()

    return render(request, 'smart_dash/index.html',{'form':form})

@login_required
def finance(request):
    if request.method == 'POST':
        form = FinancialForm(request.POST)
        if form.is_valid():
            instance  = form.save()
            instance.username = request.user
            instance.save()
            return redirect('/')
    else:
        form = FinancialForm()

    return render(request,'smart_dash/finance.html',{'form':form})

@login_required
def infoscreen(request):
    

    latest_time  = Stats.objects.last().created_at
    church_name = ChurchLeader.objects.filter(email=request.user)[0].church_name
    youth_g1 = Stats.objects.filter(username=request.user).filter(created_at=latest_time).filter(church_name=church_name).aggregate(Sum('youth_g1'))
    youth_g2 = Stats.objects.filter(username=request.user).filter(created_at=latest_time).filter(church_name=church_name).aggregate(Sum('youth_g2'))
    data1 = Stats.objects.filter(username=request.user).filter(created_at=latest_time).filter(church_name=church_name).aggregate(Sum('women'))
    ordained = Stats.objects.filter(username=request.user).filter(created_at=latest_time).filter(church_name=church_name).aggregate(Sum('ordained_ministers'))
    licensed = Stats.objects.filter(username=request.user).filter(created_at=latest_time).filter(church_name=church_name).aggregate(Sum('licensed_ministers'))
    mission =Stats.objects.filter(username=request.user).filter(created_at=latest_time).filter(church_name=church_name).aggregate(Sum('mission_workers'))
    children_g1 = Stats.objects.filter(username=request.user).filter(created_at=latest_time).filter(church_name=church_name).aggregate(Sum('children_g1'))
    children_g2 = Stats.objects.filter(username=request.user).filter(created_at=latest_time).filter(church_name=church_name).aggregate(Sum('children_g2'))
    children_g3 = Stats.objects.filter(username=request.user).filter(created_at=latest_time).filter(church_name=church_name).aggregate(Sum('children_g3'))



    mission = str(mission['mission_workers__sum'])
    pie2_data = [youth_g1['youth_g1__sum'],youth_g2['youth_g2__sum']]
    pie3_data = [children_g1['children_g1__sum'],children_g2['children_g2__sum'],children_g3['children_g3__sum']]
    licensed = str(licensed['licensed_ministers__sum'])
    ordained = str(ordained['ordained_ministers__sum'])
    data2 = Stats.objects.filter(username=request.user).filter(created_at=latest_time).aggregate(Sum('men'))
    pie_data = [data1['women__sum'],data2['men__sum']]
    print(pie3_data)
    return render(request, 'smart_dash/info.html', {'youth_data':pie2_data,
                                                    'data':ordained,
                                                    'data1':licensed,
                                                    'data2':mission,
                                                    'pie_data':pie_data,
                                                    'children_data':pie3_data})


@login_required
#@staff_member_required
def staff_info(request):
    user = request.user
    if user.is_superuser:
        if request.method == 'POST':
            form = FilterForm(request.POST)
            print(request.POST['church_name'])
            if request.POST['church_name'] != '': 
                latest_time  = Stats.objects.last().created_at
                data = Stats.objects.filter(church_name=request.POST['church_name']).filter(created_at = latest_time).aggregate(Sum('ordained_ministers'))
                data2 = Stats.objects.filter(church_name=request.POST['church_name']).filter(created_at = latest_time).aggregate(Sum('licensed_ministers'))
                data3 = Stats.objects.filter(church_name=request.POST['church_name']).filter(created_at=latest_time).aggregate(Sum('mission_workers'))
                d = Stats.objects.filter(church_name=request.POST['church_name']).filter(created_at = latest_time).aggregate(Sum('women'))
                c = Stats.objects.filter(church_name=request.POST['church_name']).filter(created_at = latest_time).aggregate(Sum('men'))
                youth_g1 = Stats.objects.filter(church_name=request.POST['church_name']).filter(created_at = latest_time).aggregate(Sum('youth_g1'))
                youth_g2 = Stats.objects.filter(church_name=request.POST['church_name']).filter(created_at = latest_time).aggregate(Sum('youth_g2'))
                children_g1 = Stats.objects.filter(church_name=request.POST['church_name']).filter(created_at = latest_time).aggregate(Sum('children_g1'))
                children_g2 = Stats.objects.filter(church_name=request.POST['church_name']).filter(created_at = latest_time).aggregate(Sum('children_g2'))
                children_g3 = Stats.objects.filter(church_name=request.POST['church_name']).filter(created_at = latest_time).aggregate(Sum('children_g3'))


            

                pi2_data = [youth_g1['youth_g1__sum'],youth_g2['youth_g2__sum']]
                pi3_data = [children_g1['children_g1__sum'],children_g2['children_g2__sum'],children_g3['children_g3__sum']]
                data = str(data['ordained_ministers__sum'])
                data2 = str(data2['licensed_ministers__sum'])
                data3 = str(data3['mission_workers__sum'])
                pi_data = [d['women__sum'],c['men__sum']]

            else:

                latest_time  = Stats.objects.last().created_at
                data = Stats.objects.filter(created_at = latest_time).aggregate(Sum('ordained_ministers'))
                data2 = Stats.objects.filter(created_at = latest_time).aggregate(Sum('licensed_ministers'))
                data3 = Stats.objects.filter(created_at=latest_time).aggregate(Sum('mission_workers'))
                d = Stats.objects.filter(created_at = latest_time).aggregate(Sum('women'))
                c = Stats.objects.filter(created_at = latest_time).aggregate(Sum('men'))
                youth_g1 = Stats.objects.filter(created_at = latest_time).aggregate(Sum('youth_g1'))
                youth_g2 = Stats.objects.filter(created_at = latest_time).aggregate(Sum('youth_g2'))
                children_g1 = Stats.objects.filter(created_at = latest_time).aggregate(Sum('children_g1'))
                children_g2 = Stats.objects.filter(created_at = latest_time).aggregate(Sum('children_g2'))
                children_g3 = Stats.objects.filter(created_at = latest_time).aggregate(Sum('children_g3'))


                data = str(data['ordained_ministers__sum'])
                data2 = str(data2['licensed_ministers__sum'])
                data3 = str(data3['mission_workers__sum'])
                pi2_data = [youth_g1['youth_g1__sum'],youth_g2['youth_g2__sum']]
                pi3_data = [children_g1['children_g1__sum'],children_g2['children_g2__sum'],children_g3['children_g3__sum']]
                pi_data = [d['women__sum'],c['men__sum']]
                print(pi2_data)
                
            return render(request, 'smart_dash/infostaff.html',{'data':data,'data2':data2,'data3':data3 ,'form':form, 'pi_data':pi_data,'pi2_data':pi2_data,'pi3_data':pi3_data})
        
            

        else:
            form = FilterForm()
            latest_time  = Stats.objects.last().created_at
            data = Stats.objects.filter(created_at = latest_time).filter(created_at = latest_time).aggregate(Sum('ordained_ministers'))
            data2 = Stats.objects.filter(created_at = latest_time).filter(created_at = latest_time).aggregate(Sum('licensed_ministers'))
            data3 = Stats.objects.filter(created_at = latest_time).aggregate(Sum('mission_workers'))
            d = Stats.objects.filter(created_at = latest_time).aggregate(Sum('women'))
            c = Stats.objects.filter(created_at = latest_time).aggregate(Sum('men'))
            youth_g1 = Stats.objects.filter(created_at = latest_time).aggregate(Sum('youth_g1'))
            youth_g2 = Stats.objects.filter(created_at = latest_time).aggregate(Sum('youth_g2'))
            children_g1 = Stats.objects.filter(created_at = latest_time).aggregate(Sum('children_g1'))
            children_g2 = Stats.objects.filter(created_at = latest_time).aggregate(Sum('children_g2'))
            children_g3 = Stats.objects.filter(created_at = latest_time).aggregate(Sum('children_g3'))


            data = str(data['ordained_ministers__sum'])
            data2 = str(data2['licensed_ministers__sum'])
            data3 = str(data3['mission_workers__sum'])
            pi_data = [d['women__sum'],c['men__sum']]
            pi2_data = [youth_g1['youth_g1__sum'],youth_g2['youth_g2__sum']]
            pi3_data = [children_g1['children_g1__sum'],children_g2['children_g2__sum'],children_g3['children_g3__sum']]
            
            return render(request, 'smart_dash/infostaff.html',{'data':data,'data2':data2,'data3':data3 , 'form':form, 'pi_data':pi_data,'pi2_data':pi2_data,'pi3_data':pi3_data})
    else:
        return redirect('/')
    


@login_required
def report(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            instance  = form.save()
            instance.username = request.user
            instance.save()
    
    else:
        form = ReportForm()

    return render(request,'smart_dash/reports.html', {'form':form})

def nav(request):
    return render(request,'smart_dash/nav2.html' )