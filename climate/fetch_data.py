import requests
from django.shortcuts import get_object_or_404
from .models import *
import requests
from bs4 import BeautifulSoup
import threading

def rec(self,ModelName,path):
    self.path=path
    self.ModelName=ModelName
    ls=[]
    l=[]
    month=''
    country=''
    pk=''
    tc=0
    mc=0
    yc=1
    cnt=0
    # def store_record(request):

    res=requests.get(self.path)
    file=list((res.text).split('\r\n'))
    for i in file:
        sub_list=list((i).split())
        if len(sub_list)>0:
            ls.append(sub_list)
    country=ls[0][0]

    if Country.objects.filter(name__iexact=country).count()==1:
        pass
    else:
        obj=Country(name=country)
        obj.save()
    contry_obj=get_object_or_404(Country,name=country)

    for i in ls[7:]:
        if mc <=22:
            for j in ls[7:]:
                t=j[tc]
                m=ls[6][mc]
                y=j[yc]
                if self.ModelName.objects.filter(country=contry_obj,month=m,year=y).count()==1:
                    pass
                else:
                    temp_obj=self.ModelName(country=contry_obj,temp=t,month=m,year=y)
                    temp_obj.save()
                    cnt=cnt+1
                    print(cnt)

        tc+=2
        mc+=2
        yc+=2
    print('Donne')

def scrap_data(self):
    r= requests.get('https://www.metoffice.gov.uk/climate/uk/summaries/datasets#Yearorder')
    soup=BeautifulSoup(r.content,"html.parser")
    data=soup.find_all("a",{"class":"external"})
    l=[]
    lmin=[]
    lmax=[]
    lmean=[]
    lsun=[]
    lrain=[]
    for x in data:
        d=x.get('href')
        l.append(d)

    for j in l:
        if 'Tmin/ranked' in j:
            lmin.append(j)
        if 'Tmax/ranked' in j:
            lmax.append(j)
        if 'Tmean/ranked' in j:
            lmean.append(j)
        if 'Sunshine/ranked' in j:
            lsun.append(j)
        if 'Rainfall/ranked' in j:
            lrain.append(j)

    for path in lmin[:5]:
        rec(self,MinTemp,path)
    for path in lmax[:5]:
        rec(self,MaxTemp,path)
    for path in lmean[:5]:
        rec(self,MeanTemp,path)
    for path in lsun[:5]:
        rec(self,Sunshine,path)
    for path in lrain[:5]:
        rec(self,Rainfall,path)
