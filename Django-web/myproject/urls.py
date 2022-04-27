from django.contrib import admin
from django.urls import path
from mydiary import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('new/', views.new, name="new"),
    path('detail/<int:index>', views.detail, name="detail"),
    path('edit/<int:index>', views.edit, name='edit'),
    path('detail/<int:pk>/delete', views.delete, name="delete"),
    path('complete/', views.complete, name="complete"),
]
