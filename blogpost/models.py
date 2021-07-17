from django.db import models

# Create your models here.
CATEGORY = (("bussiness", "ビジネス"),
            ("life", "生活"), ("other", "その他"))


class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=50)
    choices = CATEGORY
