from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Home,About,Profile,Category,Skills,Portfolio,ContactForm

 
def index(request):
    home = Home.objects.latest('updated')

    about = About.objects.latest('updated')
    profiles = Profile.objects.filter(about=about)


     # Skills
    categories = Category.objects.all()

    # Portfolio
    portfolios = Portfolio.objects.all()

    # form = ContactForm.data.latest('updated')
    
    context={
        'home': home,
        'about': about,
        'profiles': profiles,
        'categories': categories,
        'portfolios': portfolios,
        # 'form': form,

    }
    return render(request, 'index.html', context)

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = "Website Inquiry" 
			body = {
			'first_name': form.cleaned_data['first_name'], 
			'last_name': form.cleaned_data['last_name'], 
			'email': form.cleaned_data['email_address'], 
			'message':form.cleaned_data['message'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'email', ['popoolatunde52@gmail.com']) 
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return redirect ("main:index")
      
	form = ContactForm()
	return render(request, "index.html", {'form':form})