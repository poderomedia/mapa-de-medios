from django.http import HttpResponse
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS admin
    url(r'^admin/',  include(admin.site.urls)), # admin site
    url(r'^select2/', include('select2.urls')), # select2 multiselect admin
    url(r'^home/', view=TemplateView.as_view(template_name="medioschile/index.html"), name='home'),
    url(r'^api/', view=TemplateView.as_view(template_name="api.html"), name='api'),
    url(r'^medioschile/', include('medioschile.urls', namespace='medioschile')), # medioschile
    url(r'^medioscolombia/', include('medioscolombia.urls', namespace='medioscolombia')), # medioscolombia
    url(r'^redactor/', include('redactor.urls')), # redactor editor
    url(r'^search/', include('haystack.urls')),

)	+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
