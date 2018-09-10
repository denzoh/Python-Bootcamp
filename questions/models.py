from django.db import models
from students.models import CreateUser

# Create your models here.
class CreateQuestion(models.Model):
    category = models.CharField(max_length=255)
    body = models.TextField()
    url = models.TextField()
    pub_date = models.DateField()
    vote_total = models.IntegerField()
    hunter = models.ForeignKey(CreateUser,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.category

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
