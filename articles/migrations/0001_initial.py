# Generated by Django 3.2.4 on 2021-08-01 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Captcha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=150, null=True)),
                ('name_article', models.CharField(blank=True, max_length=150, null=True)),
                ('id_sous_category', models.IntegerField(blank=True, default=0, null=True)),
                ('contenu', models.TextField()),
                ('e_mail', models.EmailField(max_length=254)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=150, null=True)),
                ('titres_articles', models.CharField(max_length=100)),
                ('sous_category_id', models.IntegerField(blank=True, default=0, null=True)),
                ('contenu', models.TextField()),
                ('image_path', models.ImageField(upload_to='articles/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre_page', models.CharField(blank=True, max_length=100, null=True)),
                ('sous_titre_page', models.CharField(blank=True, max_length=100, null=True)),
                ('sous_category_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
