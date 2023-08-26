from django.db import models
from django.contrib import admin
from django.utils import timezone, html
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()



class Advertisement(models.Model): # это класс-модель
    # он реализует таблицу Advertisement
    title = models.CharField("заголовок", max_length=128)
    text = models.TextField("описание")
    price = models.FloatField("цена")
    auction = models.BooleanField("торг", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    image = models.ImageField("изображение", upload_to='media/')

    author = models.ForeignKey(User, on_delete=models.CASCADE)


    @admin.display(description="дата создания")
    def handle_date(self):
        if self.created_at.date() == timezone.now().date():
            create_time = self.created_at.time().strftime('%H:%M:%S')
            return html.format_html(
                '<span style ="color: green; font-weight= bold;">Сегодня в {}</span>', create_time
            )
        return self.created_at.strftime('%d.%m.%Y at %H:%M:%S')

    @admin.display(description="дата создания")
    def update_date(self):

        if self.update_at.date() == timezone.now().date():
            update_time = self.update_at.time().strftime('%H:%M:%S')
            return html.format_html(
                '<span style ="color: green; font-weight= bold;">Сегодня в {}</span>', update_time
            )
        return self.created_at.strftime('%d.%m.%Y at %H:%M:%S')

    @admin.display(description="фото")
    def photo(self):
        if self.image:
            return html.format_html(
                "<img src = '{}' width = '100px' heigth = '100px' > ",
                self.image.url
            )
        return html.format_html(
            "<img src = 'http://127.0.0.1:8000/media/image.jpg' width = '100px' heigth = '100px' > ",
        )
       
    def __str__(self):
        return f"title: {self.title}, text: {self.text}"
        