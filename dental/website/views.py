from django.shortcuts import render
from django.core.mail import send_mail

def home(request):

	if request.method == "POST":
		your_name = request.POST['your-name']
		your_phone = request.POST['your-phone']
		your_email = request.POST['your-email']
		your_address = request.POST['your-address']
		your_schedule = request.POST['your-schedule']
		your_time = request.POST['your-time']
		your_message = request.POST['your-message']

		send_mail(

			'New Appointment Request', 					
			'From: ' + your_name + "\n Contact# " + your_phone + "\n Day:" + 
				your_schedule + "\n Time: " + your_time + "\n\n" + your_message,
			your_email, 					
			['ramifamilyphotos2018@gmail.com', your_email],
			fail_silently=True,
		)

		return render(request, 'home.html', {'your_name': your_name})

	else:
		return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		send_mail(

			'New Request/Feedback', 					
			'From: ' + message_name + "\n" + message_email + "\n\n" + message, 						
			message_email, 					
			['ramifamilyphotos2018@gmail.com', message_email],
			fail_silently=False,
			)

		return render(request, 'contact.html', {'message_name': message_name})
	else:
		return render(request, 'contact.html', {})

def about(request):
	return render(request, 'about.html', {})

def service(request):
	return render(request, 'service.html', {})

def pricing(request):
	return render(request, 'pricing.html', {})

def blog_details(request):
	return render(request, 'blog-details.html', {})

def base(request):
	if request.method == "POST":
		nl_email = request.POST['nl-email']

		send_mail(

			'News Letter Subscription', 					
			'From: ' + nl_email, 						
			nl_email, 					
			['ramifamilyphotos2018@gmail.com', nl_email],
			fail_silently=False,
			)

		return render(request, 'base.html', {'nl_email': nl_email})

