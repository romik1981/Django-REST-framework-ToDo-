from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = "Create Superuser and some test users"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int)

    def handle(self, *args, **options):
        # удаляем всех пользователей
        User.objects.all().delete()
        user_count = options["count"]
        # создаём супер пользователя
        User.objects.create_superuser("admin", "belyakov1981@mail.ru", "12345")
        # создаём тестовых пользователей
        for i in range(user_count):
            User.objects.create_user(f"user_{i}", f"user_{i}@test.com", f"1234{1}")

        print("done!")
