"""
URL configuration for tourism project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from tour import views as tourview
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header='Trippy Admin'
admin.site.site_title='Trippy Portal'
admin.site.index_title='Welcome to Trippy Portal'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',tourview.home,name='home'),
    path('service/',tourview.service,name='service'),
    path('contact/',tourview.contact,name='contact'),
    path('about/',tourview.about,name='about'),
    path('service/<int:tour_id>/',tourview.detail,name='detail'),
    path('service/<int:tour_id>/create', tourview.createreview,name='createreview'),
    path('review/<int:review_id>', tourview.updatereview,name='updatereview'),
    path('review/<int:review_id>/delete',tourview.deletereview,name='deletereview'),
    path('accounts/', include('accounts.urls')),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)