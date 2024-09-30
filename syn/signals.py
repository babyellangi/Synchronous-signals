from django.dispatch import Signal, receiver
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define a custom signal
my_signal = Signal()

@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    logging.info("Signal handler executed.")
