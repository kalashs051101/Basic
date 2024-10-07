from django.shortcuts import render

# Create your views ehere.
# def generate_pd# views.py

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa  # Import required libraries

def generate_pdf(request):
    # Retrieve data or perform calculations
    invoice_id = 123
    customer_name = 'John Doe'
    amount = 199.99
    
    # Context data for the template rendering
    context = {
        'invoice_id': invoice_id,
        'customer_name': customer_name,
        'amount': amount,
    }
    
    # Rendered template
    template_path = 'pdf.html'
    template = get_template(template_path)
    html = template.render(context)
    
    filename = f"invoice_{invoice_id}.pdf"  # Example: invoice_123.pdf
    # Create a PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="invoice.pdf"'
    
    pisa_status = pisa.CreatePDF(html, dest=response)
    print(filename)
    
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')

    # subject = 'Your Invoice'
    # message = 'Please find your invoice attached.'
    # from_email = 'your_email@example.com'
    # to_email = ['recipient_email@example.com']
    
    # email = EmailMessage(subject, message, from_email, to_email)
    # email.attach(pdf_filename, response.content, 'application/pdf')
    # email.send()
    
    # return HttpResponse('Invoice sent successfully!')
    return response
