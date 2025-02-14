# Observer Pattern

class Observer:
    def update(self, event, data):
        pass

class EventManager:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_type, listener):
        if event_type not in self.listeners:
            self.listeners[event_type] = []
        self.listeners[event_type].append(listener)

    def unsubscribe(self, event_type, listener):
        self.listeners[event_type].remove(listener)

    def notify(self, event_type, data):
        for listener in self.listeners.get(event_type, []):
            listener.update(event_type, data)

class UserObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, event, data):
        print(f'{self.name} received {event}: {data}')

# Usage
manager = EventManager()
user1 = UserObserver('Alice')
user2 = UserObserver('Bob')

manager.subscribe('login', user1)
manager.subscribe('login', user2)
manager.subscribe('logout', user1)

manager.notify('login', {'user': 'Saad'})
manager.notify('logout', {'user': 'Saad'})

