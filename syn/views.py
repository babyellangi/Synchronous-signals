from django.http import HttpResponse
from .signals import my_signal
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def emit_signal(request):
    logging.info("Before emitting the signal.")
    my_signal.send(sender=None)
    logging.info("After emitting the signal.")
    return HttpResponse("Signal emitted!")
