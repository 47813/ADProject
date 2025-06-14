from django.core.management.base import BaseCommand
from library.models import Video, BorrowHistory
from django.contrib.auth.models import User
from faker import Faker
import random
from datetime import timedelta, timezone

class Command(BaseCommand):
    help = '랜덤 비디오 대출 이력을 생성합니다.'

    def add_arguments(self, parser):
        parser.add_argument('--total', type=int, default=50, help='생성할 대출 기록 수')

    def handle(self, *args, **options):
        fake = Faker()
        videos = list(Video.objects.all())
        users = list(User.objects.all())
        total = options['total']

        if not videos or not users:
            self.stdout.write(self.style.ERROR("❌ 비디오와 사용자 데이터가 필요합니다."))
            return

        for _ in range(total):
            video = random.choice(videos)
            user = random.choice(users)
            borrowed_at = fake.date_time_between(start_date='-1y', end_date='now', tzinfo=timezone.utc)
            returned = random.choice([True, False])
            returned_at = borrowed_at + timedelta(days=random.randint(1, 30)) if returned else None

            BorrowHistory.objects.create(
                video=video,
                user=user,
                borrowed_at=borrowed_at,
                returned_at=returned_at
            )

        self.stdout.write(self.style.SUCCESS(f"✅ 비디오 대출 기록 {total}개 생성 완료!"))