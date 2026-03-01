from rest_framework import generics
from .models import Dragon
from .serializers import DragonSerializer
from django.shortcuts import render

def dragon_ui(request):
    return render(request, 'dragons/index.html')

class DragonListCreate(generics.ListCreateAPIView):
    queryset = Dragon.objects.all()
    serializer_class = DragonSerializer

class DragonRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dragon.objects.all()
    serializer_class = DragonSerializer
    lookup_field = "pk"