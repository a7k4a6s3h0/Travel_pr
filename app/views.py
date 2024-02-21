from django.shortcuts import render



from .models import Travel_places
# Create your views here.

def homee(request):
    return render(request, 'index.html')   

def list_view(request):
    dic_book = {
        'name1': Travel_places.objects.all()
    }
    return render(request, 'booking.html',dic_book)    