from django.db import models

# Create your models here.
class api_student(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    roll=models.PositiveIntegerField()
    desc=models.CharField(max_length=200)


    def __str__(self):
        return self.name
    

class Excelupload(models.Model):
    excel_file_upload=models.FileField(upload_to="excel/")

    def __str__(self):
        return str(self.excel_file_upload)