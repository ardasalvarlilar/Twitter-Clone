from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.urls import reverse
import uuid
# Create your models here.

class Tags(models.Model):
   title = models.CharField(max_length=50,null=True,blank=False)
   slug = AutoSlugField(populate_from='title', unique=True)

   def __str__(self):
    return f'{self.title}'

class Post(models.Model):
  title = models.CharField(max_length=200,null=True,blank=False)
  tags = models.ManyToManyField(Tags)
  content = models.TextField()
  image= models.FileField(upload_to='post_images',blank=True)
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  posted_at= models.DateTimeField(auto_now_add=True)
  # slug = models.SlugField(unique=True, blank=True, null=True)
  slug = AutoSlugField(populate_from="title", unique=True)


  def __str__(self):
    return f'{self.title}-{self.user}-{self.content}'


  # def save(self, *args, **kwargs):
  #   if not self.slug:
  #     random_number = str(uuid.uuid4().int)[:1000000000]
  #     self.slug = f"{slugify(self.title)}-{random_number}"
  #     super().save(*args, **kwargs)




class Yorum(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments',null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.FileField(upload_to='comment_images',blank=True)
    commented_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True,blank=False,null=True)

    def generate_slug(self):
      return f'{self.post}-{self.author.username}-{self.content[:30]}'
    slug = AutoSlugField(populate_from='generate_slug', unique=True)

    def __str__(self):
        return f'{self.author.username} - {self.commented_at}'