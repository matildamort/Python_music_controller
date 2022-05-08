from django.db import models
import string
import random

#creates a unique code, with the length of 6. If the code is not unique, it will continue to iterate through until a unique code is created.  
def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break
        
#return code

# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=10, default ="" , unique = True)
    #Creates host and limits each room to only have one host per room.
    host = models.CharField(max_length=50, unique = True)
    guest_can_pause = models.BooleanField(null=False, default = False)
    votes_to_skip = models.IntegerField(null=False, default =1)
    created_at = models.DateTimeField(auto_now_add=True)

    

    
