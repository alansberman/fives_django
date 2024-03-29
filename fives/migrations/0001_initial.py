# Generated by Django 2.2.7 on 2019-11-22 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chosen_word', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Guess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_shared', models.IntegerField(default=0)),
                ('guess_text', models.CharField(max_length=5)),
                ('is_correct', models.BooleanField()),
            ],
        ),
    ]
