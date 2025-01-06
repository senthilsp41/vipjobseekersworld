
from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from .forms import ConversationMessageForm
from .models import Conversation
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail

@login_required
def new_conversation(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    
    if item.created_by == request.user:
        return redirect('dashboard:index')

    conversations = Conversation.objects.filter(item=item, members__in=[request.user])
    
    if conversations:
        return redirect('conversation:detail', pk=conversations.first().id)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.members.add(request.user)
            conversation.members.add(item.created_by)
            conversation.save()
            
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            
            # Sending email notification
            send_mail(
                subject='VIP Job Seekers World Conversations...',
                message=(
                    f'Hello {item.created_by.username},\n\n'
                    f'You have received a message from {request.user.username}. '
                    f'That message is: {conversation_message.content}\n\n'
                    'Kindly reply to this user; it will be helpful for them. '
                    'Keep posting new jobs and help others.\n'
                    'Thank you!'
                ),
                from_email='pandisenthil17@gmail',  
                recipient_list=[item.created_by.email], 
                fail_silently=False,
            )
            
            messages.success(request, f"Hi {request.user.username}, your message has been sent successfully. Kindly wait for a reply and check your inbox frequently.")
            return redirect('item:detail', pk=item_pk)
    else:
        form = ConversationMessageForm()
    
    return render(request, 'conversation/new.html', {
        'form': form,
        'messages': messages.get_messages(request), 
    })

@login_required
def inbox(request):
    conversations = Conversation.objects.filter(members__in=[request.user.id])
    
    return render(request, 'conversation/inbox.html', {
        'conversations': conversations
    })

@login_required
def detail(request, pk):
    conversation = get_object_or_404(Conversation, pk=pk, members__in=[request.user.id])

    if request.method == "POST":
        form = ConversationMessageForm(request.POST)
        
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            messages.success(request, f"Hi {request.user.username}, your message has been sent successfully. Kindly wait for a reply and check your inbox frequently.")
            
            
            return redirect('conversation:detail', pk=pk)
    else:
        form = ConversationMessageForm()
        
    return render(request, 'conversation/detail.html', {
        "conversation": conversation,
        'form': form,
    })

@login_required
def delete_conversation(request, id):
    conversation = get_object_or_404(Conversation, id=id)

    # Check if the logged-in user is part of the conversation
    if request.user in conversation.members.all():
        conversation.delete()
        messages.success(request, "Conversation deleted successfully.")
    else:
        messages.error(request, "You don't have permission to delete this conversation.")

    return redirect('conversation:inbox')
