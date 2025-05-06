# GRIB Check

## Overview
GribCheck is a Python library designed for validating GRIB files.
It provides a set of checks that can be applied to GRIB messages, ensuring that they conform to specific standards and expectations.

## Prerequisites
 ``` bash
pip install pandas eccodes
```

## Usage
To use GribCheck, you need to specify the type of data you want to check.
The library currently supports the following types:

- wmo
- tigge
- s2s
- s2s_refcst
- uerra
- crra
- lam
- destiny

You can specify the type of data using the `-t` or `--grib_type` command-line argument.
For example, to check a GRIB file of type "tigge", you would run the following command:

``` bash
python GribCheck.py -t tigge /path/to/file.grib2
```

The output provides the result of each check performed on the GRIB messages in the file. 
Each check is marked with a status of either "PASS" or "FAIL", and may include details about the specific validation performed. 
Comment may be included to provide additional context or information about the check.
They have the status `NONE`.

The report follows a hierarchical structure, where checks can contain sub-checks and assertions, forming branches. If an assertion fails, the failure propagates upward, and the entire branch is marked as failed.

The following command demonstrates a check on a file of type "s2s". 
For demonstration purposes, we'll change the type to "uerra" to intentionally trigger check failures and showcase the output.

```
$ grib_check.py -t uerra -c data/S2S_SET/S2.ENFH.AMMC.CF.PL.grib2
FAIL: data/S2S_SET/S2.ENFH.AMMC.CF.PL.grib2
  FAIL: field 0
    NONE: Matched parameter: temperature_pl.ammc
      model: glob
      paramId: 130
      centre: ammc
      discipline: 0
      parameterCategory: 0
      parameterNumber: 0
      typeOfFirstFixedSurface: 100
    FAIL: temperature_pl.ammc
      FAIL: Default Statistical Process
        FAIL: numberOfTimeRange(None) == 1
        FAIL: numberOfMissingInStatisticalProcess(None) == 0
        FAIL: typeOfTimeIncrement(None) == 2
        FAIL: minuteOfEndOfOverallTimeInterval(None) == 0
        FAIL: secondOfEndOfOverallTimeInterval(None) == 0
        FAIL: indicatorOfUnitForTimeRange(None) == 1
        FAIL: lengthOfTimeRange(None) + startStep(24) == endStep(24)
        PASS: Uerra Basic Checks
          PASS: hour(0) <= 24
          PASS: step(24) in [1, 2, 4, 5] or step(24) % 3 == 0
      FAIL: Default Point in time
        PASS: perturbationNumber(0) == 0
              topd=typeOfProcessedData(3)
        PASS: numberOfForecastsInEnsemble(33) != 0
              topd=typeOfProcessedData(3)
        FAIL: Uerra Point in Time
          FAIL: productDefinitionTemplateNumber(60) == 1
          PASS: forecastTime(24) in [1, 2, 4, 5] or forecastTime(24) % 3 == 0
      PASS: Default Given level
        PASS: typeOfFirstFixedSurface(pl) != 255
        PASS: scaleFactorOfFirstFixedSurface exists(True)
        PASS: scaledValueOfFirstFixedSurface exists(True)
        PASS: typeOfSecondFixedSurface(255) == 255
        PASS: scaleFactorOfSecondFixedSurface is missing(True)
        PASS: scaledValueOfSecondFixedSurface is missing(True)
      PASS: Uerra Pressure Level
        PASS: level(850) in [1000, 975, 950, 925, 900, 875, 850, 825, 800, 750, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 20, 10]
              invalid pressure level
```



## Adding a new GRIB type

To explain how to add a new GRIB type, we'll walk through a scenario where we introduce a project called "destiny". 
This project will inherit the WMO checks and define additional custom restrictions.

Add a new file called `checker/Destiny.py` and derive the `Destiny` class from `Wmo`.
This way, you gain access to many predefined checks.

``` python
from checker.Wmo import Wmo
from Assert import Le, Lt, Ne, Eq, Fail, IsIn, IsMultipleOf
from Report import Report

class Destiny(Wmo):
    def __init__( self, param_file=None, valueflg=False):
        param_file= param_file if param_file is not None else f"{script_path}/WmoParameters.json"
        super().__init__(param_file, valueflg=valueflg)

    def _point_in_time(self, message, p) -> Report:
        report = Report("Point In Time (Destiny)")
        report.add(IsultipleOf(message["step"], 3))

        return super()._basic_checks(message, p).add(report)
```
Add Destiny option in GribCheck.py

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

Add a new JSON file `./checker/WmoParameters.json` in the parameters directory.

```json
[
  {
      "pairs": [
          {"key": "stream", "value": "enfo"},
          {"key": "dataType", "value": "pf"}
      ],
      "expected": [
          {"key": "productDefinitionTemplateNumber", "value": 1},
          {"key": "paramId", "value": "167"},
          {"key": "shortName", "value": "2t"},
          {"key": "name", "value": "2 metre temperature"}
      ],
      "checks": ["point_in_time"]
  }
]
```

In this way, we apply the `point_in_time` check from WMO and extend it with our own custom checks.
To start the checks, use the following command:

``` bash
python GribCheck.py -t destiny /path/to/file.grib2
```

### Parameters

The parameters file is a JSON document that defined the parameters to be validated.
Each parameter is represented as a dictionary with the following optional and required fields:

- `name`: (option) The name of the parameter.
- `expected`: (optional) A list of simple and quick checks to be performed on a GRIB message.
- `pairs`: A list of key-value pairs that are used to select the most appropriate parameter for validation.
- `checks`: A list of more complex validations to be performed on the message.

A parameter is considered a match if all key-value pairs match those in the message.
If multiple parameters match, the one with the highest number of matching key-value pairs is selected.
Once a parameter is selected, validations defined in both `expected` and `checks` are executed.

Below is an example entry from a parameters file:

```json
[
{
  "name" : "sea_surface_height_o2d.s2",
  "expected" : [
    {"key": "class", "value": 0},
    {"key": "values", "min": [-100000000.0, 100000000.0], "max": [-100000000.0, 100000000.0]}
  ],
  "pairs" : [
    {"key": "class", "value": "s2"},
    {"key": "paramId", "value": 151145},
    {"key": "discipline", "value": 10},
    {"key": "parameterCategory", "value": 3},
    {"key": "parameterNumber", "value": 1},
    {"key": "typeOfFirstFixedSurface", "value": 160},
    {"key": "scaleFactorOfFirstFixedSurface", "value": 0},
    {"key": "scaledValueOfFirstFixedSurface", "value": 0}
  ],
  "checks" : [
    "basic_checks",
    "daily_average",
    "given_level",
    "has_bitmap",
    "resolution_s2s_ocean"
  ]
},
]
```
> **_NOTE:_**  The support for `min`/`max` in the `expected` field is still under development.


# Development
## Grib

The Grib class is a wrapper around ecCodes.

### Message

A message is a wrapper around the ecCodes handle, with the key difference that it provides automatic memory management.

To get the value of a key, we can use either the `get` method or the square brackets `[]` operator.
While square brackets are more convenient, it returns the value in the native format (e.g., a string).
The `get` method, on the other hand, can return the value in a specific format, such as `float`, `int`, or `str`.

```python
grib = Grib("path/to/file.grib2")
message = grib.next()
print(f"message['stream'] = {message['stream']}")
# message['stream'] = enfo
print(f"message.get('stream', int) = {message.get('stream', int)}")
# message.get('stream', int) = 1035
```
### KeyValue type

Values returned by a Message are stored in a KeyValue type.
Each KeyValue contains the key name, the value (which can be a number or a string), and the corresponding data type.

```python
a = KeyValue("a", 5)
print(f"a.key() = {a.key()}\n a.value() = {a.value()}\n a.type() = {a.type()}")
# a.key() = a
# a.value() = 5
# a.type() = <class 'int'>
```

### Mathematical operations

KeyValue supports various mathematical operations. These operations serve two purposes:
First, they modify the value as expected.
Secondly, they construct a mathematical expression in string format to demonstrate how the value was calculated.
This can help users to understand the logic behind the calculations.

The key changes the format of the string representation of the KeyValue after the operation.
For example, if we add two KeyValue objects together, the resulting KeyValue will have a string representation that shows the addition operation.
Inside the parentheses, the string representation of the KeyValue is displayed.


```python
a = KeyValue("a", 5)
b = KeyValue("b", 6)
c = a + b

print(f"c.key() = {c.key()}")
# c.value() = a(5) + b(6)

print(f"c.value() = {c.value()}")
# c.value() = 11

print(f"{c} = {c.value()}")
# a(5) + b(6) = 11
```

### Check functions

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


