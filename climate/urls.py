from django.conf.urls import url
from . import views
app_name='climate'
urlpatterns=[
url(r'^$',views.HomePage.as_view(),name='home'),
url(r'^detail/(?P<pk>\d+)/$',views.CountryDetail.as_view(),name='detail'),
url(r'^sub_detail/(?P<pk>\d+)/$',views.CountrySubDetail.as_view(),name='sub_detail'),
url(r'^min_detail/(?P<pk>\d+)/$',views.CountryMinDetail.as_view(),name='min_detail'),
url(r'^mean_detail/(?P<pk>\d+)/$',views.CountryMeanDetail.as_view(),name='mean_detail'),
url(r'^rain_detail/(?P<pk>\d+)/$',views.CountryRainDetail.as_view(),name='rain_detail'),
url(r'^sun_detail/(?P<pk>\d+)/$',views.CountrySunnyDetail.as_view(),name='sun_detail'),
url(r'^charts/(?P<tbl>[\w-]+)/(?P<pk>\d+)/(?P<key>\d+)/$',views.ChartView.as_view(),name='charts'),
url(r'login/$',views.UserLogin.as_view(),name='login'),
url(r'^upload/$',views.UploadView.as_view(),name='upload'),
url(r'^update/$',views.Upadate_Data.as_view(),name='update'),
]
