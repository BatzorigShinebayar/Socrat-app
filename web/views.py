from .models import *
from .forms import CommentForm
from django.shortcuts import render
from django.db.models import Sum

def index(request):
    hero = IndexBanner.objects.all()
    info = IndexInfo.objects.all()
    botbanner = IndexBotBanner.objects.all()
    portCount = Portfolio.objects.all().count()
    portfolio = Portfolio.objects.filter().order_by('created_date')
    value = Portfolio.objects.aggregate(Sum('value')).get('value__sum', 0.00)
    newses = News.objects.filter().order_by('created_date')
    indexbanner = IncubationMidBanner.objects.filter().order_by('created_date')
    benefit = IncubationProgramBenefit.objects.all()
    quote = TeamMembers.objects.all()
    return render(request, 'web/index.html', locals())



def SingUp(request):
    return render(request, 'web/page-signup.html', locals())


def handler404(request, exception):
    return render(request, 'web/page-404.html', locals())

def team(request):
    data = TeamMembers.objects.all()
    params = {}
    teamtype = TeamType.objects.filter().order_by('created_date')
    params.update({'tag_id': 4})
    teammembers = TeamMembers.objects.order_by('team_type')
    teambanner = TeamBanner.objects.all()
    return render(request, 'web/team.html', locals())


def portfolioPage(request):
    context = {
        'portfolio': Portfolio,
        'banner': PortfolioBanner
    }
    params = {}
    portfoliobanner = PortfolioBanner.objects.filter().order_by('created_date')
    sector = Sector.objects.filter().order_by('created_date')
    params.update({'tag_id': 4})
    portfolio = Portfolio.objects.filter().order_by('created_date')
    return render(request, 'web/portfolio.html', locals())


def portfoltioDetail(request, sector_id):
    portfolio = Portfolio.objects.filter(id=sector_id).order_by('created_date')
    sector = Sector.objects.filter().order_by('created_date')
    portfoliotimeline = PortfolioTimeline.objects.filter(portfolio_id=sector_id)
    portfolioimages = PortfolioImages.objects.filter(portfolio_images=sector_id)
    return render(request, 'web/portfolio-detail.html', locals())


def news(request):
    needs = NeedFiles.objects.filter().order_by('created_date')
    links = NeedLinks.objects.filter().order_by('created_date')
    news_type = NewsType.objects.filter().order_by('id')
    newsbanner = NewsBanner.objects.all()
    type_get = request.GET['type']
    tag_get = request.GET['tag']
    params = {}

    if request.GET['type'] and request.GET['tag']:
        params.update({'type__id': request.GET['type'], 'tag__id': request.GET['tag']})
    elif request.GET['tag']:
        params.update({'tag__id': request.GET['tag']})
    elif request.GET['type']:
        params.update({'type__id': request.GET['type']})
    newses = News.objects.filter(**params).order_by('created_date')

    return render(request, 'web/news.html', locals())


def news_detail(request, article_id):
    needs = NeedFiles.objects.filter().order_by('created_date')
    links = NeedLinks.objects.filter().order_by('created_date')
    tags = NewsTag.objects.all()
    news_type = NewsType.objects.filter().order_by('id')
    links = NeedLinks.objects.filter().order_by('created_date')
    news = News.objects.filter(id=article_id).order_by('created_date').last()
    author = TeamMembers.objects.filter(id=article_id).order_by('created_date')
    other_news = News.objects.filter(tag=article_id)
    comments = news.comments.filter(news=news)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = news
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'web/news-detail.html', locals())

    def get_queryset(self):
        pk = self.kwargs['pk']
        return comments.objects.filter(news_id=pk)

def incubationPage(request):
    info = IncubationServiceGeneralInfo.objects.filter().order_by('created_date')
    benefit = IncubationProgramBenefit.objects.filter().order_by('created_date')
    incubation = IncubationProgram.objects.filter().order_by('created_date')
    types = IncubationTypes.objects.filter().order_by('created_date')
    stage = IncubationServiceStage.objects.filter().order_by('created_date')
    banner = IncubationBanner.objects.filter().order_by('created_date')
    midbanner = IncubationMidBanner.objects.filter().order_by('created_date')
    botbanner = IncubationBotBanner.objects.filter().order_by('created_date')
    gallery = IncubationPageGallery.objects.filter().order_by('created_date')
    inews = News.objects.filter().order_by('created_date')

    return render(request, 'web/service.html', locals())


def faq(request):
    faq = Faq.objects.filter().order_by('created_date')
    faqtype = FaqType.objects.filter().order_by('id')
    faqbanner = FaqBanner.objects.filter().order_by('created_date')

    params = {}

    if request.GET['type']:
        params.update({'type__id': request.GET['type']})

    return render(request, 'web/page-faq.html', locals())


def about(request):
    about = About.objects.filter().order_by('created_date')
    aboutbanner = AboutBanner.objects.filter().order_by('created_date')
    botbanner = AboutBotBanner.objects.filter().order_by('created_date')
    info = AboutInfo.objects.all()
    return render(request, 'web/about.html', locals())
