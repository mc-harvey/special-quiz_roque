from django.db import models
from django.conf import settings
import random
from django.utils.text import slugify
import os


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    new_filename = random.randint(1, 151251251)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    
    return f"post_images/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)
# Create your models here.
class Post(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.content[:50])
            unique_slug = base_slug
            counter = 1
            while Post.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

def __str__(self):
    return f"Post by {self.user.username} on {self.created_at}"




