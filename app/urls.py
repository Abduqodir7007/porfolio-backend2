from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import QuoteView, SkillCategoryView, SkillView, ProjectView
router = DefaultRouter()
router.register(r'quote', QuoteView, basename='quote')
router.register(r'skill', SkillView, basename='skill')
router.register(r'project', ProjectView, basename='project')
router.register(r'skillcategory', SkillCategoryView, basename='skillcategory')

urlpatterns = [
    path('', include(router.urls)), 
]

