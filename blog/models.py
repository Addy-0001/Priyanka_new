from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    


class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'images', blank = True)
    excerpt = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    content = models.TextField()
    slug = models.SlugField()

    def __str__(self):
        return f'{self.title}'