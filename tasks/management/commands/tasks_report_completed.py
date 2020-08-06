# coding: utf-8
from django.core.management import BaseCommand
from datetime import datetime, timezone
from tasks.models import TodoItem


class Command(BaseCommand):
    help = u'Display completed tasks over last days'

    def add_arguments(self, parser):
        parser.add_argument('--days', dest='days_over',
                            type=int, default=5)

    def handle(self, *args, **options):
        now = datetime.now(timezone.utc)
        for task in TodoItem.objects.filter(is_completed=True):
            if (now - task.updated).days < options['days_over']:
                print(f'Задача {task}, выполненная {task.updated} была выполнена в течение'
                      f' последних {options["days_over"]} дней')
