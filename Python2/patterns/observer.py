# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "alex"
__date__ = "$May 14, 2015 1:49:41 AM$"


class Event(object):
    _observers = []

    def __init__(self, subject):
        self.subject = subject

    @classmethod
    def register(cls, observer):
        if observer not in cls._observers:
            cls._observers.append(observer) \

    @classmethod
    def unregister(self, cls, observer):
        if observer in cls._observers:
            self._observers.remove(observer)

    @classmethod
    def notify(cls, subject):
        event = cls(subject)
        for observer in cls._observers:
            observer(event)


class WriteEvent(Event):
    def __repr__(self):
        return 'WriteEvent'


class AnotherObserver(object):
    def __call__(self,event):
        print '%s told me' % event


def log(event):
    print '%s was written' % event.subject


WriteEvent.register(log)
WriteEvent.register(AnotherObserver())
WriteEvent.notify('a given file')