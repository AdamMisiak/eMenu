import logging

from celery.decorators import periodic_task
from celery.schedules import crontab
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models import Q
from django.utils.timezone import datetime, now
from menus.models import Dish

User = get_user_model()
logger = logging.getLogger(__name__)


def send_mail_with_dishes(user, subject, message):
    send_mail(
        subject=subject, message=message, from_email="emenu@emenu.dev", recipient_list=[user.email], fail_silently=False
    )
    logger.error("Email to user {} has been send".format(user))


@periodic_task(run_every=(crontab(minute=0, hour=10)), name="send_mail_with_new_dishes", ignore_result=True)
def prepare_mail_with_new_dishes():
    yesterday = "{}-{}-{}".format(now().day - 1, now().month, now().year)
    subject = "Dishes created or edited in {}".format(yesterday)
    message = """
        Dishes created or edited in {}: \n
        --------------------------------------- \n
    """.format(
        yesterday
    )

    dishes_from_yesterday = Dish.objects.filter(
        Q(created__date=datetime(now().year, now().month, now().day - 1))
        | Q(modified__date=datetime(now().year, now().month, now().day - 1))
    )
    active_users = User.objects.filter(is_active=True)
    if dishes_from_yesterday:
        for dish in dishes_from_yesterday:
            message += """
                NAME: {} \n
                DESCRIPTION: {} \n
                PRICE: {} PLN\n
                VEGAN: {} \n
                ADDED TO MENU: {} \n
                --------------------------------------- \n
            """.format(
                dish.name, dish.description, dish.price, dish.vegan, dish.menu.name
            )
    else:
        message += """
            There are no new dishes :( \n
            We will send you another mail tomorrow! \n
        """

    for user in active_users:
        send_mail_with_dishes(user, subject, message)
