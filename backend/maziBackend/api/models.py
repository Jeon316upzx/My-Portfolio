from django.db import models


class Article (models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    title = models.CharField(max_length=300)
    content = models.TextField(max_length=10000)
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
