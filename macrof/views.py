from django.shortcuts import render
from django.http import HttpResponse
from .models import Macro
# Create your views here.

def cmacroMacro(request):
    macro_data = Macro.objects.get(pk=request.GET.get('pk',1))
    context = {'macro_data':macro_data}
    return render(request, 'macrof/registerMacro.html', context)