from django.db import models
from django.conf import settings
from PIL import Image as PILImage
import os


class Image(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.title

    def orientation(self):
        try:
            img_path = os.path.join(settings.MEDIA_ROOT, self.image.name)
            with PILImage.open(img_path) as img:
                width, height = img.size
                return 'landscape' if width > height else 'portrait'
        except Exception:
            return 'landscape'
