# Generated by Django 3.1.2 on 2020-10-08 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('question', models.TextField(max_length=400)),
                ('priority', models.CharField(choices=[{'H', 'High'}, {'Medium', 'M'}, {'Low', 'L'}], max_length=6)),
            ],
        ),
    ]
