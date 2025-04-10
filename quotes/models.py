from django.db import models
from django.utils.text import slugify

class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(blank=True, null=True, unique=True)
    image = models.ImageField(upload_to='uploads/authors', blank=True, null=True)

    def save(self, *args, **kw):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kw)

    def __str__(self):
        return self.name

class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True)
    quote = models.TextField()
    meaning = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.quote[:50] + ('...' if len(self.quote) > 50 else '')
