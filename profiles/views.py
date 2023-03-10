from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import redirect, reverse

from .models import UserProfile, Ticket
from .forms import UserProfileForm, TicketForm
from home.forms import NewsletterForm
from home.models import Newsletter

from checkout.models import Order
# Create your views here.


@login_required
def profile(request):
    """Display the user's profile"""
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else: 
            messages.error(reuqest, 'Update failed. PLease ensure the form is valid.')
    form = UserProfileForm(instance=profile)
    orders = profile.orders.all()
    tickets = Ticket.objects.filter(user=request.user)
    ticketform = TicketForm()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'ticketform': ticketform,
        'profile': profile,
        'orders': orders,
        'on_profile_page': True,
        'tickets': tickets,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


@login_required
def tickets(request):
    """  """
    form = TicketForm(request.POST)
    if form.is_valid():
        ticket_new = form.save(commit=False)
        ticket_new.user = request.user
        ticket_new.save()
    return redirect('profile')


@login_required
def editemail(request):
    """Allows a user to update their newsletter email if logged in"""
    form = NewsletterForm(request.POST)
    if request.user.is_authenticated:
        newsletter = Newsletter.objects.get(user_id=request.user)
        newsletter.email = form.data["email"]
        newsletter.save()
        send_mail(
            "Subject here",
            "Here is the message.",
            "from@example.com",
            [form.data["email"]],
            fail_silently=False,
        )
        return redirect("create_post")


@login_required
def ticketdetail(request, ticket_id):
    """ A view to show individual ticket details """
    form = TicketForm()
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    if request.POST:
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()

    context = {
        'ticket': ticket,
        'ticketform': form,
    }

    return render(request, 'profiles/ticket_detail.html', context)


@login_required
def ticketdelete(request, ticket_id):
    """ A view to delete a ticket the user made """
    ticket = get_object_or_404(Ticket, pk=ticket_id)

    if request.method == 'POST':
        ticket.delete()
        # Return a success URL
        return redirect(reverse('profile'))