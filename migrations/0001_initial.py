# Generated by Django 5.0.4 on 2024-05-07 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vendas',
            fields=[
                ('id_vendas', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField()),
                ('produto', models.TextField(max_length=50)),
                ('cliente', models.TextField(max_length=50)),
            ],
        ),
    ]