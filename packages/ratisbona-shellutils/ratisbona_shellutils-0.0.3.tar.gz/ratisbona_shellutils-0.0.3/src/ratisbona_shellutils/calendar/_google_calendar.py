import pickle
from datetime import datetime, date, timedelta, time
from pathlib import Path
from typing import Any, Optional

from google.auth.exceptions import RefreshError
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from ratisbona_utils.colors import RGBColor, hex_to_rgb
from ratisbona_utils.datetime import to_datetime, ensure_timezone, ensure_no_timezone
from ratisbona_utils.functional import Function
from ratisbona_utils.monads import Just, Nothing, Maybe
from ratisbona_utils.strings import indent, wrap_text
from ratisbona_utils.terminals.vt100 import color_block

# https://console.cloud.google.com/workspace-api/credentials?inv=1&invt=AbnYUA&project=calclient

# Define the scope for Google Calendar API
SCOPES = ["https://www.googleapis.com/auth/calendar"]
TOKEN_DIR = Path.home() / ".local" / "ratisbona_calendar"
TOKEN_FILE = TOKEN_DIR / "token.pickle"
CREDENTIALS_FILE = TOKEN_DIR / "credentials.json"  # Place your credentials.json here

# Type aliases
CalendarService = Any
CalendarEvent = dict
Calendar = dict
DateSpec = dict
DateTimeSpec = dict
EventId = str


def authenticate() -> CalendarService:
    """
    Authenticates the user with Google OAuth 2.0 and returns a service object to interact with Google Calendar API.
    Tokens are saved in TOKEN_DIR.
    """
    creds = None

    # Ensure the token directory exists
    TOKEN_DIR.mkdir(parents=True, exist_ok=True)

    if not CREDENTIALS_FILE.exists():
        raise FileNotFoundError(f"Credentials file not found: {CREDENTIALS_FILE}")

    # Load existing token if available
    if TOKEN_FILE.exists():
        with TOKEN_FILE.open("rb") as token:
            creds = pickle.load(token)

    # Refresh or generate a new token if necessary
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except RefreshError as error:
                print(f"Cannot refresh token: {error}")
                flow = InstalledAppFlow.from_client_secrets_file(
                    str(CREDENTIALS_FILE), SCOPES
                )
                creds = flow.run_local_server(port=0)
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(CREDENTIALS_FILE), SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save the new token
        with TOKEN_FILE.open("wb") as token:
            pickle.dump(creds, token)

    return build("calendar", "v3", credentials=creds)


def list_calendars(service: CalendarService) -> list[Calendar]:
    """
    Lists all available calendars.
    """
    calendars = service.calendarList().list().execute().get("items", [])
    return calendars


def find_calendar_by_name(name: str, *, service: CalendarService) -> Maybe[Calendar]:
    """
    Finds a calendar by its name.
    """
    calendars = list_calendars(service)
    for calendar in calendars:
        if name in Just(calendar)["summary"].default_also_on_error(""):
            return Just(calendar)

    return Nothing


def as_datetime(event: CalendarEvent, key: str) -> Maybe[datetime]:
    """
    Converts a datetime string from an event to a datetime object.
    """
    maybe_field = Just(event)[key]
    # maybe_datetime = maybe_field["dateTime"].bind(datetime.fromisoformat) or (
    #    maybe_field["date"].bind(date.fromisoformat).bind(to_datetime)
    # )
    maybe_datetime = (
        maybe_field["dateTime"].bind(datetime.fromisoformat)
        or maybe_field["date"].bind(date.fromisoformat).bind(to_datetime)
        or maybe_field.bind(datetime.fromisoformat)
        or (maybe_field.bind(date.fromisoformat).bind(to_datetime))
    )

    maybe_datetime = maybe_datetime.bind(ensure_timezone)
    maybe_datetime.maybe_warn("Invalid datetime format!")
    return maybe_datetime


def start_datetime(event: CalendarEvent) -> Maybe[datetime]:
    return as_datetime(event, "start")


def end_datetime(event: CalendarEvent) -> Maybe[datetime]:
    return as_datetime(event, "end")


def list_events(
    service: CalendarService,
    time_min: datetime,
    time_max: datetime,
    calendar_id="primary",
    max_results=100,
) -> list[CalendarEvent]:
    """
    Lists upcoming events from the specified calendar.
    """
    time_min = ensure_timezone(time_min)
    time_max = ensure_timezone(time_max)

    events_result = (
        service.events()
        .list(
            calendarId=calendar_id,
            maxResults=max_results,
            timeMin=time_min.isoformat(),
            timeMax=time_max.isoformat(),
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    events = Just(events_result)["items"]

    if not events:
        return []

    return sorted(
        events.unwrap_value(),
        key=lambda x: start_datetime(x).default_also_on_error(datetime.min),
    )


def insert_event(service: CalendarService, event: CalendarEvent, calendar_id="primary"):
    """
    Inserts an event into the specified calendar.
    :param service: Google Calendar API service object.
    :param event: Event details as a dictionary.
    :param calendar_id: The calendar ID where the event will be inserted.
    :return: The created event.
    """
    created_event = (
        service.events().insert(calendarId=calendar_id, body=event).execute()
    )
    print(f"Event created: {created_event.get('htmlLink')}")
    return created_event


def get_color(calendar: Calendar) -> Maybe[RGBColor]:
    return Just(calendar)["backgroundColor"].bind(hex_to_rgb)


def search_by_date_and_summary_or_description_part(
    calendar_id: str,
    search_text: str,
    start: datetime,
    *,
    service: CalendarService,
    max_results=1000,
    search_description=True,
    timedelta_hours_plusminus=2,
) -> Maybe[CalendarEvent]:
    min_time = start - timedelta(hours=timedelta_hours_plusminus)
    max_time = start + timedelta(hours=timedelta_hours_plusminus)

    events = list_events(
        service, min_time, max_time, calendar_id, max_results=max_results
    )
    for event in events:
        just_event = Just(event)
        if search_text in just_event["summary"].default_also_on_error(""):
            return just_event
        if search_description and search_text in just_event[
            "description"
        ].default_also_on_error(""):
            return just_event
    return Nothing


def spec_by_date(theDate: date) -> DateSpec:
    return {"date": theDate.isoformat()}


def spec_by_datetime(the_datetime: datetime) -> DateTimeSpec:
    return {
        "dateTime": ensure_no_timezone(the_datetime).isoformat(),
        "timeZone": "Europe/Amsterdam",
    }

def spec_by_date_and_maybe_time(the_date: date, maybe_time: Optional[time]) -> DateSpec | DateTimeSpec:
    if maybe_time:
        return spec_by_datetime(datetime.combine(the_date, maybe_time))
    return spec_by_date(the_date)


def create_entry(
    summary: str,
    start_spec: DateSpec | DateTimeSpec,
    end_spec: DateSpec | DateTimeSpec,
    description: Maybe[str] = Nothing,
):
    body = {"summary": summary, "start": start_spec, "end": end_spec}
    if description:
        body["description"] = description.unwrap_value()
    return body


def nothing_color_function(_: CalendarEvent) -> Maybe[RGBColor]:
    return Nothing


def format_event(
    event: CalendarEvent,
    *,
    colorprovider: Function[CalendarEvent, Maybe[RGBColor]] = nothing_color_function,
) -> str:
    just_event = Just(event)
    colorblockfield = (
        just_event.bind(colorprovider).bind(color_block).default_or_throw(" ")
    )

    print(start_datetime(event))

    start_datetime_field = (
        start_datetime(event)
        .bind(ensure_no_timezone)
        .bind(datetime.strftime, "%Y-%m-%d %H:%M")
        .default_or_throw("-" * 15)
    )
    end_datetime_field = (
        end_datetime(event)
        .bind(ensure_no_timezone)
        .bind(datetime.strftime, "%Y-%m-%d %H:%M")
        .default_or_throw("-" * 15)
    )
    maybe_description = just_event["description"]
    maybe_summary = just_event["summary"]
    maybe_link = just_event["htmlLink"]

    result_text = f"{colorblockfield}{start_datetime_field} - {end_datetime_field}: {maybe_summary.default_or_throw('')}"

    def indent_properly(text: str) -> str:
        return indent(text, 4)

    def wrap_properly(text: str) -> str:
        return wrap_text(text, 76)

    def prepend_newline(text: str) -> str:
        return f"\n{text}"

    result_text += (
        maybe_description.bind(wrap_properly)
        .bind(indent_properly)
        .bind(prepend_newline)
        .default_or_throw("")
    )
    result_text += (
        maybe_link.bind(indent_properly).bind(prepend_newline).default_or_throw("")
    )
    return result_text


if __name__ == "__main__":
    # Authenticate and build the service
    calendar_service = authenticate()

    # Example usage: List upcoming events
    print("Upcoming events:")
    events = list_events(
        calendar_service, datetime.now(), datetime.now() + timedelta(days=30)
    )
    for event in events:
        print(
            f"{start_datetime(event).default_or_throw('-' * 25)}"
            f"_-_{end_datetime(event).default_or_throw('-' * 25)}"
            f" - {Just(event)['summary'].default_or_throw('-- no summary --')}"
        )

    # Example usage: Insert a new event
    new_event = {
        "summary": "Sample Event",
        "location": "123 Main St, Anytown, USA",
        "description": "A test event.",
        "start": {
            "dateTime": "2025-01-25T10:00:00-05:00",
            "timeZone": "America/New_York",
        },
        "end": {
            "dateTime": "2025-01-25T11:00:00-05:00",
            "timeZone": "America/New_York",
        },
        "attendees": [
            {"email": "example@example.com"},
        ],
    }

    print("Inserting new event:")
    # insert_event(calendar_service, new_event)
