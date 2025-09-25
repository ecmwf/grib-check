## Adding a new GRIB convention

To explain how to add a new GRIB convention, we'll walk through a scenario where we introduce a project called "destine". 
This project will inherit the WMO checks and define additional custom checks.
Starting with the WMO checks is a good idea because they represent a universal set of checks that apply to all GRIB messages.
By extending them, you begin with a solid foundation.

Add a new file called `checker/Destiny.py` and derive the `Destiny` class from `Wmo`.
This way, you gain access to many predefined checks like `point_in_time`, `basic_checks`, and `given_level`.
You can also override existing checks or create new ones.
The list of existing checks can be found in the `checker/Wmo.py` file.
If you want to reuse a check, you can call the base class method and add your own checks to the report.
It's demonstrated in the code below in the `_point_in_time()` method.
If you want to create a new check, you can define it in the `Destiny` class.
The check needs to be registered in the constructor using `self.register_checks()`.
The `_destine_limits()` method is an example of a new check that we created.

``` python
from checker.Wmo import Wmo
from Assert import Le, Lt, Ne, Eq, Fail, IsIn, IsMultipleOf
from Report import Report

class DestinE(Wmo):
    def __init__( self, lookup_table, valueflg=False):
        super().__init__(lookup_table, valueflg=valueflg)
        self.register_checks({
            "destine_limits": self._destine_limits
        })

    # Reuse / override checks
    def _point_in_time(self, message, p) -> Report:
        report = Report("Point In Time (DestinE)")
        report.add(IsMultipleOf(message["step"], 3))
        return super()._point_in_time(message, p).add(report)

    # Create new checks
    def _destine_limits(self, message, p) -> Report:
        report = Report("DestinE Limits")
        report.add(Le(message["step"], 30))
        report.add(IsIn(message["forecastTime"], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
        report.add(IsIn(message["indicatorOfUnitOfTimeRange"], [0, 1]))
        report.add(IsIn(message["timeIncrementBetweenSuccessiveFields"], [0, 1]))
        return report
```
Add Destiny option in GribCheck.py

``` python
# ...
# ...
from checker.Destiny import DestinE
      elif self.args.convention == "destine":
# ...
          checker = Destiny(param_file=self.args.parameters, valueflg=self.args.valueflg)
# ...
    parser.add_argument("-t", "--convention", help="convention to check", choices=["tigge", "s2s", "s2s_refcst", "uerra", "crra", "lam", "wmo", "destine"], default="wmo")
# ...

```

Add a new JSON file `./checker/WmoParameters.json` in the parameters directory.

```json
[
  {
      "name": "Name of the check",
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
      "checks": [
          "point_in_time",
          "destine_limits"
    ]
  }
]
```

In this way, we apply the `point_in_time` check from WMO and extend it with our own custom checks.
To start the checks, use the following command:

``` bash
grib_check -t destine /path/to/file.grib2
```

### Parameters

The parameters file is a JSON document that defined the parameters to be validated.
Each parameter is represented as a dictionary with the following optional and required fields:

- `name`: The name of the parameter.
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
