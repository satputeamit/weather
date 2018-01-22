from .models import *


def chart_data(self,data):
    self.data=data
    l=[]
    for i in self.data:

        l.append(i)
    
    return (l)

def get_table(self,ModelName,pk):
    self.pk=pk
    self.ModelName=ModelName
    d={}
    arr=0
    y_list=[]
    yr_obj=self.ModelName.objects.filter(country=self.pk)
    for y in yr_obj:
        y_list.append(y.year)
    year=sorted(set(y_list))

    for yr in year:
        l=[]
        obj=self.ModelName.objects.filter(country=self.pk,year=yr)
        for t in obj:
            l.append(t.temp)

        d[yr]=l
        arr+=1
    return sorted(d.items())
