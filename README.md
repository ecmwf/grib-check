<h3 align="center">
  <a href="https://github.com/ecmwf/grib-check/actions/workflows/ci.yml?query=branch%3Amaster"><img src="https://github.com/ecmwf/grib-check/actions/workflows/ci.yml/badge.svg" alt="master"></a>
</h3>

# GRIB Check

> [!IMPORTANT]
> This software is **Emerging** and subject to ECMWF's guidelines on [Software Maturity](https://github.com/ecmwf/codex/raw/refs/heads/main/Project%20Maturity).
>
> Support level: None.
> The project is made available as-is, with no guarantee of support.
> However, bug reports and community contributions are encouraged and appreciated.

GribCheck is a Python library designed for validating GRIB files.
It provides a set of checks that can be applied to GRIB messages, ensuring that they conform to specific standards and expectations.

## Further Information
- Developer documentation is available at [GribCheck Developer documentation](./docs/devdoc.md).
- [Checks documentation](./docs/checkdocs.md) provides detailed information on how to add new checks and customize existing ones.
- [Parameter files documentation](./docs/paramdocs.md) explains how to create and manage parameter files used by GribCheck.

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
- destine (under development)

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

# License
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
