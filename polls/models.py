from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=128)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    choice_text = models.CharField(max_length=32)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

class User(models.Model):
    email = models.EmailField(max_length=32,unique=True,default='example@example.com')
    password = models.CharField(max_length=32)

    def __str__(self):
        return self.username