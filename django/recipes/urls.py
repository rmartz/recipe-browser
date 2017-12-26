from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from recipes import views


router = DefaultRouter()
router.register(r'recipes', views.RecipeViewSet, 'recipes')
router.register(r'ingredients', views.IngredientViewSet, 'ingredients')

urlpatterns = [
    url(r'^', include(router.urls))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
