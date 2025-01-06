# from django.shortcuts import render, redirect
from item.models import Item, Category  
from .forms import EmailForm, OTPForm, NewPasswordForm
import random
from .forms import SignupForm
from django.contrib.auth import logout
from django.contrib import messages  
from django.contrib.auth import views as auth_views  
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User 
from jobs.models import Profile
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import smart_bytes
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.forms import SetPasswordForm
from django.utils.encoding import force_bytes
from django.utils.encoding import force_str  
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.utils.html import strip_tags



# def password_reset_confirm(request, uidb64, token):
#     try:
#         # Decode the UID and retrieve the user
#         uid = force_str(urlsafe_base64_decode(uidb64)) 
#         user = User.objects.get(pk=uid)
#     except (TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None

#     if user is not None and default_token_generator.check_token(user, token):
#         if request.method == 'POST':
#             form = SetPasswordForm(user, request.POST)
#             if form.is_valid():
#                 form.save()  # Save the new password

#                 # Send a success email to the user after password reset
#                 send_mail(
#                     "Password Reset Successful",  
#                     "Your password has been reset successfully. You can now log in with your new password.",  # Message body
#                     settings.DEFAULT_FROM_EMAIL,  # Sender's email (configured in settings.py)
#                     [user.email],  # Recipient email
#                     fail_silently=False  # Set to False to raise an error if sending fails
#                 )

#                 # Show success message on the webpage
#                 messages.success(request, "Your password has been reset successfully. You can now log in.")
                
#                 # Redirect to the homepage or login page
#                 return redirect('jobs:index')  # Change this to your desired redirect page

#         else:
#             form = SetPasswordForm(user)

#         return render(request, 'jobs/password_reset_confirm.html', {'form': form})
#     else:
#         messages.error(request, "The password reset link is invalid or has expired.")
#         return redirect('jobs:password_reset')



# def password_reset_done(request):
#     """
#     View for informing the user that the password reset request was successful.
#     This will be shown after the user submits their email for password reset.
#     """
#     return render(request, 'jobs/password_reset_done.html')

# def password_reset_complete(request):
#     """
#     View for informing the user that their password has been successfully reset.
#     This will be shown after the user changes their password.
#     """
#     return render(request, 'jobs/password_reset_complete.html')

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings

from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import PasswordResetForm

def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        
        if form.is_valid():
            email_input = form.cleaned_data["email"]  # Renamed to avoid overwriting
            
            try:
                user = User.objects.get(email=email_input)
            except User.DoesNotExist:
                messages.error(request, "No user found with this email address.")
                return redirect('jobs:password_reset')
            
            # Generate token and UID
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            
            # Get domain and protocol
            try:
                site_name = get_current_site(request).name
                domain = get_current_site(request).domain
            except Exception:
                # Hardcode the domain for production (if `get_current_site` fails)
                domain = "vipjobseekersworld.onrender.com"
                site_name = "VIP Job Seekers World"
            protocol = 'https' if request.is_secure() else 'http'
            
            # Prepare the reset link
            reset_link = f"{protocol}://{domain}/reset/{uid}/{token}/"
            
            # Email context
            context = {
                'site_name': site_name,
                'domain': domain,
                'protocol': protocol,
                'uid': uid,
                'token': token,
                'reset_link': reset_link,  
            }

            # Render email body
            html_message = render_to_string('jobs/password_reset_email.html', context)
            
            # Send email
            email_subject = "Password Reset Request"
            try:
                email_message = EmailMessage(
                    subject=email_subject,
                    body=html_message,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[email_input],  # Use the original email input
                )
                email_message.content_subtype = "html"  # Set the email content to HTML
                email_message.send(fail_silently=False)
                
                messages.success(request, "A password reset link has been sent to your email address.")
                return redirect('jobs:password_reset_done')
            except Exception as e:
                messages.error(request, f"Error sending email: {str(e)}")
                return redirect('jobs:password_reset')
    
    else:
        form = PasswordResetForm()

    return render(request, 'jobs/password_reset.html', {'form': form})







def index(request):
    items = Item.objects.filter(is_active=False).order_by('-create_at')[:12]
    category = Category.objects.all()
    total_users = User.objects.count()
    return render(request, 'jobs/index.html', {
        'category': category,
        'items': items,
        # 'messages': messages.get_messages(request),
        'messages': messages.get_messages(request),
        'total_users': total_users,
    })

def indexs(request):
    categories = Category.objects.all()
    items = Item.objects.all()
    return render(request, 'jobs/index2.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'jobs/contact.html')

def blog(request):
    return render(request, 'jobs/blog.html')

# def signup(request):
#     user_count = User.objects.count() 
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
        
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Your account has been created! You can now log in.")
#             return redirect('jobs:login')  
#     else:
#         form = SignupForm()
    
#     return render(request, 'jobs/signup.html', {
#         'form': form,
#         'user_count': user_count
#     })
def signup(request):
    user_count = User.objects.count()
    if request.method == 'POST':
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            profile_picture = form.cleaned_data.get('profile_picture')
            if profile_picture:
                Profile.objects.create(user=user, profile_picture=profile_picture)
            messages.success(request, "Your account has been created! You can now log in.")
            return redirect('jobs:login')
    else:
        form = SignupForm()
    return render(request, 'jobs/signup.html', {
        'form': form,
        'user_count': user_count
    })

def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out successfully.")  # Optional logout message
    return redirect('jobs:index')



class CustomLoginView(auth_views.LoginView):
    def form_valid(self, form):
        """On successful login, add a welcome message."""
        response = super().form_valid(form)
        messages.success(self.request, f"Hello {form.cleaned_data['username']}, welcome to VIP Job Seekers World! You are logged in successfully.")
        return response

    def form_invalid(self, form):
        """On failed login, show an error message."""
        messages.error(self.request, "Invalid username or password. Please try again.")
        return super().form_invalid(form)
    
    
    
def debug_view(request):
    try:
        password_reset_confirm_url = reverse('jobs:password_reset_confirm', kwargs={'uidb64': 'dummy_uid', 'token': 'dummy_token'})
        return render(request, 'jobs/debug.html', {'url': password_reset_confirm_url})
    except Exception as e:
        return render(request, 'jobs/debug.html', {'error': str(e)})
    
    

def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            request.user.set_password(new_password)
            request.user.save()
            messages.success(request, "Password reset successfully.")
            return redirect('some_view')
    else:
        form = PasswordResetForm()

    return render(request, 'new_password', {'form': form})
    
    
otp_storage = {}  # Temporary storage for email-OTP mapping (use a database in production)


# Step 1: Request Email
def request_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            user = User.objects.filter(email=email).first()
            if user:
                # Generate OTP
                otp = get_random_string(length=6, allowed_chars='0123456789')
                # Store OTP and email in session
                request.session['otp'] = otp
                request.session['email'] = email

                # Send OTP to the user email
                send_mail(
                    'Your OTP for password reset',
                    f'Your OTP is: {otp}',
                    'noreply@yourdomain.com',
                    [email],
                    fail_silently=False,
                )

                messages.success(request, 'OTP has been sent to your email.')
                return redirect('jobs:verify_otp')
            else:
                messages.error(request, 'Email address not found.')
                return redirect('jobs:request_email')
    else:
        form = EmailForm()

    return render(request, 'jobs/request_email.html', {'form': form})


# Step 2: Verify OTP
def verify_otp(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        stored_otp = request.session.get('otp')
        email = request.session.get('email')

        if otp == stored_otp:
            # OTP verified successfully, redirect to reset password page
            return redirect('jobs:new_password', email=email)
        else:
            messages.error(request, 'Invalid OTP')
            return redirect('jobs:verify_otp')

    return render(request, 'jobs/verify_otp.html')

from .forms import NewPasswordForm

def reset_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "Email not found.")
            return redirect('jobs:reset_password')

        # Generate OTP and send email
        otp = str(random.randint(100000, 999999))
        request.session['otp'] = otp
        send_mail(
            'Your OTP for password reset',
            f'Your OTP is {otp}.',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        return redirect('jobs:verify_otp')
    
    return render(request, 'jobs/reset_password.html')
    
def send_otp(request, email):
    otp = str(random.randint(100000, 999999))  # Generate a random 6-digit OTP
    
    # Store OTP in session for later comparison
    request.session['otp'] = otp
    
    # Send OTP email
    send_mail(
        'Your OTP for password reset',
        f'Your OTP for resetting your password is: {otp}',
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
    messages.success(request, "OTP sent to your email. Please check your inbox.")
    return redirect('jobs:verify_otp')


def new_password(request, email):
    if request.method == 'POST':
        password = request.POST.get('password')
        user = User.objects.get(email=email)
        user.set_password(password)
        user.save()
        messages.success(request, 'Password has been successfully updated.')
        return redirect('jobs:login')  # Redirect to login page after password change

    return render(request, 'jobs/new_password.html', {'email': email})
