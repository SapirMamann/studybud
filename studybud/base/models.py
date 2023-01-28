from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):                           #creating user that inherit from abstractuser and not from django.contrib.auth.models user
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True, unique=True)                           #it has to be unique so django wont face 2 emails trying to connect with differnet passwords and it wont know who it refers to
    bio = models.TextField(null=True)
    
    avatar = models.ImageField(null=True, default="avatar.svg") 
    
    USERNAME_FIELD = 'email'                            #so i can log in with my email and not by providing username
    REQUIRED_FIELDS = []
    
class Topic(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) #only takes the initial time stamp
    
    class Meta:
        ordering = ['-updated', '-created']  #method of meta 
        
    def __str__(self):
        return self.name
    
    
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) #only takes the initial time stamp
    
    class Meta:
        ordering = ['-updated', '-created']  #method of meta 
        
    def __str__(self):
        return self.body[0:50]