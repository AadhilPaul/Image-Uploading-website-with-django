from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to="profile_pics")
    description = models.TextField(default="This user has no description", blank=True)
    dob = models.DateField(default=None, blank=True, null=True)
    phone_number = models.IntegerField(default=None, null=True, blank=True)
    country = models.CharField(default="Unknown", max_length=55, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    class Meta:
        verbose_name_plural = "Profiles"

