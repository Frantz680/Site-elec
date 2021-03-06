# Generated by Django 3.2.4 on 2021-08-08 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actualites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_actu', models.CharField(blank=True, max_length=150, null=True)),
                ('user', models.CharField(blank=True, max_length=150, null=True)),
                ('contenu', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ArticleNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_sous_category', models.IntegerField(blank=True, null=True)),
                ('note_contenu', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50, null=True, unique=True)),
                ('icon', models.ImageField(upload_to='icon_categorie/')),
            ],
        ),
        migrations.CreateModel(
            name='PictureCarrousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='carrousel/')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sous_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=30, unique=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
