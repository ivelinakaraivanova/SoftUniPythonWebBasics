# Generated by Django 3.2.4 on 2021-06-15 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_auto_20210615_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('Home', 'Home stuff'), ('Work', 'Work stuff')], max_length=20),
        ),
    ]
