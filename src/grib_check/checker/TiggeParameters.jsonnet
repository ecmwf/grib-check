local templates = import 'Parameter.libsonnet';

[
  templates.Wmo {
    name: '10_meter_u_velocity_sfc.glob',
    expected+: [
      { key: 'values', min: [-100, -1], max: [1, 100] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 165 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 2 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 10 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: '10_meter_u_velocity_sfc.lam',
    expected+: [
      { key: 'values', min: [-100, -1], max: [1, 100] },
    ],
    pairs+: [
      { key: 'model', value: 'lam' },
      { key: 'paramId', value: 165 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 2 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 10 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: '10_meter_u_velocity_sfc.lam.mogreps-mo-eua',
    expected+: [
      { key: 'suiteName', value: 1 },
      { key: 'values', min: [-100, 10], max: [-10, 100] },
    ],
    pairs+: [
      { key: 'model', value: 'lam' },
      { key: 'suiteName', value: 'mogreps-mo-eua' },
      { key: 'paramId', value: 165 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 2 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 10 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: '10_meter_v_velocity_sfc.glob',
    expected+: [
      { key: 'values', min: [-100, -1], max: [1, 100] },
    ],
    pairs+: [
      { key: 'paramId', value: 166 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 3 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 10 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: '10_meter_v_velocity_sfc.lam.mogreps-mo-eua',
    expected+: [
      { key: 'suiteName', value: 1 },
      { key: 'values', min: [-100, 10], max: [-10, 100] },
    ],
    pairs+: [
      { key: 'model', value: 'lam' },
      { key: 'suiteName', value: 'mogreps-mo-eua' },
      { key: 'paramId', value: 166 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 3 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 10 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'convective_available_potential_energy_sfc.glob',
    expected+: [
      { key: 'values', min: [0, 10], max: [0, 17000] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 7 },
      { key: 'parameterNumber', value: 6 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 8 },
    ],
    checks+: [
      'point_in_time',
      'predefined_thickness',
    ],
  },
  templates.Wmo {
    name: 'convective_available_potential_energy_sfc.lam',
    expected+: [
      { key: 'values', min: [0, 100], max: [0, 17000] },
    ],
    pairs+: [
      { key: 'model', value: 'lam' },
      { key: 'paramId', value: 59 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 7 },
      { key: 'parameterNumber', value: 6 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 8 },
    ],
    checks+: [
      'point_in_time',
      'predefined_thickness',
    ],
  },
  templates.Wmo {
    name: 'convective_available_potential_energy_sfc.lam.glameps-hirlamcons-eu',
    expected+: [
      { key: 'suiteName', value: 9 },
      { key: 'values', min: [-1000, 10], max: [0, 17000] },
    ],
    pairs+: [
      { key: 'model', value: 'lam' },
      { key: 'suiteName', value: 'glameps-hirlamcons-eu' },
      { key: 'paramId', value: 59 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 7 },
      { key: 'parameterNumber', value: 6 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 8 },
    ],
    checks+: [
      'point_in_time',
      'predefined_thickness',
    ],
  },
  templates.Wmo {
    name: 'convective_inhibition_sfc.glob',
    expected+: [
      { key: 'values', min: [-60000, 0], max: [-10, 5] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 7 },
      { key: 'parameterNumber', value: 7 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 8 },
    ],
    checks+: [
      'point_in_time',
      'predefined_thickness',
    ],
  },
  templates.Wmo {
    name: 'convective_inhibition_sfc.lam',
    expected+: [
      { key: 'values', min: [-60000, 1], max: [-10, 4000] },
    ],
    pairs+: [
      { key: 'model', value: 'lam' },
      { key: 'paramId', value: 228001 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 7 },
      { key: 'parameterNumber', value: 7 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 8 },
    ],
    checks+: [
      'point_in_time',
      'predefined_thickness',
    ],
  },
  templates.Wmo {
    name: 'field_capacity_sfc',
    expected+: [
      { key: 'values', min: [1e+99, -1e+99], max: [99, -99] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 12 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaleFactorOfSecondFixedSurface', value: 1 },
      { key: 'scaledValueOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfSecondFixedSurface', value: 2 },
      { key: 'typeOfFirstFixedSurface', value: 106 },
      { key: 'typeOfSecondFixedSurface', value: 106 },
    ],
    checks+: [
      'point_in_time',
      'given_thickness',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'land_sea_mask_sfc.glob',
    expected+: [
      { key: 'values', min: [0, 0], max: [1, 1] },
    ],
    pairs+: [
      { key: 'paramId', value: 172 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'land_sea_mask_sfc.lam.hirlam-dmi-eu',
    expected+: [
      { key: 'suiteName', value: 11 },
      { key: 'values', min: [-0.001, 0], max: [1, 1.11] },
    ],
    pairs+: [
      { key: 'model', value: 'lam' },
      { key: 'suiteName', value: 'hirlam-dmi-eu' },
      { key: 'paramId', value: 172 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'orography_sfc',
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
  templates.Wmo {
    name: 'potential_temperature_pv',
    expected+: [
      { key: 'values', min: [220, 265], max: [380, 1200] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 2 },
      { key: 'typeOfFirstFixedSurface', value: 109 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'potential_vorticity_level',
    ],
  },
  templates.Wmo {
    name: 'potential_vorticity_pt',
    expected+: [
      { key: 'values', min: [-0.005, -1e-06], max: [1e-06, 0.002] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 14 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 320 },
      { key: 'typeOfFirstFixedSurface', value: 107 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'potential_temperature_level',
    ],
  },
  templates.Wmo {
    name: 'snow_depth_water_equivalent_sfc',
    expected+: [
      { key: 'values', min: [0, 0], max: [100, 15000] },
    ],
    pairs+: [
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
    name: 'snow_fall_water_equivalent_sfc',
    expected+: [
      { key: 'values', min: [-1500000.0, 1500000.0], max: [-1500000.0, 1500000.0] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 228144 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 53 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'soil_moisture_sfc',
    expected+: [
      { key: 'values', min: [-1e-19, 0], max: [450, 800] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 22 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaleFactorOfSecondFixedSurface', value: 1 },
      { key: 'scaledValueOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfSecondFixedSurface', value: 2 },
      { key: 'typeOfFirstFixedSurface', value: 106 },
      { key: 'typeOfSecondFixedSurface', value: 106 },
    ],
    checks+: [
      'point_in_time',
      'given_thickness',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'soil_temperature_sfc',
    expected+: [
      { key: 'values', min: [200, 230], max: [300, 350] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 2 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaleFactorOfSecondFixedSurface', value: 1 },
      { key: 'scaledValueOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfSecondFixedSurface', value: 2 },
      { key: 'typeOfFirstFixedSurface', value: 106 },
      { key: 'typeOfSecondFixedSurface', value: 106 },
    ],
    checks+: [
      'point_in_time',
      'given_thickness',
    ],
  },
  templates.Wmo {
    name: 'specific_humidity_pl',
    expected+: [
      { key: 'values', min: [-0.1, 0.001], max: [5e-05, 0.1] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 100 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'sunshine_duration_sfc',
    expected+: [
      { key: 'values', min: [0, 0], max: [3600.00000001, 3600.00000001] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 6 },
      { key: 'parameterNumber', value: 24 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'surface_air_temperature_sfc.glob',
    expected+: [
      { key: 'values', min: [180, 290], max: [270, 350] },
    ],
    pairs+: [
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'surface_air_dew_point_temperature_sfc.lam',
    expected+: [
      { key: 'values', min: [110, 290], max: [270, 350] },
    ],
    pairs+: [
      { key: 'model', value: 'lam' },
      { key: 'paramId', value: 168 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 6 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 2 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'surface_air_dew_point_temperature_sfc.lam',
    expected+: [
      { key: 'suiteName', value: 1 },
      { key: 'values', min: [110, 290], max: [270, 350] },
    ],
    pairs+: [
      { key: 'model', value: 'lam' },
      { key: 'suiteName', value: 'mogreps-mo-eua' },
      { key: 'paramId', value: 168 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 6 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 1 },
      { key: 'scaledValueOfFirstFixedSurface', value: 15 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'surface_air_maximum_temperature_sfc',
    expected+: [
      { key: 'values', min: [160, 255], max: [300, 380] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 121 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'typeOfStatisticalProcessing', value: 2 },
    ],
    checks+: [
      'six_hourly',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'surface_air_minimum_temperature_sfc',
    expected+: [
      { key: 'values', min: [160, 260], max: [300, 330] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 122 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'typeOfStatisticalProcessing', value: 3 },
    ],
    checks+: [
      'six_hourly',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'surface_air_maximum_temperature_sfc.ammc',
    expected+: [
      { key: 'centre', value: 1 },
      { key: 'values', min: [175, 240], max: [300, 10000] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'centre', value: 'ammc' },
      { key: 'paramId', value: 121 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'typeOfStatisticalProcessing', value: 2 },
    ],
    checks+: [
      'six_hourly',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'time_integrated_top_net_thermal_radiation_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 179 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 5 },
      { key: 'parameterNumber', value: 5 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 8 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time_integrated_surface_latent_heat_flux_sfc',
    expected+: [
      { key: 'values', min: [-3e+7, -1e+4], max: [2e+3, 8e+7] },
    ],
    pairs+: [
      { key: 'paramId', value: 147 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 10 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time_integrated_surface_net_solar_radiation_sfc.glob',
    expected+: [
      { key: 'values', min: [-10, 100000.0], max: [100000.0, 10000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 176 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 4 },
      { key: 'parameterNumber', value: 9 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time_integrated_surface_net_solar_radiation_downwards_sfc',
    expected+: [
      { key: 'values', min: [-10, 10000000.0], max: [100000.0, 1000000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 169 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 4 },
      { key: 'parameterNumber', value: 7 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time_integrated_surface_net_thermal_radiation_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 177 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 5 },
      { key: 'parameterNumber', value: 5 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time_integrated_surface_net_thermal_radiation_downwards_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 175 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 5 },
      { key: 'parameterNumber', value: 3 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time_integrated_surface_sensible_heat_flux_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 146 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 11 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'total_cloud_cover_sfc',
    expected+: [
      { key: 'values', min: [0, 1e-10], max: [100, 100.00001] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 6 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 8 },
    ],
    checks+: [
      'point_in_time',
      'predefined_thickness',
    ],
  },
  templates.Wmo {
    name: 'total_precipitation_sfc.glob',
    expected+: [
      { key: 'values', min: [-0.05, 0.1], max: [0.0, 100.0] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 228228 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 52 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'total_precipitation_sfc.lam',
    expected+: [
      { key: 'values', min: [-0.05, 0.1], max: [0.0, 400.0] },
    ],
    pairs+: [
      { key: 'model', value: 'lam' },
      { key: 'paramId', value: 228228 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 52 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'large_scale_precipitation_sfc.glob',
    expected+: [
      { key: 'values', min: [-0.05, 0.1], max: [0.0, 100.0] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 54 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 255 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'large_scale_precipitation_sfc.lam',
    expected+: [
      { key: 'values', min: [-0.05, 0.1], max: [0.0, 400.0] },
    ],
    pairs+: [
      { key: 'model', value: 'lam' },
      { key: 'paramId', value: 3062 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
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
    name: 'wilting_point_sfc',
    expected+: [
      { key: 'values', min: [1e+99, -1e+99], max: [99, -99] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 26 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaleFactorOfSecondFixedSurface', value: 1 },
      { key: 'scaledValueOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfSecondFixedSurface', value: 2 },
      { key: 'typeOfFirstFixedSurface', value: 106 },
      { key: 'typeOfSecondFixedSurface', value: 106 },
    ],
    checks+: [
      'point_in_time',
      'given_thickness',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'maximum_wind_gust.lam',
    expected+: [
      { key: 'values', min: [0, 15], max: [0, 150] },
    ],
    pairs+: [
      { key: 'model', value: 'lam' },
      { key: 'paramId', value: 228028 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 22 },
      { key: 'typeOfStatisticalProcessing', value: 2 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 10 },
    ],
    checks+: [
      'three_hourly',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'maximum_wind_gust.lam.mogreps',
    expected+: [
      { key: 'suiteName', value: 1 },
      { key: 'values', min: [0, 20], max: [0, 800] },
    ],
    pairs+: [
      { key: 'model', value: 'lam' },
      { key: 'suiteName', value: 'mogreps-mo-eua' },
      { key: 'paramId', value: 228028 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 22 },
      { key: 'typeOfStatisticalProcessing', value: 2 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 10 },
    ],
    checks+: [
      'three_hourly',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'mean_sea_level_pressure_sfc',
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
    name: 'mean_sea_level_pressure_sfc.lfpw',
    expected+: [
      { key: 'centre', value: 1 },
      { key: 'values', min: [85000, 104000], max: [98000, 121000] },
    ],
    pairs+: [
      { key: 'paramId', value: 151 },
      { key: 'centre', value: 'lfpw' },
      { key: 'step', value: 0 },
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
    name: 'geopotential_height_pl',
    expected+: [
      { key: 'values', min: [-5000, 30600], max: [200, 35000] },
    ],
    pairs+: [
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 5 },
      { key: 'typeOfFirstFixedSurface', value: 100 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'geopotential_pl',
    expected+: [
      { key: 'values', min: [-5000, 306000], max: [2000, 350000] },
    ],
    pairs+: [
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 4 },
      { key: 'typeOfFirstFixedSurface', value: 100 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'temperature_pl',
    expected+: [
      { key: 'values', min: [150, 275], max: [200, 330] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 130 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 100 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'temperature_pl.ammc',
    expected+: [
      { key: 'centre', value: 1 },
      { key: 'values', min: [-999, 260], max: [200, 350] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 130 },
      { key: 'centre', value: 'ammc' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 100 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'u_velocity_pl',
    expected+: [
      { key: 'values', min: [-250, 5], max: [1, 250] },
    ],
    pairs+: [
      { key: 'paramId', value: 131 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 2 },
      { key: 'typeOfFirstFixedSurface', value: 100 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'v_velocity_pl',
    expected+: [
      { key: 'values', min: [-200, -2], max: [2, 200] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 132 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 3 },
      { key: 'typeOfFirstFixedSurface', value: 100 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'u_velocity_pv',
    expected+: [
      { key: 'values', min: [-120, -30], max: [70, 120] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 2 },
      { key: 'typeOfFirstFixedSurface', value: 109 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'potential_vorticity_level',
    ],
  },
  templates.Wmo {
    name: 'v_velocity_pv',
    expected+: [
      { key: 'values', min: [-120, -50], max: [55, 120] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 3 },
      { key: 'typeOfFirstFixedSurface', value: 109 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'potential_vorticity_level',
    ],
  },
  templates.Wmo {
    name: 'w_vertical_velocity_pl',
    expected+: [
      { key: 'values', min: [-25, 0], max: [-2, 25] },
    ],
    pairs+: [
      { key: 'paramId', value: 135 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 8 },
      { key: 'typeOfFirstFixedSurface', value: 100 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'soil_type_sfc',
    expected+: [
      { key: 'values', min: [0, 1], max: [5, 10] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 43 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'surface_pressure_sfc',
    expected+: [
      { key: 'values', min: [48000, 80000], max: [101500, 115000] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 134 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'eastward_turbulent_surface_stress_sfc',
    expected+: [
      { key: 'values', min: [-1500000.0, 1500000.0], max: [-1500000.0, 1500000.0] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 180 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 38 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'northward_turbulent_surface_stress_sfc',
    expected+: [
      { key: 'values', min: [-1500000.0, 1500000.0], max: [-1500000.0, 1500000.0] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 181 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 37 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'water_runoff_sfc',
    expected+: [
      { key: 'values', min: [-0.001, 5], max: [0.3, 30] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 228205 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 33 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'sea_ice_cover_sfc.glob',
    expected+: [
      { key: 'values', min: [-1500000.0, 1500000.0], max: [-1500000.0, 1500000.0] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 31 },
      { key: 'discipline', value: 10 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'snow_density_sfc.glob',
    expected+: [
      { key: 'values', min: [-1500000.0, 1500000.0], max: [-1500000.0, 1500000.0] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 33 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 61 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'sea_surface_temperature_sfc.glob',
    expected+: [
      { key: 'values', min: [200, 290], max: [260, 320] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 34 },
      { key: 'discipline', value: 10 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'convective_available_potential_energy_sfc.glob.s2',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'values', min: [0, 10], max: [0, 17000] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'class', value: 's2' },
      { key: 'paramId', value: 59 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 7 },
      { key: 'parameterNumber', value: 6 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 8 },
    ],
    checks+: [
      'daily_average',
      'predefined_thickness',
      'resolution_s2s',
    ],
  },
  templates.Wmo {
    name: 'total_column_water_sfc.s2',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'values', min: [-3.0, 2], max: [30, 150] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'class', value: 's2' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 51 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 8 },
    ],
    checks+: [
      'daily_average',
      'predefined_thickness',
      'resolution_s2s',
    ],
  },
  templates.Wmo {
    name: 'total_column_water_sfc',
    expected+: [
      { key: 'values', min: [-3.0, 2], max: [30, 150] },
    ],
    pairs+: [
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 51 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 8 },
    ],
    checks+: [
      'point_in_time',
      'predefined_thickness',
    ],
  },
  templates.Wmo {
    name: 'surface_air_temperature_sfc.glob.s2',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'values', min: [170, 290], max: [270, 360] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'class', value: 's2' },
      { key: 'paramId', value: 167 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
    ],
    checks+: [
      'daily_average',
      'given_level',
      'resolution_s2s',
    ],
  },
  templates.Wmo {
    name: 'surface_air_dew_point_temperature_sfc',
    expected+: [
      { key: 'values', min: [30, 290], max: [270, 350] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 168 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 6 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'surface_air_dew_point_temperature_sfc.s2',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'values', min: [30, 290], max: [270, 350] },
    ],
    pairs+: [
      { key: 'class', value: 's2' },
      { key: 'paramId', value: 168 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 6 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
    ],
    checks+: [
      'daily_average',
      'given_level',
      'resolution_s2s',
    ],
  },
  templates.Wmo {
    name: 'skin_temperature_sfc.s2',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'values', min: [160, 300], max: [300, 355] },
    ],
    pairs+: [
      { key: 'class', value: 's2' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 17 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'daily_average',
      'predefined_level',
      'resolution_s2s',
    ],
  },
  templates.Wmo {
    name: 'soil_moisture_top_20_cm_sfc.glob',
    expected+: [
      { key: 'values', min: [-1e-17, 70], max: [100, 1500] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 228086 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 22 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 106 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 0 },
      { key: 'typeOfSecondFixedSurface', value: 106 },
      { key: 'scaleFactorOfSecondFixedSurface', value: 1 },
      { key: 'scaledValueOfSecondFixedSurface', value: 2 },
    ],
    checks+: [
      'daily_average',
      'given_thickness',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'soil_moisture_top_100_cm_sfc.glob',
    expected+: [
      { key: 'values', min: [-1e-15, 70], max: [380, 1400] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 228087 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 22 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 106 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 0 },
      { key: 'typeOfSecondFixedSurface', value: 106 },
      { key: 'scaleFactorOfSecondFixedSurface', value: 1 },
      { key: 'scaledValueOfSecondFixedSurface', value: 10 },
    ],
    checks+: [
      'daily_average',
      'given_thickness',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'soil_temperature_top_20_cm_sfc.glob',
    expected+: [
      { key: 'values', min: [180, 240], max: [300, 350] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 228095 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 2 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 106 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 0 },
      { key: 'typeOfSecondFixedSurface', value: 106 },
      { key: 'scaleFactorOfSecondFixedSurface', value: 1 },
      { key: 'scaledValueOfSecondFixedSurface', value: 2 },
    ],
    checks+: [
      'daily_average',
      'given_thickness',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'soil_temperature_top_20_cm_sfc.glob.rums',
    expected+: [
      { key: 'centre', value: 1 },
      { key: 'values', min: [0, 250], max: [300, 350] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'centre', value: 'rums' },
      { key: 'paramId', value: 228095 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 2 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 106 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 0 },
      { key: 'typeOfSecondFixedSurface', value: 106 },
      { key: 'scaleFactorOfSecondFixedSurface', value: 1 },
      { key: 'scaledValueOfSecondFixedSurface', value: 2 },
    ],
    checks+: [
      'daily_average',
      'given_thickness',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'soil_temperature_top_100_cm_sfc.glob',
    expected+: [
      { key: 'values', min: [190, 240], max: [300, 350] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 228096 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 2 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 106 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 0 },
      { key: 'typeOfSecondFixedSurface', value: 106 },
      { key: 'scaleFactorOfSecondFixedSurface', value: 1 },
      { key: 'scaledValueOfSecondFixedSurface', value: 10 },
    ],
    checks+: [
      'daily_average',
      'given_thickness',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'soil_temperature_top_100_cm_sfc.glob.s2.rums',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'centre', value: 1 },
      { key: 'values', min: [0, 250], max: [300, 350] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'class', value: 's2' },
      { key: 'centre', value: 'rums' },
      { key: 'paramId', value: 228096 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 2 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 106 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 0 },
      { key: 'typeOfSecondFixedSurface', value: 106 },
      { key: 'scaleFactorOfSecondFixedSurface', value: 1 },
      { key: 'scaledValueOfSecondFixedSurface', value: 10 },
    ],
    checks+: [
      'daily_average',
      'given_thickness',
      'has_bitmap',
      'resolution_s2s',
    ],
  },
  templates.Wmo {
    name: 'snow_depth_water_equivalent_sfc.glob.s2',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'values', min: [-1e-05, 0], max: [100, 15000] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'class', value: 's2' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 60 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'daily_average',
      'predefined_level',
      'resolution_s2s',
    ],
  },
  templates.Wmo {
    name: 'snow_depth_water_equivalent_sfc.glob.s2.cwao',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'centre', value: 1 },
      { key: 'values', min: [-4e-19, 0], max: [100, 40000] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'class', value: 's2' },
      { key: 'centre', value: 'cwao' },
      { key: 'paramId', value: 228141 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 60 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'daily_average',
      'predefined_level',
      'resolution_s2s',
    ],
  },
  templates.Wmo {
    name: 'total_cloud_cover_sfc.glob.s2',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'values', min: [-0.1, 5], max: [90.0, 101.0] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'class', value: 's2' },
      { key: 'paramId', value: 228164 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 6 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 8 },
    ],
    checks+: [
      'daily_average',
      'predefined_thickness',
      'resolution_s2s',
    ],
  },
  templates.Wmo {
    name: 'total_cloud_cover_sfc.glob.s2.lfpw',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'centre', value: 1 },
      { key: 'step', value: 1 },
      { key: 'values', min: [-0.1, 5], max: [70.0, 101.0] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'class', value: 's2' },
      { key: 'centre', value: 'lfpw' },
      { key: 'step', value: '0-24' },
      { key: 'paramId', value: 228164 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 6 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 8 },
    ],
    checks+: [
      'daily_average',
      'predefined_thickness',
      'resolution_s2s',
    ],
  },
  templates.Wmo {
    name: 'convective_precipitation_sfc.glob',
    expected+: [
      { key: 'values', min: [-0.05, 0.1], max: [0.0, 100.0] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'paramId', value: 228143 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 37 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'sea_ice_cover_sfc.glob.s2',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'values', min: [-1500000.0, 1500000.0], max: [-1500000.0, 1500000.0] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'class', value: 's2' },
      { key: 'paramId', value: 31 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
      { key: 'discipline', value: 10 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'daily_average',
      'predefined_level',
      'has_bitmap',
      'resolution_s2s',
    ],
  },
  templates.Wmo {
    name: 'snow_density_sfc.glob.s2',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'values', min: [-1500000.0, 1500000.0], max: [-1500000.0, 1500000.0] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'class', value: 's2' },
      { key: 'paramId', value: 33 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 61 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'daily_average',
      'predefined_level',
      'resolution_s2s',
    ],
  },
  templates.Wmo {
    name: 'sea_surface_temperature_sfc.glob.s2',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'values', min: [180, 290], max: [260, 320] },
    ],
    pairs+: [
      { key: 'model', value: 'glob' },
      { key: 'class', value: 's2' },
      { key: 'paramId', value: 34 },
      { key: 'typeOfStatisticalProcessing', value: 0 },
      { key: 'discipline', value: 10 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'daily_average',
      'predefined_level',
      'has_bitmap',
      'resolution_s2s',
    ],
  },
//templates.Wmo {
 // name: 'snow_albedo_sfc.glob',
//  expected+: [
//    { key: 'values', min: [-1500000.0, 1500000.0], max: [-1500000.0, 1500000.0] },
//  ],
//  pairs+: [
//    { key: 'model', value: 'glob' },
//    { key: 'paramId', value: 228032 },
//    { key: 'typeOfStatisticalProcessing', value: 0 },
//    { key: 'discipline', value: 0 },
//    { key: 'parameterCategory', value: 19 },
//    { key: 'parameterNumber', value: 19 },
//    { key: 'typeOfFirstFixedSurface', value: 1 },
 // ],
 // checks+: [
//    'daily_average',
//    'predefined_level',
//    'has_bitmap',
//  ],
//},
  templates.Wmo {
    name: 'high_cloud_cover_sfc',
    expected+: [
      { key: 'values', min: [0, 1e-10], max: [0.9999, 100.00001] },
    ],
    pairs+: [
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
    name: 'medium_cloud_cover_sfc',
    expected+: [
      { key: 'values', min: [0, 1e-10], max: [0.9999, 100.00001] },
    ],
    pairs+: [
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
    name: 'low_cloud_cover_sfc',
    expected+: [
      { key: 'values', min: [0, 1e-10], max: [0.9999, 100.00001] },
    ],
    pairs+: [
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
    name: 'low_cloud_cover_sfc.egrr',
    expected+: [
      { key: 'values', min: [0, 1e-10], max: [0.9999, 400.00001] },
    ],
    pairs+: [
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
    name: 'pressure_ml',
    expected+: [
      { key: 'values', min: [100, 100000], max: [100, 108000] },
    ],
    pairs+: [
      { key: 'paramId', value: 54 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 105 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'pressure_ml.edzw',
    expected+: [
      { key: 'origin', value: 0 },
      { key: 'values', min: [100, 100000], max: [100, 108000] },
    ],
    pairs+: [
      { key: 'paramId', value: 54 },
      { key: 'origin', value: 'edzw' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 118 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'specific_humidity_ml',
    expected+: [
      { key: 'values', min: [-0.1, 0.01], max: [0, 0.1] },
    ],
    pairs+: [
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 105 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'specific_humidity_ml.edzw',
    expected+: [
      { key: 'origin', value: 0 },
      { key: 'values', min: [-0.1, 0.01], max: [0, 0.1] },
    ],
    pairs+: [
      { key: 'paramId', value: 133 },
      { key: 'origin', value: 'edzw' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 118 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'temperature_ml',
    expected+: [
      { key: 'values', min: [150, 300], max: [200, 330] },
    ],
    pairs+: [
      { key: 'paramId', value: 130 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 105 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'temperature_ml.edzw',
    expected+: [
      { key: 'origin', value: 0 },
      { key: 'values', min: [150, 300], max: [200, 330] },
    ],
    pairs+: [
      { key: 'paramId', value: 130 },
      { key: 'origin', value: 'edzw' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 118 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'u_velocity_ml',
    expected+: [
      { key: 'values', min: [-200, 10], max: [0.1, 200] },
    ],
    pairs+: [
      { key: 'paramId', value: 131 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 2 },
      { key: 'typeOfFirstFixedSurface', value: 105 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'u_velocity_ml.edzw',
    expected+: [
      { key: 'origin', value: 0 },
      { key: 'values', min: [-200, 10], max: [0.1, 200] },
    ],
    pairs+: [
      { key: 'paramId', value: 131 },
      { key: 'origin', value: 'edzw' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 2 },
      { key: 'typeOfFirstFixedSurface', value: 118 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'v_velocity_ml',
    expected+: [
      { key: 'values', min: [-200, -1], max: [1, 200] },
    ],
    pairs+: [
      { key: 'paramId', value: 132 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 3 },
      { key: 'typeOfFirstFixedSurface', value: 105 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'v_velocity_ml.edzw',
    expected+: [
      { key: 'origin', value: 0 },
      { key: 'values', min: [-200, -1], max: [1, 200] },
    ],
    pairs+: [
      { key: 'paramId', value: 132 },
      { key: 'origin', value: 'edzw' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 3 },
      { key: 'typeOfFirstFixedSurface', value: 118 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'cloud_cover_ml',
    expected+: [
      { key: 'values', min: [0, 1e-10], max: [0, 100.00001] },
    ],
    pairs+: [
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 6 },
      { key: 'parameterNumber', value: 22 },
      { key: 'typeOfFirstFixedSurface', value: 105 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'cloud_cover_ml.edzw',
    expected+: [
      { key: 'origin', value: 0 },
      { key: 'values', min: [0, 1e-10], max: [0, 100.00001] },
    ],
    pairs+: [
      { key: 'paramId', value: 260257 },
      { key: 'origin', value: 'edzw' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 6 },
      { key: 'parameterNumber', value: 22 },
      { key: 'typeOfFirstFixedSurface', value: 118 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'specific_cloud_ice_water_content_pl',
    expected+: [
      { key: 'values', min: [0, 0.001], max: [0, 0.01] },
    ],
    pairs+: [
      { key: 'paramId', value: 247 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 84 },
      { key: 'typeOfFirstFixedSurface', value: 100 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'cloud_cover_pl.glob',
    expected+: [
      { key: 'values', min: [0, 1e-10], max: [100, 100.00001] },
    ],
    pairs+: [
      { key: 'paramId', value: 260257 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 6 },
      { key: 'parameterNumber', value: 22 },
      { key: 'typeOfFirstFixedSurface', value: 100 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'specific_cloud_liquid_water_content_pl',
    expected+: [
      { key: 'values', min: [0, 100000.0], max: [0, 1000000.0] },
    ],
    pairs+: [
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 83 },
      { key: 'typeOfFirstFixedSurface', value: 100 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'specific_cloud_ice_water_content_ml',
    expected+: [
      { key: 'values', min: [0, 0.001], max: [0, 0.01] },
    ],
    pairs+: [
      { key: 'paramId', value: 247 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 84 },
      { key: 'typeOfFirstFixedSurface', value: 105 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'specific_cloud_ice_water_content_ml.edzw',
    expected+: [
      { key: 'origin', value: 0 },
      { key: 'values', min: [0, 0.001], max: [0, 0.01] },
    ],
    pairs+: [
      { key: 'paramId', value: 247 },
      { key: 'origin', value: 'edzw' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 84 },
      { key: 'typeOfFirstFixedSurface', value: 118 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'specific_cloud_liquid_water_content_ml',
    expected+: [
      { key: 'values', min: [0, 100000.0], max: [0, 1000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 246 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 83 },
      { key: 'typeOfFirstFixedSurface', value: 105 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'specific_cloud_liquid_water_content_ml.edzw',
    expected+: [
      { key: 'origin', value: 0 },
      { key: 'values', min: [0, 100000.0], max: [0, 1000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 246 },
      { key: 'origin', value: 'edzw' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 83 },
      { key: 'typeOfFirstFixedSurface', value: 118 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'relative_humidity_pl',
    expected+: [
      { key: 'values', min: [0, 30], max: [0, 180] },
    ],
    pairs+: [
      { key: 'paramId', value: 157 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 100 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'cloud_cover_hl',
    expected+: [
      { key: 'values', min: [0, 1e-10], max: [80, 100.00001] },
    ],
    pairs+: [
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 6 },
      { key: 'parameterNumber', value: 22 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'height_level',
    ],
  },
  templates.Wmo {
    name: 'pressure_hl',
    expected+: [
      { key: 'values', min: [100, 100000], max: [100, 108000] },
    ],
    pairs+: [
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'height_level',
    ],
  },
  templates.Wmo {
    name: 'specific_cloud_liquid_water_content_hl',
    expected+: [
      { key: 'values', min: [0, 100000.0], max: [0, 1000000.0] },
    ],
    pairs+: [
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 83 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'height_level',
    ],
  },
  templates.Wmo {
    name: 'specific_cloud_ice_water_content_hl',
    expected+: [
      { key: 'values', min: [0, 0.001], max: [0, 0.01] },
    ],
    pairs+: [
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 84 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'height_level',
    ],
  },
  templates.Wmo {
    name: 'relative_humidity_hl',
    expected+: [
      { key: 'values', min: [0, 40], max: [1, 160] },
    ],
    pairs+: [
      { key: 'paramId', value: 157 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'height_level',
    ],
  },
  templates.Wmo {
    name: 'temperature_hl',
    expected+: [
      { key: 'values', min: [150, 300], max: [200, 330] },
    ],
    pairs+: [
      { key: 'paramId', value: 130 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'height_level',
    ],
  },
  templates.Wmo {
    name: 'wind_speed_hl',
    expected+: [
      { key: 'values', min: [0, 10], max: [10, 150] },
    ],
    pairs+: [
      { key: 'paramId', value: 10 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'height_level',
    ],
  },
  templates.Wmo {
    name: 'wind_direction_hl',
    expected+: [
      { key: 'values', min: [0, 1], max: [359, 360.1] },
    ],
    pairs+: [
      { key: 'paramId', value: 3031 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'height_level',
    ],
  },
  templates.Wmo {
    name: 'percolation_sfc',
    expected+: [
      { key: 'values', min: [0, 1], max: [0.8, 30] },
    ],
    pairs+: [
      { key: 'paramId', value: 260430 },
      { key: 'discipline', value: 1 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 16 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 177 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: '2_metre_relative_humidity',
    expected+: [
      { key: 'values', min: [0, 25], max: [90, 160] },
    ],
    pairs+: [
      { key: 'paramId', value: 260242 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'surface_runoff',
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
    name: 'albedo_sfc',
    expected+: [
      { key: 'values', min: [0, 20], max: [60, 100] },
    ],
    pairs+: [
      { key: 'paramId', value: 260509 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 19 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'albedo_sfc.uerra-egrr',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'centre', value: 1 },
      { key: 'values', min: [0, 20], max: [0, 100] },
    ],
    pairs+: [
      { key: 'class', value: 'ur' },
      { key: 'centre', value: 'egrr' },
      { key: 'paramId', value: 260509 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 19 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'time_integrated_surface_clear-sky_solar_radiation_downwards',
    expected+: [
      { key: 'values', min: [-0.1, 100000000.0], max: [0, 1000000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260423 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 4 },
      { key: 'parameterNumber', value: 52 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time_integrated_surface_clear-sky_solar_radiation_upwards',
    expected+: [
      { key: 'values', min: [-0.1, 100000000.0], max: [0, 1000000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260427 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 4 },
      { key: 'parameterNumber', value: 53 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time_integrated_surface_clear-sky_thermal_radiation_downwards',
    expected+: [
      { key: 'values', min: [-0.1, 100000000.0], max: [0, 1000000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260428 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 5 },
      { key: 'parameterNumber', value: 8 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time_integrated_surface_direct_solar_radiation',
    expected+: [
      { key: 'values', min: [-10, 100000000.0], max: [0, 1000000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260264 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 4 },
      { key: 'parameterNumber', value: 13 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time_integrated_surface_net_solar_radiation_sfc.lam',
    expected+: [
      { key: 'values', min: [-0.1, 100000000.0], max: [0, 1000000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 176 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 4 },
      { key: 'parameterNumber', value: 9 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: '10_metre_wind_speed',
    expected+: [
      { key: 'values', min: [0, 10], max: [10, 300] },
    ],
    pairs+: [
      { key: 'paramId', value: 207 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 10 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: '10_metre_wind_direction',
    expected+: [
      { key: 'values', min: [0, 0.1], max: [359.0, 360.01] },
    ],
    pairs+: [
      { key: 'paramId', value: 260260 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 10 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: '10_metre_wind_gust_since_pp',
    expected+: [
      { key: 'values', min: [0.001, 10], max: [10, 150] },
    ],
    pairs+: [
      { key: 'paramId', value: 49 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 22 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 10 },
      { key: 'typeOfStatisticalProcessing', value: 2 },
    ],
    checks+: [
      'since_prev_pp',
      'given_level',
    ],
  },
  templates.Wmo {
    name: '2_metre_maximum_temperature',
    expected+: [
      { key: 'values', min: [200, 340], max: [200, 340] },
    ],
    pairs+: [
      { key: 'paramId', value: 201 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'typeOfStatisticalProcessing', value: 2 },
    ],
    checks+: [
      'since_prev_pp',
      'given_level',
    ],
  },
  templates.Wmo {
    name: '2_metre_minimum_temperature',
    expected+: [
      { key: 'values', min: [200, 340], max: [200, 340] },
    ],
    pairs+: [
      { key: 'paramId', value: 202 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'typeOfStatisticalProcessing', value: 3 },
    ],
    checks+: [
      'since_prev_pp',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'evaporation_sfc',
    expected+: [
      { key: 'values', min: [-10, 0], max: [0, 5] },
    ],
    pairs+: [
      { key: 'paramId', value: 260259 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 79 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'snow_depth_sfc',
    expected+: [
      { key: 'values', min: [0, 0], max: [0, 5] },
    ],
    pairs+: [
      { key: 'paramId', value: 3066 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 11 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'surface_roughness_sfc',
    expected+: [
      { key: 'values', min: [0, 0.001], max: [0.5, 10] },
    ],
    pairs+: [
      { key: 'paramId', value: 173 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'liquid_non-frozen_soil_moisture_level',
    expected+: [
      { key: 'values', min: [0, 0.1], max: [0.1, 1] },
    ],
    pairs+: [
      { key: 'paramId', value: 260210 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 10 },
      { key: 'typeOfFirstFixedSurface', value: 151 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'has_bitmap',
      'has_soil_level',
    ],
  },
  templates.Wmo {
    name: 'liquid_non-frozen_soil_moisture_layer',
    expected+: [
      { key: 'values', min: [0, 0.1], max: [0.1, 1] },
    ],
    pairs+: [
      { key: 'paramId', value: 260210 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 10 },
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
  templates.Wmo {
    name: 'volumetric_soil_moisture_level',
    expected+: [
      { key: 'values', min: [0, 0.1], max: [0.1, 1] },
    ],
    pairs+: [
      { key: 'paramId', value: 260199 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 25 },
      { key: 'typeOfFirstFixedSurface', value: 151 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'has_bitmap',
      'has_soil_level',
    ],
  },
  templates.Wmo {
    name: 'volumetric_soil_moisture_layer',
    expected+: [
      { key: 'values', min: [0, 0.1], max: [0.1, 1] },
    ],
    pairs+: [
      { key: 'paramId', value: 260199 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 25 },
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
  templates.Wmo {
    name: 'soil_heat_flux_sfc',
    expected+: [
      { key: 'values', min: [-1000, -10], max: [10, 1000] },
    ],
    pairs+: [
      { key: 'paramId', value: 260364 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 26 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'soil_temperature_level',
    expected+: [
      { key: 'values', min: [180, 270], max: [280, 350] },
    ],
    pairs+: [
      { key: 'paramId', value: 260360 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 18 },
      { key: 'typeOfFirstFixedSurface', value: 151 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'has_bitmap',
      'has_soil_level',
    ],
  },
  templates.Wmo {
    name: 'soil_temperature_layer',
    expected+: [
      { key: 'values', min: [200, 280], max: [285, 350] },
    ],
    pairs+: [
      { key: 'paramId', value: 260360 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 18 },
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
  templates.Wmo {
    name: 'cloud_cover_pl.lam',
    expected+: [
      { key: 'values', min: [0, 1e-10], max: [0, 100] },
    ],
    pairs+: [
      { key: 'paramId', value: 260257 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 6 },
      { key: 'parameterNumber', value: 22 },
      { key: 'typeOfFirstFixedSurface', value: 100 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'skin_temperature_sfc',
    expected+: [
      { key: 'values', min: [160, 300], max: [280, 355] },
    ],
    pairs+: [
      { key: 'paramId', value: 235 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 17 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'total_column_water_vapour_sfc',
    expected+: [
      { key: 'values', min: [-3.0, 10], max: [30, 150] },
    ],
    pairs+: [
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 64 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 8 },
    ],
    checks+: [
      'point_in_time',
      'predefined_thickness',
    ],
  },
  templates.Wmo {
    name: 'total_cloud_cover_sfc.ur.eswi',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'centre', value: 1 },
      { key: 'values', min: [0, 2e-10], max: [90.0, 100.0] },
    ],
    pairs+: [
      { key: 'class', value: 'ur' },
      { key: 'centre', value: 'eswi' },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 6 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 8 },
    ],
    checks+: [
      'point_in_time',
      'predefined_thickness',
    ],
  },
  templates.Wmo {
    name: 'soil_depth',
    expected+: [
      { key: 'values', min: [0.005, 100], max: [0.005, 100] },
    ],
    pairs+: [
      { key: 'paramId', value: 260367 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 27 },
      { key: 'typeOfFirstFixedSurface', value: 151 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'has_bitmap',
      'has_soil_level',
    ],
  },
  templates.Wmo {
    name: 'volumetric_field_capacity',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260211 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 11 },
    ],
    checks+: [
      'point_in_time',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'volumetric_wilting_point',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260200 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 27 },
    ],
    checks+: [
      'point_in_time',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'wind_speed_ml',
    expected+: [
      { key: 'values', min: [0, 10], max: [10, 150] },
    ],
    pairs+: [
      { key: 'paramId', value: 10 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 105 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'height_level',
    ],
  },
  templates.Wmo {
    name: 'wind_direction_ml',
    expected+: [
      { key: 'values', min: [0, 1], max: [359, 360.1] },
    ],
    pairs+: [
      { key: 'paramId', value: 3031 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 105 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'height_level',
    ],
  },
  templates.Wmo {
    name: 'specific_rain_water_content_ml',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 75 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 85 },
      { key: 'typeOfFirstFixedSurface', value: 105 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'specific_snow_water_content_ml',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 76 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 86 },
      { key: 'typeOfFirstFixedSurface', value: 105 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'graupel_ml',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260028 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 32 },
      { key: 'typeOfFirstFixedSurface', value: 105 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'turbulent_kinetic_energy_ml',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260155 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 19 },
      { key: 'parameterNumber', value: 11 },
      { key: 'typeOfFirstFixedSurface', value: 105 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'specific_rain_water_content_pl',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 75 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 85 },
      { key: 'typeOfFirstFixedSurface', value: 100 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'specific_snow_water_content_pl',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 76 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 86 },
      { key: 'typeOfFirstFixedSurface', value: 100 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'graupel_pl',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260028 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 32 },
      { key: 'typeOfFirstFixedSurface', value: 100 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'pseudo-adiabatic_potential_temperature_pl',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 3014 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 3 },
      { key: 'typeOfFirstFixedSurface', value: 100 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'geometric_vertical_velocity_pl',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260238 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 9 },
      { key: 'typeOfFirstFixedSurface', value: 100 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'potential_vorticity_pl',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 60 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 14 },
      { key: 'typeOfFirstFixedSurface', value: 100 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'visibility_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 3020 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 19 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'cloud_base_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260107 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 6 },
      { key: 'parameterNumber', value: 11 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'cloud_top_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260108 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 6 },
      { key: 'parameterNumber', value: 12 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'sea_ice_cover_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 31 },
      { key: 'discipline', value: 10 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'sea_surface_temperature_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 34 },
      { key: 'discipline', value: 10 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'precipitation_type_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260015 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 19 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'specific_rain_water_content_hl',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 75 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 85 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'height_level',
    ],
  },
  templates.Wmo {
    name: 'specific_snow_water_content_hl',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 76 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 86 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'height_level',
    ],
  },
  templates.Wmo {
    name: 'turbulent_kinetic_energy_hl',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260155 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 19 },
      { key: 'parameterNumber', value: 11 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'height_level',
    ],
  },
  templates.Wmo {
    name: '2_metre_specific_humidity_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 174096 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'time_integral_of_rain_flux_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 235015 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 65 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'total_column_cloud_liquid_water_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 78 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 69 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 8 },
    ],
    checks+: [
      'point_in_time',
      'predefined_thickness',
    ],
  },
  templates.Wmo {
    name: 'total_column_cloud_ice_water_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 79 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 70 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 8 },
    ],
    checks+: [
      'point_in_time',
      'predefined_thickness',
    ],
  },
  templates.Wmo {
    name: 'total_column_graupel_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260001 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 74 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 8 },
    ],
    checks+: [
      'point_in_time',
      'predefined_thickness',
    ],
  },
  templates.Wmo {
    name: 'direct_solar_radiation_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
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
    name: 'time_integral_of_top_net_solar_radiation_flux_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 178 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 4 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 8 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time_integral_of_surface_latent_heat_evaporation_flux_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 235019 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 30 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time_integral_of_surface_latent_heat_sublimation_flux_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 235071 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 31 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time_integral_of_surface_eastward_momentum_flux_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 235017 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 17 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time_integral_of_surface_northward_momentum_flux_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 235018 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 18 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time_integral_of_total_solid_precipitation_flux_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260645 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 128 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time_integral_of_snow_evaporation_flux_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 235072 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 192 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'localTablesVersion', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: '10_metre_eastward_wind_gust_since_pp_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260646 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 23 },
      { key: 'typeOfStatisticalProcessing', value: 2 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 10 },
    ],
    checks+: [
      'since_prev_pp',
      'given_level',
    ],
  },
  templates.Wmo {
    name: '10_metre_northward_wind_gust_since_pp_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260647 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 24 },
      { key: 'typeOfStatisticalProcessing', value: 2 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 10 },
    ],
    checks+: [
      'since_prev_pp',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'fog_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260648 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 6 },
      { key: 'parameterNumber', value: 50 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'snow_on_ice_total_depth_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260650 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 11 },
      { key: 'typeOfFirstFixedSurface', value: 174 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'fraction_of_snow_cover_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260289 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 121 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'snow_albedo_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 228032 },
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
    name: 'temperature_of_snow_layer_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 238 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 28 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'sea_ice_thickness_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 174098 },
      { key: 'discipline', value: 10 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 160 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'sea_ice_surface_temperature_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260649 },
      { key: 'discipline', value: 10 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 8 },
      { key: 'typeOfFirstFixedSurface', value: 174 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'surface_roughness_length_for_heat',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260651 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 192 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'localTablesVersion', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'volumetric_soil_ice_layer',
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
  templates.Wmo {
    name: 'time_integral_of_evapotranspiration_flux_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 235073 },
      { key: 'discipline', value: 2 },
      { key: 'parameterCategory', value: 0 },
      { key: 'parameterNumber', value: 39 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'snow_melt_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 3099 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 16 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'lake_total_layer_temperature_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 228011 },
      { key: 'discipline', value: 1 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 162 },
    ],
    checks+: [
      'point_in_time',
      'predefined_thickness',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'lake_mix_layer_temperature_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 228008 },
      { key: 'discipline', value: 1 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 166 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'lake_mix_layer_depth_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 228009 },
      { key: 'discipline', value: 1 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 166 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'lake_bottom_temperature_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 228010 },
      { key: 'discipline', value: 1 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 162 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'lake_shape_factor_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 228012 },
      { key: 'discipline', value: 1 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 10 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'lake_ice_surface_temperature_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 228013 },
      { key: 'discipline', value: 1 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 6 },
      { key: 'typeOfFirstFixedSurface', value: 174 },
    ],
    checks+: [
      'point_in_time',
      'predefined_level',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'lake_ice_total_depth_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 228014 },
      { key: 'discipline', value: 1 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 5 },
      { key: 'typeOfFirstFixedSurface', value: 174 },
      { key: 'typeOfSecondFixedSurface', value: 176 },
    ],
    checks+: [
      'point_in_time',
      'predefined_thickness',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'lake_total_depth_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 228007 },
      { key: 'discipline', value: 1 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 162 },
    ],
    checks+: [
      'point_in_time',
      'predefined_thickness',
      'has_bitmap',
    ],
  },
  templates.Wmo {
    name: 'momentum_flux_u_component_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260062 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 17 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'momentum_flux_v_component_sfc',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260063 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 18 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time_integrated_surface_clear-sky_net_solar_radiation',
    expected+: [
      { key: 'values', min: [-0.1, 100000000.0], max: [0, 1000000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 210 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 4 },
      { key: 'parameterNumber', value: 11 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time_integrated_surface_clear-sky_net_thermal_radiation',
    expected+: [
      { key: 'values', min: [-0.1, 100000000.0], max: [0, 1000000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 211 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 5 },
      { key: 'parameterNumber', value: 6 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'turbulent_kinetic_energy_pl',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 260155 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 19 },
      { key: 'parameterNumber', value: 11 },
      { key: 'typeOfFirstFixedSurface', value: 100 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'depth_of_20_C_isotherm_o2d.s2',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'class', value: 's2' },
      { key: 'paramId', value: 151163 },
      { key: 'discipline', value: 10 },
      { key: 'parameterCategory', value: 4 },
      { key: 'parameterNumber', value: 14 },
      { key: 'typeOfFirstFixedSurface', value: 20 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 2 },
      { key: 'scaledValueOfFirstFixedSurface', value: 29315 },
    ],
    checks+: [
      'daily_average',
      'given_level',
      'has_bitmap',
      'resolution_s2s_ocean',
    ],
  },
  templates.Wmo {
    name: 'average_salinity_in_the_upper_300_m_o2d.s2',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'class', value: 's2' },
      { key: 'paramId', value: 151175 },
      { key: 'discipline', value: 10 },
      { key: 'parameterCategory', value: 4 },
      { key: 'parameterNumber', value: 21 },
      { key: 'typeOfFirstFixedSurface', value: 160 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 0 },
      { key: 'typeOfSecondFixedSurface', value: 160 },
      { key: 'scaleFactorOfSecondFixedSurface', value: 0 },
      { key: 'scaledValueOfSecondFixedSurface', value: 300 },
    ],
    checks+: [
      'daily_average',
      'given_thickness',
      'has_bitmap',
      'resolution_s2s_ocean',
    ],
  },
  templates.Wmo {
    name: 'mean_sea_water_temperature_in_the_upper_300_m_o2d.s2',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'class', value: 's2' },
      { key: 'paramId', value: 151127 },
      { key: 'discipline', value: 10 },
      { key: 'parameterCategory', value: 4 },
      { key: 'parameterNumber', value: 15 },
      { key: 'typeOfFirstFixedSurface', value: 160 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 0 },
      { key: 'typeOfSecondFixedSurface', value: 160 },
      { key: 'scaleFactorOfSecondFixedSurface', value: 0 },
      { key: 'scaledValueOfSecondFixedSurface', value: 300 },
    ],
    checks+: [
      'daily_average',
      'given_thickness',
      'has_bitmap',
      'resolution_s2s_ocean',
    ],
  },
  templates.Wmo {
    name: 'mean_sea_water_potential_temperature_in_the_upper_300_m_o2d.s2',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'class', value: 's2' },
      { key: 'paramId', value: 151126 },
      { key: 'discipline', value: 10 },
      { key: 'parameterCategory', value: 4 },
      { key: 'parameterNumber', value: 18 },
      { key: 'typeOfFirstFixedSurface', value: 160 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 0 },
      { key: 'typeOfSecondFixedSurface', value: 160 },
      { key: 'scaleFactorOfSecondFixedSurface', value: 0 },
      { key: 'scaledValueOfSecondFixedSurface', value: 300 },
    ],
    checks+: [
      'daily_average',
      'given_thickness',
      'has_bitmap',
      'resolution_s2s_ocean',
    ],
  },
  templates.Wmo {
    name: 'ocean_mixed_layer_thickness_defined_by_sigma_theta_0.01_kg/m3_o2d.s2',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'class', value: 's2' },
      { key: 'paramId', value: 151225 },
      { key: 'discipline', value: 10 },
      { key: 'parameterCategory', value: 4 },
      { key: 'parameterNumber', value: 14 },
      { key: 'typeOfFirstFixedSurface', value: 169 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 2 },
      { key: 'scaledValueOfFirstFixedSurface', value: 1 },
    ],
    checks+: [
      'daily_average',
      'given_level',
      'has_bitmap',
      'resolution_s2s_ocean',
    ],
  },
  templates.Wmo {
    name: 'eastward_sea_water_velocity_o2d.s2',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'class', value: 's2' },
      { key: 'paramId', value: 151131 },
      { key: 'discipline', value: 10 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 2 },
      { key: 'typeOfFirstFixedSurface', value: 160 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'daily_average',
      'given_level',
      'has_bitmap',
      'resolution_s2s_ocean',
    ],
  },
  templates.Wmo {
    name: 'northward_sea_water_velocity_o2d.s2',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'class', value: 's2' },
      { key: 'paramId', value: 151132 },
      { key: 'discipline', value: 10 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 3 },
      { key: 'typeOfFirstFixedSurface', value: 160 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'daily_average',
      'given_level',
      'has_bitmap',
      'resolution_s2s_ocean',
    ],
  },
  templates.Wmo {
    name: 'sea-ice_thickness_o2d.s2',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'class', value: 's2' },
      { key: 'paramId', value: 174098 },
      { key: 'discipline', value: 10 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 160 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'daily_average',
      'given_level',
      'has_bitmap',
      'resolution_s2s_ocean',
    ],
  },
  templates.Wmo {
    name: 'sea_surface_height_o2d.s2',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'class', value: 's2' },
      { key: 'paramId', value: 151145 },
      { key: 'discipline', value: 10 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 160 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'daily_average',
      'given_level',
      'has_bitmap',
      'resolution_s2s_ocean',
    ],
  },
  templates.Wmo {
    name: 'sea_surface_practical_salinity_o2d.s2',
    expected+: [
      { key: 'class', value: 0 },
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'class', value: 's2' },
      { key: 'paramId', value: 151219 },
      { key: 'discipline', value: 10 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 3 },
      { key: 'typeOfFirstFixedSurface', value: 160 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
      { key: 'scaledValueOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'daily_average',
      'given_level',
      'has_bitmap',
      'resolution_s2s_ocean',
    ],
  },
]
