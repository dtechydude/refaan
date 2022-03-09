from django.db import models
from django.contrib.auth.models import User, AbstractUser, BaseUserManager
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image


COUNTRY_CHOICES = (
    ('nigeria','Nigeria'),
    ('other africa','Other Africa'),
    ('non africa', 'Non africa'),

)

trade_list = (
('mansory', 'Mansory'),
('furniture', 'Furniture'),
('welding', 'Welding'),
('automobile', 'Automobile'),
('computer', 'Computer'),
)

#class User(AbstractUser):
#    pass



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone = models.IntegerField(null=False, blank=False, default=00000000000)
    bio = models.TextField(max_length=5000, blank=True)
    country = models.CharField(max_length=40, choices=COUNTRY_CHOICES, default='select')
    TYPE_SELECT = (('female', 'Female'), ('male', 'Male'),)
    gender = models.CharField(max_length=11, choices=TYPE_SELECT, default='0')
    trade = MultiSelectField(choices=trade_list, default='mansory')


    def __str__(self):
        return f'{self.user.username} Profile'

    #overiding the save method so we can resize our images
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)


