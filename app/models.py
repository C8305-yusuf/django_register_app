from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=254)
    mobile = models.CharField(max_length=50)
    
    GENDER = (
        ("Female" , "Female"),
        ("Male" , "Male"),
        ("Other" , "Other"),
        ("Prefer Not to" , "Prefer Not to"),
    )
    
    gender = models.CharField(max_length=50, choices=GENDER)
    number = models.CharField(null=True, blank=True, max_length=50, default="")
    image = models.ImageField(upload_to="profile_pics/", default="default_avatar.png")
    
    PATH = (
        ("AWS-DevOps" , "AWS-DevOps"),
        ("Full Stack" , "Full Stack"),
        ("Data Science" , "Data Science"),
        ("Cyber Security" , "Cyber Security"),
        ("Custom" , "Custom"),
    )
    
    path = models.CharField(max_length=50, choices=PATH)
    register_date = models.DateTimeField(auto_now_add = True)
    last_update_date = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return (f"{self.first_name} {self.last_name} - {self.path}")
        # return self.number + " " + self.last_name
