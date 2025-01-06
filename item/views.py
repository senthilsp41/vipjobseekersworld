from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages  

from django.shortcuts import render, get_object_or_404, redirect
from .models import Category,Item,ChatMessage 
from .forms import NewItemForm,EditItemForm,ChatMessageForm
from django.core.paginator import Paginator 
from .models import ChatMessage


# from .models import Chat, ChatMessage
# from .forms import ChatMessageForm


# Create your views here.
# def detail(request, pk):
#     item = get_object_or_404(Item, pk=pk)
#     related_items = Item.objects.filter(category=item.category, is_active=False).exclude(pk=pk)[:3]

#     return render(request, 'item/detail.html', {
#         'item': item,
#         'related_items': related_items
#     })



def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', '0')

    # Fetch all categories
    categories = Category.objects.all()
    items = Item.objects.all()  # Fetch active items

    # Apply category filter
    if category_id != '0':
        items = items.filter(category_id=int(category_id))

    # Apply search query filter
    if query:
        items = items.filter(Q(job_title__icontains=query) | Q(skills__icontains=query))

    return render(request, 'item/items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
    })

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    
    
    print(f"Item: {item}, Image: {item.image}")  

    
    related_items = Item.objects.filter(category=item.category, is_active=False).exclude(pk=pk)[:3]

    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()  

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'New Item'
    })

@login_required
def edit(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES,instance=item)
        
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)  

    return render(request, 'item/form.html', {
        'form': form,
        'title': 'Edit Item'
    })
    
@login_required
def delete(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()
    
    return redirect('dashboard:index')
# @login_required
# def chat_view(request):
#     if request.method == 'POST':
#         message_content = request.POST.get('message')

#         # Create a new message
#         new_message = ChatMessage(sender=request.user, message=message_content)
#         new_message.save()

#         # Redirect to the chat page to reload the messages
#         return redirect('item:chat')

#     # Get all chat messages (order by timestamp so the newest messages come first)
#     messages = ChatMessage.objects.all().order_by('-timestamp')

#     return render(request, 'item/chat.html', {
#         'messages': messages,
#     })
# @login_required
# def chat_view(request):
#     messages = ChatMessage.objects.all().order_by('-timestamp')  # Get messages, newest first
#     paginator = Paginator(messages, 20)  # Show 20 messages per page

#     page_number = request.GET.get('page', 1)  # Get the page number from the URL, default to 1
#     page_obj = paginator.get_page(page_number)

#     context = {
#         'page_obj': page_obj,                # Contains the messages for the current page
#         'is_paginated': page_obj.has_other_pages(),  # Checks if there are more pages
#     }
#     return render(request, 'item/chat.html', context)


@login_required
def send_message(request):
    if request.method == 'POST':
        receiver_id = request.POST.get('receiver_id')
        message_content = request.POST.get('message')  # This should match the model field name

        if not receiver_id or not message_content:
            messages.error(request, "Both receiver and message are required.")
            return redirect('item:chat')

        try:
            receiver = User.objects.get(id=receiver_id)
            message = ChatMessage(sender=request.user, receiver=receiver, message=message_content)
            message.save()
            messages.success(request, "Message sent!")
        except User.DoesNotExist:
            messages.error(request, "User does not exist.")

        return redirect('item:chat')
@login_required
@login_required
def delete_message(request, message_id):
    # Get the message object or return 404 if not found
    message = get_object_or_404(ChatMessage, id=message_id)

    # Check if the logged-in user is the sender or an admin
    if request.user == message.sender or request.user.is_staff:
        message.delete()
        messages.success(request, "Message deleted successfully.")
    else:
        messages.error(request, "You don't have permission to delete this message.")
    
    return redirect('item:chat')




# @login_required
# def chat_view(request):
#     messages = ChatMessage.objects.filter(
#         Q(deleted_by_user=False) | Q(sender=request.user)
#     ).order_by('-timestamp')
    
#     return render(request, 'item/chat.html', {
#         'messages': messages,
#     })

@login_required
def chat_view(request):
    if request.method == 'POST':
        message_content = request.POST.get('message')

        # Create a new message
        new_message = ChatMessage(sender=request.user, message=message_content)
        new_message.save()

        # Redirect to the chat page to reload the messages
        return redirect('item:chat')

    # Get all chat messages (order by timestamp so the newest messages come first)
    messages = ChatMessage.objects.all().order_by('-timestamp')

    # Apply pagination (20 messages per page)
    paginator = Paginator(messages, 20)  # Show 20 messages per page
    page_number = request.GET.get('page', 1)  # Get the page number from the URL, default to 1

    # Catch EmptyPage error to prevent showing non-existent pages
    try:
        page_obj = paginator.get_page(page_number)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)  # Load the last page if the requested page is empty

    return render(request, 'item/chat.html', {
        'page_obj': page_obj,                # Contains the messages for the current page
        'is_paginated': page_obj.has_other_pages(),  # Checks if there are more pages
    })

