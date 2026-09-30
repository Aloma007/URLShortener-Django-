from django.db import models
import string
import random

def generate_short_code():
    # Generates a random 6-character string of letters and numbers
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=6))

class ShortURL(models.Model):
    url = models.URLField(max_length=2000)
    short_code = models.CharField(max_length=10, unique=True, default=generate_short_code)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    access_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.short_code} -> {self.url}"