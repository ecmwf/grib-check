local templates = import 'Parameter.libsonnet';
local wmo_params = import 'WmoParameters.jsonnet';

wmo_params +
[
  {
      "name": "ERA6 specific checks",
      "pairs": [
          {"key": "class", "value": "e6"},
      ],
      "expected": [
          {"key": "productionStatusOfProcessedData", "value": 3},
          {"key": "generatingProcessIdentifier", "value": 159},
          {"key": "backgroundProcess", "value": 255},
      ],
      "checks": [
#          "point_in_time",
          "basic_checks_era6",
    ]
  }
]
