# Generated by Django 3.1.5 on 2021-02-09 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.FileField(upload_to='Image/About/Story/%Y/%m/%d', verbose_name='Story Image')),
                ('story', models.CharField(max_length=200, verbose_name='Story Title')),
                ('story_desc', models.TextField(verbose_name='Story Description')),
                ('link', models.CharField(max_length=300, verbose_name='Link')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
            },
        ),
        migrations.CreateModel(
            name='AboutBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('image', models.FileField(upload_to='Image/Banner/About/%Y/%m/%d', verbose_name='Banner')),
                ('link', models.CharField(max_length=300, verbose_name='Link')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'About Page Hero Banner',
                'verbose_name_plural': 'About Page Hero Banner',
            },
        ),
        migrations.CreateModel(
            name='AboutBotBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('image', models.FileField(upload_to='Image/Banner/About/%Y/%m/%d', verbose_name='Banner')),
                ('link', models.CharField(max_length=300, verbose_name='Link')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'About Page Bot Banner',
                'verbose_name_plural': 'About Page Bot Banner',
            },
        ),
        migrations.CreateModel(
            name='AboutInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.TextField(max_length=400, verbose_name='Description')),
                ('image', models.FileField(upload_to='Image/About/Info/%Y/%m/%d', verbose_name='Story Image')),
                ('link', models.CharField(max_length=300, verbose_name='Link')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'About Info',
                'verbose_name_plural': 'About Info',
            },
        ),
        migrations.CreateModel(
            name='FaqBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=300, verbose_name='Subtitle')),
                ('image', models.FileField(upload_to='Image/Banner/FAQ/%Y/%m/%d', verbose_name='Banner')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'FAQ Page Hero Banner',
                'verbose_name_plural': 'FAQ Page Hero Banner',
            },
        ),
        migrations.CreateModel(
            name='FaqType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'FAQ Type',
                'verbose_name_plural': 'FAQ Type',
            },
        ),
        migrations.CreateModel(
            name='IncubationBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.CharField(max_length=300, verbose_name='Description')),
                ('link', models.CharField(max_length=300, verbose_name='Link')),
                ('image', models.FileField(upload_to='Image/Banner/Incubation/%Y/%m/%d', verbose_name='Banner')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Incubation Page Hero Banner',
                'verbose_name_plural': 'Incubation Page Hero Banner',
            },
        ),
        migrations.CreateModel(
            name='IncubationBotBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.FileField(upload_to='Image/Banner/Incubation/%Y/%m/%d', verbose_name='MidBanner')),
                ('link', models.CharField(max_length=300, verbose_name='Link')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Incubation Page Bottom Banner',
                'verbose_name_plural': 'Incubation Page Bottom Banner',
            },
        ),
        migrations.CreateModel(
            name='IncubationMidBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('image', models.FileField(upload_to='Image/Banner/Incubation/%Y/%m/%d', verbose_name='MidBanner')),
                ('link', models.CharField(max_length=300, verbose_name='Link')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Incubation Page Middle Banner',
                'verbose_name_plural': 'Incubation Page Middle Banner',
            },
        ),
        migrations.CreateModel(
            name='IncubationPageGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('image', models.FileField(upload_to='Image/Incubation/Gallery/%Y/%m/%d', verbose_name='Image')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Incubation Gallery',
                'verbose_name_plural': 'Incubation Gallery',
            },
        ),
        migrations.CreateModel(
            name='IncubationProgramBenefit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('image', models.FileField(upload_to='Image/Incubation/Icon/%Y/%m/%d', verbose_name='icon')),
                ('is_published', models.CharField(choices=[('0', 'no'), ('1', 'yes')], max_length=1, null=True, verbose_name='Is Published')),
                ('description', models.TextField(verbose_name='Description')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Incubation Program Benefit',
                'verbose_name_plural': 'Incubation Program Benefit',
            },
        ),
        migrations.CreateModel(
            name='IncubationServiceGeneralInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('short_description', models.TextField(verbose_name='Short Description')),
                ('description', models.TextField(verbose_name='Description')),
                ('link', models.CharField(max_length=300, verbose_name='Link')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Incubation General Info',
                'verbose_name_plural': 'Incubation General Info',
            },
        ),
        migrations.CreateModel(
            name='IncubationServiceStage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=400, verbose_name='Subtitle')),
                ('image', models.FileField(upload_to='Image/Incubation/%Y/%m/%d', verbose_name='Banner')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Incubation Service Stage',
                'verbose_name_plural': 'Incubation Service Stage',
            },
        ),
        migrations.CreateModel(
            name='IncubationTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Short Description')),
                ('link', models.CharField(max_length=300, verbose_name='Link')),
                ('image', models.FileField(upload_to='Image/Incubation/Icon/%Y/%m/%d', verbose_name='icon')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Incubation Type',
                'verbose_name_plural': 'Incubation Type',
            },
        ),
        migrations.CreateModel(
            name='IndexBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=300, verbose_name='Subtitle')),
                ('image', models.FileField(upload_to='Image/Banner/Portfolio/%Y/%m/%d', verbose_name='Banner')),
                ('link', models.CharField(max_length=300, verbose_name='Link')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Index Page Hero Banner',
                'verbose_name_plural': 'Index Page Hero Banner',
            },
        ),
        migrations.CreateModel(
            name='IndexBotBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=200, verbose_name='Subtitle')),
                ('desc', models.TextField(max_length=500, verbose_name='Description')),
                ('image', models.FileField(upload_to='Image/Banner/Portfolio/%Y/%m/%d', verbose_name='Banner')),
                ('link', models.CharField(max_length=300, verbose_name='Link')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Index Bot Banner',
                'verbose_name_plural': 'Index Bot Banner',
            },
        ),
        migrations.CreateModel(
            name='IndexInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('desc', models.TextField(verbose_name='Description')),
                ('fact1', models.CharField(max_length=200, verbose_name='Fact 1')),
                ('fact2', models.CharField(max_length=200, verbose_name='Fact 2')),
                ('fact3', models.CharField(max_length=200, verbose_name='Fact 3')),
                ('image1', models.FileField(upload_to='Image/Portfolio/%Y/%m/%d', verbose_name='Image 1')),
                ('image2', models.FileField(upload_to='Image/Portfolio/%Y/%m/%d', verbose_name='Image 2')),
                ('image3', models.FileField(upload_to='Image/Portfolio/%Y/%m/%d', verbose_name='Image 3')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Index Info',
                'verbose_name_plural': 'Index Info',
            },
        ),
        migrations.CreateModel(
            name='NeedFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('file', models.FileField(upload_to='documents/%Y/%m/%d/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Useful Files',
                'verbose_name_plural': 'Useful Files',
            },
        ),
        migrations.CreateModel(
            name='NeedLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('link', models.CharField(blank=True, max_length=100, null=True, verbose_name='Link')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Useful Link',
                'verbose_name_plural': 'Useful Link',
            },
        ),
        migrations.CreateModel(
            name='NewsBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=300, verbose_name='Subtitle')),
                ('image', models.FileField(upload_to='Image/Banner/News/%Y/%m/%d', verbose_name='Banner')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'News Page Hero Banner',
                'verbose_name_plural': 'News Page Hero Banner',
            },
        ),
        migrations.CreateModel(
            name='NewsTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='title')),
            ],
            options={
                'verbose_name': 'News Tag',
                'verbose_name_plural': 'News Tag',
            },
        ),
        migrations.CreateModel(
            name='NewsType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='title')),
            ],
            options={
                'verbose_name': 'News Type',
                'verbose_name_plural': 'News Type',
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_published', models.CharField(choices=[('0', 'no'), ('1', 'yes')], max_length=1, null=True, verbose_name='Is Published')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('slug', models.TextField(blank=True, null=True, verbose_name='Slug')),
                ('image', models.FileField(upload_to='Image/Portfolio/%Y/%m/%d')),
                ('value', models.IntegerField(blank=True, null=True, verbose_name='Value')),
                ('current_date', models.DateField(verbose_name='Current Date')),
                ('start_date', models.DateField(verbose_name='Started Date')),
                ('end_date', models.DateField(verbose_name='End Date')),
                ('finance', models.CharField(max_length=100, verbose_name='Finance')),
                ('finance_step', models.CharField(max_length=100, verbose_name='Finance Step')),
                ('director', models.CharField(max_length=100, verbose_name='Director')),
                ('contact', models.CharField(max_length=100, verbose_name='Contact')),
                ('address', models.CharField(max_length=100, verbose_name='Address')),
                ('website', models.CharField(max_length=100, verbose_name='Website Link')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolio',
            },
        ),
        migrations.CreateModel(
            name='PortfolioBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=300, verbose_name='Subtitle')),
                ('image', models.FileField(upload_to='Image/Banner/Portfolio/%Y/%m/%d', verbose_name='Banner')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Portfolio Page Hero Banner',
                'verbose_name_plural': 'Portfolio Page Hero Banner',
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='title')),
                ('description', models.TextField(verbose_name='Read More')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Portfolio Type',
                'verbose_name_plural': 'Portfolio Type',
            },
        ),
        migrations.CreateModel(
            name='TeamBanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=300, verbose_name='Subtitle')),
                ('image', models.FileField(upload_to='Image/Banner/Team/%Y/%m/%d', verbose_name='Banner')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Team Page Hero Banner',
                'verbose_name_plural': 'Team Page Hero Banner',
            },
        ),
        migrations.CreateModel(
            name='TeamType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Title')),
                ('is_published', models.CharField(choices=[('0', 'no'), ('1', 'yes')], max_length=1, null=True, verbose_name='Is Published')),
                ('description', models.TextField(verbose_name='Description')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Team Type',
                'verbose_name_plural': 'Team Type',
            },
        ),
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.TextField(verbose_name='quote')),
                ('name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Name')),
                ('career', models.CharField(blank=True, max_length=100, null=True, verbose_name='Career')),
                ('image', models.FileField(upload_to='Image/Team Members/%Y/%m/%d', verbose_name='Image')),
                ('email', models.CharField(blank=True, max_length=100, null=True, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=100, null=True, verbose_name='Phone Number')),
                ('facebook', models.CharField(blank=True, max_length=100, null=True, verbose_name='Facebook Link')),
                ('instagram', models.CharField(blank=True, max_length=100, null=True, verbose_name='Instagram Link')),
                ('linkedin', models.CharField(blank=True, max_length=100, null=True, verbose_name='Linkedin Link')),
                ('github', models.CharField(blank=True, max_length=100, null=True, verbose_name='Github Link')),
                ('twitter', models.CharField(blank=True, max_length=100, null=True, verbose_name='Twitter Link')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('team_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.teamtype')),
            ],
            options={
                'verbose_name': 'Team Members',
                'verbose_name_plural': 'Team Members',
            },
        ),
        migrations.CreateModel(
            name='PortfolioTimeline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('date', models.DateField(max_length=20, verbose_name='Date')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('portfolio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.portfolio')),
            ],
            options={
                'verbose_name': 'Portfolio Timeline',
                'verbose_name_plural': 'Portfolio Timeline',
            },
        ),
        migrations.CreateModel(
            name='PortfolioImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_images', models.IntegerField(blank=True, null=True, verbose_name='ID')),
                ('image', models.FileField(upload_to='Image/Portfolio/%Y/%m/%d')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('portfolio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.portfolio')),
            ],
            options={
                'verbose_name': 'Pictures',
                'verbose_name_plural': 'Pictures',
            },
        ),
        migrations.CreateModel(
            name='PortfolioFAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=True, max_length=300, null=True, verbose_name='Question')),
                ('answer', models.CharField(blank=True, max_length=300, null=True, verbose_name='Answer')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('portfolio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.portfolio')),
            ],
            options={
                'verbose_name': 'Portfolio FAQ',
                'verbose_name_plural': 'Portfolio FAQ',
            },
        ),
        migrations.AddField(
            model_name='portfolio',
            name='sector',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.sector', verbose_name='Portfolio Type'),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('publish', models.CharField(choices=[('0', 'no'), ('1', 'yes')], max_length=1, verbose_name='Published')),
                ('short_desc', models.CharField(max_length=300, verbose_name='Short Description')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.FileField(upload_to='documents/%Y/%m/%d/')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='web.teammembers')),
                ('tag', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='web.newstag')),
                ('type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='web.newstype')),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
        ),
        migrations.CreateModel(
            name='IncubationProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('duration', models.CharField(max_length=200, verbose_name='Duration')),
                ('registration_link', models.CharField(max_length=100, verbose_name='Registration Link')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('investment_value', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.incubationprogrambenefit')),
            ],
            options={
                'verbose_name': 'Incubation Program',
                'verbose_name_plural': 'Incubation Program',
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=400, verbose_name='Question')),
                ('answer', models.TextField(verbose_name='Answer')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('faq_type', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='web.faqtype')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQ',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='web.news')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comment',
                'ordering': ['created_date'],
            },
        ),
    ]