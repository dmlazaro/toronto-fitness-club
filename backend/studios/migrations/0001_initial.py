# Generated by Django 4.1.3 on 2022-12-05 03:26

from django.db import migrations, models
import django.db.models.deletion
import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('lat', models.DecimalField(blank=True, decimal_places=6, max_digits=9, verbose_name='Latitude')),
                ('long', models.DecimalField(blank=True, decimal_places=6, max_digits=9, verbose_name='Longitude')),
                ('postal_code', models.CharField(max_length=7, validators=[utils.validators.validate_postal_code])),
                ('phone_num', models.CharField(max_length=16, validators=[utils.validators.validate_phone_number], verbose_name='Phone number')),
            ],
        ),
        migrations.CreateModel(
            name='StudioImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='studios/')),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='studios.studio')),
            ],
        ),
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('studio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenities', to='studios.studio')),
            ],
            options={
                'verbose_name_plural': 'amenities',
            },
        ),
    ]