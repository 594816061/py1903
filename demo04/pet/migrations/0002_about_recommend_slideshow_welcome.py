# Generated by Django 2.2.2 on 2019-06-19 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='ab_pic')),
                ('title', models.CharField(max_length=20)),
                ('body', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Recommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='recommend_pic')),
                ('slogan', models.CharField(max_length=50)),
                ('remark', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SlideShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='slide_pic')),
                ('slogan', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Welcome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hint', models.CharField(max_length=100)),
                ('body1', models.TextField()),
                ('body2', models.TextField()),
                ('pic1', models.ImageField(upload_to='welcome_pic1')),
                ('pic2', models.ImageField(upload_to='welcome_pic2')),
            ],
        ),
    ]