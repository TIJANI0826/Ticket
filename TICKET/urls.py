"""TICKET URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
# from django.contrib.auth.views import login
from account.views import *
from account import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', HomeView.as_view(), name='home'),   
    url(r'^signup/$', UserRegistration.as_view(), name='user_registration'),
    url(r'^login/$',LoginFormView.as_view(),name='login'),
    url(
        r'^profile/$',
            ProfileView.as_view(),
        
        name="profile"
    ),
    url(r'^editprofile/(?P<pk>\d+)/update$',UpdateProfile.as_view(),name='editprofile'),
    url(r'^logout/$', LogoutView.as_view(),name='logout'),
    url(
        r'^halls/$',
        
            HallView.as_view(),
        
        name="halls"
    ),
    url(
        r'^booking/(?P<hall_pk>[\d]+)/$',
        
            HallBookingView.as_view(),
            name='new-booking'
        ),
    url(
        r'^events/$',
        
            EventView.as_view(),
        
        name="events"
    ),
    url(
        r'^event/(?P<pk>[\d]+)/$',
        
            EventDetails.as_view(),
            name='event_details'
        ),
   
    url(
        r'^tickets/$',
        
            TicketDetails.as_view(),
        
        name="edit_ticket_list"
    ),

    url(
        r'^tickets/(?P<pk>[\d]+)$',
        
            EditTicketDetails.as_view(),      
            name='edit_ticket'
    ),
    
    
#    MEMBER REGISTRATIOn
    
    url(
        r'^member/add/$',
        
            RegMemberView.as_view(),
    
        name="add_member"
    ),
    
    url(
        r'^event/(?P<pk>[\d]+)/$',
        
            MemberDetails.as_view(),
            name='member_details'
        ),

# LAUNDRY

url(
        r'^laundry/add/$',
        
            LaundryReg.as_view(),
    
        name="laundry"
    ),
    
url(
        r'^laundries/$',
        
            LaundryDetails.as_view(),
        
        name="laundrys"
    ),
url(
        r'^event/(?P<pk>[\d]+)/$',
        
            LaundryDetails.as_view(),
            name='laundries_details'
        ),
url(
    r'^print/$',Print.as_view(), name="print" 
)



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

