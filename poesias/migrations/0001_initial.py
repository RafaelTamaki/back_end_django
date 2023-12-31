# Generated by Django 4.2.5 on 2023-09-26 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('data_publicacao', models.CharField(max_length=8)),
                ('imagem', models.ImageField(upload_to='book_covers/')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poesias.autor')),
                ('categorias', models.ManyToManyField(to='poesias.categoria')),
            ],
        ),
    ]
