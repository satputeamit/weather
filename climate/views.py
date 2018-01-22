from django.shortcuts import render,redirect,HttpResponse
import requests
from .fetch_data import rec,scrap_data
from .models import MaxTemp,Country,MinTemp,MeanTemp,Rainfall,Sunshine
from django.views.generic import ListView,DetailView,TemplateView,View
from .generate_table import get_table,chart_data

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePage(TemplateView):
    template_name='climate/home.html'
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        context['temp']=Country.objects.all()
        return context

class UserLogin(TemplateView):
    # template_name='climate/login.html'
    def post(self, request):
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            login(request,user)
            return redirect('climate:upload')
        else:
            return HttpResponse('invalid')

    def get(self, request):
        return render(request,'climate/login.html')

class UserLogout(View):
    def get(self,request):
        logout(request)
        return redirect('climate:home')



# def home(request):
#     temp=Country.objects.all()
#     return render(request,'climate/home.html',{'temp':temp})

class UploadView(LoginRequiredMixin,TemplateView):
    template_name='climate/upload.html'


class Upadate_Data(LoginRequiredMixin,View):

    def get(self,request):
        scrap_data(self)
        return render(request,'climate/upload_success.html')

class CountryDetail(DetailView):
    template_name='climate/detail.html'

    def get_context_data(self,*args,**kwargs):
        print(kwargs)

        context=super(CountryDetail,self).get_context_data(*args,**kwargs)
        context['country']=Country.objects.get(pk=self.kwargs['pk'])
        return context

    def get_queryset(self):
        return Country.objects.all()


class CountrySubDetail(DetailView):
    template_name='climate/sub_detail.html'

    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        pk=self.kwargs['pk']
        context['data']=get_table(self,MaxTemp,pk)
        context['country']=Country.objects.get(pk=self.kwargs['pk'])
        context['type']='MAX_Temperature'
        return context

    def get_queryset(self):
        return Country.objects.all()

class CountryMinDetail(CountrySubDetail):
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        pk=self.kwargs['pk']
        context['data']=get_table(self,MinTemp,pk)

        context['type']='MIN_Temperature'
        return context

class CountryMeanDetail(CountrySubDetail):
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        pk=self.kwargs['pk']
        context['data']=get_table(self,MeanTemp,pk)

        context['type']='MEAN_Temperature'
        return context

class CountryRainDetail(CountrySubDetail):
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        pk=self.kwargs['pk']
        context['data']=get_table(self,Rainfall,pk)

        context['type']='Rainfall(mm)'
        return context

class CountrySunnyDetail(CountrySubDetail):
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        pk=self.kwargs['pk']
        context['data']=get_table(self,Sunshine,pk)

        context['type']='Sunshine(Total_hours)'
        return context

class ChartView(TemplateView):
    template_name='climate/charts.html'
    def get_context_data(self,*args,**kwargs):
        context=super().get_context_data(*args,**kwargs)
        pk=self.kwargs['pk']
        key=self.kwargs['key']
        if self.kwargs['tbl']=='MAX_Temperature':
            data=dict(get_table(self,MaxTemp,pk))
            context['max']='Max Temperature'
        if self.kwargs['tbl']=='MIN_Temperature':
            data=dict(get_table(self,MinTemp,pk))
            context['max']='Min Temperature'
        if self.kwargs['tbl']=='MEAN_Temperature':
            data=dict(get_table(self,MeanTemp,pk))
            context['max']='Mean Temperature'
        if self.kwargs['tbl']=='Sunshine(Total_hours)':
            data=dict(get_table(self,Sunshine,pk))
            context['max']='Sunshine(Total hours)'
        if self.kwargs['tbl']=='Rainfall(mm)':
            data=dict(get_table(self,Rainfall,pk))
            context['max']='Rainfall (mm)'
        data=chart_data(self,data[key])
        results = list(map(float, data))
        context['data']=results
        context['country']=Country.objects.get(pk=self.kwargs['pk'])
        context['year']=key


        return context
