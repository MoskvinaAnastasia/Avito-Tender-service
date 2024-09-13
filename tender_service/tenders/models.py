from django.contrib.auth.models import User
from django.db import models


class Organization(models.Model):
    """Модель, представляющая организацию."""

    ORGANIZATION_TYPES = (
        ('IE', 'Индивидуальный предприниматель'),
        ('LLC', 'Общество с ограниченной ответственностью'),
        ('JSC', 'Акционерное общество'),
    )
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=3,
                            choices=ORGANIZATION_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'
        ordering = ['name']


class Tender(models.Model):
    """Модель, представляющая тендер."""

    STATUS_CHOICES = (
        ('CREATED', 'Created'),
        ('PUBLISHED', 'Published'),
        ('CLOSED', 'Closed'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='CREATED')
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Тендер'
        verbose_name_plural = 'Тендеры'
        ordering = ['-created_at']


class Bid(models.Model):
    """Модель, представляющая предложение."""

    STATUS_CHOICES = (
        ('CREATED', 'Created'),
        ('PUBLISHED', 'Published'),
        ('CANCELED', 'Canceled'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='CREATED')
    tender = models.ForeignKey(Tender, related_name='bids',
                               on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Предложение'
        verbose_name_plural = 'Предложения'
        ordering = ['-created_at']


class Review(models.Model):
    """Модель для хранения отзывов на предложения."""

    bid = models.ForeignKey(Bid,
                            related_name='reviews',
                            on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']
