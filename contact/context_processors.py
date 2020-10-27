from contact.forms import ContactForm

def contactform(request):
    return {'contactform':ContactForm}