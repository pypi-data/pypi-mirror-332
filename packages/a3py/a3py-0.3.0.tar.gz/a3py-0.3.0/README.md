# a3py

English | [简体中文](README_ZH.md)

`a3py` is a python toolkit.

## 1. Introduction

### Simplified

* Variable naming style conversion
* Date and time conversion
* Environment variables
* Hashlib

### Improved

* Faster json(with ujson)
* Readable

### Practical

* Dynamic
* SingletonMeta
* Signal

## 2. Usage

### Install

```shell script
pip install a3py

```

### Examples

```python
from datetime import date
from a3py.simplified.datetime import date2str
from a3py.improved.json import fast_dumps
from a3py.improved.readable import get_readable_size


if __name__ == "__main__":
    assert date2str(date(2019, 10, 3)) == "2019-10-03"
    assert fast_dumps([1, 2, 3]) == "[1,2,3]"
    assert get_readable_size(1024 * 1024) == "1.0MB"

```
