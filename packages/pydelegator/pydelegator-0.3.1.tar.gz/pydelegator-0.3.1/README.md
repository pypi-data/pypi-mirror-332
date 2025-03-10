# Quick guide

## 1. Install pydelegator
<h3>Past this in your console</h3>

```bash
pip install pydelegator
```


## 2. Create main delegator manager
```python 
from pydelegator.delegator_manager import DelegatorManager
main_delegator_manager = DelegatorManager() # it is your main manager
```

## 3. Create delegator
<h3>In your file where you create want to create new delegator</h3> 

```python
import <your file name> # you have to import only file but dont import copy of main_delegator_manager
your_file_name.main_delegator_manager.create_delegator(<delegator name>) 
```

## 4. Link a function to delegator
```python
def test_func(name: str, age: int):
    print(name, age)

import <your file name> # you have to import only file but dont import copy of main_delegator_manager

your_file_name.main_delegator_manager.link_func(<delegator name>, <your func>) # for exaple ("test_delegator", test_func) dont use () 
```

## 5. Call delegator
```python
import <your file name> # you have to import only file but dont import copy of main_delegator_manager

your_file_name.main_delegator_manager.call_delegator(<delegator name>, <params>) # for exaple ("test_delegator", ("Dmytro", 15, )) int tuple you can hand over args 
```