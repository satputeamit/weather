from django.db import models
from django.core.urlresolvers import reverse,reverse_lazy

MONTH_CHOICES=(
('JAN','JAN'),('FEB','FEB'),('MAR','MAR'),('APR','APR'),
('MAY','MAY'),('JUN','JUN'),('JUL','JUL'),('AUG','AUG'),
('SEP','SEP'),('OCT','OCT'),('NOV','NOV'),('DEC','DEC'),
)

class Country(models.Model):
    name=models.CharField(max_length=256)

    def __str__(self):
        return self.name

class MaxTemp(models.Model):

    country=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='max_countries')
    temp=models.DecimalField(max_digits=19,decimal_places=2)
    month=models.CharField(max_length=125, choices=MONTH_CHOICES)
    year=models.CharField(max_length=125)

    def __str__(self):
        return self.country.name +' '+self.month+' '+self.year
    class Meta:
        ordering=['-year']

    def get_absolute_url(self):
        return reverse_lazy('climate:sub_detail',kwargs={'pk':self.country.id})

class MinTemp(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='min_countries')
    temp=models.DecimalField(max_digits=19,decimal_places=2)
    month=models.CharField(max_length=125, choices=MONTH_CHOICES)
    year=models.CharField(max_length=125)

    def __str__(self):
        return self.country.name +' '+self.month+' '+self.year
    class Meta:
        ordering=['-year']

    def get_absolute_url(self):
        return reverse_lazy('climate:sub_detail',kwargs={'pk':self.country.id})

class MeanTemp(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='mean_countries')
    temp=models.DecimalField(max_digits=19,decimal_places=2)
    month=models.CharField(max_length=125, choices=MONTH_CHOICES)
    year=models.CharField(max_length=125)

    def __str__(self):
        return self.country.name +' '+self.month+' '+self.year
    class Meta:
        ordering=['-year']

    def get_absolute_url(self):
        return reverse_lazy('climate:sub_detail',kwargs={'pk':self.country.id})

class Rainfall(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='rainfall_countries')
    temp=models.DecimalField(max_digits=19,decimal_places=2)
    month=models.CharField(max_length=125, choices=MONTH_CHOICES)
    year=models.CharField(max_length=125)

    def __str__(self):
        return self.country.name +' '+self.month+' '+self.year
    class Meta:
        ordering=['-year']

    def get_absolute_url(self):
        return reverse_lazy('climate:sub_detail',kwargs={'pk':self.country.id})

class Sunshine(models.Model):
    country=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='sunshine_countries')
    temp=models.DecimalField(max_digits=19,decimal_places=2)
    month=models.CharField(max_length=125, choices=MONTH_CHOICES)
    year=models.CharField(max_length=125)

    def __str__(self):
        return self.country.name +' '+self.month+' '+self.year
    class Meta:
        ordering=['-year']

    def get_absolute_url(self):
        return reverse_lazy('climate:sub_detail',kwargs={'pk':self.country.id})


#Max temp, Min temp, Mean temp, Sunshine,
#and Rainfall for UK, England, Wales, and Scotland regions.
