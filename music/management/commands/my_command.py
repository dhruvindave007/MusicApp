from django.core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = 'Brief description of what this command does.'


    def add_arguments(self, parser):
        parser.add_argument(
            'sample_arg',
            type=str,
            help='A sample argument for demonstration purpose'
        )
    def handle(self, *args, **options):
        sample_arg_value=options['sample_arg']
        self.stdout.write(self.style.SUCCESS(f'Sample argument recived: {sample_arg_value}'))