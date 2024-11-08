from django.contrib.auth.models import AbstractUser
from django.db import models


class HealthMeasurements(models.Model):
    last_update = models.DateTimeField(auto_now=True, verbose_name="Дата и время последнего замера",
                                       help_text="Дата и время последнего замера умными носимыми устройствами")

    systolic_pressure = models.DecimalField(max_digits=7, decimal_places=4,
                                            verbose_name="Систолическое давление")
    diastolic_pressure = models.DecimalField(max_digits=7, decimal_places=4,
                                             verbose_name="Диастолическое давление")
    pulse = models.DecimalField(max_digits=7, decimal_places=4,
                                verbose_name="Пульс")
    temperature = models.DecimalField(max_digits=6, decimal_places=4,
                                      verbose_name="Температура")
    steps = models.IntegerField(verbose_name="Количество шагов")
    stress_level = models.DecimalField(max_digits=7, decimal_places=4,
                                       verbose_name="Уровень стресса")
    oxygen_level = models.DecimalField(max_digits=7, decimal_places=4,
                                       verbose_name="Уровень кислорода в крови")
    latitude = models.DecimalField(max_digits=9, decimal_places=6,
                                   verbose_name="Широта")
    longitude = models.DecimalField(max_digits=9, decimal_places=6,
                                    verbose_name="Долгота")

    def __str__(self):
        return f"Health Measurements: {self.id}"

    class Meta:
        verbose_name = "Последний замер показателей здоровья"
        verbose_name_plural = "Последние замеры показателей здоровья"


class EmployeeHealthReference(models.Model):
    last_update = models.DateField(auto_now=True, verbose_name="Дата контрольного замера",
                                   help_text="Дата диспансеризации и проведения контрольных замеров")

    blood_group = models.PositiveSmallIntegerField(verbose_name="Группа крови")
    rhesus_factor = models.BooleanField(verbose_name="Резус-фактор")
    normal_systolic_pressure = models.DecimalField(max_digits=7, decimal_places=4,
                                                   verbose_name="Эталонное систолическое давление")
    normal_diastolic_pressure = models.DecimalField(max_digits=7, decimal_places=4,
                                                    verbose_name="Эталонное диастолическое давление")
    normal_pulse = models.DecimalField(max_digits=7, decimal_places=4, verbose_name="Эталонный пульс")
    normal_temperature = models.DecimalField(max_digits=6, decimal_places=4, verbose_name="Эталонная температура")
    normal_steps = models.IntegerField(verbose_name="Эталонное количество шагов")
    normal_stress_level = models.DecimalField(max_digits=7, decimal_places=4, verbose_name="Эталонный уровень стресса")
    normal_oxygen_level = models.DecimalField(max_digits=7, decimal_places=4,
                                              verbose_name="Эталонный уровень кислорода в крови")

    def __str__(self):
        return f"Health Benchmark: {self.id}"

    class Meta:
        verbose_name = "Эталонное значение показателей здоровья"
        verbose_name_plural = "Эталонные значения показателей здоровья"


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
    health_measurement = models.ForeignKey(
        HealthMeasurements, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Показатели здоровья"
    )
    health_reference = models.ForeignKey(
        EmployeeHealthReference, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Нормативы здоровья"
    )

    def __str__(self):
        return f"{self.last_name} {self.first_name} ({self.position})"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"
