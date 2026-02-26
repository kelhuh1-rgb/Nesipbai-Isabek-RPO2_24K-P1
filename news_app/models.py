from django.db import models

class Category(models.Model):
    name = models.CharField('Название категорий', max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField('Название поста',max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField('Описание')
    image_URL = models.CharField('ccылка на картинку', max_length=500)
    created_at = models.DateTimeField('время записи', auto_now_add=True)

    def __str__(self):
        return self.title

class Adv(models.Model):
    name = models.CharField("Compony name", max_length=255, default="Compony name")
    image_url = models.CharField("URL ссылка", max_length=500)

    def __str__(self):
        return self.name
