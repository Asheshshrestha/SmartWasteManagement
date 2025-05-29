from django.test import TestCase, Client
from django.contrib.auth.models import User
from notifications.signals import notify
from django.urls import reverse

from SmartWasteMS.bin.models import dustbin # Assuming this is the correct path to your dustbin model

class NotificationURLTest(TestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create a dustbin
        self.dustbin_instance = dustbin.objects.create(
            bin_no='BIN001', 
            # Add other required fields for your dustbin model here
            # For example:
            # location='Test Location',
            # capacity=100,
            # current_fill_level=0, 
            # status='Empty'
        )
        
        # Log in the user (important for accessing pages that require authentication)
        self.client = Client()
        self.client.login(username='testuser', password='testpassword')

    def test_notification_detail_link(self):
        # Create a notification for the user about the dustbin
        # The 'verb' can be anything descriptive, e.g., "is full"
        notify.send(
            sender=self.user,  # Or another appropriate sender, like a system user or the dustbin itself if it makes sense
            recipient=self.user,
            verb='is full',
            target=self.dustbin_instance,
            description=f'Dustbin {self.dustbin_instance.bin_no} is full.'
        )
        
        # Get the URL for the notification page
        # Assuming 'notifications_page' is the name of the URL pattern for notice.html
        # You might need to adjust this if your URL pattern has a different name
        # For example, if it's in an app namespace, it might be 'notifications:notice_list'
        # If you don't have a name for it, you can use the direct path '/notice/'
        try:
            # Attempt to reverse the URL if it's named 'notice_list' or similar
            # This is a common name for notification lists. Adjust if your app uses a different name.
            # If your notifications app has an app_name, prefix it like 'notifications:notice_list'
            notification_page_url = reverse('notifications:all') # Common name for all notifications
        except Exception:
            # Fallback to a hardcoded URL if reversing fails (adjust path if necessary)
            notification_page_url = '/notice/' 
            # Or, if you have a specific URL for unread notices:
            # notification_page_url = reverse('notifications:unread')


        # Simulate a GET request to the notification page
        response = self.client.get(notification_page_url)
        
        # Check that the request was successful
        self.assertEqual(response.status_code, 200)
        
        # Construct the expected detail URL
        # Assuming 'update_dustbin_data' is the name of your URL pattern for updating dustbin data
        # and it takes 'bin_no' as an argument.
        expected_detail_url = reverse('update_dustbin_data', args=[self.dustbin_instance.bin_no])
        
        # Check if the expected URL is present in the response content
        # This is a simple check. For more robust parsing, BeautifulSoup or Django's assertContains could be used.
        # We are looking for the href attribute within an anchor tag.
        # Example: <a href="/update_dustbin_data/BIN001/">Detail</a>
        self.assertContains(response, f'href="{expected_detail_url}"', html=True)

    def tearDown(self):
        # Clean up created objects
        self.user.delete()
        self.dustbin_instance.delete()

# Example of how your dustbin model might look in SmartWasteMS/bin/models.py
# (This is for context, not part of the tests.py file itself)
# from django.db import models
# class dustbin(models.Model):
#     bin_no = models.CharField(max_length=100, unique=True)
#     location = models.CharField(max_length=255)
#     capacity = models.IntegerField()
#     current_fill_level = models.IntegerField(default=0)
#     status = models.CharField(max_length=50, default='Empty')
#
#     def __str__(self):
#         return self.bin_no
#
#     class Meta:
#        db_table='dustbin'
#        verbose_name_plural='dustbins'
