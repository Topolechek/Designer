from django.db import models

class FeedBack(models.Model):
    name = models.CharField('Имя', max_length=50, blank=True, null=True)
    phone = models.CharField('Телефон', max_length=80)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Форма обратной связи"
        verbose_name_plural = "Формы обратной связи"
