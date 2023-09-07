from .models import Redes

def context(request):
    dict={}
    listRedes=Redes.objects.all()
    for redes in listRedes:
        dict[redes.key]=redes.url
    return dict 
