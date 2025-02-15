from django.db import models

# Create your models here.
# class Contact(models.Model):
#     name = models.CharField(max_length=250)
#     email = models.EmailField()
#     phone = models.CharField(max_length=10)
#     mode_of_contact = models.CharField('Contact by', max_length=50)
#     question_categories = models.CharField('How can we help you?', max_length=50)
#     message = models.TextField(max_length=3000)
#
#     def __str__(self):
#         return self.email


from django.db import models

# class ContactMessage(models.Model):
#     name = models.CharField(max_length=255)
#     phone = models.CharField(max_length=20)
#     email = models.EmailField()
#     message = models.TextField()
#     created_at = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"Message from {self.name}"

from django.db import models

class Contact(models.Model):
        name = models.CharField(max_length=255)
        phone = models.CharField(max_length=20)
        email = models.EmailField()
        message = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"Message from {self.name}"

