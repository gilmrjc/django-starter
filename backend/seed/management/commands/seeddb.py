"""
Seed db command module.
"""
from django.db.utils import IntegrityError
from django.core.management.base import BaseCommand

from users.models import User
from seed.services import create_qa_data


class Command(BaseCommand):
    """
    Command to create seed data.
    """

    help = "Creates initial data for integration tests"  # noqa: A003
    requires_migrations_checks = True
    verbosity = 1

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear-db",
            action="store_true",
            help="Clear the database before running the seed.",
        )
        parser.add_argument(
            "--skip-admin",
            action="store_true",
            help="Skip admin user creation.",
        )
        parser.add_argument(
            "--skip-qa-data",
            action="store_true",
            help="Skip qa data creation.",
        )

    def handle(self, *args, **options):
        """
        Command execution.
        """
        self.verbosity = options["verbosity"]

        if options["clear_db"]:
            self.stdout.write(
                "Database is going to be cleared",
                self.style.WARNING,
            )

            # Delete all relevant objects.

            self.stdout.write(
                "Database cleared",
                self.style.WARNING,
            )

        if not options["skip_admin"]:
            self.create_admin()

        if not options["skip_qa_data"]:
            self.create_qa_data()

    def create_admin(self):
        """
        Create admin user.
        """
        try:
            admin = User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="password",
            )
            admin.emailaddress_set.create(
                email="admin@example.com",
                verified=True,
            )

            self.stdout.write("- Admin user created")
        except IntegrityError:
            self.stdout.write(
                "Admin user already exists",
                self.style.WARNING,
            )

    def create_qa_data(self):
        """
        Create QA data. This data is used in the e2e testing.
        """
        create_qa_data()
        self.stdout.write("- QA data created")
