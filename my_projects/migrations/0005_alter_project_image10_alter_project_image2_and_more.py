# Generated by Django 4.0.3 on 2022-05-25 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_projects', '0004_rename_left_or_right_project_on_if_left'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image10',
            field=models.ImageField(blank=True, upload_to='my_projects/images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image2',
            field=models.ImageField(blank=True, upload_to='my_projects/images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image3',
            field=models.ImageField(blank=True, upload_to='my_projects/images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image4',
            field=models.ImageField(blank=True, upload_to='my_projects/images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image5',
            field=models.ImageField(blank=True, upload_to='my_projects/images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image6',
            field=models.ImageField(blank=True, upload_to='my_projects/images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image7',
            field=models.ImageField(blank=True, upload_to='my_projects/images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image8',
            field=models.ImageField(blank=True, upload_to='my_projects/images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image9',
            field=models.ImageField(blank=True, upload_to='my_projects/images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='image_cover',
            field=models.ImageField(upload_to='my_projects/images/%Y/%m/%d/'),
        ),
    ]
