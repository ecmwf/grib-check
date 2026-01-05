local templates = import 'Parameter.libsonnet';
#local wmo_params = import 'WmoParameters.jsonnet';

local allBasicChecks = [
          "basic_checks_era6",
          "level_keys_era6",
          "pressure_level_era6",
          "height_level_era6",
          "model_level_era6",
          "pt_level_era6",
          "pv_level_era6",
          "overall_time_era6",
          "check_expected_paramid_era6",
];

#wmo_params +
[
  {
      "name": "ERA6 specific basic checks",
      "pairs": [
          {"key": "class", "value": "e6"},
      ],
      "expected": [
          {"key": "tablesVersion", "value": 35},
      ],
      "checks": allBasicChecks
  }
] 

+

[
  {
      "name": "Low cloud cover",
      "pairs": [
          {"key": "class", "value": "e6"},
          {"key": "paramId", "value": "3073"},
      ],
      "expected": [
          {"key": "typeOfLevel", "value": "lowCloudLayer"},
      ],
      "checks": allBasicChecks
  }
] 
