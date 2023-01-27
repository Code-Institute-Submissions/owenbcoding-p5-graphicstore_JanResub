from django.db import models
from django.contrib.auth.models import User

# Custom model newsletter 1


class Newsletter(models.Model):
    email = models.EmailField(max_length=254, null=False, blank=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True)
