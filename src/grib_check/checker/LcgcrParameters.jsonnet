local templates = import 'Parameter.libsonnet';
[
  templates.Wmo {
    name: 'Time-mean_2_metre_temperature.sfc.lcgcr',
    expected+: [
      { key: 'values', min: [170, 290], max: [270, 360] },
    ],
    pairs+: [
      { key: 'paramId', value: 228004 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaledValueOfFirstFixedSurface', value: 2 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'Time-mean_mean_sea_level_pressure.sfc.lcgcr',
    expected+: [
      { key: 'values', min: [88000, 104000], max: [98000, 115000] },
    ],
    pairs+: [
      { key: 'paramId', value: 235151 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 101 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'Time-mean_total_precipitation_rate.sfc.lcgcr',
    expected+: [
      { key: 'values', min: [-0.05, 0.1], max: [0.0, 500.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 235055 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 52 },
//    { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'mean_sea_level_pressure_sfc.lcgcr',
    expected+: [
      { key: 'values', min: [88000, 104000], max: [98000, 115000] },
    ],
    pairs+: [
      { key: 'paramId', value: 151 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 101 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'orography.sfc.lcgcr',
    expected+: [
      { key: 'values', min: [-1300, 0], max: [1000, 8888] },
    ],
    pairs+: [
      { key: 'paramId', value: 228002 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 5 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
    ],
  },
]
