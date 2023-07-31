
from django.shortcuts import render, redirect
from django.core.mail import send_mail


# Create your views here.

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import WaitlistForm  

def join_waitlist(request):
    # if request.method == 'POST':
    #     form = WaitlistForm(request.POST)
    #     # if form.is_valid():
    #     #     # form.save()

    #     #     # # Get the user's input from the form
    #     #     # first_name = form.cleaned_data['first_name']
    #     #     # last_name = form.cleaned_data['last_name']
    #     #     # email = form.cleaned_data['email']
    #     #     # phone_number = form.cleaned_data['phone_number']
    #     #     # profession = form.cleaned_data['profession']

    #     #     # # Send email to the user
    #     #     # subject = 'Thank you for joining our waitlist'
    #     #     # message = f"Dear {first_name} {last_name},\n\nThank you for joining our waitlist! Your profession as {profession} has been registered with the email address {email} and phone number {phone_number}.\n\nBest regards,\nThe MedAssist Team"
    #     #     # from_email = 'your_email@example.com'  # Replace with your email address
    #     #     # recipient_list = [email]
    #     #     # send_mail(subject, message, from_email, recipient_list)

    #     #     # # Redirect to a success page after submission
    #     #     print("Form is valid")
    #     #     return redirect('waitlist_success')
    # else:
    #     form = WaitlistForm()
    
    if request.method == 'POST':
        print("POST request")
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        profession = request.POST.get('profession')
        
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'phone_number': phone_number,
            'profession': profession
        }
        
        message = f"Dear {first_name},\n\nThank you for joining our waitlist! We will contact you when we are ready to launch.\n\nBest regards,\nThe MedAssist Team"
        
        send_mail(
            'Thank you for joining our waitlist',
            message,
            '',
            [email],

        )
        
        return render(request, 'base/waitlist_success.html', data)
        

    return render(request, 'base/home.html')

   


