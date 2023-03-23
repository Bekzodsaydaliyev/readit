from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        if self.user.get_full_name():
            return self.user.get_full_name()
        return self.user.username

    # @property
    # def full_name(self):
    #     if self.user.first_name and self.user.last_name:
    #         return f"{self.user.first_name} {self.user.last_name}"
    #     return self.user.username


def user_post_save(instance, sender, created, *args, **kwargs):
    if created:
        Profile.objects.create(user_id=instance.id)


post_save.connect(user_post_save, sender=User)


class Category(models.Model):
    title = models.CharField(max_length=222)

    def __str__(self):
        return self.title


class Tag(models.Model):
    title = models.CharField(max_length=222)

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=222)
    image = models.ImageField(upload_to='article')
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=222)
    email = models.EmailField()
    subject = models.CharField(max_length=222)
    message = models.TextField()


class Feedback(models.Model):
    name = models.CharField(max_length=222)
    avatar = models.ImageField(upload_to='avatar/')
    subject = models.CharField(max_length=222)
    description = models.TextField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)







