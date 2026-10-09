import heapq
from task import Task


class TaskScheduler:
    def __init__(self):
        self.heap = []
        self.index = 0

    def add_task(self, name, priority, deadline, duration):
        task = Task(name, priority, deadline, duration)

        # Store task in the min-heap.
        # Lower priority value means higher priority.
        heapq.heappush(
            self.heap,
            (priority, self.index, task)
        )

        self.index += 1

    def schedule_tasks(self, current_time):
        scheduled_tasks = []

        # Make a copy so scheduling does not remove
        # tasks from the original heap.
        temp_heap = self.heap.copy()
        heapq.heapify(temp_heap)

        while temp_heap:
            priority, index, task = heapq.heappop(temp_heap)

            # Check whether the task can be completed
            # before or exactly at its deadline.
            if current_time + task.duration <= task.deadline:
                scheduled_tasks.append(task)

        return scheduled_tasks

    def complete_task(self, name):
        new_heap = []

        # Remove the task with the matching name.
        for priority, index, task in self.heap:
            if task.name != name:
                new_heap.append(
                    (priority, index, task)
                )

        self.heap = new_heap

        # Restore the min-heap property.
        heapq.heapify(self.heap)

    def change_priority(self, name, new_priority):
        task_to_update = None

        # Find the task.
        for priority, index, task in self.heap:
            if task.name == name:
                task_to_update = task
                break

        if task_to_update is None:
            return

        # Remove the task from the heap first.
        new_heap = []

        for priority, index, task in self.heap:
            if task.name != name:
                new_heap.append(
                    (priority, index, task)
                )

        self.heap = new_heap
        heapq.heapify(self.heap)

        # Change its priority.
        task_to_update.priority = new_priority

        # Reinsert it so the heap property is maintained.
        heapq.heappush(
            self.heap,
            (
                task_to_update.priority,
                self.index,
                task_to_update
            )
        )

        self.index += 1