import json
import os
from datetime import datetime, timedelta
from config import MEMORY_PATH

SCHEDULE_PATH = os.path.join(
    os.path.dirname(MEMORY_PATH),
    "schedule.json"
)


def load_schedule():

    if not os.path.exists(SCHEDULE_PATH):
        return []

    try:

        with open(SCHEDULE_PATH, "r") as f:
            return json.load(f)

    except:

        return []


def save_schedule(schedule):

    os.makedirs(
        os.path.dirname(SCHEDULE_PATH),
        exist_ok=True
    )

    with open(SCHEDULE_PATH, "w") as f:
        json.dump(schedule, f, indent=2)


def add_reminder(
    task: str,
    delay_minutes: int = 0,
    delay_hours: int = 0
) -> str:

    schedule = load_schedule()

    now = datetime.now()

    due_time = now + timedelta(
        minutes=delay_minutes,
        hours=delay_hours
    )

    schedule.append({
        "task": task,
        "due_time": due_time.isoformat(),
        "created": now.isoformat(),
        "completed": False
    })

    save_schedule(schedule)

    return f"Reminder set for {due_time.strftime('%I:%M %p')}"


def check_reminders() -> list:

    schedule = load_schedule()

    now = datetime.now()

    due_tasks = []

    updated_schedule = []

    for item in schedule:

        due_time = datetime.fromisoformat(
            item["due_time"]
        )

        if not item["completed"] and now >= due_time:

            due_tasks.append(item["task"])

            item["completed"] = True

        if not item["completed"]:

            updated_schedule.append(item)

    save_schedule(updated_schedule)

    return due_tasks


def list_reminders() -> str:

    schedule = load_schedule()

    if not schedule:

        return "No reminders set."

    active = [
        s for s in schedule
        if not s["completed"]
    ]

    if not active:

        return "No active reminders."

    result = "Active reminders:\n"

    for i, item in enumerate(active, 1):

        due = datetime.fromisoformat(
            item["due_time"]
        )

        result += f"{i}. {item['task']} - Due: {due.strftime('%I:%M %p')}\n"

    return result.strip()
