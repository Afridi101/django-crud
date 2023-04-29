from django.db import models
# Create your models here.


class Test(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=512)
    # file = models.ImageField(upload_to='images/', null=True, blank=True)


# class User(models.Model):
#         id = models.AutoField(max_length=100)
#         password = models.CharField(max_length=255)
#         last_login = models.DateTimeField()
#         is_superuser = models.BooleanField()
#         username = models.CharField(max_length=100)
#         first_name = models.CharField(max_length=100)
#         email = models.EmailField()
#         date_joined = models.DateTimeField()
