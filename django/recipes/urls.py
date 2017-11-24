from django.conf.urls import url, include
from recipes import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'recipes', views.RecipeViewSet)
router.register(r'ingredients', views.IngredientViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
