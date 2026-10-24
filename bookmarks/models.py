from django.db import models


class Bookmark(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()
    CATEGORY_CHOICE = [
        ('Python', 'Python'),
        ('CSS', 'CSS'),
        ('HTML', 'HTML'),
        ('Django', 'Django'),
        ('JavaScript', 'JavaScript'),
        ('General', 'General'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICE, default='General')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
