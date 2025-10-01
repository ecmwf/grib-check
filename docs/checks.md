# Checks

Checks are functions applied to GRIB messages.
They take a message and parameters as arguments, and return a report.

Many checks are already predefined in the WMO class and can be used directly.
If necessary, they can be overridden or extended.
New checks can also be added.

Checks are used in parameter files, where they are listed under `checks`.
When the parameter is applied, all checks in the list are executed.

This section explains how to work with checks. 

## Extending checks

Normally, you would derive directly or indirectly from the WMO class.
This gives you access to many checks.
Sometimes, we want to extend some of them.
In such cases, we override the function from the base class but retain the results produced by the original function.
One way to achieve this is by merging the reports and returning the combined result.

``` python
def some_check(self, message, p) -> Report:
    report = Report("Extended check")
    return super().some_check(message, p).add(report)
```

## Overriding checks

Sometimes the way we test GRIB files differs significantly from the base class.
However, what we are doing is essentially the same, so we want to keep the same name.
For example, the pressure levels have completely different values.
In such cases, we can override checks from the base class simply by creating a new check with the same name.

``` python
def some_check(self, message, p) -> Report:
    report = Report("Overridden Check")
    return report
```


## New checks

To create a new check, two steps are required.
First, you need to write a check function.
Second, you must register it in derived class using `self.register_checks()`.
Only then can it be used in the parameter file.


``` python
def check_new(self, message, p) -> Report:
    report = Report("Overridden Check")
    return report
```

``` python
self.register_checks({
  "check_new": self._check_new
})
```
