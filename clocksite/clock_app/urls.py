from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.clock),
    path('shifts_list/', views.shifts_list),
    # path('account/', include('django.contrib.auth.urls')),
]
