# Generated by Django 2.0.6 on 2018-09-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlesSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Articles', max_length=15)),
                ('header', models.CharField(default='Articles', max_length=30)),
                ('title', models.CharField(default='Articles', max_length=35)),
                ('sub_title', models.TextField(default='Maecenas tincidunt lacus at velit.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AuthTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='AuthTest', max_length=15)),
                ('title', models.CharField(default='AuthTest view', max_length=35)),
                ('text', models.CharField(default='Integer pede justo, lacinia eget, tincidunt eget, tempus vel, pede. pellentesque viverra pede ac diam. morbi vel lectus in quam fringilla rhoncus. nullam porttitor lacus at turpis.', max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='ContactSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Contact', max_length=15)),
                ('header', models.CharField(default='Contact', max_length=30)),
                ('title', models.CharField(default='Où nous trouver', max_length=35)),
                ('sub_title', models.TextField(default="N'hésitez pas à nous contacter...", max_length=200)),
                ('sub_title2', models.TextField(default='... en nous laissant un message...', max_length=200)),
                ('sub_title3', models.TextField(default='... ou en passant directement nous voir:', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EventsSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Events', max_length=15)),
                ('header', models.CharField(default='Galerie', max_length=30)),
                ('title', models.CharField(default='Derniers événements', max_length=35)),
                ('sub_title', models.TextField(default='Praesent blandit lacinia erat.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HeroSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Hero', max_length=15)),
                ('icon1', models.CharField(default='fab fa-cloudversify', max_length=20)),
                ('icon2', models.CharField(default='far fa-paint-brush', max_length=20)),
                ('icon3', models.CharField(default='far fa-compass', max_length=20)),
                ('title1', models.CharField(default='Molestie nam', max_length=20)),
                ('title2', models.CharField(default='Suspendisse suspendisse', max_length=20)),
                ('title3', models.CharField(default='Sapien mattis', max_length=20)),
                ('text1', models.CharField(default='Vestibulum rutrum rutrum neque. duis mattis egestas metus.', max_length=200)),
                ('text2', models.CharField(default='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. maecenas ut massa quis augue luctus tincidunt.', max_length=200)),
                ('text3', models.CharField(default='Quisque ut erat. fusce consequat.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('message', models.TextField(max_length=3000)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_new', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='PresentationSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Presentation', max_length=15)),
                ('title', models.CharField(default='Hello world!', max_length=35)),
                ('sub_title', models.TextField(default='Nunc purus. proin eu mi.', max_length=200)),
                ('text1', models.TextField(default='Integer tincidunt ante vel ipsum. sed accumsan felis. sed sagittis. mauris lacinia sapien quis libero. quisque erat eros, viverra eget, congue eget, semper rutrum, nulla. curabitur gravida nisi at nibh. nam ultrices, libero non mattis pulvinar, nulla pede ullamcorper augue, a suscipit nulla elit ac nulla. suspendisse ornare consequat lectus.', max_length=800)),
                ('text2', models.TextField(default='Duis aliquam convallis nunc. aliquam augue quam, sollicitudin vitae, consectetuer eget, rutrum at, lorem. integer aliquet, massa id lobortis convallis, tortor risus dapibus augue, vel accumsan tellus nisi eu orci. vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; duis faucibus accumsan odio. proin leo odio, porttitor id, consequat in, consequat ut, nulla. vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl. in eleifend quam a odio. morbi vel lectus in quam fringilla rhoncus. morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl.', max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='PromoSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Promo', max_length=15)),
                ('title', models.CharField(default='Praesent blandit lacinia erat.', max_length=35)),
                ('text', models.CharField(default='Phasellus sit amet erat. praesent lectus. in blandit ultrices enim. integer non velit.', max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='ReviewSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Review', max_length=15)),
                ('title', models.CharField(default='Google Review', max_length=35)),
                ('sub_title', models.CharField(default='Ce que disent les gens de nous', max_length=200)),
                ('g_api', models.CharField(blank=True, default='AIzaSyAKrXyewXcDPgvG66yHBmm3vFZDoJDDS1M', max_length=1000, null=True)),
                ('g_place_id', models.CharField(blank=True, default='ChIJPwMEJQwCjkcRkmHo22dFFpo', max_length=1000, null=True)),
                ('g_review_all_url', models.CharField(blank=True, default='https://goo.gl/9XWfVB', max_length=1000, null=True)),
                ('g_review_new_url', models.CharField(blank=True, default='https://goo.gl/owSQ5r', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.CharField(blank=True, default='#', max_length=1000, null=True)),
                ('tripadvisor', models.CharField(blank=True, default='#', max_length=1000, null=True)),
                ('google', models.CharField(blank=True, default='https://www.google.ch/maps/place/MySite.', max_length=1000, null=True)),
                ('twitter', models.CharField(blank=True, default='#', max_length=1000, null=True)),
                ('instagram', models.CharField(blank=True, default='#', max_length=1000, null=True)),
                ('linkedin', models.CharField(blank=True, default='#', max_length=1000, null=True)),
                ('snapchat', models.CharField(blank=True, default='#', max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteInformations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='MySite.', max_length=25)),
                ('name_add', models.CharField(default='Forall', max_length=15)),
                ('oppening', models.CharField(default='2016', max_length=4)),
                ('adress', models.CharField(default='awesome street', max_length=30)),
                ('city', models.CharField(default='LeMonde', max_length=30)),
                ('post_code', models.CharField(default='2000', max_length=8)),
                ('phone', models.CharField(blank=True, default='032-725-08-58', max_length=30, null=True)),
                ('mail', models.EmailField(blank=True, default='jrosk.ad@gmail.com', max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SiteOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapBox', models.CharField(blank=True, default='', max_length=1000, null=True)),
                ('carousel_auto_scroll', models.BooleanField(default=False)),
                ('carousel_auto_scroll_speed', models.IntegerField(default=5000)),
            ],
        ),
    ]
