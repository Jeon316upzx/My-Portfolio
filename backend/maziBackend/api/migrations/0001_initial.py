# Generated by Django 2.0.2 on 2019-04-20 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.CharField(max_length=10000)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
