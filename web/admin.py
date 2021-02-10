from django.contrib import admin
from .models import *


class PortfolioImagesAdmin(admin.TabularInline):
    model = PortfolioImages
    fields = ['image']
    extra = 0


class PortfolioTimeLineAdmin(admin.TabularInline):
    model = PortfolioTimeline
    fields = ['title', 'date', 'description']
    extra = 0


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['title']
    inlines = [PortfolioTimeLineAdmin, PortfolioImagesAdmin]


class TeamMembersAdmin(admin.TabularInline):
    model = TeamMembers
    fields = ['name', 'career', 'image', 'email']
    extra = 0


class TeamTypeAdmin(admin.ModelAdmin):
    list_display = ['title']
    ordering = ['title']
    inlines = [TeamMembersAdmin]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_date')
    list_filter = ('news', 'created_date')
    search_fields = ('name', 'email', 'body')


admin.site.register(IndexInfo)
admin.site.register(IndexBotBanner)
admin.site.register(IndexBanner)
admin.site.register(IncubationBotBanner)
admin.site.register(IncubationMidBanner)
admin.site.register(IncubationBanner)
admin.site.register(IncubationTypes)
admin.site.register(IncubationServiceStage)
admin.site.register(IncubationProgramBenefit)
admin.site.register(IncubationServiceGeneralInfo)
admin.site.register(IncubationProgram)
admin.site.register(IncubationPageGallery)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(PortfolioTimeline)
admin.site.register(PortfolioImages)
admin.site.register(PortfolioBanner)
admin.site.register(Sector)
admin.site.register(Faq)
admin.site.register(FaqType)
admin.site.register(FaqBanner)
admin.site.register(TeamType)
admin.site.register(TeamMembers)
admin.site.register(TeamBanner)
admin.site.register(News)
admin.site.register(NewsBanner)
admin.site.register(NewsTag)
admin.site.register(NewsType)
admin.site.register(NeedFiles)
admin.site.register(NeedLinks)
admin.site.register(About)
admin.site.register(AboutBanner)
admin.site.register(AboutBotBanner)
admin.site.register(AboutInfo)
