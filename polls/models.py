from secrets import choice
from django.db import models

# Create your models here.

class Question(models.Model):
   # id = models.PrimaryKey(auto_increment=True) #not necessary to write this line as django automatically increases the numbering, you can also write it while leaving the brackets empty
    Question_text = models.CharField(max_length=255)
    Question_description = models.CharField(max_length=255, default="Basic Description") #so former Questions will have Basic Description in this new field
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):  #this is Python related and not database related, it replaces default object title with actual title 
        return self.Question_text

    #so the below is what you are hoping to achieve with the above 
    #  1)        "Are you happy about Django?"       "June 16, 09:50 WAT"
    #  2)        "ARE YOU ..."                       "JUNE 17, 10:00 WAT"


class Choices(models.Model):
    Question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_answer = models.CharField(max_length=20)
    votes = models.IntegerField(default=0) #default makes it 0/0 for a start before 1/0 - meaning first yes

    def __str__(self):
        return self.choice_answer

    #  id        Question                         choice_answer      votes
    #  1)    "Are you happy about Django"         yes/no             1/0
