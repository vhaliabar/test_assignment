from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

class Course(models.Model) :
    title = models.CharField('Назва',
            max_length=200,
            validators=[MinLengthValidator(4, "Title must be greater than 4 characters")],
            help_text="введіть назву курсу"
    )
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    lectures = models.CharField('Кількість лекцій',
            max_length=200,
            validators=[MinLengthValidator(1, "Title must be greater than 1 characters")],
            help_text="введіть кількість лекцій", null = True
    )

    start = models.CharField('дата початку',
            max_length=25,
            help_text="введіть дату старту курсу", null = True
    )

    finish = models.CharField('дата закінчення',
            max_length=25,
            help_text="введіть дату закінчення курсу", null = True
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title