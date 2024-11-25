# Generated by Django 5.1.3 on 2024-11-25 08:51

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('judul', models.CharField(max_length=200)),
                ('tanggal', models.DateField(auto_now_add=True)),
                ('isi', models.TextField()),
                ('gambar_url', models.URLField(max_length=1000)),
            ],
        ),
    ]
