
from django.urls import path,include
from watchlist_app.api.views import (StreamPlatformVS, ReviewList,ReviewDetail, 
                                     WatchListAV,WatchDetailsAV,
                                     StreamPlatformAV,StreamPlatformDetialAV,
                                     ReviewCreate,UserReview,WatchListGV)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream',StreamPlatformVS,basename='streamplatform')

urlpatterns = [
     
    path('list/',WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>/',WatchDetailsAV.as_view(), name='movie_detail'),
    path('',include(router.urls)),
    # path('stream/',StreamPlatformAV.as_view(),name='stream'),
    # path('stream/<int:pk>',StreamPlatformDetialAV.as_view(),name='stream_detail'),
    # path('review/',ReviewList.as_vsiew(),name='review_list'),
    # path('review/<int:pk>',ReviewDetail.as_view(),name='review_detail'),
    path('<int:pk>/review-create/',ReviewCreate.as_view(),name='review_create'),
    path('<int:pk>/reviews/',ReviewList.as_view(),name='review_list'),

    path('review/<int:pk>/',ReviewDetail.as_view(),name='review_detail'),
    path('reviews/',UserReview.as_view(),name='user-review_detail'),
    path('list2/',WatchListGV.as_view(),name='watch_movie_list'),
    

]
