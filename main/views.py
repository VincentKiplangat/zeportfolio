from .cache_utils import compress_and_cache, decompress_from_cache
from .forms import ContactForm
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Contact


@csrf_exempt  # Disable CSRF for AJAX (or use CSRF token in AJAX request)
def contact_form(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Read JSON data from request

            name = data.get("name", "").strip()
            phone = data.get("phone", "").strip()
            email = data.get("email", "").strip()
            message = data.get("message", "").strip()

            Contact.objects.create(name=name, phone=phone, email=email, message=message)

            if not (name and phone and email and message):
                return JsonResponse({"status": "error", "message": "All fields are required."})

            # Send email to admin
            admin_email = "vkorir.vkk@gmail.com"  # Replace with your email
            subject = "New Contact Form Submission"
            admin_message = f"Name: {name}\nPhone: {phone}\nEmail: {email}\n\nMessage:\n{message}"
            send_mail(subject, admin_message, admin_email, [admin_email])

            # Send auto-reply to sender
            user_subject = "Thank You for Contacting Us"
            user_message = f"Hello {name},\n\nThank you for reaching out. I have received your message and will get back to you shortly.\n\nKind regards,\nKiplangat Vincent"
            send_mail(user_subject, user_message, admin_email, [email])

            return JsonResponse({"status": "success", "message": "Message sent successfully!"})

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid data format."})

    return JsonResponse({"status": "error", "message": "Invalid request."})



# views.py
@csrf_exempt
def send_comment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        blog_title = request.POST.get('blog_title')  # Get the blog title from the form

        # Combine the blog title with the message body
        subject = f"New Comment on {blog_title} from {name}"
        body = f"Blog Title: {blog_title}\n\nName: {name}\nEmail: {email}\nMessage: {message}"
        from_email = 'your_email@example.com'  # Your email

        try:
            # Send the email to yourself (don't send to the user)
            send_mail(subject, body, from_email, ['your_email@example.com'])
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})




def error_404(request):
    return render(request, "404.html")


from django.shortcuts import render

# Create your views here.


def blog(request):
    return render(request, "single-blog.html")


def blog2(request):
    return render(request, "single-blog2.html")


def blog3(request):
    return render(request, "single-blog3.html")


def blog4(request):
    return render(request, "single-blog4.html")


def blog5(request):
    return render(request, "single-blog5.html")


def blog6(request):
    return render(request, "single-blog6.html")


def home(request):
    return render(request, "index-main.html")


