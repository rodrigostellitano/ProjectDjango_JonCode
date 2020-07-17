from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS = (
        ('rascunho', 'Rascunho'),
        ('publicado','Publicado'),

    )


    title = models.CharField(max_length=250)
    slug  = models.CharField(max_length=250)
    author = models.ForeignKey(User,
                                on_delete=models.CASCADE)
    content = models.TextField()
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=timezone.now)
    changed = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                                choices=STATUS,
                                default='rascunho')

    class Meta:
        ordering = ('title',)

    def __str__(self):
        #return self.title
        return '{} - {}' .format(self.title, self.status)

# Create your models here.
