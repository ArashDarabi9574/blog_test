from django.db import models

# getting user model
# new branch commit
# User =  get_user_model()
# Create your models here.


class Post(models.Model):
    """
    This's a class to define post for blog app
    """

    author = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    status = models.BooleanField()
    category = models.ForeignKey("Category", on_delete=models.SET_NULL, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_data = models.DateTimeField()

    def __st__(self):
        return self.title

    def get_snippet(self):
        return self.content[0:5]


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
