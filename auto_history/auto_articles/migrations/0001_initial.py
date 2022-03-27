# Generated by Django 4.0.3 on 2022-03-27 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('date_publication', models.DateTimeField(verbose_name='Дата публикации')),
                ('estimation', models.FloatField(max_length=4, verbose_name='Оценка')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Body',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Кузов',
                'verbose_name_plural': 'Кузова',
            },
        ),
        migrations.CreateModel(
            name='Brend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('creator', models.CharField(max_length=250, verbose_name='Создатель')),
                ('logo', models.ImageField(upload_to='', verbose_name='Логотип')),
                ('about_brand', models.TextField(verbose_name='О марке')),
                ('number_fans', models.PositiveIntegerField(verbose_name='Количество фанатов')),
            ],
            options={
                'verbose_name': 'Марка',
                'verbose_name_plural': 'Марки',
            },
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_release', models.DateField(verbose_name='Год выпуска')),
                ('rating', models.FloatField(max_length=4, verbose_name='Рейтинг')),
                ('features', models.TextField(verbose_name='Особенности')),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_articles.body')),
                ('brend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_articles.brend')),
            ],
            options={
                'verbose_name': 'Автомобиль',
                'verbose_name_plural': 'Автомобили',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Страна',
                'verbose_name_plural': 'Страны',
            },
        ),
        migrations.CreateModel(
            name='Drive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Привод',
                'verbose_name_plural': 'Привода',
            },
        ),
        migrations.CreateModel(
            name='Engine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Двигатель',
                'verbose_name_plural': 'Двигатели',
            },
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Трансмисия',
                'verbose_name_plural': 'Трансмисии',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('first_name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('number', models.PositiveIntegerField(verbose_name='Телефон')),
                ('city', models.CharField(max_length=300, verbose_name='Город')),
                ('personal_car', models.CharField(max_length=100, verbose_name='Личный автомобиль')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Сomment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текст')),
                ('date_comment', models.DateTimeField(verbose_name='Дата комментария')),
                ('articles', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auto_articles.articles')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_articles.user')),
            ],
            options={
                'verbose_name': 'Комментария',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_auto', models.ImageField(upload_to='', verbose_name='Фото')),
                ('сar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_articles.car')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=50, verbose_name='Имя')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auto_articles.user')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование')),
                ('brend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_articles.brend')),
            ],
            options={
                'verbose_name': 'Модель',
                'verbose_name_plural': 'Модели',
            },
        ),
        migrations.CreateModel(
            name='Link_selection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(verbose_name='Ссылка')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_articles.car')),
            ],
            options={
                'verbose_name': 'Ссылка на подбор',
                'verbose_name_plural': 'Ссылки на подборы',
            },
        ),
        migrations.CreateModel(
            name='Like_car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_articles.car')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_articles.user')),
            ],
            options={
                'verbose_name': 'Понравившая машина',
                'verbose_name_plural': 'Понравившие машины',
            },
        ),
        migrations.CreateModel(
            name='Favorite_brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_articles.brend')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_articles.user')),
            ],
            options={
                'verbose_name': 'Любимая марка',
                'verbose_name_plural': 'Любимые марки',
            },
        ),
        migrations.AddField(
            model_name='car',
            name='drive',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_articles.drive'),
        ),
        migrations.AddField(
            model_name='car',
            name='engine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_articles.engine'),
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_articles.model'),
        ),
        migrations.AddField(
            model_name='car',
            name='transmission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_articles.transmission'),
        ),
        migrations.AddField(
            model_name='brend',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_articles.country'),
        ),
        migrations.AddField(
            model_name='articles',
            name='car',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auto_articles.car'),
        ),
        migrations.AddField(
            model_name='articles',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auto_articles.user'),
        ),
    ]