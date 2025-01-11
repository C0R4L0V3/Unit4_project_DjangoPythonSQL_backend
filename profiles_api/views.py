from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .serializers import ProfileSerializer
from .models import Profile

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    # modifying view to handle fetching profile by user
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        username = self.request.query_params.get('username')
        if user_id:
            return self.queryset.filter(user_id=user_id)
        elif username:
            return self.queryset.filter(user__username=username)
        return self.queryset

# class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Profile.objects.all().order_by('id')
#     serializer_class = ProfileSerializer