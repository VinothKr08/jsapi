# Generated by Django 2.2.2 on 2019-06-20 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopicsList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_no', models.IntegerField()),
                ('title', models.CharField(max_length=120)),
            ],
        ),
    ]
