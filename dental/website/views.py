from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request, 'home.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		send_mail(

			'Appointment Request For: ' + message_name, 					
			'From: ' + message_name + "\n" + message_email + "\n\n" + message, 						
			message_email, 					
			['ramifamilyphotos2018@gmail.com', message_email],
			fail_silently=True,
			)

		return render(request, 'contact.html', {'message_name': message_name})
	else:
		return render(request, 'contact.html', {})