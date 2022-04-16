from django.db import models

class Recepts(models.Model):
    title = models.CharField('Название', max_length=50)
    ingridients = models.CharField('Ингридиенты', max_length=250)
    recept_text = models.TextField('Рецепт')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
