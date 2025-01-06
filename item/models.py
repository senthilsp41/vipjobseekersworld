# from django.db import models
# from django.utils import timezone 
# from django.contrib.auth.models import User
# on_delete_options = [
#     models.CASCADE,
#     models.PROTECT,
#     models.SET_NULL,
#     models.SET_DEFAULT,
#     models.RESTRICT,
# ]
# # Create your models here.

# class Category(models.Model):
#     name=models.CharField(max_length=250)
#     # image=models.ImageField(upload_to='items_images',blank=True,null=True)
    
#     class Meta:
#         ordering=('name',)
#         verbose_name_plural='Category'
        
#     def __str__(self):
#         return self.name
    
# from django.db import models

# class Item(models.Model):
#     # category=models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
#     # Company Information
#     image=models.ImageField(upload_to='items_images',blank=True,null=True)
#     company_name = models.CharField(max_length=255)
#     company_email = models.EmailField()
#     company_website = models.URLField(blank=True, null=True)
#     company_description = models.TextField(blank=True, null=True)

#     # Job Information
#     job_title = models.CharField(max_length=255)
#     job_location = models.CharField(max_length=255)
#     job_type = models.CharField(max_length=50, choices=[
#         ('Linkedin', 'LinkedIn'),
#         ('Naukri', 'Naukri'),
#         ('CompanyWebsite', 'Website'),
#         ('others', 'Others'),
#     ])
#     companyfind_website = models.URLField(blank=True, null=True)
#     salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

#     # Interview Experience
    
#     interview_date = models.DateField()
#     interview_rounds = models.TextField()
#     interview_type = models.CharField(max_length=50, choices=[
#         ('walkin', 'Walk-in'),
#         ('reference', 'Reference'),
#         ('online', 'Online'),
#         ('phone', 'Phone'),
#     ])
#     interview_feedback = models.TextField(blank=True, null=True)
#     candidate_name = models.CharField(max_length=255)
#     candidate_email = models.EmailField()
#     is_active=models.BooleanField(default=False)
#     created_by=models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
#     create_at=models.DateField(auto_now_add=True)
#     skills = models.CharField(max_length=255, blank=True, null=True)
#     experience_required = models.CharField(max_length=255, blank=True, null=True)
#     mobile_number = models.CharField(max_length=15, blank=True, null=True)
    
    
   

#     def __str__(self):
#         return f"{self.job_title} at {self.company_name} (Interview by {self.candidate_name})"

from django.db import models
from django.utils import timezone 
from django.contrib.auth.models import User
on_delete_options = [
    models.CASCADE,
    models.PROTECT,
    models.SET_NULL,
    models.SET_DEFAULT,
    models.RESTRICT,
]
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=250)
    # image=models.ImageField(upload_to='items_images',blank=True,null=True)
    
    class Meta:
        ordering=('name',)
        verbose_name_plural='Category'
        
    def __str__(self):
        return self.name
    
from django.db import models

class Item(models.Model):
    # category=models.ForeignKey(Category,related_name='items',on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    # Company Information
    image=models.ImageField(upload_to='items_images',blank=True,null=True)
    company_name = models.CharField(max_length=255)
    company_email = models.EmailField()
    company_website = models.URLField(blank=True, null=True)
    company_description = models.TextField(blank=True, null=True)

    # Job Information
    job_title = models.CharField(max_length=255)
    job_location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=50, choices=[
        ('Linkedin', 'LinkedIn'),
        ('Naukri', 'Naukri'),
        ('CompanyWebsite', 'Website'),
        ('others', 'Others'),
    ])
    companyfind_website = models.URLField(blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Interview Experience
    
    interview_date = models.DateField()
    interview_rounds = models.TextField()
    interview_type = models.CharField(max_length=50, choices=[
        ('walkin', 'Walk-in'),
        ('reference', 'Reference'),
        ('online', 'Online'),
        ('offline','Offline'),
        ('others','Others')
    ])
    interview_feedback = models.TextField(blank=True, null=True)
    candidate_name = models.CharField(max_length=255)
    candidate_email = models.EmailField()
    is_active=models.BooleanField(default=False)
    created_by=models.ForeignKey(User,related_name='items',on_delete=models.CASCADE)
    create_at=models.DateField(auto_now_add=True)
    skills = models.CharField(max_length=255, blank=True, null=True)
    experience_required = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    uploaded_by = models.CharField(max_length=50, choices=[
        ('recruiter', 'Recruiter'),
        ('working_employee', 'Working Employee'),
        ('job_seeker', 'Job Seeker'),
        ('freelancer', 'Freelancer'),
        ('others', 'Others')
    ], default='job_seeker')
    
    
   

    def __str__(self):
        return f"{self.job_title} at {self.company_name} (Interview by {self.candidate_name})"
    
class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    deleted_by_user = models.ManyToManyField(User, related_name="deleted_messages", blank=True)


    def __str__(self):
        return f"Message from {self.sender.username} at {self.timestamp}"


    
