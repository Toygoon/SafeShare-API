from django.core.management import BaseCommand

from api.models import RiskFactor


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
