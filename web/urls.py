from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('portfolio/', portfolioPage, name='portfolio'),
    path('portfolio-detail/<int:sector_id>/', portfoltioDetail, name='portfolio'),
    path('team/', team, name='team'),
    path('news/', news, name='news'),
    path('faq/', faq, name='faq'),
    path('about/', about, name='about'),
    path('SingUp/', SingUp, name='sing-up'),
    path('news-detail/<int:article_id>', news_detail, name='news-detail'),
    path('service/', incubationPage, name='service'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

