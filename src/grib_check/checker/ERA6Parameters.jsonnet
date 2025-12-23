local templates = import 'Parameter.libsonnet';
local wmo_params = import 'WmoParameters.jsonnet';

wmo_params +
[
  {
      "name": "ERA6 specific basic checks",
      "pairs": [
          {"key": "class", "value": "e6"},
      ],
      "expected": [
          {"key": "tablesVersion", "value": 35},
      ],
      "checks": [
          "basic_checks_era6",
          "level_keys",
          "pressure_level",
    ]
  }
]
