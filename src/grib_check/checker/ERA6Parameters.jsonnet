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
          "check_range",
          "topd_era6",
          "togp_era6",
];

#wmo_params +
[
  {
      "name": "ERA6 specific basic checks",
      "pairs": [
          {"key": "class", "value": "e6"},
      ],
      "expected": [
          {"key": "tablesVersion", "value": 36},
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
          { key: 'values', min: [0, 100], max: [0, 100] },
          { key: "typeOfLevel", value: "lowCloudLayer"},
      ],
      "checks": allBasicChecks
  }
] 

+

[
  {
      "name": "Medium cloud cover",
      "pairs": [
          {"key": "class", "value": "e6"},
          {"key": "paramId", "value": "3074"},
      ],
      "expected": [
          { key: 'values', min: [0, 100], max: [0, 100] },
          { key: "typeOfLevel", value: "mediumCloudLayer"},
      ],
      "checks": allBasicChecks
  }
]

+

[
  {
      "name": "High cloud cover",
      "pairs": [
          {"key": "class", "value": "e6"},
          {"key": "paramId", "value": "3075"},
      ],
      "expected": [
          { key: 'values', min: [0, 100], max: [0, 100] },
          { key: "typeOfLevel", value: "highCloudLayer"},
      ],
      "checks": allBasicChecks
  }
]
