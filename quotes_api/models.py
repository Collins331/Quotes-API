from django.db import models

# Create your models here.

class Quote(models.Model):
    author = models.CharField(max_length=100, default='Unknown')
    category = models.CharField(max_length=100)
    description = models.TextField(blank=False, max_length=500)
    author_image = models.ImageField(default='unknown.png')
    created = models.DateTimeField(auto_now_add=True)
    platform = models.CharField(default='LincSoftwares', max_length=100)
    username = models.CharField(default='Lincoln_331', max_length=100)

    def __str__(self):
        return '%s %s %s' % (self.author, self.description, self.created)
