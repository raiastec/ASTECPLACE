# Generated by Django 5.1.3 on 2025-05-23 19:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0003_rename_anuncio_anuncios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anuncios',
            name='imagens',
        ),
        migrations.CreateModel(
            name='ImagemAnuncios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='imagens/anuncios/')),
                ('anuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anuncios.anuncios')),
            ],
        ),
    ]
