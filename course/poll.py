import subprocess
from pyquery import PyQuery as pq
from threading import Thread
from time import sleep
from course.models import Course
from bot.models import Bot


def scrape(course, bot):
    try:
        url = 'https://selfservice.mypurdue.purdue.edu/prod/bwckschd.p_disp_detail_sched?term_in=201920&crn_in=' + course.crn
        process = subprocess.run(['curl', url], stdout=subprocess.PIPE)
        out = process.stdout
        dom = pq(out)
        table = pq(dom.find('table.datadisplaytable')[1])
        available = int(pq(table('td')[3]).text())
        course.spots = available
        course.save()
        if course.spots > 0:
            bot.notify(course)
    except:
        print('Scraping error')


def check_and_notify():
    bot = Bot.objects.first()
    while True:
        for c in Course.objects.all():
            print('Checking', c.name)
            thread = Thread(target=scrape, args=(c, bot,))
            thread.start()
            thread.join()
            sleep(45)


def run():
    thread = Thread(target=check_and_notify)
    thread.start()
    thread.join()
