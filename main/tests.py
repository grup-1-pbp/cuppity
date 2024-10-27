from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from main.models import Food

class FoodCRUDTests(TestCase):
    def setUp(self):
        # Create a test user and log them in (since views may require login)
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        # Create a sample Food object for testing edit and delete functionality
        self.food = Food.objects.create(
            name='Test Food',
            restaurant='Test Restaurant',
            price=100,
            deskripsi='A test description',
            image_url='http://example.com/test.jpg',
            preference='Indo'
        )

    def test_add_food(self):
        # Test the add food functionality with a POST request
        url = reverse('addProduct:add_food')
        response = self.client.post(url, {
            'name': 'Sample Food',
            'restaurant': 'Sample Restaurant',
            'price': 150,
            'deskripsi': 'A description of the food',
            'image_url': 'http://example.com/sample.jpg',
            'preference': 'Chin'
        })

        # Check the response JSON
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {'success': True})

        # Verify that the food was added to the database
        self.assertTrue(Food.objects.filter(name='Sample Food').exists())

    def test_edit_food(self):
        # Test the edit functionality for an existing food item
        url = reverse('addProduct:edit_food', args=[self.food.id])
        response = self.client.post(url, {
            'name': 'Updated Food',
            'restaurant': 'Updated Restaurant',
            'price': 200,
            'deskripsi': 'Updated description',
            'image_url': 'http://example.com/updated.jpg',
            'preference': 'West'
        })

        # Check for a redirect after a successful edit
        self.assertEqual(response.status_code, 302)

        # Refresh the food object from the database and verify changes
        self.food.refresh_from_db()
        self.assertEqual(self.food.name, 'Updated Food')
        self.assertEqual(self.food.restaurant, 'Updated Restaurant')
        self.assertEqual(self.food.price, 200)
        self.assertEqual(self.food.deskripsi, 'Updated description')
        self.assertEqual(self.food.image_url, 'http://example.com/updated.jpg')
        self.assertEqual(self.food.preference, 'West')

    def test_delete_food(self):
        # Test the delete functionality for an existing food item
        url = reverse('addProduct:delete_food', args=[self.food.id])
        response = self.client.post(url)

        # Check for a redirect after a successful delete
        self.assertEqual(response.status_code, 302)

        # Verify that the food object was deleted from the database
        self.assertFalse(Food.objects.filter(id=self.food.id).exists())