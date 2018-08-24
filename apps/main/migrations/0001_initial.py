# Generated by Django 2.0.6 on 2018-08-24 19:56

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
                ('sub_title', models.TextField(default='In est risus, auctor sed, tristique in, tempus sit amet, sem. vestibulum rutrum rutrum neque.', max_length=200)),
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
                ('sub_title3', models.TextField(default='... ou en passant directement nous voir.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EventsSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Events', max_length=15)),
                ('header', models.CharField(default='Galerie', max_length=30)),
                ('title', models.CharField(default='Derniers événements', max_length=35)),
                ('sub_title', models.TextField(default='Curabitur at ipsum ac tellus semper interdum. maecenas pulvinar lobortis est. donec quis orci eget orci vehicula condimentum.', max_length=200)),
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
                ('title1', models.CharField(default='Tortor sem', max_length=20)),
                ('title2', models.CharField(default='Sapien et', max_length=20)),
                ('title3', models.CharField(default='Condimentum massa', max_length=20)),
                ('text1', models.CharField(default='In hac habitasse platea dictumst. quisque id justo sit amet sapien dignissim vestibulum.', max_length=200)),
                ('text2', models.CharField(default='Morbi ut odio. vivamus in felis eu sapien cursus vestibulum.', max_length=200)),
                ('text3', models.CharField(default='Quisque ut erat. donec dapibus.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MainOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='PersonnalWebsiteForall', help_text='Nom du projet.', max_length=15)),
                ('name', models.CharField(default='MySite.', help_text='Nom du commerce.', max_length=15)),
                ('name_add', models.CharField(default='Forall', help_text='type de commerce.', max_length=9)),
                ('description', models.CharField(default='Hello world!', help_text='Très brève description.', max_length=30)),
                ('oppening', models.CharField(default='2016', help_text="Année d'ouverture.", max_length=4)),
                ('adress', models.CharField(default='awesome street', help_text='numéro + rue (12 rue des champs)', max_length=30)),
                ('city', models.CharField(blank=True, default='LeMonde', max_length=30, null=True)),
                ('post_code', models.CharField(blank=True, default='2000', max_length=4, null=True)),
                ('phone', models.CharField(blank=True, default='032-725-08-58', max_length=30, null=True)),
                ('mail', models.EmailField(blank=True, default='jrosk.ad@gmail.com', max_length=30, null=True)),
                ('facebook', models.CharField(blank=True, default='https://www.facebook.com/mcflysdinerneuchatel', max_length=1000, null=True)),
                ('tripadvisor', models.CharField(blank=True, default='https://www.tripadvisor.com/Restaurant_Review-g188066-d12069550-Reviews-McFly_s_Diner-Neuchatel.html', max_length=1000, null=True)),
                ('google', models.CharField(blank=True, default="https://www.google.ch/maps/place/McFly's+Diner+Neuch%C3%A2tel/@46.9922131,6.9248096,15z/data=!4m2!3m1!1s0x0:0x399ca68c2bcc87de?sa=X&ved=0ahUKEwiZ6cPbroPZAhWMOhQKHdR_Cz8Q_BIIggEwCg", max_length=1000, null=True)),
                ('twitter', models.CharField(blank=True, default='https://twitter.com/', max_length=1000, null=True)),
                ('instagram', models.CharField(blank=True, default='https://www.instagram.com/?hl=en', max_length=1000, null=True)),
                ('linkedin', models.CharField(blank=True, default='https://www.linkedin.com/', max_length=1000, null=True)),
                ('snapchat', models.CharField(blank=True, default='https://www.snapchat.com/', max_length=1000, null=True)),
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
                ('sub_title', models.TextField(default='Suspendisse accumsan tortor quis turpis. lorem ipsum dolor sit amet, consectetuer adipiscing elit.', max_length=200)),
                ('text1', models.TextField(default='Proin leo odio, porttitor id, consequat in, consequat ut, nulla. suspendisse potenti. suspendisse potenti. donec semper sapien a libero. in hac habitasse platea dictumst. aenean sit amet justo. donec ut mauris eget massa tempor convallis. cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus.', max_length=800)),
                ('text2', models.TextField(default='Mauris sit amet eros. in hac habitasse platea dictumst. vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; nulla dapibus dolor vel est. maecenas leo odio, condimentum id, luctus nec, molestie sed, justo. proin interdum mauris non ligula pellentesque ultrices. nullam orci pede, venenatis non, sodales sed, tincidunt eu, felis. ut tellus. vivamus vel nulla eget eros elementum pellentesque. vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; mauris viverra diam vitae quam.', max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='PromoSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Promo', max_length=15)),
                ('title', models.CharField(default='A title', max_length=35)),
                ('text', models.CharField(default='Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. phasellus in felis. duis consequat dui nec nisi volutpat eleifend. aliquam erat volutpat.', max_length=800)),
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
    ]
