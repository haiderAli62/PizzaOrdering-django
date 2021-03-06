# Generated by Django 2.0.3 on 2018-09-13 17:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=64)),
                ('size', models.DecimalField(decimal_places=2, max_digits=5)),
                ('extras', models.CharField(blank=True, max_length=64, null=True)),
                ('user', models.ManyToManyField(related_name='customer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
