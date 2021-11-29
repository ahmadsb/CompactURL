from django.db import models
from .utils import create_shortened_url

# Create your models here.
'''
Url shortener model
'''


class Shortener(models.Model):
    '''
    generate an url shortener based on the long one

    created -> date when the short url was created

    times_followed -> Times the shortened link has been followed

    long_url -> root/long url 

    short_url ->  an url shortener
    '''

    created = models.DateTimeField(auto_now_add=True)

    times_followed = models.PositiveIntegerField(default=0)

    long_url = models.URLField()

    short_url = models.CharField(max_length=15, unique=True, blank=True)

    class Meta:

        ordering = ["-created"]

    def __str__(self):

        return f'compact: {self.long_url} to {self.short_url}'

    def save(self, *args, **kwargs):
        # If I don't have short url so generate one
        if not self.short_url:
            # We pass the model instance
            self.short_url = create_shortened_url(self)

        super().save(*args, **kwargs)
