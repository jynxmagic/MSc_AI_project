class TaskTemplate:
    def __init__(self) -> None:
        return

    
    def listener_callback(self, msg) -> None:
        msg.data = msg.data.strip()
        if msg.data in [*self.get_task_list().keys()]:
            self.get_task_list()[msg.data]()
        else:
            print("Couldn't find task ", msg.data)
        return

    def get_task_list() -> dict:
        return {}