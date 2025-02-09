from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from watchlist_app.api import serializers
from watchlist_app import models


class StreanPlatformTestcase(APITestCase):

  def setUp(self):
    self.user= User.objects.create_user(username = 'test',
                                password = 'password')
    self.token = Token.objects.get(user__username=self.user)
    self.client.credentials(HTTP_AUTHORIZATION = 'Token '+self.token.key)

    self.stream = models.StreamPlatform.objects.create(name='netflix',
                                                       about='#1 streaming Platform',website="http://netflix.com")

  def test_streamplatform_create(self):
    data = {

        "name":"Netflix",
        'about':'#1 streaming Platform',
        'website':"http://netflix.com"

    }

    reseponse = self.client.post(reverse('streamplatform-list'),data)

    self.assertEqual(reseponse.status_code,status.HTTP_403_FORBIDDEN)

  def test_streamplatform_list(self):
    response = self.client.get(reverse('streamplatform-list'))
    self.assertEqual(response.status_code,status.HTTP_200_OK)

  def test_streamplatform_ind(self):
    response = self.client.get(reverse('streamplatform-detail',args=(self.stream.id,)))
    self.assertEqual(response.status_code,status.HTTP_200_OK)

class WatchListTestCases(APITestCase):

  def setUp(self):
    self.user= User.objects.create_user(username = 'test',
                                password = 'password')
    self.token = Token.objects.get(user__username=self.user)
    self.client.credentials(HTTP_AUTHORIZATION = 'Token '+self.token.key)

    self.stream = models.StreamPlatform.objects.create(name='netflix',
                                                       about='#1 streaming Platform',website="http://netflix.com")
    self.watchlist = models.WatchList.objects.create(platform=self.stream,title='hum',storyline='movie',active=True)
  
  def test_watchlist_create(self):
    data = {
      'platform':self.stream,
      'title':'hum',
      'storyline':'movie',
      'active':True

    }
    reseponse = self.client.post(reverse('movie_list'),data)
    self.assertEqual(reseponse.status_code,status.HTTP_403_FORBIDDEN)

  def test_watchlist_list(self):
    response = self.client.get(reverse('movie_list'))
    self.assertEqual(response.status_code,status.HTTP_200_OK)

  def test_watchlist_ind(self):
    response = self.client.get(reverse('movie_detail',args=(self.watchlist.id,)))
    self.assertEqual(response.status_code,status.HTTP_200_OK)
    self.assertEqual(models.WatchList.objects.count(),1)
    self.assertEqual(models.WatchList.objects.get().title,'hum')

class ReviewTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username="example", password="Password@123")
        self.token = Token.objects.get(user__username=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        self.stream = models.StreamPlatform.objects.create(name="Netflix", 
                                about="#1 Platform", website="https://www.netflix.com")
        self.watchlist = models.WatchList.objects.create(platform=self.stream, title="Example Movie",
                                storyline="Example Movie", active=True)
        self.watchlist2 = models.WatchList.objects.create(platform=self.stream, title="Example Movie",
                                storyline="Example Movie", active=True)
        self.review = models.Review.objects.create(review_user=self.user, rating=5, description="Great Movie", 
                                watchlist=self.watchlist2, active=True)
    
    def test_review_create(self):
        data = {
            "review_user": self.user,
            "rating": 5,
            "description": "Great Movie!",
            "watchlist": self.watchlist,
            "active": True
        }

        response = self.client.post(reverse('review_create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Review.objects.count(), 2)

        response = self.client.post(reverse('review_create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_review_create_unauth(self):
        data = {
            "review_user": self.user,
            "rating": 5,
            "description": "Great Movie!",
            "watchlist": self.watchlist,
            "active": True
        }

        self.client.force_authenticate(user=None)
        response = self.client.post(reverse('review_create', args=(self.watchlist.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_review_update(self):
        data = {
            "review_user": self.user,
            "rating": 4,
            "description": "Great Movie! - Updated",
            "watchlist": self.watchlist,
            "active": False
        }
        response = self.client.put(reverse('review_detail', args=(self.review.id,)), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_list(self):
        response = self.client.get(reverse('review_list', args=(self.watchlist.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_review_ind(self):
        response = self.client.get(reverse('review_detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_review_ind_delete(self):
        response = self.client.delete(reverse('review_detail', args=(self.review.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_review_user(self):
        response = self.client.get('/watch/reviews/?username' + self.user.username)
        self.assertEqual(response.status_code, status.HTTP_200_OK)