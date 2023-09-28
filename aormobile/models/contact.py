from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    batch = models.IntegerField()
    status = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def full_name(self):
        fullname = "%s %s"%(self.first_name, self.last_name)
        return fullname
    
    def __str__(self):
        return self.full_name()