from django.shortcuts import render, get_object_or_404
from .models import *
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, \
	ListAPIView, RetrieveAPIView
from .serializers import *


# Create your views here.

class MultipleFieldLookupMixin:
    def get_object(self):
        queryset = self.get_queryset()           
        filter = {}
        for slug in self.lookup_fields:
            if self.kwargs[slug]: 
                filter[slug] = self.kwargs[slug]
        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj
        
#------------------------------>
class GameList(ListCreateAPIView):
    queryset = Game.active.all()
    serializer_class = GameSerializer

class GameDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Game.active.all()
    serializer_class = GameSerializer
    lookup_fields = ['slug','id']

#---------------------------->
class SoftwareList(ListCreateAPIView):
    queryset = Software.active.all()
    serializer_class = SoftwareSerializer

class SoftwareDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Software.active.all()
    serializer_class = SoftwareSerializer
    lookup_fields = ['slug','id']

#---------------------------->
class PlatformList(ListCreateAPIView):
    queryset = Platform.active.all()
    serializer_class = PlatformSerializer

class PlatformDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Platform.active.all()
    serializer_class = PlatformSerializer
    lookup_fields = ['slug','id']

#---------------------------->
class GameCategoryList(ListCreateAPIView):
    queryset = Game_Category.active.all()
    serializer_class = GameCategorySerializer

class GameCategoryDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Game_Category.active.all()
    serializer_class = GameCategorySerializer
    lookup_fields = ['slug','id']

#---------------------------->
class SoftwareCategoryList(ListCreateAPIView):
    queryset = Software_Category.active.all()
    serializer_class = SoftwareCategorySerializer

class SoftwareCategoryDetail(MultipleFieldLookupMixin, RetrieveUpdateDestroyAPIView):
    queryset = Software_Category.active.all()
    serializer_class = SoftwareCategorySerializer
    lookup_fields = ['slug','id']



class CommentList(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    