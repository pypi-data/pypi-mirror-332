from datetime import datetime, timedelta, date, time
from pathlib import Path

import click
import re

from ratisbona_shellutils.cli import blue_dosbox
from ratisbona_utils.datetime._datetime import try_parse_leading_isodate
from ratisbona_utils.io import errprint

from ratisbona_shellutils.calendar._gitlogging import get_git_log, find_git_root
from ratisbona_shellutils.calendar._google_calendar import (
    authenticate,
    list_calendars,
    list_events,
    start_datetime,
    get_color,
    format_event,
    search_by_date_and_summary_or_description_part,
    create_entry,
    spec_by_datetime,
    find_calendar_by_name,
    CalendarEvent, spec_by_date_and_maybe_time, spec_by_date,
)
from ratisbona_utils.colors import RGBColor
from ratisbona_utils.datetime import ensure_timezone
from ratisbona_utils.monads import Just, Maybe
from ratisbona_utils.terminals.vt100 import color_block


@click.group
def google_calendar_cli():
    errprint(blue_dosbox("Google Calendar Cli"))


@google_calendar_cli.command("list-calendars")
def list_calendars_cli():
    service = authenticate()
    calendars = list_calendars(service)
    if not calendars:
        print("No calendars found.")
        return

    calendars.sort(key=lambda x: x["summary"])

    for calendar in calendars:
        maybe_color = get_color(calendar)
        print(
            f"{maybe_color.bind(color_block).default_or_throw(' ')} - {calendar['summary']} - {calendar['id']}"
        )


@google_calendar_cli.command("list-events")
@click.option("time_min", "-m", type=click.DateTime(), required=True)
@click.option("time_max", "-M", type=click.DateTime(), required=True)
def list_events_cli(time_min: datetime, time_max: datetime):

    time_min, time_max = map(ensure_timezone, (time_min, time_max))
    service = authenticate()
    calendars = list_calendars(service)
    if not calendars:
        print("No calendars found.")
        return

    events = []
    colors = {}
    for calendar in calendars:
        maybe_color = get_color(calendar)
        new_events = list_events(
            service, time_min, time_max, calendar["id"], max_results=10
        )
        if maybe_color:
            for event in new_events:
                colors[event["id"]] = maybe_color.unwrap_value()
        events.extend(new_events)

    def map_based_color_provider(event: CalendarEvent) -> Maybe[RGBColor]:
        return Just(colors)[event["id"]]

    def start_datetime_or_begin_of_time(event: CalendarEvent) -> datetime:
        return start_datetime(event).default_or_throw(datetime.min)

    events.sort(key=start_datetime_or_begin_of_time)

    for event in events:
        print(format_event(event, colorprovider=map_based_color_provider))


class PureDateParamType(click.ParamType):
    name = "date"

    def convert(self, value, param, ctx):
        try:
            return datetime.strptime(value, "%Y-%m-%d").date()
        except ValueError:
            self.fail(f"{value} is not a valid date", param, ctx)


class PureTimeParamType(click.ParamType):
    name = "time"

    def convert(self, value, param, ctx):
        try:
            return datetime.strptime(value, "%H:%M").time()
        except ValueError:
            self.fail(f"{value} is not a valid time", param, ctx)


@google_calendar_cli.command("entry")
@click.option("--calendar_name", "-c", type=str, required=True)
@click.option("--summary", "-u", type=str, required=True)
@click.option("--start-date", "-S", type=PureDateParamType(), required=True)
@click.option("--end-date", "-E", type=PureDateParamType(), default=None)
@click.option("--start-time", "-s", type=PureTimeParamType(), default=None)
@click.option("--end-time", "-e", type=PureTimeParamType(), default=None)
@click.option("--description", "-d", type=str, default=None)
def entry_cli(
    calendar_name: str,
    summary: str,
    start_date: date,
    end_date: date,
    start_time: time,
    end_time: time,
    description: str,
):
    service = authenticate()

    maybe_calendar = find_calendar_by_name(calendar_name, service=service)
    maybe_calendar_id = maybe_calendar["id"]
    if not maybe_calendar_id:
        print(
            f"Calendar {calendar_name} not found. Maybe use list_calendars to find the correct name."
        )
        return
    calendar_id = maybe_calendar_id.unwrap_value()
    color = maybe_calendar.bind(get_color).default_or_throw(RGBColor((255, 255, 255)))

    if not end_date:
        end_date = start_date

    if start_time and not end_time:
        end_time = start_time + timedelta(hours=1)

    if not description:
        description = summary

    start_spec = spec_by_date_and_maybe_time(start_date, start_time)
    end_spec = spec_by_date_and_maybe_time(end_date, end_time)

    event = create_entry(summary, start_spec, end_spec, description=Just(description))

    print(format_event(event, colorprovider=lambda _: color))

    print(service.events().insert(calendarId=calendar_id, body=event).execute())


@google_calendar_cli.command("sync-gitlog")
@click.option(
    "repo_path", "-r", type=click.Path(exists=True, path_type=Path), required=True
)
@click.option("wet_run", "-w", is_flag=True, default=False)
@click.option("calendar_name", "-c", type=str, required=True)
def sync_gitlog_cli(repo_path: Path, wet_run: bool, calendar_name: str):
    service = authenticate()

    maybe_calendar = find_calendar_by_name(calendar_name, service=service)
    maybe_calendar_id = maybe_calendar["id"]
    if not maybe_calendar_id:
        print(
            f"Calendar {calendar_name} not found. Maybe use list_calendars to find the correct name."
        )
        return
    calendar_id = maybe_calendar_id.unwrap_value()
    maybe_color = maybe_calendar.bind(get_color)

    real_repo_path = find_git_root(repo_path)
    if not real_repo_path:
        print(
            f"No Git repository found in {repo_path}. Try something that contains a .git folder!"
        )
        return

    log_entries = get_git_log(real_repo_path.unwrap_value(), max_entries=10_000)
    if len(log_entries) == 0:
        print(f"No log entries found in {repo_path}.")
        return

    def no_matter_what_color_provider(_: CalendarEvent) -> Maybe[RGBColor]:
        return maybe_color

    for log_entry in log_entries:
        maybe_event = search_by_date_and_summary_or_description_part(
            service=service,
            calendar_id=calendar_id,
            search_text=log_entry.commit_hash,
            start=log_entry.the_datetime,
            timedelta_hours_plusminus=48,
            search_description=True,
            max_results=1000,
        )
        if maybe_event:
            print(f"\n\nEvent already exists for {log_entry.the_datetime}: ")
            print(
                format_event(
                    maybe_event.unwrap_value(), colorprovider=no_matter_what_color_provider
                )
            )
            continue

        event = create_entry(
            "["
            + real_repo_path.unwrap_value().name
            + "] "
            + log_entry.message.split("\n")[0],
            spec_by_datetime(log_entry.the_datetime),
            spec_by_datetime(log_entry.the_datetime + timedelta(hours=1)),
            description=Just(log_entry.commit_hash + "\n\n" + log_entry.message),
        )
        if not wet_run:
            print(f"\n\nWould create event for {log_entry.the_datetime}:")
            print(format_event(event, colorprovider=no_matter_what_color_provider))
            continue

        print(f"\n\nCreating event for {log_entry.the_datetime}:")
        print(format_event(event, colorprovider=no_matter_what_color_provider))

        service.events().insert(calendarId=calendar_id, body=event).execute()






@google_calendar_cli.command("sync-files")
@click.option("wet_run", "-w", is_flag=True, default=False)
@click.option("calendar_name", "-c", type=str, required=True)
@click.argument("filepaths", nargs=-1, type=click.Path(path_type=Path))
def sync_file_listings(filepaths: list[Path], wet_run: bool, calendar_name: str):
    service = authenticate()

    maybe_calendar = find_calendar_by_name(calendar_name, service=service)
    maybe_calendar_id = maybe_calendar["id"]
    if not maybe_calendar_id:
        print(
            f"Calendar {calendar_name} not found. Maybe use list_calendars to find the correct name."
        )
        return
    calendar_id = maybe_calendar_id.unwrap_value()
    maybe_color = maybe_calendar.bind(get_color)

    for filepath in filepaths:
        maybe_date_result = try_parse_leading_isodate(filepath.with_suffix("").name)
        if not maybe_date_result:
            print(f"Could not parse date from {filepath.name} -- ignored.")
            continue

        # Create a datetime object from the date
        the_date, the_rest = maybe_date_result.unwrap_value()
        the_rest = re.sub(r"^_-_", "", the_rest.strip())
        the_rest = re.sub(r"^_", "", the_rest)
        the_rest = re.sub(r".san$", "", the_rest)
        
        the_datetime = datetime.combine(the_date, time.min)
        the_summary = f"[File] {the_rest}"
        maybe_event = search_by_date_and_summary_or_description_part(
            service=service,
            calendar_id=calendar_id,
            search_text=the_summary,
            start=the_datetime,
            timedelta_hours_plusminus=24,
            search_description=False,
            max_results=1000,
        )
        if maybe_event:
            print(f"\n\nEvent already exists for {filepath.name}: ")
            print(
                format_event(
                    maybe_event.unwrap_value(), colorprovider=lambda _: maybe_color
                    
                )
            )
            continue

        event = create_entry(
            the_summary,
            spec_by_date(the_date),
            spec_by_date(the_date),
            description=Just(f"Filepath: {filepath}"),
        )
        if not wet_run:
            print(f"\n\nWould create event for {filepath.name}:")
            print(format_event(event, colorprovider=lambda _: maybe_color))
            continue

        print(f"\n\nCreating event for {filepath.name}:")
        print(format_event(event, colorprovider=lambda _: maybe_color))

        service.events().insert(calendarId=calendar_id, body=event).execute()