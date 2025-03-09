import html
import weakref
import threading
import ipywidgets
import collections

from IPython.display import display


def collect_results(items):
    """ collect items from iterable inside a separate thread """
    results = collections.deque()
    cancelled = threading.Event()
    proxy = weakref.proxy(results)

    output = ipywidgets.HTML()
    cancel = ipywidgets.Button(description="Cancel")
    widgets = ipywidgets.VBox([cancel, output])
    display(widgets)

    def update_output(text):
        output.value = "<pre>%s</pre>" % html.escape(text)

    def cancel_widget(b):
        update_output("Cancelling ...")
        cancelled.set()

    cancel.on_click(cancel_widget)

    def process_items():
        count = 0
        try:
            for item in items:
                update_output("Running (%d)" % count)

                if item is not None:
                    proxy.append(item)
                    count += 1

                if cancelled.is_set():
                    update_output("Cancelled (%d)" % count)
                    break
            else:
                update_output("Completed (%d)" % count)

        except ReferenceError:
            update_output("Stopped (%d)" % count)

    threading.Thread(target=process_items).start()

    return results
