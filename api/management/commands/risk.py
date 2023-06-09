import random
from datetime import datetime, timedelta

from django.core.management import BaseCommand

from api.models import RiskFactor, RiskReport, LatLng, User


class Command(BaseCommand):
    def handle(self, *args, **options):
        do()

    help = 'Generate and save the pre-defined risk factors'


def do():
    # Make pre-defined records
    r = [RiskFactor(name='환자 발생', risk_level=2, risk_impact=30),
         RiskFactor(name='폭력 사태', risk_level=2, risk_impact=40),
         RiskFactor(name='화재', risk_level=3, risk_impact=50),
         RiskFactor(name='태풍', risk_level=4, risk_impact=70),
         RiskFactor(name='낙석', risk_level=5, risk_impact=80),
         RiskFactor(name='붕괴', risk_level=5, risk_impact=80)]

    # Check existence
    for i in range(len(r)):
        found = RiskFactor.objects.all().filter(name=r[i].name)

        if len(found) < 1:
            r[i].save()

            print(f'[{i + 1}/{len(r)}] Created database named "{r[i].name}"')

    # Make sample risk reports
    n = 10
    base = (35.8380000, 128.7120000)
    max = 0.0009999

    for i in range(n):
        latlng = LatLng(lat=random.uniform(base[0], base[0] + max), lng=random.uniform(base[1], base[1] + max))
        latlng.save()

        users = User.objects.all().filter(name='sample')
        if len(users) < 1:
            user = User(name='sample', user_id='sample', user_pw='sample')
            user.save()
        else:
            user = users.last()

        # Find random date
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 12, 31)

        random_hour = random.randint(0, 23)
        random_minute = random.randint(0, 59)
        random_second = random.randint(0, 59)

        random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))

        random_datetime = datetime(
            random_date.year, random_date.month, random_date.day,
            random_hour, random_minute, random_second
        )

        rr = RiskReport(title='sample title', summary='sample summary',
                        risk_factor=RiskFactor.objects.all().filter(name=random.choice(r).name).last(), latlng=latlng,
                        user=user, is_solved=random.choice([True, False]), reported_at=random_datetime)

        rr.save()
        print(f'[{i + 1}/{n}] Created database {rr.to_dict()}')
