import argparse
from io import StringIO
from django.core.exceptions import ObjectDoesNotExist
from bot.models import Bot
from course.models import Course


class Parser(argparse.ArgumentParser):
    def __init__(self):
        super().__init__()
        self.function_map = {
            'ping': self.handle_ping,
            'list': self.handle_list,
            'help': self.handle_help,
            '--help': self.handle_help,
            'add': self.handle_add,
            'remove': self.handle_remove
        }

        self.bot = Bot.objects.first()

        self.add_argument('help', help="Show this help message")
        self.add_argument('ping', help="Ping the server")
        self.add_argument('list', help='List courses being watched')
        self.add_argument('add', help='Add course by CRN. Format: add <CRN> <course name>')
        self.add_argument('remove', help='Remove course by ID. Format: remove <course ID>')

    def parse_input(self, text):
        args = [t.lower() for t in text.split(' ') if t]

        if args[0] in self.function_map:
            self.function_map[args[0]](args)

    def handle_ping(self, *args):
        self.bot.send_message('pong')

    def handle_list(self, *args):
        if Course.objects.count() == 0:
            self.bot.send_message('No courses to show')
            return

        message = ''
        for c in Course.objects.all():
            message += "{0} Available: {1}\n".format(c, c.spots)
        self.bot.send_message(message)

    def handle_help(self, *args):
        message = StringIO()
        self.print_help(file=message)
        self.bot.send_message(message.getvalue())
        message.close()

    def handle_add(self, args):
        try:
            crn = args[1]
        except IndexError:
            self.bot.send_message('Please specify CRN')
            return

        if len(args[2:]) == 0:
            self.bot.send_message('Please specify course name')
            return

        name = ' '.join(args[2:])

        try:
            Course.objects.get(crn=crn)
            self.bot.send_message('Error: Duplicate CRN')
            return
        except ObjectDoesNotExist:
            c = Course(crn=crn, name=name)
            c.save()
            message = 'Added course: {0} - {1}'.format(c.crn, c.name)
            self.bot.send_message(message)

    def handle_remove(self, args):
        try:
            _id = args[1]
        except IndexError:
            self.bot.send_message('Please specify course ID')
            return

        try:
            int(_id)
        except ValueError:
            self.bot.send_message('Error: Invalid course ID')
            return

        try:
            c = Course.objects.get(pk=_id)
        except ObjectDoesNotExist:
            message = 'Course with id {0} does not exist'.format(_id)
            self.bot.send_message(message)
            return

        crn = c.crn
        name = c.name
        c.delete()
        message = 'Removed course: {0} - {1}'.format(crn, name)
        self.bot.send_message(message)
