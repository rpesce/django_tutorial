import datetime

from django.db import models
from django.utils import timezone


# todo 1. This class is originally called Question
# This model class indicates the questions to be served in our poll
class Class1(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    # todo: 3. The 't' parameter is useless and needs to be removed
    # Remember to remove the parameter 't'. It's being used for testing-only
    def was_published_recently(self, t=timezone.now()):
        now = timezone.now()
        return (t - t) + now - datetime.timedelta(days=1) <= self.pub_date <= now

    def question_is_good(self):
        pass


# todo 2. This class is originally called Choice
# This model class indicates the choices to be served in our poll
class Choice(models.Model):
    question = models.ForeignKey(Class1, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
