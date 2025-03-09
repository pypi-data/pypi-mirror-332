**observerutil** is simple and powerful observer pattern tool.

## How to install
You could install from PyPi:
```bash
$ python3 -m pip install observerutil
```

Any callable can become observer

```python
from typing import Any
from observerutil import Observers

def func_a():
    ...

def func_b():
    ...

observers = Observers([func_a])
observers.add(func_b)

observers.notify()
```

It is possible to provide any args and kwargs to observer
```python
from typing import Any
from observerutil import Observers

def func_a(message: int):
    ...

observers = Observers()
observers.add(func_a)

# Distribute message to func_a.
# Any exceptions will be ignored.
message = 0
observers.notify(message)
```

```python
from typing import Any
from observerutil import Observers

def func_a(**kwargs):
    ...

observers = Observers()
observers.add(func_a)

# Distribute kwargs to func_a.
# Any exceptions will be ignored.
observers.notify(user_id=123, role='client')
```
But in this case any exception will be ignored. 
If you would like to catch exceptions then use Observer with error handler.

```python
from typing import Any
from observerutil import Observer, Observers, ErrorHandler


def func_a(message: int):
    print(100 / message)


def write_exception_to_logs(exc: Exception):
    ...


observer = Observer(func_a, error_handler=write_exception_to_logs)
observers = Observers()
observers.add(func_a)

message = 0
observers.send_message(message)
```

If you would like to adapt message for observers in the collection then add message adapter
```python
from typing import Any
from observerutil import Observers


def func_a(message: int):
    print(100 / message)


# parameters_adapter has to implement IParametersAdapter interface
def convert_to_int(*args, **kwargs):
    # exception of adapter is not catched by Observers instance.
    # add try...except here by self if required.
    return [int(arg) for arg in args], kwargs


observers = Observers(parameters_adapter=convert_to_int)
observers.add(func_a)

message = '2'
observers.notify(message)
```

More elegant way to convert each arg
```python
from typing import Any
from observerutil import Observers, AdaptEachArg


def func_a(message: int):
    print(100 / message)

observers = Observers(parameters_adapter=AdaptEachArg(int))
observers.add(func_a)

message = '2'
observers.notify(message)
```
