from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^wikiapp/', include('wikiapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
(r'^wikiapp/(?P<page_name>[^/]+)/edit/$','wikiapp.wiki.views.edit_page'),
(r'^wikiapp/(?P<page_name>[^/]+)/save/$','wikiapp.wiki.views.save_page'),
(r'^wikiapp/(?P<page_name>[^/]+)/$','wikiapp.wiki.views.view_page')
)
