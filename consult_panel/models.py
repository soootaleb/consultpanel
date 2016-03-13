from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.CharField(max_length=200)
    
    def __str__(self):
        return self.first_name + " " + self.last_name;

class Formation(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, default=1)
    
    def is_formation_of_user(self, the_user):
        return self.user.id == the_user.id;
    
    def __str__(self):
        return self.name