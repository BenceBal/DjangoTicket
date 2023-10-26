from django.db import models

class ShopCustomer(models.Model):

    personalid = models.CharField(max_length=30, primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)  
    age =models.IntegerField()
    joined = models.DateField(auto_now_add=True)
    fanClubMember = models.BooleanField(default=False)
    fanClubMemberid = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.firstName

