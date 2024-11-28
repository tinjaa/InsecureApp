from django.db import models

# 5. Flaw Cryptographic Failure
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
