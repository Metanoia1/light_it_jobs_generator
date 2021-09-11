from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Company(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Manager(models.Model):
    name = models.CharField(max_length=50, unique=True)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="managers"
    )

    def __str__(self):
        return self.name


class Worker(models.Model):
    STATUS_EMPLOYED = "Employed"
    STATUS_UNEMPLOYED = "Unemployed"
    STATUS = ((STATUS_EMPLOYED, "Employed"), (STATUS_UNEMPLOYED, "Unemployed"))

    name = models.CharField(max_length=50, unique=True)
    status = models.CharField(
        choices=STATUS, default=STATUS_UNEMPLOYED, max_length=50
    )
    skills = models.ManyToManyField(
        "Skill",
        through="WorkerSkill",
        related_name="workers",
    )

    def __str__(self):
        return self.name


class Position(models.Model):
    RELATED_NAME = "positions"
    STATUS_ACTIVE = "Active"
    STATUS_BUSY = "Busy"
    STATUS = ((STATUS_ACTIVE, "Active"), (STATUS_BUSY, "Busy"))

    name = models.CharField(max_length=50)
    workers_num = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(100)]
    )
    status = models.CharField(
        choices=STATUS, default=STATUS_ACTIVE, max_length=50
    )
    manager = models.ForeignKey(
        Manager, on_delete=models.CASCADE, related_name=RELATED_NAME
    )
    skills = models.ManyToManyField(
        "Skill",
        through="PositionSkill",
        related_name=RELATED_NAME,
    )

    def __str__(self):
        return self.name


class Offer(models.Model):
    RELATED_NAME = "offers"
    STATUS_ACCEPTED = "Accepted"
    STATUS_DECLINED = "Declined"
    STATUS_PENDING = "Pending"
    STATUS = (
        (STATUS_ACCEPTED, "Accepted"),
        (STATUS_DECLINED, "Declined"),
        (STATUS_PENDING, "Pending"),
    )

    name = models.CharField(max_length=50)
    status = models.CharField(
        choices=STATUS, default=STATUS_PENDING, max_length=50
    )
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, related_name=RELATED_NAME
    )
    manager = models.ForeignKey(
        Manager, on_delete=models.CASCADE, related_name=RELATED_NAME
    )
    worker = models.ForeignKey(
        Worker, on_delete=models.CASCADE, related_name=RELATED_NAME
    )

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=50, unique=True)
    rate = models.DecimalField(max_digits=5, decimal_places=2)
    level_rate = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class LevelAbstractModel(models.Model):
    level = models.PositiveSmallIntegerField(
        default=1, validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        abstract = True


class WorkerSkill(LevelAbstractModel):
    RELATED_NAME = "workerskills"
    worker = models.ForeignKey(
        Worker, on_delete=models.CASCADE, related_name=RELATED_NAME
    )
    skill = models.ForeignKey(
        Skill, on_delete=models.CASCADE, related_name=RELATED_NAME
    )


class PositionSkill(LevelAbstractModel):
    RELATED_NAME = "positionskills"
    position = models.ForeignKey(
        Position, on_delete=models.CASCADE, related_name=RELATED_NAME
    )
    skill = models.ForeignKey(
        Skill, on_delete=models.CASCADE, related_name=RELATED_NAME
    )
