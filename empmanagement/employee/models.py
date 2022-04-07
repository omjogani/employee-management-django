from pyexpat import model
from django.db import models

from pickle import TRUE
from turtle import title
from django.db import models


designations_opt = (
    ('Team Leader','Team Leader'),
    ('Project Manager','Project Manager'),
    ('Senior Developer','Senior Developer'),
    ('Junior Developer','Junior Developer'),
    ('Intern','Intern'),
    ('QA Tester','QA Tester')
)

months = (
    ('January','January'),
    ('February','February'),
    ('March','March'),
    ('April','April'),
    ('May','May'),
    ('June','June'),
    ('July','July'),
    ('August','August'),
    ('September','September'),
    ('October','October'),
    ('November','November'),
    ('December','December')
)

days = (('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),
('11','11'),('12','12'),('13','13'),('14','14'),('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),
('21','21'),('22','22'),('23','23'),('24','24'),('25','25'),('26','26'),('27','27'),('28','28'),('29','29'),('30','30'),('31','31'))

# Create your models here.

class Employee(models.Model):
    eID = models.CharField(primary_key=True,max_length=20)
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    phoneNo = models.CharField(max_length=12,unique=True)
    email = models.EmailField(max_length=70,unique=True)
    addharNo = models.CharField(max_length=20,unique=True)
    dOB = models.DateField()
    designation = models.CharField(max_length=50,choices=designations_opt)
    salary = models.CharField(max_length=20)
    joinDate = models.DateField()

    def __str__(self):  
        return "%s %s" % (self.eID, self.firstName)

class Attendance(models.Model):
    eId = models.ForeignKey(Employee,on_delete=models.CASCADE)
    month = models.CharField(max_length=50,choices=months)
    days = models.CharField(max_length=5,choices=days)

    def __str__(self):
        return "%s %s" % (self.eId, self.month)

class Notice(models.Model):
    Id = models.CharField(primary_key=True,max_length=20)
    title = models.CharField(max_length=250)
    description = models.TextField()
    publishDate = models.DateTimeField()

    def __str__(self):
        return self.title 


class workAssignments(models.Model):
    Id = models.CharField(max_length=20)
    assignerId = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="assignerId")
    work = models.TextField()
    assignDate = models.DateTimeField()
    dueDate = models.DateTimeField()
    taskerId = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="taskerId") 

class Requests(models.Model):
    Id = models.CharField(max_length=20)
    requesterId = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="requesterId")
    requestMessage = models.TextField()
    requestDate = models.DateTimeField()
    destinationEmployeeId = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name="toEmployeeId") 