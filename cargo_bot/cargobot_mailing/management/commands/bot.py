from django.core.management.base import BaseCommand
from django.conf import settings
from telegram import Bot
from telegram.utils.request import Request
from telegram.ext import Updater

class Command(BaseCommand):

    help = 'telegram bot'
    
    def handle(self, *args, **options):
        request = Request(
            connect_timeout=0.5,
            read_timeout=1.0,
            con_pool_size=8,
        )
        bot = Bot(
            request=request,
            token=settings.TOKEN
        )
        print(bot.get_me())

        updater = Updater(
            bot=bot,
            use_context=True
        )
        
        updater.start_polling()
        updater.idle()