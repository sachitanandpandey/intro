from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'intro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #    (r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'^admin/', include(admin.site.urls)),
    (r'^tinymce/',include('tinymce.urls')),
    (r'^$', 'pages.views.MainHomePage'),
    (r'^register/$','member.views.MemberRegistration'),
    (r'^login/$','member.views.LoginRequest'),
    (r'^logout/$','member.views.LogoutRequest'),
    (r'^profile/$','member.views.Profile'),

)
