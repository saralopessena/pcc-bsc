from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField 



class Posts(models.Model):
    title = models.CharField(max_length=30)
    create_at = models.DateTimeField(auto_now_add=True)
    description = RichTextUploadingField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    link_img = models.CharField(null=True, max_length=255)
    def __str__(self):
        return self.title


class Comments(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=255)
    status = models.BooleanField(default=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert, force_update, using, update_fields)