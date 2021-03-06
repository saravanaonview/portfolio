# Generated by Django 2.2.15 on 2020-08-16 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Description', models.CharField(max_length=200)),
                ('WhenExactly', models.DateTimeField()),
                ('image', models.ImageField(upload_to='blog/images/')),
            ],
        ),
        migrations.DeleteModel(
            name='BlogConfig',
        ),
    ]
