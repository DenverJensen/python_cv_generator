# Generated by Django 4.1.3 on 2022-11-23 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('summary', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
                ('school', models.CharField(max_length=200)),
                ('university', models.CharField(max_length=200)),
                ('previous_work', models.CharField(max_length=1000)),
                ('skills', models.CharField(max_length=1000)),
            ],
        ),
    ]
