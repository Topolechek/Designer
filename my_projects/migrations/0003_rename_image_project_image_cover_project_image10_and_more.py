# Generated by Django 4.0.3 on 2022-05-24 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_projects', '0002_alter_project_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='image',
            new_name='image_cover',
        ),
        migrations.AddField(
            model_name='project',
            name='image10',
            field=models.ImageField(blank=True, upload_to='my_projects/images/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image2',
            field=models.ImageField(blank=True, upload_to='my_projects/images/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image3',
            field=models.ImageField(blank=True, upload_to='my_projects/images/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image4',
            field=models.ImageField(blank=True, upload_to='my_projects/images/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image5',
            field=models.ImageField(blank=True, upload_to='my_projects/images/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image6',
            field=models.ImageField(blank=True, upload_to='my_projects/images/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image7',
            field=models.ImageField(blank=True, upload_to='my_projects/images/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image8',
            field=models.ImageField(blank=True, upload_to='my_projects/images/'),
        ),
        migrations.AddField(
            model_name='project',
            name='image9',
            field=models.ImageField(blank=True, upload_to='my_projects/images/'),
        ),
        migrations.AddField(
            model_name='project',
            name='left_or_right',
            field=models.BooleanField(default=False),
        ),
    ]