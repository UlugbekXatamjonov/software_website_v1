# from .views import list_view, software_detail, game_detail, game_like
from django.urls import path
from .views import *

app_name = "software"

urlpatterns = [
    path('games/<int:id>/<slug:slug>/', GameDetail.as_view()),
    path('games/', GameList.as_view()),

    path('softwares/<int:id>/<slug:slug>/', SoftwareDetail.as_view()),
    path('softwares/', SoftwareList.as_view()),

    path('platforms/<int:id>/<slug:slug>/', PlatformDetail.as_view()),
    path('platforms/', PlatformList.as_view()),

    path('game_category/<int:id>/<slug:slug>/', GameCategoryDetail.as_view()),
    path('game_category/', GameCategoryList.as_view()),

    path('software_category/<int:id>/<slug:slug>/', SoftwareCategoryDetail.as_view()),
    path('software_category/', SoftwareCategoryList.as_view()),


    # path('comments/', CommentList.as_view()),
    # path('comments/<int:pk>/', CommentDetail.as_view()),

]
