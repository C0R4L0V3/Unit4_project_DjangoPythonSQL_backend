from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import viewsets
from .serializers import ProfileSerializer
from .models import Profile
from blogpost_api.models import BlogPostSchema
from blogpost_api.serializers import BlogPostSerializer
from django.http import JsonResponse
from rest_framework import generics

class ProfileView(generics.ListCreateAPIView):
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer
    
    def retrieve(self, request, pk=None):
        try:
            #get the profile using the user ID (pk in this case)
            profile = Profile.objects.get(user_id=pk)
            profile_data = ProfileSerializer(profile).data

            #fetch the user's blogs
            blog_post = BlogPostSchema.objects.filter(author=profile.user)
            blog_post_data = BlogPostSerializer(blog_post, many=True).data

            #  combine the profile and blog post data
            res_data = {
                'profile': profile_data,
                'blogs': blog_post_data
            }
            print(res_data)
            return JsonResponse(res_data)
        except Profile.DoesNotExist:
            raise NotFound('Profile not found')
        
class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all().order_by('id')
    serializer_class = ProfileSerializer

    def retrieve(self, request, pk=None):
        try:
            #get the profile using the user ID (pk in this case)
            profile = Profile.objects.get(user_id=pk)
            profile_data = ProfileSerializer(profile).data

            #fetch the user's blogs
            blog_post = BlogPostSchema.objects.filter(author=profile.user)
            blog_post_data = BlogPostSerializer(blog_post, many=True).data

            #  combine the profile and blog post data
            res_data = {
                'profile': profile_data,
                'blogs': blog_post_data
            }
            print(res_data)
            return JsonResponse(res_data)
        except Profile.DoesNotExist:
            raise NotFound('Profile not found')

# class ProfileViewSet(viewsets.ModelViewSet):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer

#     # modifying to combine user profile and users blog posts
#     def retrieve(self, request, pk=None):
#         try:
#             #get the profile using the user ID (pk in this case)
#             profile = Profile.objects.get(user_id=pk)
#             profile_data = ProfileSerializer(profile).data

#             #fetch the user's blogs
#             blog_post = BlogPostSchema.objects.filter(author=profile.user)
#             blog_post_data = BlogPostSerializer(blog_post, many=True).data

#             #  combine the profile and blog post data
#             res_data = {
#                 'profile': profile_data,
#                 'blogs': blog_post_data
#             }
#             print(res_data)
#             return JsonResponse(res_data)
#         except Profile.DoesNotExist:
#             raise NotFound('Profile not found')
 



    
    # modifying view to handle fetching profile by user
    # def get_queryset(self):
    #     user_id = self.request.query_params.get('user_id')
    #     username = self.request.query_params.get('username')
    #     if user_id:
    #         return self.queryset.filter(user_id=user_id)
    #     elif username:
    #         return self.queryset.filter(user__username=username)
    #     return self.queryset

# class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Profile.objects.all().order_by('id')
#     serializer_class = ProfileSerializer