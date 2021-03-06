# Generated by Django 3.1.5 on 2021-01-24 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=170, verbose_name='Автор')),
                ('slug', models.CharField(default='', max_length=64)),
            ],
            options={
                'db_table': 'th_author',
            },
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=170)),
                ('content', models.TextField()),
                ('slug', models.CharField(default='', max_length=64)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='threads_common.author')),
            ],
            options={
                'db_table': 'th_thread',
            },
        ),
    ]
