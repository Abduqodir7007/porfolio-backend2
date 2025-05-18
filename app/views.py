from django.shortcuts import render
from .models import Quote, SkillCategory, Skill, Project
from .serializer import QuoteSerializer, SkillCategorySerializer, SkillSerializer, ProjectSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class QuoteView(ModelViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    
class SkillCategoryView(ModelViewSet):
    queryset = SkillCategory.objects.all()
    serializer_class = SkillCategorySerializer

class ProjectView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
class SkillView(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    