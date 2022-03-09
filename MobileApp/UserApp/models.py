from pickle import FALSE, TRUE
from django.db import models
class User(models.Model):
          email = models.EmailField()
          age = models.PositiveIntegerField()
          gender = models.BooleanField()
          password = models.CharField(max_length=50)
          hasbicycle = models.BooleanField(default=FALSE) 

          def __str__(self):
              return self.email    

#         name = models.CharField(max_length=50)
#         currentLocation = Location()
#         profilePhoto = models.ImageField(upload_to="pictures")
#         socialAccount = models.CharField(max_length=50)
