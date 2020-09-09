"""ibprojecten URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# Added to open Files on dev server
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from ibprojecten.api.views import (HomePageView,
                                    requirementList,
                                    requirementDetail,
                                    ProductViewSet,
                                    ProductTypeViewSet,
                                    RequirementViewSet,
                                    ScopeViewSet,
                                    ScopeTypeViewSet,
                                    CriteriaViewSet,
                                    CriteriaTypeViewSet,
                                    DimensionViewSet,
                                    SubDimensionViewSet,
                                    SubDimensionTypeViewSet,
                                    DataElementViewSet)


router = DefaultRouter()
router.register(prefix='products', viewset=ProductViewSet)
router.register(prefix='producttype', viewset=ProductTypeViewSet)
router.register(prefix='requirement', viewset=RequirementViewSet)
router.register(prefix='scope', viewset=ScopeViewSet)
router.register(prefix='scopetype', viewset=ScopeTypeViewSet)
router.register(prefix='criteria', viewset=CriteriaViewSet)
router.register(prefix='dimension', viewset=DimensionViewSet)
router.register(prefix='subdimension', viewset=SubDimensionViewSet)
router.register(prefix='subdimensiontype', viewset=SubDimensionTypeViewSet)
router.register(prefix='datalement', viewset=DataElementViewSet)

urlpatterns = router.urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
    url(r'^api/requirements/$', requirementList, name='requirements'),
    url(r'^api/requirements/(?P<pk>[0-9]+)/$', requirementDetail),
    #url(r'^status/', include('ibprojecten.health.urls')),
    url(r'^$', HomePageView.as_view(), name='home'),
]


# To open Files on development server add this:
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)