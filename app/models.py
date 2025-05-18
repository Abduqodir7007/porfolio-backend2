from django.db import models

class Quote(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.author}'

class SkillCategory(models.Model):
    name = models.CharField(max_length=100) 
    
    class Meta:
        verbose_name = 'SkillCategories'
        
    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=100) 
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    
    def __str__(self):
        return f"{self.name}"

class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/')
    caption = models.TextField()
    url = models.URLField()
    skills = models.ManyToManyField(Skill, related_name='projects')
    
    def __str__(self):
        return self.name