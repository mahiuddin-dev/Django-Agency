from django.db import models

# Create your models here.
class About(models.Model):
    Branch_Name = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)
    Email = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)

    def __str__(self):
        return self.Branch_Name    

class TeamMember(models.Model):
    Name = models.CharField(max_length=50)
    Job_Role = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='Startup/Team')
    
    def __str__(self):
        return self.Name


class SocialLink(models.Model):
    Member = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    Social_Media_Name = models.CharField(max_length=50)
    Social_Media_link = models.CharField(max_length=250)

    def __str__(self):
        return self.Member.Name + ' -> ' + self.Social_Media_Name


