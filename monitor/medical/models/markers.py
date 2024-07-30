from backend.models import TimeBasedModel
from django.db import models


class PatientSystem(TimeBasedModel):
    class Meta:
        verbose_name = 'Система'
        verbose_name_plural = 'Системы'
        ordering = ['-name']
    
    name = models.CharField(max_length=255, verbose_name='Название')
    states = models.ManyToManyField("UserState", related_name="systems")
    
    def __str__(self):
        return self.name

class UserState(TimeBasedModel):
    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояния'
        ordering = ['-name']
    
    name = models.CharField(max_length=255, verbose_name='Название состояния')
    marksers = models.ManyToManyField("Marker", related_name="states")

    def __str__(self):
        return self.name


class Marker(TimeBasedModel):
    class Meta:
        verbose_name = 'Маркер'
        verbose_name_plural = 'Маркеры'
        ordering = ['-name']
    
    name = models.CharField(max_length=255, verbose_name='Название')
    
    def __str__(self):
        return self.name

class MarkerCondition(TimeBasedModel):
    class Meta:
        verbose_name = 'Маркер с условием'
        verbose_name_plural = 'Маркеры с условием'
        ordering = ['-name']
    
    name = models.ForeignKey(Marker, on_delete=models.SET_NULL, null=True, blank=True)
    measurement = models.ForeignKey("Measurement", on_delete=models.SET_NULL, null=True, blank=True)
    deviations = models.ForeignKey("Deviations", on_delete=models.SET_NULL, null=True, blank=True)
    

class Measurement(TimeBasedModel):
    class Meta:
        verbose_name = 'ЕДиница измерения'
        verbose_name_plural = 'Единицы измерений'
        ordering = ['-name']
    
    name = models.CharField(max_length=255, verbose_name='Название')
    
    def __str__(self):
        return self.name

class Condition(TimeBasedModel):
    class Meta:
        verbose_name = 'Условие'
        verbose_name_plural = 'Условия'
    
    class ConditionType(models.TextChoices):
        gt = ">", "Больше"
        lt = "<", "Меньше"
        gte = ">=", "Больше или равно"
        lte = "<=", "Меньше или равно"
        eq = "==", "Равно"
    
    class Sex(models.TextChoices):
        MEN = "Муж", "Мужской"
        WOMEN = "Жен", "Женский"
        BOTH = "Общ", "Общий"
    
    class IndicatorsType(models.TextChoices):
        NORMAL = "Норма", "Норма"
        MODERATE = "Умеренные отклонения", "Умеренные"
        MARKED = "Выраженные отклонения", "Выраженные"
        CRITICAL = "Критические отклонения", "Критические"
    
    indicator = models.FloatField("Показатель", null=True, blank=True)
    condition_type = models.CharField(max_length=2, choices=ConditionType.choices, verbose_name='Тип условия', null=True, blank=True)
    sex = models.CharField(max_length=3, choices=Sex.choices, verbose_name='Пол', null=True, blank=True)
    indicators_type = models.CharField(max_length=32, choices=IndicatorsType.choices, verbose_name='Тип индикаторов', null=True, blank=True)
    is_age = models.BooleanField(verbose_name="Условие возраста", default=False, null=True, blank=True)
    
    def __str__(self):
        return f"{self.indicators_type}. {self.condition_type} {self.indicator} Пол = {self.sex} возрастное условие = {self.is_age}"


class Deviations(TimeBasedModel):
    class Meta:
        verbose_name = 'Показатель'
        verbose_name_plural = 'Показатели'
    normal = models.ManyToManyField(Condition, related_name="normal_dev")
    moderate = models.ManyToManyField(Condition, related_name="moderate_dev")
    marked = models.ManyToManyField(Condition, related_name="marked_dev")
    critical = models.ManyToManyField(Condition, related_name="critical_dev")
    