from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.id}: {self.name}'

    class Meta:
        verbose_name_plural = 'people'


class Category(models.Model):
    HOME_CHOICE = 'Home' # how it looks in the db table
    WORK_CHOICE = 'Work' # how it looks in the db
    NAME_CHOICES = (
        (HOME_CHOICE, 'Home stuff'), # how it looks
        (WORK_CHOICE, 'Work stuff'),
    )

    name = models.CharField(max_length=20, choices=NAME_CHOICES)

    def __str__(self):
        return f'{self.id}: {self.name}'

    class Meta:
        verbose_name_plural = 'categories'


class Todo(models.Model):
    title = models.CharField(max_length=30)
    state = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    # owner = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)
    categories = models.ManyToManyField(Category)

