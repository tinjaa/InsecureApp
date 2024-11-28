from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    # 5. Flaw Cryptographic Failure
    password = models.CharField(max_length=100)
    #admin = models.BooleanField(default=False)
