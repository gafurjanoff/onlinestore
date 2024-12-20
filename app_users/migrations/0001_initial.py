# Generated by Django 5.1.3 on 2024-11-21 10:36

import app_users.managers
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(max_length=100, verbose_name='First name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last name')),
                ('username', models.CharField(blank=True, max_length=100, null=True, verbose_name='Username')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('bio', models.TextField(blank=True, null=True, verbose_name='About')),
                ('profile_image', models.ImageField(blank=True, default='profile-images/user-default.png', null=True, upload_to='profile-images/', verbose_name='Profile image')),
                ('location', models.CharField(blank=True, max_length=100, null=True, verbose_name='Location')),
                ('occupation', models.CharField(blank=True, max_length=200, null=True, verbose_name='Occupation')),
                ('social_telegram', models.URLField(blank=True, null=True, verbose_name='Telegram')),
                ('social_instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('social_facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('social_twitter', models.URLField(blank=True, null=True, verbose_name='Twitter')),
                ('social_whatsapp', models.URLField(blank=True, null=True, verbose_name='Whatsapp')),
                ('social_linkedin', models.URLField(blank=True, null=True, verbose_name='LinkedIn')),
                ('social_youtube', models.URLField(blank=True, null=True, verbose_name='YouTube')),
                ('social_github', models.URLField(blank=True, null=True, verbose_name='GitHub')),
                ('social_website', models.URLField(blank=True, null=True, verbose_name='Website')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', app_users.managers.MyUserManager()),
            ],
        ),
    ]
