from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template

from .forms import ContactForm


def home(request):
    return render(request, 'home.html', {})


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': 'Contact Us',
        'content': 'Please fill out this form to send us you query',
        'form': contact_form
    }

    if contact_form.is_valid():
        data = contact_form.cleaned_data

        subject = 'Code Warrior - Message from ' + data.get('email')
        txt_ = get_template('contact/message.txt').render(data)
        html_ = get_template('contact/message.html').render(data)
        from_email = 'Code Warrior <' + data.get('email') + '>'
        recipient_list = [x[1] for x in settings.MANAGERS]
        send_mail(
            subject,
            txt_,
            from_email,
            recipient_list,
            html_message=html_,
            fail_silently=False
        )
    
    # if contact_form.errors:
    #     errors = contact_form.errors.as_json()
    #     if request.is_ajax():
    #         # Since data is already in json, we use HttpResponse
    #         return HttpResponse(errors, status=400, content_type='application/json')
    
    return render(request, 'contact/contact.html', context)
