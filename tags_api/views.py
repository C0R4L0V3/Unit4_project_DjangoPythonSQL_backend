from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import TagSerializer
from .models import TagSchema

class TagViewSet(viewsets.ModelViewSet):
    queryset = TagSchema.objects.all()
    serializer_class = TagSerializer

    '''
    ModelViewSet automatically provides implementations for common CRUD operations:
	•	GET (list and retrieve)
	•	POST (create)
	•	PUT/PATCH (update)
	•	DELETE (delete)

So, when you use ModelViewSet, you don’t need to manually define the logic for handling these operations like you would with individual views such as ListCreateAPIView and RetrieveUpdateDestroyAPIView. For example:
	•	ModelViewSet already knows how to fetch a list of objects (GET), and you don’t have to write a separate view like ListCreateAPIView.
	•	Similarly, it handles object retrieval (GET) and updates (PUT/PATCH) without needing a separate RetrieveUpdateDestroyAPIView.

    With ModelViewSet, you can use DRF’s routers to automatically generate the URLs for the viewset. This saves you from manually defining URL patterns for each action (e.g., GET, POST, PUT, DELETE). Here’s an example of how the router works:
    
    By using ModelViewSet, you’re following the DRY (Don’t Repeat Yourself) principle. Instead of repeating yourself across different generic views (ListCreateAPIView, RetrieveUpdateDestroyAPIView, etc.), you define the operations in a single ModelViewSet, which makes the code more consistent and easier to maintain.

    '''