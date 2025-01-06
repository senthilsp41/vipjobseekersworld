from django import forms

from .models import ChatMessage

from .models import Item

INPUT_CLASSES='w-100 py-4 px-4 rounded border'

# class NewItemForm(forms.ModelForm):
#     class Meta:
#         model=Item
#         fields=('category','job_title','company_name','company_email','company_website','company_description','job_location','job_type','salary','interview_date','interview_rounds','interview_type','candidate_name','candidate_email','skills','experience_required','image','companyfind_website','mobile_number',)
        
#         widgets={
#         'category':forms.Select(attrs={
#             'class':INPUT_CLASSES
#         }),
#         'job_title':forms.TextInput(attrs={
#             'class':INPUT_CLASSES
#         }),
#         'company_name':forms.TextInput(attrs={
#             'class':INPUT_CLASSES
#         }),
#         'company_email':forms.EmailInput(attrs={
#             'class':INPUT_CLASSES
#         }),
#         'company_website':forms.TextInput(attrs={
#             'class':INPUT_CLASSES
#         }),
#         'skills':forms.TextInput(attrs={
#             'class':INPUT_CLASSES
#         }),
#         'experience_required':forms.TextInput(attrs={
#             'class':INPUT_CLASSES
#         }),
#         'image': forms.FileInput(attrs={'class': INPUT_CLASSES}),
#         'company_description':forms.Textarea(attrs={
#             'class':INPUT_CLASSES
#         }),
#         'job_location':forms.TextInput(attrs={
#             'class':INPUT_CLASSES
#         }),
#         'job_find':forms.Select(attrs={
#             'class':INPUT_CLASSES
#         }),
#         'salary':forms.NumberInput(attrs={
#             'class':INPUT_CLASSES
#         }),
#         'interview_date':forms.DateInput(attrs={
#             'class':INPUT_CLASSES
#         }),
#         'interview_rounds':forms.NumberInput(attrs={
#             'class':INPUT_CLASSES
#         }),
#         'interview_type':forms.Select(attrs={
#             'class':INPUT_CLASSES
#         }),
#         'interview_experience':forms.TextInput(attrs={
#             'class':INPUT_CLASSES
#         }),
#         'candidate_name':forms.TextInput(attrs={
#             'class':INPUT_CLASSES
#         }),
#         'candidate_email':forms.EmailInput(attrs={
#             'class':INPUT_CLASSES
#         }),
#         'mobile_number':forms.TextInput(attrs={
#             'class':INPUT_CLASSES
#         }),
#         'companyfind_website':forms.TextInput(attrs={
#             'class':INPUT_CLASSES
#         }),
        
#     }
        
class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = (
            'category', 'uploaded_by','job_title','company_name', 'company_website', 'interview_date','interview_type', 'company_email','job_location',
            'skills','company_description', 'experience_required', 'salary', 'job_type','interview_feedback',
          'candidate_email','companyfind_website',
            'image', 'mobile_number',
        )

        # Define field widgets
        widgets = {
            'category': forms.Select(attrs={'class': INPUT_CLASSES}),
            'job_title':forms.TextInput(attrs={'class':INPUT_CLASSES,'placeholder': 'Enter the job title'}),
            'company_name': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Enter the company Name'}),
            'company_email': forms.EmailInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Enter the company Email(optional)'}),
            'company_website': forms.TextInput(attrs={'class': INPUT_CLASSES, 'placeholder': 'Enter the company website(optional)'}),
            'job_location': forms.TextInput(attrs={'class': INPUT_CLASSES,'placeholder': 'Enter the job location'}),
            'skills': forms.TextInput(attrs={'class': INPUT_CLASSES,'placeholder': 'Enter required skills (e.g., Python, Java)'}),
            'company_description':forms.Textarea(attrs={'class':INPUT_CLASSES, 'placeholder': 'Enter a brief job description of the company' }),
            'experience_required': forms.TextInput(attrs={'class': INPUT_CLASSES,'placeholder': 'Enter the experience required (e.g., 2 years)'}),
            'salary': forms.NumberInput(attrs={'class': INPUT_CLASSES,'placeholder': 'Enter the salary amount'}),
            'job_type': forms.Select(attrs={'class': INPUT_CLASSES,'placeholder': 'Where did you find this job? (e.g., Naukri, LinkedIn..)'}),
            'interview_type': forms.Select(attrs={'class': INPUT_CLASSES,'placeholder': 'Where did you find this job? (e.g., Naukri, LinkedIn..)'}),
            'uploaded_by': forms.Select(attrs={'class': INPUT_CLASSES,'placeholder': 'Where did you find this job? (e.g., Naukri, LinkedIn..)'}),
            # 'interview_experience': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'interview_date':forms.TextInput(attrs={'class': INPUT_CLASSES,'placeholder': 'Enter Interview Date'}),
           
            'candidate_email': forms.EmailInput(attrs={'class': INPUT_CLASSES,'placeholder': 'Enter Your Valid Email'}),
            'interview_feedback':forms.Textarea(attrs={'class':INPUT_CLASSES,'placeholder': 'Share your interview experience (optional)'}),
            'companyfind_website':forms.TextInput(attrs={'class':INPUT_CLASSES,'placeholder': 'Share Naukri/LinkedIn job link'}),
            'image': forms.FileInput(attrs={'class': INPUT_CLASSES}),
            'mobile_number': forms.TextInput(attrs={'class': INPUT_CLASSES,'placeholder': 'Enter the mobile number (optional)'}),
        }

        # Define custom field labels
        labels = {
            'job_type': "Job Find",
            'candidate_name':"Your Name",
            'candidate_email':"Your Email",
            'interview_feedback':"Share with your Interview Experience",
            'companyfind_website':'Application link for the company.',
            'uploaded_by':"Your Role"

        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['image'].required = False
        self.fields['image'].required = False
         
        self.fields['interview_feedback'].required = False
        self.fields['mobile_number'].required = False
        self.fields['company_website'].required = False
        self.fields['company_email'].required = False
        
        
class EditItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('job_title','company_name','company_email','company_website','company_description','job_location','job_type','salary','interview_date','interview_rounds','candidate_name','candidate_email','skills','experience_required','image','is_active','companyfind_website','mobile_number',)
        
        widgets={
        
        'job_title':forms.TextInput(attrs={
            'class':INPUT_CLASSES
        }),
        'company_name':forms.TextInput(attrs={
            'class':INPUT_CLASSES
        }),
        'company_email':forms.EmailInput(attrs={
            'class':INPUT_CLASSES
        }),
        'company_website':forms.TextInput(attrs={
            'class':INPUT_CLASSES
        }),
        'skills':forms.TextInput(attrs={
            'class':INPUT_CLASSES
        }),
        'experience_required':forms.TextInput(attrs={
            'class':INPUT_CLASSES
        }),
        'image': forms.FileInput(attrs={'class': INPUT_CLASSES}),
        'company_description':forms.Textarea(attrs={
            'class':INPUT_CLASSES
        }),
        'job_location':forms.TextInput(attrs={
            'class':INPUT_CLASSES
        }),
        'job_type':forms.Select(attrs={
            'class':INPUT_CLASSES
        }),
        'salary':forms.NumberInput(attrs={
            'class':INPUT_CLASSES
        }),
        'interview_date':forms.DateInput(attrs={
            'class':INPUT_CLASSES
        }),
        'interview_rounds':forms.NumberInput(attrs={
            'class':INPUT_CLASSES
        }),
        'candidate_name':forms.TextInput(attrs={
            'class':INPUT_CLASSES
        }),
        'mobile_number':forms.TextInput(attrs={
            'class':INPUT_CLASSES
        }),
        'candidate_email':forms.EmailInput(attrs={
            'class':INPUT_CLASSES
        }),
         'companyfind_website':forms.TextInput(attrs={
            'class':INPUT_CLASSES
        }),
          
        
    }
        


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ['message']  # No need to include 'receiver' if it's not a group chat.
