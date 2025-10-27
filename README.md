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
  <a href="#usage">Usage</a>
  •
  <a href="#documentation">Documentation</a>
</p>

> [!IMPORTANT]
> This software is **Emerging** and subject to ECMWF's guidelines on [Software Maturity](https://github.com/ecmwf/codex/raw/refs/heads/main/Project%20Maturity).
>
> Support level: None.
> The project is made available as-is, with no guarantee of support.
> However, bug reports and community contributions are encouraged and appreciated.

GribCheck is a Python tool that validates **project-specific** conventions of GRIB files.
It performs a **limited set of checks** on GRIB messages to ensure they comply with the project's **internal standards** and expectations.

Please note that GribCheck is not a general-purpose GRIB validator.
For instance, it does not verify whether a file fully complies with the WMO GRIB standard or whether it is a technically valid GRIB file.


## Installation

``` bash
pip install grib-check
```

## Usage

To use GribCheck, you need to specify the GRIB convention you want to check.
The library currently supports the following conventions:

- tigge : [The THORPEX Interactive Grand Global Ensemble (TIGGE)](https://confluence.ecmwf.int/display/TIGGE)
- lam : [TIGGE Limited-Area Model (TIGGE LAM)](https://confluence.ecmwf.int/display/TIGL)
- s2s : [Subseasonal to Seasonal (S2S)](http://s2sprediction.net/)
- s2s_refcst : [S2S Reforecasts](http://s2sprediction.net/)
- uerra : [Uncertainties in Ensembles of Regional ReAnalysis (UERRA)](https://uerra.eu/)
- crra : [Copernicus Regional Reanalysis (CERRA)](https://climate.copernicus.eu/copernicus-regional-reanalysis-europe-cerra)

Experimental conventions that are under development include:

- wpmip : [Weather Prediction Model Intercomparison Project (WP-MIP)](https://www.wcrp-esmo.org/activities/wp-mip/)

You can specify the convention using the `-C` or `--convention` command-line argument.
For example, to check a GRIB file of type "tigge", you would run the following command:

``` bash
grib-check -C tigge /path/to/file.grib2
```

The output provides the result of each check performed on the GRIB messages in the file. 
Each check may be annotated with an additional context or information of the check performed which may be useful for diagnostics.
Checks typically have the status FAIL or PASS.
Sometimes, however, a status cannot be assigned - for example if a test is skipped or message is purely informational - in which case the status "----" is used.

The report follows a hierarchical structure, where checks can contain sub-checks and assertions, forming branches. If an assertion fails, the failure propagates upward, and the entire branch is marked as failed.

The following command demonstrates a check on a file of convention "s2s". 
For demonstration purposes, we'll change the convention to "uerra" to intentionally trigger check failures and showcase the output.

![grib-check output](docs/example_output.png "Example output of grib-check command")

## Documentation

- [Components](./docs/components.md)
- [Parameters](./docs/params.md)
- [Checks](./docs/checks.md)
- [Adding new GRIB conventions](./docs/conventions.md)

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
