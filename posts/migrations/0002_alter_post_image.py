# Generated by Django 3.2.23 on 2023-12-12 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='https://res.cloudinary.com/dpk2gl3yf/image/upload/v1702330716/media/images/default_profile_kdcc4u.jpg', upload_to='images/'),
        ),
    ]
