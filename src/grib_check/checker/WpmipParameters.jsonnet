local templates = import 'Parameter.libsonnet';
[
  templates.Wmo {
    name: 'total_precipitation_sfc.wpmip',
    expected+: [
      { key: 'values', min: [-0.05, 0.1], max: [0.0, 500.0] },
    ],
    pairs+: [
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
    name: 'orography_sfc.wpmip',
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
    name: 'mean_sea_level_pressure_sfc.wpmip',
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
    name: 'time_integrated_surface_net_thermal_radiation_downwards_sfc.wpmip',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
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
    name: 'time_integral_of_top_net_solar_radiation_flux_sfc.wpmip',
    expected+: [
      { key: 'values', min: [-1e+5, 1e+05], max: [1e+05, 8e+06] },
    ],
    pairs+: [
      { key: 'paramId', value: 178 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 4 },
      { key: 'parameterNumber', value: 9 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 8 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time_integrated_top_net_thermal_radiation_sfc.wpmip',
    expected+: [
      { key: 'values', min: [-4e+06, -8e+5], max: [-1.8e+6, -2e+5] },
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
    name: 'time_integrated_top_solar_radiation_sfc.wpmip',
    expected+: [
      { key: 'values', min: [0.0, 100000000.0], max: [0.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 212 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 4 },
      { key: 'parameterNumber', value: 7 },
      { key: 'typeOfStatisticalProcessing', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 8 },
    ],
    checks+: [
      'from_start',
      'predefined_level',
    ],
  },
  templates.Wmo {
    name: 'time_integrated_surface_sensible_heat_flux_sfc.wpmip',
    expected+: [
      { key: 'values', min: [-1e+8, 0], max: [0, 1e+8] },
    ],
    pairs+: [
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
    name: 'time_integrated_surface_latent_heat_flux_sfc.wpmip',
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
    name: 'land_sea_mask_sfc.wpmip',
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
    name: 'time_integrated_surface_net_solar_radiation_sfc.wpmip',
    expected+: [
      { key: 'values', min: [-1e+5, 1e+05], max: [1e+05, 8e+06] },
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
    name: 'surface_pressure_sfc.wpmip',
    expected+: [
      { key: 'values', min: [48000, 80000], max: [101500, 115000] },
    ],
    pairs+: [
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
    name: '2_metre_specific_humidity_sfc.wpmip',
    expected+: [
      { key: 'values', min: [0, 2], max: [0, 2] },
    ],
    pairs+: [
      { key: 'paramId', value: 174096 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 1 },
      { key: 'parameterNumber', value: 0 },
      { key: 'typeOfFirstFixedSurface', value: 103 },
      { key: 'scaledValueOfFirstFixedSurface', value: 2 },
      { key: 'scaleFactorOfFirstFixedSurface', value: 0 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
    ],
  },
  templates.Wmo {
    name: 'sea_surface_temperature_sfc.wpmip',
    expected+: [
      { key: 'values', min: [170, 290], max: [270, 360] },
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
    ],
  },
  templates.Wmo {
    name: 'sea_ice_area_fraction_sfc.wpmip',
    expected+: [
      { key: 'values', min: [0, 1], max: [0, 1] },
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
    ],
  },
  templates.Wmo {
    name: 'surface_air_temperature_sfc.wpmip',
    expected+: [
      { key: 'values', min: [170, 290], max: [270, 360] },
    ],
    pairs+: [
      { key: 'paramId', value: 167 },
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
    name: 'surface_air_dew_point_temperature_sfc.wpmip',
    expected+: [
      { key: 'values', min: [30, 290], max: [270, 350] },
    ],
    pairs+: [
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
    name: 'total_cloud_cover_sfc.wpmip',
    expected+: [
      { key: 'values', min: [-0.1, 5], max: [90.0, 101.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 228164 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 6 },
      { key: 'parameterNumber', value: 1 },
      { key: 'typeOfFirstFixedSurface', value: 1 },
      { key: 'typeOfSecondFixedSurface', value: 8 },
    ],
    checks+: [
      'predefined_thickness',
    ],
  },
  templates.Wmo {
    name: 'low_cloud_cover_sfc.wpmip',
    expected+: [
      { key: 'values', min: [-0.1, 5], max: [90.0, 101.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 3073 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 6 },
      { key: 'parameterNumber', value: 3 },
    ],
    checks+: [
    ],
  },
  templates.Wmo {
    name: 'high_cloud_cover_sfc.wpmip',
    expected+: [
      { key: 'values', min: [-0.1, 5], max: [90.0, 101.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 3075 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 6 },
      { key: 'parameterNumber', value: 5 },
    ],
    checks+: [
    ],
  },
  templates.Wmo {
    name: 'medium_cloud_cover_sfc.wpmip',
    expected+: [
      { key: 'values', min: [-0.1, 5], max: [90.0, 101.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 3074 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 6 },
      { key: 'parameterNumber', value: 4 },
    ],
    checks+: [
    ],
  },
  templates.Wmo {
    name: 'time_integrated_short_wave_(solar)_radiation_downwards_sfc.wpmip',
    expected+: [
      { key: 'values', min: [-10, 1.6e+05], max: [1e+06, 1e+07] },
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
    name: 'sea_ice_thickness_sfc.wpmip',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
      { key: 'paramId', value: 262000 },
      { key: 'discipline', value: 10 },
      { key: 'parameterCategory', value: 2 },
      { key: 'parameterNumber', value: 1 },
    ],
    checks+: [
      'point_in_time',
    ],
  },
  templates.Wmo {
    name: '10_meter_u_velocity_sfc.wpmip',
    expected+: [
      { key: 'values', min: [-100, -1], max: [1, 100] },
    ],
    pairs+: [
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
    name: '10_meter_v_velocity_sfc.wpmip',
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
    name: 'time_integrated_surface_net_thermal_radiation_sfc.wpmip',
    expected+: [
      { key: 'values', min: [-100000000.0, 100000000.0], max: [-100000000.0, 100000000.0] },
    ],
    pairs+: [
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
    name: 'geopotential_pl.wpmip',
    expected+: [
      { key: 'values', min: [-5000, 40000], max: [200, 40000] },
    ],
    pairs+: [
      { key: 'paramId', value: 156 },
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
    name: 'geopotential_pl.wpmip',
    expected+: [
      { key: 'values', min: [-5000, 306000], max: [2000, 350000] },
    ],
    pairs+: [
      { key: 'paramId', value: 129 },
      { key: 'discipline', value: 0 },
      { key: 'parameterCategory', value: 3 },
      { key: 'parameterNumber', value: 4 },
    ],
    checks+: [
      'point_in_time',
      'given_level',
      'pressure_level',
    ],
  },
  templates.Wmo {
    name: 'temperature_pl.wpmip',
    expected+: [
      { key: 'values', min: [150, 275], max: [200, 330] },
    ],
    pairs+: [
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
    name: 'u_velocity_pl.wpmip',
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
    name: 'v_velocity_pl.wpmip',
    expected+: [
      { key: 'values', min: [-200, -2], max: [2, 200] },
    ],
    pairs+: [
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
    name: 'specific_humidity_pl.wpmip',
    expected+: [
      { key: 'values', min: [-0.1, 0.01], max: [0, 0.1] },
    ],
    pairs+: [
      { key: 'paramId', value: 133 },
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
]
