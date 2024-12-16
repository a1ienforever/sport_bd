from autoslug import AutoSlugField
from django.db import models

from django.db import models


class Sport(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Название вида спорта")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    slug = AutoSlugField(unique=True, editable=False, manager_name="objects", populate_from="name")


    class Meta:
        verbose_name = "Вид спорта"
        verbose_name_plural = "Виды спорта"
        ordering = ['name']  # Сортировка по имени по умолчанию

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название команды")
    city = models.CharField(max_length=255, verbose_name="Город")
    created_at = models.DateField(verbose_name="Дата основания", auto_now_add=True)
    slug = AutoSlugField(unique=True, editable=False)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='team', verbose_name='Вид спорта')

    def __str__(self):
        return self.name


class Athlete(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    date_of_birth = models.DateField(verbose_name="Дата рождения")
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Команда")
    slug = AutoSlugField(unique=True, editable=False, populate_from='first_name')
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='athlete', verbose_name='Вид Спорта')


    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Achievement(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название достижения")
    date = models.DateField(verbose_name="Дата получения")
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, related_name="achievements", verbose_name="Спортсмен")
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='achievements', verbose_name='Вид Спорта')


    def __str__(self):
        return f"{self.title} - {self.athlete}"


class Coach(models.Model):
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    team = models.OneToOneField(Team, on_delete=models.CASCADE, verbose_name="Команда")
    slug = AutoSlugField(unique=True, editable=False)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='coach', verbose_name='Вид Спорта')



    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.team.name}"


class Competition(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название соревнования")
    location = models.CharField(max_length=255, verbose_name="Место проведения")
    date = models.DateField(verbose_name="Дата проведения")
    slug = AutoSlugField(unique=True, editable=False)
    teams = models.ManyToManyField(Team, related_name='competitions')
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='competitions', verbose_name='Вид Спорта')



    def __str__(self):
        return self.name


class Result(models.Model):
    athlete = models.ForeignKey(Athlete, on_delete=models.CASCADE, verbose_name="Спортсмен")
    competition = models.ForeignKey(Competition, on_delete=models.CASCADE, verbose_name="Соревнование")
    score = models.FloatField(verbose_name="Результат")
    position = models.PositiveIntegerField(verbose_name="Место")
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, related_name='results', verbose_name='Вид Спорта')

    class Meta:
        unique_together = ('athlete', 'competition')

    def __str__(self):
        return f"{self.athlete} - {self.competition} - {self.position} место"


