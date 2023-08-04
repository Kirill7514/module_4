from django.db import models
from django.db import migrations


# Create your models here.
class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    text = models.TextField("текст")
    price = models.FloatField("цена")
    user = models.CharField("пользователь", max_length=128)
    date = models.DateField("дата", auto_now_add=True)
    class Meta:
        db_table = 'advertisements'
    def __str__(self):
        return f'<Advertisement: Advertisement(id={self.id}, title={self.title}, price={self.price})>'

