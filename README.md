<p align="center">
  <a href="https://github.com/ecmwf/grib-check/actions/workflows/ci.yml?query=branch%3Amaster">
    <img src="https://github.com/ecmwf/grib-check/actions/workflows/ci.yml/badge.svg" alt="master">
  </a>
  <a href="https://github.com/ecmwf/codex/raw/refs/heads/main/Project Maturity">
    <img src="https://github.com/ecmwf/codex/raw/refs/heads/main/Project Maturity/emerging_badge.svg" alt="Maturity Level">
  </a>
  <a href="https://opensource.org/licenses/apache-2-0">
    <img src="https://img.shields.io/badge/Licence-Apache 2.0-blue.svg" alt="Licence">
  </a>
  <a href="https://github.com/ecmwf/grib-checks/releases">
    <img src="https://img.shields.io/github/v/release/ecmwf/grib-check?color=purple&label=Release" alt="Latest Release">
  </a>
</p>


<p align="center">
  <a href="#installation">Installation</a>
  •
  <a href="#installation">Usage</a>
  •
  <a href="#installation">Documentation</a>
</p>

# GRIB Check

> [!IMPORTANT]
> This software is **Emerging** and subject to ECMWF's guidelines on [Software Maturity](https://github.com/ecmwf/codex/raw/refs/heads/main/Project%20Maturity).
>
> Support level: None.
> The project is made available as-is, with no guarantee of support.
> However, bug reports and community contributions are encouraged and appreciated.

GribCheck is a Python library designed for validating GRIB files.
It provides a set of checks that can be applied to GRIB messages, ensuring that they conform to specific standards and expectations.

## Installation

Installing GribCheck is straightforward. You can clone the repository and install it using pip.

``` bash
pip install grib-check
```
## Usage

To use GribCheck, you need to specify the convention you want to check.
The library currently supports the following conventions:

- tigge : [The THORPEX Interactive Grand Global Ensemble (TIGGE)](https://confluence.ecmwf.int/display/TIGGE)
- lam : [TIGGE Limited-Area Model (TIGGE LAM)](https://confluence.ecmwf.int/display/TIGL)
- s2s : [Subseasonal to Seasonal (S2S)](http://s2sprediction.net/)
- s2s_refcst : [S2S Reforecasts](http://s2sprediction.net/)
- uerra : [Uncertainties in Ensembles of Regional ReAnalysis (UERRA)](https://uerra.eu/)
- crra : [Copernicus Regional Reanalysis (CERRA)](https://climate.copernicus.eu/copernicus-regional-reanalysis-europe-cerra)

Experimental conventions that are under development include:

- wmo : General checks required by [World Meteorological Organization (WMO)](https://public.wmo.int/en)
- wpmip : [Weather Prediction Model Intercomparison Project (WP-MIP)](https://www.wcrp-esmo.org/activities/wp-mip/)

You can specify the convention using the `-t` or `--convention` command-line argument.
For example, to check a GRIB file of type "tigge", you would run the following command:

``` bash
grib-check -t tigge /path/to/file.grib2
```

The output provides the result of each check performed on the GRIB messages in the file. 
Each check may be annotated with an additional context or information of the check performed which may be useful for diagnostics.
Checks typically have the status FAIL or PASS.
Sometimes, however, a status cannot be assigned - for example if a test is skipped or message is purely informational - in which case the status NONE is used.

The report follows a hierarchical structure, where checks can contain sub-checks and assertions, forming branches. If an assertion fails, the failure propagates upward, and the entire branch is marked as failed.

The following command demonstrates a check on a file of convention "s2s". 
For demonstration purposes, we'll change the convention to "uerra" to intentionally trigger check failures and showcase the output.

```
$ grib-check -t uerra -c data/S2S_SET/S2.ENFH.AMMC.CF.PL.grib2
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

## Documentation

- [Components](./docs/devdoc.md)
- [Checks](./docs/checkdocs.md)
- [Parameters](./docs/params.md)

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
