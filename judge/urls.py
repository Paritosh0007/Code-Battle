from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.views.generic import RedirectView

from .views import home, contact_page
from accounts.views import RegisterView, ProfileView, LoginView, LeaderBoardView


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^leaderboard/$', LeaderBoardView.as_view(), name='leaderboard'),
    url(r'^profile/(?P<username>[a-zA-Z0-9]+)/$', ProfileView.as_view(), name='profile'),
    url(r'^account/', include('accounts.urls', namespace='account')),
    url(r'^accounts/', include('accounts.passwords.urls')),
    url(r'^accounts/$', RedirectView.as_view(url='/account')),
    url(r'^questions/', include('questions.urls', namespace='question')),
    url(r'^question/', include('grader.urls', namespace='grader')),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
