# Generated by Django 3.2.6 on 2022-03-22 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Episodes',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=320)),
                ('content', models.TextField()),
                ('author', models.CharField(default='Chrysalis Team', max_length=200)),
                ('anchor_link', models.CharField(max_length=512)),
                ('slug', models.SlugField(default='', max_length=150)),
                ('timeStamp', models.DateTimeField(blank=True)),
                ('publish', models.BooleanField(default=False)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
    ]