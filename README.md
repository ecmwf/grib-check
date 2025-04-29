# GRIB Check

## Quick start

Install dependencies

 ``` bash
.python -m venv venv
source venv/bin/activate
pip install pandas eccodes
```

Add a new file called checker/Destiny.py
Derive the `Destiny` class from `Wmo`, to inherit the test pool.

``` python
from checker.Wmo import Wmo
from Assert import Le, Lt, Ne, Eq, Fail, IsIn, IsMultipleOf
from Report import Report

class Destiny(Wmo):
    def __init__( self, param_file=None, valueflg=False):
        super().__init__(param_file, valueflg=valueflg)

    def _point_in_time(self, message, p) -> Report:
        report = Report("Point In Time (Destiny)")
        report.add(IsultipleOf(message["step"], 3))

        return super()._basic_checks(message, p).add(report)
```
Add Destiny to available projects in GribCheck.py

``` python
...
...
from checker.Destiny import Destiny
...
      elif self.args.grib_type == "destiny":
          checker = Destiny(param_file=self.args.parameters, valueflg=self.args.valueflg)
...
    parser.add_argument("-t", "--grib_type", help="type of data to check", choices=["tigge", "s2s", "s2s_refcst", "uerra", "crra", "lam", "wmo", "destiny"], default="tigge")
...

```

Run the check

``` bash
python GribCheck.py -t destiny /path/to/file.grib2
```

## Grib

The Grib class is a wrapper around ecCodes.

### Message

A message is a wrapper around the ecCodes handle, with the key difference that it provides automatic memory management.

### KeyValue

TODO

#### Mathematical operations

## Check functions

A check takes a message and parameters as arguments and returns a report.
We can override checks from the base class simply by creating a new check with the same name.

``` python
    def check_overridden(self, message, p) -> Report:
        report = Report("Simple Check")
        return report
```

Sometimes, we want to extend tests defined in a base class.
In such cases, we override the function from the base class but retain the results produced by the original function.
One way to achieve this is by merging the reports and returning the combined result.

``` python
    def check_extended(self, message, p) -> Report:
        report = Report("Extended check")
        return super().check_extended(message, p).add(report)
```
### Report

A report serves as a container for various entities, such as assertions, informational messages, and nested reports.
Each report has a status, which is determined by the statuses of the entities it contains.
For example, if a single assertion fails, the report's status will be set to "fail" accordingly.
Reports can also be nested, and the same rules for status propagation apply to nested reports as well.

```python
        report = Report("Extended check")
        report.add(Ge(message['bitsPerValue'], 0))
```

### Assertion

An assertion verifies whether values meet the expected conditions.
For example, we can check whether `bitsPerValue` is a positive number.
A typical report contains one or more assertions.

```python
Ge(message['a'], message['b']) # a >= b
```


