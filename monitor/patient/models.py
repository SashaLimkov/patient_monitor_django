from backend.models import TimeBasedModel
from django.db import models


class Patient(TimeBasedModel):
    class Meta:
        verbose_name = "Пациент"
        verbose_name_plural = "Пациены"
        
    class Sex(models.TextChoices):
        MEN = "Муж", "Мужской"
        WOMEN = "Жен", "Женский"
    
    lotus_id = models.CharField("Lotus ID", max_length=250)
    FIO = models.CharField("ФИО", max_length=255)
    bithday = models.DateField("Дата рождения")
    sex = models.CharField("Пол", max_length=3, choices=Sex.choices, default=Sex.MEN)

class MedicalHistory(TimeBasedModel):
    class Meta:
        verbose_name = "История Болезни"
        verbose_name_plural = "Истории Болезни"
        
    lotus_id = models.CharField("Lotus ID", max_length=250)
    is_active = models.BooleanField(verbose_name="Последняя ИБ", default=False)
    number = models.CharField("Номер", max_length=250)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True)
    income_datetime = models.DateTimeField("Дата поступления")
    curent_department_name = models.CharField("Текущее отделенние", max_length=250)
    outcome_date = models.DateField("Дата выписки")   
    
class Diagnosis(TimeBasedModel):
    class Meta:
        verbose_name = "Диагноз"
        verbose_name_plural = "Диагнозы"
        
    d_type = models.ForeignKey("DiagnosisType", on_delete=models.SET_NULL, null=True, blank=True)
    main_issue = models.CharField("Основное заболевание", max_length=5000)
    mkb = models.CharField("МКБ", max_length=32)
    ksg = models.CharField("КСГ", max_length=32)
    standart = models.CharField("Стандарт", max_length=5000)    
    
    def __str__(self):
        return self.main_issue

class DiagnosisType(TimeBasedModel):
    class Meta:
        verbose_name = "Тип диагноза"
        verbose_name_plural = "Типы диагнозов"
        ordering = ["name"]

    name = models.CharField("Название", max_length=250)
    
    def __str__(self):
        return self.name