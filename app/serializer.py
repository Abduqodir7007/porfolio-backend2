from rest_framework import serializers
from .models import Quote, SkillCategory, Skill, Project


class QuoteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Quote
        fields = ['id', 'text', 'author']


class SkillCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillCategory
        fields = ['id', 'name']
        
class SkillSerializer(serializers.ModelSerializer):
    category = SkillCategorySerializer(read_only=True)
    
    class Meta:
        model = Skill
        fields = ['id', 'name', 'category']
class ProjectSerializer(serializers.ModelSerializer):
    skills = SkillSerializer(many=True, read_only=True)
    
    class Meta:
        model = Project
        fields = ['id', 'name', 'image', 'caption', 'url', 'skills']
        
