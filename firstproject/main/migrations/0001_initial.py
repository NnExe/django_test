# Generated by Django 4.0.4 on 2022-04-16 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recepts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('ingridients', models.CharField(max_length=250, verbose_name='Ингридиенты')),
                ('recept_text', models.TextField(verbose_name='Рецепт')),
            ],
        ),
    ]