from django.shortcuts import render

# Create your views here.

def stream_view(request):
    
    context = {
        
    }
    return render(request, "stream.html", context=context)