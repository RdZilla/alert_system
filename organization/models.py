from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    MALE = "MALE"
    FEMALE = "FEMALE"
    GENDER_CHOICES = (
        (MALE, "Мужской"),
        (FEMALE, "Женский")
    )

    last_name = models.CharField(max_length=150, verbose_name="Фамилия")
    first_name = models.CharField(max_length=150, verbose_name="Имя")
    middle_name = models.CharField(max_length=150, verbose_name="Отчество")
    birth_date = models.DateField(verbose_name="Дата рождения", blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, verbose_name="Пол")
    phone_number = models.CharField(max_length=20, verbose_name="Номер телефона")
    position = models.CharField(max_length=150, verbose_name="Должность")

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.position})"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
