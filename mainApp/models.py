from django.db import models


# Create your models here.
class MyCovidRecord(models.Model):
    unique_id = models.CharField(max_length=128)
    country_id = models.CharField(max_length=50)
    total_confirmed_cases = models.IntegerField()
    total_deaths_cases = models.IntegerField()
    total_recovered_cases = models.IntegerField()
    date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Country: " + self.country_id + " , total confirmed cases: " + str(self.total_confirmed_cases) + \
               " , total deaths cases: " + str(self.total_deaths_cases) + \
               ", total recovered cases: " + str(self.total_recovered_cases)
