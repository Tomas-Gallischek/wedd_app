from django.shortcuts import render
from . models import xp

def index(request):
    
    on_xp = xp.objects.first().on_xp
    on_xp_need = xp.objects.first().on_xp_need
    on_lvl = xp.objects.first().on_lvl
    ona_xp = xp.objects.first().ona_xp
    ona_xp_need = xp.objects.first().ona_xp_need
    ona_lvl = xp.objects.first().ona_lvl
    
    
    context = {
        'on_xp': on_xp,
        'on_xp_need': on_xp_need,
        'on_lvl': on_lvl,
        
        'ona_xp': ona_xp,
        'ona_xp_need': ona_xp_need,
        'ona_lvl': ona_lvl,
        
    }
    
    return render(request, 'main_app/index.html', context)

# Funkce pro tým Ženich
def on_view(request):
    on_xp = xp.objects.first().on_xp
    on_xp += 1
    xp.objects.update(on_xp=on_xp)
    xp.objects.first().save()
    
    return render(request, 'main_app/on.html')

# Funkce pro tým Nevěsta
def ona_view(request):
    ona_xp = xp.objects.first().ona_xp
    ona_xp += 1
    xp.objects.update(ona_xp=ona_xp)
    xp.objects.first().save()
     
    return render(request, 'main_app/ona.html')