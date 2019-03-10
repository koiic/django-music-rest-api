from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from music.serializers import SongsSerializer
from .models import Songs


class BaseViewTest(APITestCase):
	client = APIClient()

	@staticmethod
	def create_song(title="", artist=""):
		if title != "" and artist != "":
			Songs.objects.create(title=title, artist=artist)

	def setUp(self):
		# add test data
		self.create_song("like glue", "sean paul")
		self.create_song("simple song", "konshens")
		self.create_song("love is wicked", "brick and lace")
		self.create_song("jam rock", "damien marley")


class GetAllSongsTest(BaseViewTest):
	"""
	This test ensures that all songs added in the setUp method
	exist when we make a GET request to the songs/ endpoint
	"""

	def test_get_all_songs(self):
		response = self.client.get(
			reverse('songs-all', kwargs={"version": "v1"})
		)
		expected_data = Songs.objects.all()
		serialized_object = SongsSerializer(expected_data, many=True)
		self.assertEqual(response.data, serialized_object.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
