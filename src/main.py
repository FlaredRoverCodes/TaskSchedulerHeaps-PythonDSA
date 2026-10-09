from task_scheduler import TaskScheduler


if __name__ == "__main__":
    scheduler = TaskScheduler()

    scheduler.add_task(
        "Write report",
        1,
        10,
        3
    )

    scheduler.add_task(
        "Email client",
        2,
        5,
        1
    )

    scheduler.add_task(
        "Team meeting",
        3,
        8,
        2
    )

    scheduler.add_task(
        "Design review",
        1,
        7,
        4
    )

    # Assume current time is 0 hours
    print(
        "Scheduled Tasks:",
        [
            task.name
            for task in scheduler.schedule_tasks(0)
        ]
    )

    scheduler.complete_task("Email client")

    print(
        "Scheduled Tasks after completing 'Email client':",
        [
            task.name
            for task in scheduler.schedule_tasks(0)
        ]
    )

    scheduler.change_priority(
        "Team meeting",
        0
    )

    print(
        "Scheduled Tasks after changing 'Team meeting' priority:",
        [
            task.name
            for task in scheduler.schedule_tasks(0)
        ]
    )