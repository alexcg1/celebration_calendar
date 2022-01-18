from pprint import pprint
import pretty_errors
import wikipediaapi
import sys
from datetime import datetime, timedelta
from progress.bar import Bar

MAX_DAYS = 2
USE_CACHED = True # Use pickle file if already exists


def print_dir(object):
    print(dir(object))


start_date = datetime(year=2022, month=1, day=1)
total_days = 365

date_list = [(start_date + timedelta(days=day)) for day in range(total_days)]
date_list = [date.strftime("%B %-d") for date in date_list][:MAX_DAYS]


def get_events(date, level=0, has_wiki_page=True):
    page = wiki_wiki.page(date)
    event_dict = {"date": date, "events": [], "url": page.fullurl}
    for section in page.sections:
        if "holidays and observances" in section.title.lower():
            events = section.text.split("\n")
            for event in events:
                event_data = process_event(event)
                if event_data:
                    event_dict["events"].append(event_data)

    return event_dict

def process_event(event_text, has_wiki_page=True):
    # Implement events without wiki page later
    page = wiki_wiki.page(event_text)
    if page.exists():
        event_data = {"title": event_text, "url": page.fullurl}

        return event_data


wiki_wiki = wikipediaapi.Wikipedia("en")


all_events = []
for date in Bar(f"Getting events").iter(date_list):
    events = get_events(date)
    all_events.append(events)

pprint(all_events)
