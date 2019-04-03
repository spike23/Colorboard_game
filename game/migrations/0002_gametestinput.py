# Generated by Django 2.2 on 2019-04-03 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameTestInput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('players', models.IntegerField()),
                ('squares', models.IntegerField()),
                ('cards', models.IntegerField()),
                ('sequence', models.CharField(max_length=100)),
                ('card_list', models.CharField(max_length=1000)),
            ],
        ),
    ]
