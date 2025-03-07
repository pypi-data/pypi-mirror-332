class NoCreationError(AttributeError):
    pass

def confirm_lax(auto_true=None, auto_false=None, start="Do you allow", center="", end="? (Enter, y, Y):", possible_yes=("", "y", "Y")):
  if opt.yes_always is True:
   if callable(auto_true): auto_true()
   return True
  print (start, center, end, end=" ")
  answer = input()
  if answer in possible_yes:
   if callable(auto_true): auto_true()
   return True
  else:
   if callable(auto_false): auto_false()
   return False
  print ("#: {type(cmd)} is discarded.")
# May have to refine this one...
def confirm_firm(auto_true=None, auto_false=None, start="Do you allow", center="", end="?", strongly_yes=("y", "Y")):
  answer = input()
  if opt.yes_always is True: return True
  if answer in strongly_yes:
   if callable(auto_true): auto_true()
   return True
  else:
   if callable(auto_false): auto_false()
   return False
# confirmations done for

def serialize_clean(x):
  if isinstance(x, (str, bool)):
    return x
  if isinstance(x, (tuple, list)):
    return [serialize_clean(y) for y in x ]
  return x.__serialize__()
  assert False, type(x)

def prioritize(value):
  def describe(self):
    self.__priority__ = value
    return self
  return describe
weak = prioritize(False)
strong = prioritize(True)

def resolve(A, B, **methods):
    body = {}
    for key, value in methods.items():
        a = getattr(A, key)
        b = getattr(B, key)
        if hasattr(a, '__priority__') and hasattr(b, '__priority__'):
            if a.__priority__ and not b.__priority__:
              body[key] = a
            elif not a.__priority__ and b.__priority__:
              body[key] = b
            elif a is b:
              body[key] = a
            else: assert False, (A, B, key)
        elif hasattr(a, '__priority__'):
            body[key] = a if a.__priority__ else b
        elif hasattr(b, '__priority__'):
            body[key] = b if b.__priority__ else a
        else: assert False, (A, B, key)        
    return body

def log(*args, **kwargs):
    from startup import options
    if options.debug:
        return print(*args, **kwargs)

def choose(args, default=ValueError("Choose require a least one arg.")):
    from random import choice
    if len(args) == 0:
        if isinstance(default, Exception):
            raise default
        return default
    elif len(args) > 1:
        return choice(args)
    else:
        return args[0]

def create_reflector(res):
  from threading import Thread
  from watchdog.events import FileSystemEventHandler
  from watchdog.observers import Observer
  from time import sleep
  
  class Reflector(FileSystemEventHandler):
    def __init__(self):
      super().__init__()
      self.active = True
      self.events = []
      self.calls = []
    
    def dispatch(self, event):
      self.events.append(event)

    def start(self):
      self.thread = Thread(target=self.loop, daemon=True)
      self.thread.start()

    def stop(self):
      assert self.active
      self.active = False

    def tick(self):
      sleep(0.1)
      return True

    def loop(self):
      self.guard = Observer()
      self.guard.schedule(self, res.__path__, recursive=True)
      self.guard.start()
      try:
        while self.active:
          self.active = self.tick()
      except KeyboardInterrupt:
        self.guard.stop()
      self.guard.join()

    def __call__(self, fun):
      return self.at()(fun)
    def at(self, **kwargs):
      def __reflector_descriptor__(fun):
        if len(kwargs) == 0:
          self.calls.append(fun)
        else:
          self.calls.append(({
            k: v for k, v in kwargs.items() if v != None
          }, fun))
        # register function
        return fun
      return __reflector_descriptor__

    def __next__(self):
      if len(self.events):
        event = self.events.pop()
        for call in self.calls:
          if isinstance(call, tuple) and len(call) == 2:
            for k, v in call[0].items():
              if not res.__test__(k, v, event):
                break
            else:
              call[1](event)
          else:
            call(event)
        return event
      else:
        return None

    def __iter__(self):
      from time import sleep
      try:
       while self.active:
        n = next(self)
        if n is None:
          sleep(0.1)
        else:
          yield n
      except KeyboardInterrupt:
        pass

  reflector = Reflector()
  reflector.start()

  # create_reflector
  return reflector
