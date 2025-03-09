import weakref
import threading
import ipywidgets
import collections


from IPython.display import display


class Worker:
    def __init__(self):
        self.tasks = collections.deque()

    def submit(self, func, *args, **kwargs):
        task = (func, args, kwargs)
        self.tasks.append(task)

    def results(self):
        results = collections.deque()
        cancelled = threading.Event()
        proxy = weakref.proxy(results)

        progress = ipywidgets.FloatProgress(description="Progress")
        cancel = ipywidgets.Button(description="Cancel")
        widgets = ipywidgets.HBox([progress, cancel])

        task_count = len(self.tasks)

        def on_cancel(b):
            if len(self.tasks):
                cancel.disabled = True
                cancelled.set()

        cancel.on_click(on_cancel)

        def update_progress():
            if task_count > 0:
                task_done = task_count - len(self.tasks)
                value = 100 * task_done / task_count
                progress.value = value

        def execute_task(task):
            func, args, kwargs = task
            result = func(*args, **kwargs)
            proxy.append(result)
            update_progress()

        def execute_queue():
            while self.tasks:
                task = self.tasks.popleft()
                if cancelled.is_set():
                    progress.bar_style = "warning"
                    break
                try:
                    execute_task(task)
                except ReferenceError:
                    progress.bar_style = "warning"
                    break
                except Exception:
                    pass
            else:
                progress.bar_style = "success"
            cancel.disabled = True

        display(widgets)

        threading.Thread(target=execute_queue).start()

        return results

