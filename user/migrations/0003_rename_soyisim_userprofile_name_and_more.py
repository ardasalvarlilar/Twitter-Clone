# Generated by Django 4.2.4 on 2023-12-14 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_userprofile_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='soyisim',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='sifre',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='profil_resmi',
            new_name='profile_pic',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='isim',
            new_name='surname',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='kullanici_adi',
            new_name='username',
        ),
    ]