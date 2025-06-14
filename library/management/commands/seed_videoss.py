from django.core.management.base import BaseCommand
from library.models import Video
from faker import Faker

class Command(BaseCommand):
    help = 'Generate random videos'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for i in range(30):
            Video.objects.create(
                title=f"{fake.word().title()} Video {i+1}",
                author=fake.name(),
                isbn=f"{fake.random_number(digits=13)}"
            )
        self.stdout.write(self.style.SUCCESS("✅ 30개의 비디오 생성 완료!"))