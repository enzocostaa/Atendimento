# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('Horario', models.CharField(max_length=200)),
                ('Descricao', models.TextField()),
                ('Data_de_criacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('Data_de_postagem', models.DateTimeField(blank=True, null=True)),
                ('Nome', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
