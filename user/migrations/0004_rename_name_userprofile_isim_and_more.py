# Generated by Django 4.2.4 on 2023-12-14 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_soyisim_userprofile_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='name',
            new_name='isim',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='username',
            new_name='kullanici_adi',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='profile_pic',
            new_name='profil_resmi',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='password',
            new_name='sifre',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='surname',
            new_name='soyisim',
        ),
    ]