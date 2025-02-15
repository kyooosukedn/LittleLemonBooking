from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from restaurant.models import MenuItem, Booking
from datetime import date

class MenuItemTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.menu_item = MenuItem.objects.create(
            title='Test Item',
            price=10.99,
            inventory=50,
            category='main',
            description='Test description'
        )

    def test_get_menu_items(self):
        """Test retrieving menu items"""
        response = self.client.get(reverse('menuitem-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

class BookingTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.force_authenticate(user=self.user)

    def test_create_booking(self):
        """Test creating a new booking"""
        data = {
            'first_name': 'Test User',
            'reservation_date': date.today().isoformat(),
            'reservation_slot': 12
        }
        response = self.client.post(reverse('booking-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_bookings(self):
        """Test retrieving bookings"""
        response = self.client.get(reverse('booking-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class UserTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        """Test user registration"""
        data = {
            'username': 'newuser',
            'password': 'newpass123',
            'email': 'test@example.com'
        }
        response = self.client.post(reverse('user-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='newuser').exists())
