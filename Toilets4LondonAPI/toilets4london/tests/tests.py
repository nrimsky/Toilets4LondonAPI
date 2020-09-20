from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class AuthenticationTests(APITestCase):
    toilet_list_url=reverse('toilet-list')

    def setUp(self):
        # create a new user making a post request to djoser endpoint
        self.user=self.client.post('/auth/users/',data={'email':'nina@example.com','password':'banana678!'})
        # obtain a json web token for the newly created user
        response=self.client.post('/auth/token/login/',data={'email':'nina@example.com','password':'banana678!'})
        self.token=response.data['auth_token']
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='TOKEN '+self.token)

    # retrieve a list of all user profiles while the request user is authenticated
    def test_userprofile_list_authenticated(self):
        response=self.client.get(self.toilet_list_url)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
    #
    # # retrieve a list of all user profiles while the request user is unauthenticated
    # def test_userprofile_list_unauthenticated(self):
    #     self.client.force_authenticate(user=None)
    #     response=self.client.get(self.profile_list_url)
    #     self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)
    #
    # # check to retrieve the profile details of the authenticated user
    # def test_userprofile_detail_retrieve(self):
    #     response=self.client.get(reverse('profile',kwargs={'pk':1}))
    #     # print(response.data)
    #     self.assertEqual(response.status_code,status.HTTP_200_OK)
    #
    #
    # # populate the user profile that was automatically created using the signals
    # def test_userprofile_profile(self):
    #     profile_data={'description':'I am a very famous game character','location':'nintendo world','is_creator':'true',}
    #     response=self.client.put(reverse('profile',kwargs={'pk':1}),data=profile_data)
    #     print(response.data)
    #     self.assertEqual(response.status_code,status.HTTP_200_OK)
