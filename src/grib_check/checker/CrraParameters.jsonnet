local templates = import 'Parameter.libsonnet';
local wmo_params = import 'WmoParameters.jsonnet';
 
wmo_params +
[
  templates.Wmo {
    name: 'snow_albedo_sfc.rr',
    expected+: [
      { key: 'values', min: [-1500000.0, 1500000.0], max: [-1500000.0, 1500000.0] },
    ],
    pairs+: [
      { key: 'class', value: 'rr' },
      { key: 'paramId', value: 228032 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 19 },
      { key: 'parameterNumber', value: 19 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'snow_depth_water_equivalent_sfc.rr',
    expected+: [
      { key: 'values', min: [-1e-05, 0], max: [100, 15000] },
    ],
    pairs+: [
      { key: 'paramId', value: 228141 },
      { key: 'class', value: 'rr' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 60 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'high_cloud_cover_sfc.rr',
    expected+: [
      { key: 'values', min: [0, 1e-10], max: [0.9999, 100.00001] },
    ],
    pairs+: [
      { key: 'paramId', value: 3075 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 6 },
      { key: 'parameterNumber', value: 5 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 8 },
    ],
    checks+: [
      'point_in_time',
      'predefined_thickness',
    ],
  },
  templates.Wmo {
    name: 'medium_cloud_cover_sfc.rr',
    expected+: [
      { key: 'values', min: [0, 1e-10], max: [0.9999, 100.00001] },
    ],
    pairs+: [
      { key: 'paramId', value: 3074 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 6 },
      { key: 'parameterNumber', value: 4 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 8 },
    ],
    checks+: [
      'point_in_time',
      'predefined_thickness',
    ],
  },
  templates.Wmo {
    name: 'low_cloud_cover_sfc.rr',
    expected+: [
      { key: 'values', min: [0, 1e-10], max: [0.9999, 100.00001] },
    ],
    pairs+: [
      { key: 'paramId', value: 3073 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 6 },
      { key: 'parameterNumber', value: 3 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 8 },
    ],
    checks+: [
      'point_in_time',
      'predefined_thickness',
    ],
  },
  templates.Wmo {
    name: 'time-mean_forecast_surface_roughness.rr',
    expected+: [
      { key: 'values', min: [0, 0.001], max: [0.5, 10] },
    ],
    pairs+: [
      { key: 'paramId', value: 235244 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time-mean_sea_ice_surface_temperature.rr',
    expected+: [
      { key: 'values', min: [200, 230], max: [300, 350] },
    ],
    pairs+: [
      { key: 'paramId', value: 263006 },
      { key: 'discipline', value: 10 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 8 },
      { key: 'typeOfFirstFixedSurface', value: 174 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'surface_roughness_length_for_heat.rr',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260651 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 200 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'localTablesVersion', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'direct_solar_radiation_sfc.rr',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'class', value: 'rr' },
      { key: 'paramId', value: 47 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 4 },
      { key: 'parameterNumber', value: 54 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'surface_runoff.rr',
    expected+: [
      { key: 'values', min: [-0.001, 1], max: [0.1, 100] },
    ],
    pairs+: [
      { key: 'paramId', value: 174008 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 34 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'volumetric_soil_ice_layer.rr',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260644 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 38 },
      { key: 'typeOfFirstFixedSurface', value: 151 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'typeOfSecondFixedSurface', value: 151 },
      { key: 'scaleFactorOfSecondFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_thickness',
      'has_bitmap',
      'has_soil_layer',
    ],
  },
]
