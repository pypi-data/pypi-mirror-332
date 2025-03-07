import threading


class Thread(threading.Thread):
    def __init__(
        self,
        abort_event: threading.Event | None = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        if abort_event:
            self._abort_event = abort_event
            self._abort_event_internal = False
        else:
            self._abort_event = threading.Event()
            self._abort_event_internal = True

    def abort(self):
        if self._abort_event_internal:
            self._abort_event.set()
        else:
            raise RuntimeError("abort event is externally managed")

    def is_aborted(self):
        return self._abort_event.is_set()
