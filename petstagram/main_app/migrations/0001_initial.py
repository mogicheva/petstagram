# Generated by Django 4.0.2 on 2022-02-25 11:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import petstagram.main_app.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Some', max_length=30)),
                ('type', models.CharField(choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Bunny', 'Bunny'), ('Parrot', 'Parrot'), ('Fish', 'Fish'), ('Other', 'Other')], max_length=6)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), petstagram.main_app.validators.validator_only_letters])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), petstagram.main_app.validators.validator_only_letters])),
                ('picture', models.URLField()),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Do not show', 'Do not show')], max_length=11, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PetPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', validators=[petstagram.main_app.validators.validate_photo_size])),
                ('description', models.TextField(blank=True, null=True)),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
                ('tagged_pets', models.ManyToManyField(to='main_app.Pet')),
            ],
        ),
        migrations.AddField(
            model_name='pet',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile'),
        ),
        migrations.AlterUniqueTogether(
            name='pet',
            unique_together={('name', 'user_profile')},
        ),
    ]