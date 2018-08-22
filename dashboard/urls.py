from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', TemplateView.as_view(template_name='dashboard/dashboard.html'), name='dashboard'),
    path('icons/', TemplateView.as_view(template_name='dashboard/icons.html'), name='icons'),
    path('map/', TemplateView.as_view(template_name='dashboard/map.html'), name='map'),
    path('notifications/', TemplateView.as_view(template_name='dashboard/notifications.html'), name='notifications'),
    path('tables/', TemplateView.as_view(template_name='dashboard/tables.html'), name='tables'),
    path('typography/', TemplateView.as_view(template_name='dashboard/typography.html'), name='typography'),
    path('upgrade/', TemplateView.as_view(template_name='dashboard/upgrade.html'), name='upgrade'),
    path('user/', TemplateView.as_view(template_name='dashboard/user.html'), name='user'),
    path('weather/', TemplateView.as_view(template_name='dashboard/weather.html', extra_context={
        'pagetitle': 'Weather Forecast: Lauttasaari, Helsinki'}), name='weather'),
]
