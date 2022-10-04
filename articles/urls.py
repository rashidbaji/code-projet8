from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from articles.views import compte, connexion, home, propos, style, contactez


urlpatterns = [
    path("", home, name="index"),
    path("propos", propos, name="propos"),
    path("connexion", connexion, name="connexion"),
    path("compte", compte, name="compte"),
    path("contact", contactez, name="contactez"),
    
    path("style", style, name="style"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)