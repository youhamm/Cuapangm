from django.urls import path
from . import views

app_name = 'macrof'
urlpatterns = [
    path('cmacro/', views.cmacroMacro, name='cmacro'),
]