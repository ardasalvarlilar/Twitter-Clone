# Generated by Django 4.2.4 on 2023-12-15 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_alter_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='yorum',
            old_name='yazar',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='yorum',
            old_name='tarih',
            new_name='commented_at',
        ),
        migrations.RenameField(
            model_name='yorum',
            old_name='icerik',
            new_name='content',
        ),
        migrations.AddField(
            model_name='yorum',
            name='image',
            field=models.FileField(blank=True, upload_to='comment_images'),
        ),
    ]
