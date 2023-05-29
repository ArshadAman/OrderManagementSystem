# from django.db.models.signals import post_save, pre_save
# from django.dispatch import receiver
# from django.core.mail import send_mail
# from .models import Order

# @receiver(pre_save, sender=Order)
# def send_order_status_email(sender, instance, **kwargs):
#     # Get the previous status of the order

#     # Get the previous status of the order
#     try:
#         old_status = Order.objects.get(id=instance.id).order_status
#     except Order.DoesNotExist:
#         # The object has been deleted, no need to send email
#         return

#     # Check if the order status has changed
#     if old_status != instance.order_status:
#         # Send email to customer
#         subject = f'Order {instance.order_name} status changed to {instance.order_status}'
#         message = f'Dear customer,\n\nYour order {instance.order_name} with orderId {instance.id} has been updated to {instance.order_status}.\n\nThank you!'
#         from_email = 'devxplore202@gmail.com'
#         recipient_list = [instance.customer_email]
#         send_mail(subject, message, from_email, recipient_list)

# @receiver(post_save, sender=Order)
# def send_order_status_email(sender, instance, created, **kwargs):
#     if created:
#         # Send email to customer
#         subject = f'Order {instance.order_name} status changed to {instance.order_status}'
#         message = f'Dear customer,\n\nYour order {instance.order_name} with orderId {instance.id} has been updated to {instance.order_status}.\n\nThank you!'
#         from_email = 'devxplore202@gmail.com'
#         recipient_list = [instance.customer_email]
#         send_mail(subject, message, from_email, recipient_list)
