# coding: utf-8
from django.core.management import BaseCommand
from django.contrib.auth.models import User
from collections import Counter


class Command(BaseCommand):
    help = u'Read tasks and determine its users'

    def add_arguments(self, parser):
        return parser.add_argument('--top', dest='number',
                                   type=int, default=25)

    def handle(self, *args, **options):
        data = {}
        data2 = []
        data3 = []
        for u in User.objects.all():
            for t in u.tasks.all():
                data2.append(u.username)
                if u == t.owner:
                    if t.owner.username not in data.keys():
                        data[t.owner.username] = {'counter': 0, 'completed': 0, 'false': 0}
                    else:
                        data[t.owner.username]['counter'] += 1
                        if t.is_completed:
                            data[t.owner.username]['completed'] += 1
                        else:
                            data[t.owner.username]['false'] += 1
        data2 = Counter(data2).most_common(options['number'])
        for i in range(len(data2)):
            for u2 in data.keys():
                if data2[i][0] == u2:
                    print(f'Пользователь {u2} создал {data[u2]["counter"]} задач,'
                          f' из которых выполнил {data[u2]["completed"]}')
