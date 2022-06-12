#if __name__ == '__main__':

from tigge_check import *

parameters = [
   [
      "10_meter_u_velocity_sfc.glob",
      -100,
      -1,
      1,
      100,
      [
         ["model", str, 0, "glob"],

         ["paramId", int, 165],

         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 2],

         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 10],
         ["typeOfFirstFixedSurface", int, 103],

         [None, ],
      ],
      [point_in_time, given_level],
   ],

   [
      "10_meter_u_velocity_sfc.lam",
      -100,
      -1,
      1,
      100,
      [
         ["model", str, 0, "lam"],

         ["paramId", int, 165],

         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 2],

         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 10],

         [None, ],
      ],
      [point_in_time, given_level],
   ],

#''' 
#   MOGREPS (origin = 1(mogreps-mo-eua))
#   2014-01-10: minimum limit for 10_meter_u_velocity_sfc changed to <-100,5> because of 2014010715_00+0000
#   2014-31-03: maximum changed from <1,100> because of forecasts from 27-31.3...
#   2014-31-03: minimum  maximum changed for u,v components changed to reflect better small UK domain..
#'''
   [
      "10_meter_u_velocity_sfc.lam.mogreps-mo-eua",
      -100,
      10,
      -10,
      100,
      [
         ["model", str, 0, "lam"],
         ["suiteName", str, 1, "mogreps-mo-eua"],

         ["paramId", int, 165],

         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 2],

         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 10],
         ["typeOfFirstFixedSurface", int, 103],

         [None, ],
      ],
      [point_in_time, given_level],
   ],

   [
      "10_meter_v_velocity_sfc.glob",
      -100,
      -1,
      1,
      100,
      [
         ["paramId", int, 166],

         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 3],

         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 10],
         [None, ],
      ],
      [point_in_time, given_level],
   ],

#''' 
#   MOGREPS (origin = 1(mogreps-mo-eua))  set up for 10_meter_u_velocity_sfc
#   2014-01-08: minimum limit for 10_meter_v_velocity_sfc changed to <-100,10> because of one early January forecast..
#   2014-31-03: minimum  maximum changed for u,v components changed to reflect better small UK domain..
#'''
   [
      "10_meter_v_velocity_sfc.lam.mogreps-mo-eua",
      -100,
      10,
      -10,
      100,
      [
         ["model", str, 0, "lam"],
         ["suiteName", str, 1, "mogreps-mo-eua"],

         ["paramId", int, 166],

         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 3],

         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 10],

         [None, ],
      ],
      [point_in_time, given_level],
   ],

   [
      "convective_available_potential_energy_sfc.glob",
      0,
      10,
      0,
      17000,
      [
         ["model", str, 0, "glob"],

         ["discipline", int, 0],
         ["parameterCategory", int, 7],
         ["parameterNumber", int, 6],

         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 8],
         [None, ],
      ],
      [point_in_time, predefined_thickness],
   ],

#'''
#    2014-07-24: upper limit for cape minimum changed to <0,100> due to tigge_lam.LAEF_4tigge_08+0036.grib2, field 2 [convective_available_potential_energy_sfc.lam]: convective_available_potential_energy_sfc.lam minimum value 16.2219 is not in [0,10]
#'''
   [
      "convective_available_potential_energy_sfc.lam",
      0,
      100,
      0,
      17000,
      [
         ["model", str, 0, "lam"],

         ["paramId", int, 59],

         ["discipline", int, 0],
         ["parameterCategory", int, 7],
         ["parameterNumber", int, 6],

         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 8],
         [None, ],
      ],
      [point_in_time, predefined_thickness],
   ],

   [
      "convective_available_potential_energy_sfc.lam.glameps-hirlamcons-eu",
      -1000,
      10,
      0,
      17000,
      [
         ["model", str, 0, "lam"],
         ["suiteName", str, 9, "glameps-hirlamcons-eu"],

         ["paramId", int, 59],

         ["discipline", int, 0],
         ["parameterCategory", int, 7],
         ["parameterNumber", int, 6],

         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 8],
         [None, ],
      ],
      [point_in_time, predefined_thickness],
   ],

   [
      "convective_inhibition_sfc.glob",
      -60000,
      0,
      -10,
      5,
      [
         ["model", str, 0, "glob"],

         ["discipline", int, 0],
         ["parameterCategory", int, 7],
         ["parameterNumber", int, 7],

         ["typeOfFirstFixedSurface", int, 1],

         ["typeOfSecondFixedSurface", int, 8],
         [None, ],
      ],
      [point_in_time, predefined_thickness],
   ],
#''' 
#   eggr                  (centre=74, model=1) cin max ~ -30000
#   aladinhuneps-omsz-eu  (origin=12) cin max ~ <-60000,1>
#   aladinlaef-zamg-eu    (origin=)   cin max ~ <-...,1>
#   cosmodeeps-dwd-eu (origin=7)
#   2014-07-24: max upper limit change to <0, 4000> => tigge_lam.2014062818_slevels_lfff00000000.m011.grib2: convective_inhibition_sfc.lam.cosmodeeps-dwd-eu maximum value 3041.35 is not in [0,2000]
#'''
   [
      "convective_inhibition_sfc.lam",
      -60000,
      1,
      -10,
      4000,
      [
         ["model", str, 0, "lam"],

         ["paramId", int, 228001],

         ["discipline", int, 0],
         ["parameterCategory", int, 7],
         ["parameterNumber", int, 7],

         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 8],
         [None, ],
      ],
      [point_in_time, predefined_thickness],
   ],
   
   [
      "field_capacity_sfc",
      1e99,
      -1e99,
      99,
      -99,
      [
         ["model", str, 0, "glob"],
         ["discipline", int, 2],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 12],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaleFactorOfSecondFixedSurface", int, 1],
         ["scaledValueOfFirstFixedSurface", int, 0],
         ["scaledValueOfSecondFixedSurface", int, 2],
         ["typeOfFirstFixedSurface", int, 106],
         ["typeOfSecondFixedSurface", int, 106],
         [None, ],
      ],
      [point_in_time, given_thickness, has_bitmap],
   ],

   [
      "land_sea_mask_sfc.glob",
      0,
      0,
      1,
      1,
      [
         ["paramId", int, 172],

         ["discipline", int, 2],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 0],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level],
   ],

   [
      "land_sea_mask_sfc.lam.hirlam-dmi-eu",
      -0.001,
      0,
      1,
      1.11,
      [
         ["model", str, 0, "lam"],
         ["suiteName", str, 11, "hirlam-dmi-eu"],

         ["paramId", int, 172],

         ["discipline", int, 2],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 0],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level],
   ],

#''' 
#   MOGREPS (origin = 1(mogreps-mo-eua))
#   2014-01-08: limits for orog changed to <1000,8888>
#'''

   [
      "orography_sfc",
      -1300,
      0,
      1000,
      8888,
      [
        ["paramId", int, 228002],
        ["discipline", int, 0],
        ["parameterCategory", int, 3],
        ["parameterNumber", int, 5],
        ["typeOfFirstFixedSurface", int, 1],
        [None, ],
      ],
      [point_in_time, predefined_level],
   ],


   [
      "potential_temperature_pv",
      220,
      265,
      380,
      1200,
      [
         ["model", str, 0, "glob"],
         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 2],
         ["typeOfFirstFixedSurface", int, 109],
         [None, ],
      ],
      [point_in_time, given_level, potential_vorticity_level],
   ],

   [
      "potential_vorticity_pt",
      -0.005,
      -1e-6,
      1e-6,
      0.002,
      [
         ["model", str, 0, "glob"],
         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 14],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 320],
         ["typeOfFirstFixedSurface", int, 107],
         [None, ],
      ],
      [point_in_time, given_level, potential_temperature_level],
   ],

   [
      "snow_depth_water_equivalent_sfc",
      0,
      0,
      100,
      15000,
      [

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 60],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level],
   ],

   [
      "snow_fall_water_equivalent_sfc",
      -1.5e+6,
       1.5e+6,
      -1.5e+6,
       1.5e+6,
      [
         ["model", str, 0, "glob"],
         ["paramId", int, 228144],
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 53],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfStatisticalProcessing", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

   [
      "soil_moisture_sfc",
      -1e-19,
      0,
      450,
      800,
      [
         ["model", str, 0, "glob"],
         ["discipline", int, 2],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 22],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaleFactorOfSecondFixedSurface", int, 1],
         ["scaledValueOfFirstFixedSurface", int, 0],
         ["scaledValueOfSecondFixedSurface", int, 2],
         ["typeOfFirstFixedSurface", int, 106],
         ["typeOfSecondFixedSurface", int, 106],
         [None, ],
      ],
      [point_in_time, given_thickness, has_bitmap],
   ],

   [
      "soil_temperature_sfc",
      200,
      230,
      300,
      350,
      [
         ["model", str, 0, "glob"],
         ["discipline", int, 2],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 2],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaleFactorOfSecondFixedSurface", int, 1],
         ["scaledValueOfFirstFixedSurface", int, 0],
         ["scaledValueOfSecondFixedSurface", int, 2],
         ["typeOfFirstFixedSurface", int, 106],
         ["typeOfSecondFixedSurface", int, 106],
         [None, ],
      ],
      [point_in_time, given_thickness],
   ],
#''' 
#   S2S/CAWCR: specific_humidity_pl minimum value -0.0108485 is not in [-0.01,0.001]
#   s2s/ammc: warning: s2s.q_20160623_4.grib2, field 288 [specific_humidity_pl]: specific_humidity_pl minimum value -0.0209212 is not in [-0.02,0.001]
#   s2s/ammc: warning: s2s.q_20160717_21.grib2, field 99 [specific_humidity_pl]: specific_humidity_pl maximum value 0.0820876 is not in [5e-05,0.08]
#'''
   [
      "specific_humidity_pl",
      -1e-1,
      1.e-3,
      5e-5,
      1e-1,
      [
         ["model", str, 0, "glob"],
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 100],
         [None, ],
      ],
      [point_in_time, given_level, pressure_level],
   ],

   [
      "sunshine_duration_sfc",
      0,
      0,
      3600.00000001,
      3600.00000001,
      [
         ["model", str, 0, "glob"],
         ["discipline", int, 0],
         ["parameterCategory", int, 6],
         ["parameterNumber", int, 24],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfStatisticalProcessing", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

   [
      "surface_air_temperature_sfc.glob",
      180,
      290,
      270,
      350,
      [
         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 103],
         [None, ],
      ],
      [point_in_time, given_level],
   ],

#''' 
#   cosmodeeps-dwd-eu (origin=7)
#   2014-01-08: minimum limit for surface_air_dew_point_temperature_sfc changed to <160,290>
#   2014-11-06: glameps: tigge_lam.20141106_00+042.mem012.grib2, surface_air_dew_point_temperature_sfc.lam minimum value 128.003 is not in [160,290]
#     => [128.003,290]
#'''
   [
      "surface_air_dew_point_temperature_sfc.lam",
      110,
      290,
      270,
      350,
      [
         ["model", str, 0, "lam"],

         ["paramId", int, 168],

         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 6],

         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 2],
         [None, ],
      ],
      [point_in_time, given_level],
   ],

# mogreps specific set up! => 1.5m instead of 2m measurements 
   [
      "surface_air_dew_point_temperature_sfc.lam",
      110,
      290,
      270,
      350,
      [
         ["model", str, 0, "lam"],
         ["suiteName", str, 1, "mogreps-mo-eua"],

         ["paramId", int, 168],

         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 6],

         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 1],
         ["scaledValueOfFirstFixedSurface", int, 15],
         [None, ],
      ],
      [point_in_time, given_level],
   ],
#''' 
#   S2S/CAWCR: surface_air_maximum_temperature_sfc maximum value 359.388 is not in [300,330]
#s2s/kwbc/enfh: warning: s2s.z_s2s_c_rhmc_20150819000000_glob_prod_0006_000.sl.grib2, field 2 [surface_air_maximum_temperature_sfc]: surface_air_maximum_temperature_sfc minimum value 179.427 is not in [190,240]
#s2s/kwbc/enfh: warning: s2s.z_tigge_c_kwbc_20071002000000_ncep_prod_pf_sl_0006_001_0000_mx2t6.grib2, field 146 [surface_air_maximum_temperature_sfc]: surface_air_maximum_temperature_sfc minimum value 240.208 is not in [175,240]
#s2s/isac/enfo: warning: z_s2s_c_isac_201510190000_glob_prod_pf_0744_05.sl.grib2, field 513 [surface_air_maximum_temperature_sfc]: surface_air_maximum_temperature_sfc minimum value 245.143 is not in [175,245]
#s2s/lfpw/enfo: warning: s2s.lfpw_mx2t6_2.grib2, field 86 [surface_air_maximum_temperature_sfc]: surface_air_maximum_temperature_sfc minimum value 250.116 is not in [160,250]
#'''
   [
      "surface_air_maximum_temperature_sfc",
      160,
      255,
      300,
      380,
      [
         ["model", str, 0, "glob"],
         ["paramId", int, 121],
         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 103],
         ["typeOfStatisticalProcessing", int, 2],
         [None, ],
      ],
      [six_hourly, given_level],
   ],
#'''
#s2s_devel, ecmf, 20141222, 00UTC, test, enfo, real warning: s2s.2014122200.test.768.50.pf.sl.516.grib2, field 57 [surface_air_minimum_temperature_sfc]: surface_air_minimum_temperature_sfc maximum value 320.122 is not in [300,320]
#warning: s2s.z_tigge_c_kwbc_20090817000000_ncep_prod_pf_sl_0006_002_0000_mn2t6.grib2, field 100 [surface_air_minimum_temperature_sfc]: surface_air_minimum_temperature_sfc minimum value 188.577 is not in [190,240]
#s2s/kwbc/enfh: warning: s2s.z_s2s_c_rhmc_20150819000000_glob_prod_0006_000.sl.grib2, field 1 [surface_air_minimum_temperature_sfc]: surface_air_minimum_temperature_sfc minimum value 179.642 is not in [183,240]
#s2s/ammc/enfo: warning: s2s.mn2t6_20150917_24.grib2, field 1 [surface_air_minimum_temperature_sfc]: surface_air_minimum_temperature_sfc minimum value 167.556 is not in [175,240]
#s2s/isac/enfo: warning: z_s2s_c_isac_201510190000_glob_prod_pf_0744_24.sl.grib2, field 671 [surface_air_minimum_temperature_sfc]: surface_air_minimum_temperature_sfc minimum value 241.292 is not in [160,240]
#s2s/rums/enfh: warning: s2s.z_s2s_c_rhmc_19910316000000_glob_prod_009.sl.grib2, field 2204 [surface_air_minimum_temperature_sfc]: surface_air_minimum_temperature_sfc maximum value 325.122 is not in [300,325]
#s2s/lfpw/enfo: warning: s2s.lfpw_mn2t6_2.grib2, field 82 [surface_air_minimum_temperature_sfc]: surface_air_minimum_temperature_sfc minimum value 250.259 is not in [160,250]
#'''
   [
      "surface_air_minimum_temperature_sfc",
      160,
      260,
      300,
      330,
      [
         ["model", str, 0, "glob"],
         ["paramId", int, 122],
         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 103],
         ["typeOfStatisticalProcessing", int, 3],
         [None, ],
      ],
      [six_hourly, given_level],
   ],

#'''
#s2s/ammc: warning: s2s.mx2t6_20150910_4.grib2, field 200 [surface_air_maximum_temperature_sfc.ammc]: surface_air_maximum_temperature_sfc.ammc maximum value 1516.03 is not in [300,1500]
#s2s/ammc: warning: s2s.mx2t6_20151224_26.grib2, field 47 [surface_air_maximum_temperature_sfc.ammc]: surface_air_maximum_temperature_sfc.ammc maximum value 6963.63 is not in [300,5000]
#'''
   [
      "surface_air_maximum_temperature_sfc.ammc",
      175,
      240,
      300,
      10000,
      [
         ["model", str, 0, "glob"],
         ["centre", str, 1, "ammc"],
         ["paramId", int, 121],
         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 103],
         ["typeOfStatisticalProcessing", int, 2],
         [None, ],
      ],
      [six_hourly, given_level],
   ],

   [
      "time_integrated_top_net_thermal_radiation_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 179],
         ["discipline", int, 0],
         ["parameterCategory", int, 5],
         ["parameterNumber", int, 5],
         ["typeOfStatisticalProcessing", int, 1],
         ["typeOfFirstFixedSurface", int, 8],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

   [
      "time_integrated_surface_latent_heat_flux_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 147],
         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 10],
         ["typeOfStatisticalProcessing", int, 1],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],
#'''
# s2s/enfh/rums: warning: s2s.z_s2s_c_rhmc_19850217000000_glob_prod_1296_000.sl.grib2, field 24 [time_integrated_surface_net_solar_radiation_sfc]: time_integrated_surface_net_solar_radiation_sfc minimum value 20718.7 is not in [-0.1,20000]
# s2s/enfo/ammc: warning: s2s.ssr_20160807_25.grib2, field 62 [time_integrated_surface_net_solar_radiation_sfc]: time_integrated_surface_net_solar_radiation_sfc minimum value 10280.6 is not in [-0.1,10000]
# '''
   [
      "time_integrated_surface_net_solar_radiation_sfc.glob",
      -10,
      1e+05,
      1e+05,
      1e+07,
      [
         ["paramId", int, 176],
         ["discipline", int, 0],
         ["parameterCategory", int, 4],
         ["parameterNumber", int, 9],
         ["typeOfStatisticalProcessing", int, 1],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

   [
      "time_integrated_surface_net_solar_radiation_downwards_sfc",
      -10,
      1e+07,
      1e+05,
      1e+09,
      [
         ["paramId", int, 169],
         ["discipline", int, 0],
         ["parameterCategory", int, 4],
         ["parameterNumber", int, 7],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfStatisticalProcessing", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

   [
      "time_integrated_surface_net_thermal_radiation_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["model", str, 0, "glob"],
         ["paramId", int, 177],
         ["discipline", int, 0],
         ["parameterCategory", int, 5],
         ["parameterNumber", int, 5],
         ["typeOfStatisticalProcessing", int, 1],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

   [
      "time_integrated_surface_net_thermal_radiation_downwards_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["model", str, 0, "glob"],
         ["paramId", int, 175],
         ["discipline", int, 0],
         ["parameterCategory", int, 5],
         ["parameterNumber", int, 3],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfStatisticalProcessing", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

   [
      "time_integrated_surface_sensible_heat_flux_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["model", str, 0, "glob"],
         ["paramId", int, 146],
         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 11],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfStatisticalProcessing", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

   [
      "total_cloud_cover_sfc",
      0,
      1e-10,
      100,
      100.00001,
      [
         ["model", str, 0, "glob"],
         ["discipline", int, 0],
         ["parameterCategory", int, 6],
         ["parameterNumber", int, 1],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 8],
         [None, ],
      ],
      [point_in_time, predefined_thickness],
   ],

#'''
#   hourly extreems for cumulated parameters!

#   - TBD: the problem is that for tigge/tigge-lam there are cumulated parameters from step 0 and
#          the limits for e.g. 0-3 period should be very different to ones for e.g. 0-120 even
#          the value is divided by the period length in hours!
#'''

   [
      "total_precipitation_sfc.glob",
      -0.05,
      0.1,
      0.,
      100.,
      [
         ["model", str, 0, "glob"],

         ["paramId", int, 228228],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 52],

         ["typeOfStatisticalProcessing", int, 1],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

#'''
#   2013-xx-yy: maximum changed to <0,133> because of cosmo-de boundary effects when coupled with IFS ..
#   glameps: warning: tigge_lam.20160814_00+006.mem026.grib2, field 6 [total_precipitation_sfc.lam]: total_precipitation_sfc.lam maximum value 361.151 is not in [0,350]
#'''

   [
      "total_precipitation_sfc.lam",
      -0.05,
      0.1,
      0.,
      400.,
      [
         ["model", str, 0, "lam"],

         ["paramId", int, 228228],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 52],

         ["typeOfStatisticalProcessing", int, 1],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

#hourly extreems for cumulated parameters! 
   [
      "large_scale_precipitation_sfc.glob",
      -0.05,
      0.1,
      0.0,
      100.,
      [
         ["model", str, 0, "glob"],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 54],

         ["typeOfStatisticalProcessing", int, 1],

         ["typeOfFirstFixedSurface", int, 1],

         ["typeOfSecondFixedSurface", int, 255],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

#'''
#   glameps-hirlamcons-eu: warning: tigge_lam.20160814_00+009.mem026.grib2, field 7 [large_scale_precipitation_sfc.lam]: large_scale_precipitation_sfc.lam maximum value 370.829 is not in [0,350]
#'''
   [
      "large_scale_precipitation_sfc.lam",
      -0.05,
      0.1,
      0.0,
      400.,
      [
         ["model", str, 0, "lam"],

         ["paramId", int, 3062],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 54],

         ["typeOfStatisticalProcessing", int, 1],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

   [
      "wilting_point_sfc",
      1e99,
      -1e99,
      99,
      -99,
      [
         ["model", str, 0, "glob"],
         ["discipline", int, 2],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 26],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaleFactorOfSecondFixedSurface", int, 1],
         ["scaledValueOfFirstFixedSurface", int, 0],
         ["scaledValueOfSecondFixedSurface", int, 2],
         ["typeOfFirstFixedSurface", int, 106],
         ["typeOfSecondFixedSurface", int, 106],
         [None, ],
      ],
      [point_in_time, given_thickness, has_bitmap],
   ],


#''' 
#   cosmoleps-arpasimc-eu 20140323, 12UTC, prod: tigge_lam.vmax_10m.9999.grib2, field 11 [maximum_wind_gust.lam]: maximum_wind_gust.lam maximum value 106.861 is not in [0,100] 
#'''

   [
      "maximum_wind_gust.lam",
      0,
      15,
      0,
      150,
      [
         ["model", str, 0, "lam"],

         ["paramId", int, 228028],

         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 22],

         ["typeOfStatisticalProcessing", int, 2],

         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 10],
         [None, ],
      ],
      [three_hourly, given_level],
   ],

#''' 
#   MOGREPS (origin = 1(mogreps-mo-eua))
#   2014-01-08 minimum limit for maximum_wind_gust changed to <0,12> because of mogreps data from 2014010203_03+0033
#   2014-01-10 maximum limit for maximum_wind_gust changed to <0,200> because of mogreps data from 2014010403_06+0033
#   2014-01-10 maximum limit for maximum_wind_gust changed to <0,333> because of mogreps data from 2014010821_11+0033
#   2014-01-27 minimum limit for maximum_wind_gust changed to <0,15> because of mogreps data from 2014012521_09+0018
#   2014-02-20 maximum limit for maximum_wind_gust changed to <0,500> because of mogreps data from 2014022009_02+0021
#   2014-12-08 warning: tigge_lam.tigge_mogreps-uk_2014120709_00+0018.grib2, field 4 [maximum_wind_gust.lam]: maximum_wind_gust.lam maximum value 607.375 is not in [0,500]
#  prod-mogreps-real-20150331-09 warning: tigge_lam.tigge_mogreps-uk_2015033109_10+0006.grib2, field 4 [maximum_wind_gust.lam]: maximum_wind_gust.lam minimum value 15.125 is not in [0,15]
#'''

   [
      "maximum_wind_gust.lam.mogreps",
      0,
      20,
      0,
      800,
      [
         ["model", str, 0, "lam"],
         ["suiteName", str, 1, "mogreps-mo-eua"],

         ["paramId", int, 228028],

         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 22],

         ["typeOfStatisticalProcessing", int, 2],

         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 10],
         [None, ],
      ],
      [three_hourly, given_level],
   ],

#'''
#s2s_devel, ecmf, 20141006, 0UTC, test: field 663 [mean_sea_level_pressure_sfc.glob]: mean_sea_level_pressure_sfc.glob minimum value 90371.6 is not in [91000,103000]
#s2s_devel, ecmf: warning: s2s.128151.2014111700.test.sfc.pf.768.4.grib2, mean_sea_level_pressure_sfc maximum value 107435 is not in [98000,107000]
#tigge_lam.tigge_mogreps-uk_2014122709_03+0036.grib2, field 1: mean_sea_level_pressure_sfc minimum value 103069 is not in [90000,103000]
#warning: s2s.2015082000.prod.1104.50.pf.sl.648.grib2, field 335 [mean_sea_level_pressure_sfc]: mean_sea_level_pressure_sfc minimum value 89778 is not in [90000,104000]
#s2s/lfpw: warning: s2s.lfpw_msl_0.grib2, field 1 [mean_sea_level_pressure_sfc]: mean_sea_level_pressure_sfc minimum value 88258.8 is not in [89000,104000]
#s2s/rjtd: warning: s2s.z_tigge_c_rjtd_201605101200_glob_prod_pf_sl_0636_009_0000_msl.grib2, field 1 [mean_sea_level_pressure_sfc]: mean_sea_level_pressure_sfc maximum value 109411 is not in [98000,109000]
#s2s/ammc: warning: s2s.z_s2s_c_cwao_20010602000000_glob_prod_sl_000.grib2, field 833 [mean_sea_level_pressure_sfc]: mean_sea_level_pressure_sfc maximum value 109994
#s2s/enfh/cwao: warning: s2s.z_s2s_c_cwao_20070721000000_glob_prod_sl_001.grib2, field 298 [mean_sea_level_pressure_sfc]: mean_sea_level_pressure_sfc maximum value 110320 is not in [98000,110000]
#s2s/enfo/rjtd:2s.2017011812.prod.046.sl.grib2, field 373 [mean_sea_level_pressure_sfc]: mean_sea_level_pressure_sfc maximum value 113559 is not in [98000,113000]
#'''
   [
      "mean_sea_level_pressure_sfc",
      88000,
      104000,
      98000,
      115000,
      [
         ["paramId", int, 151],

         ["discipline", int, 0],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 0],

         ["typeOfFirstFixedSurface", int, 101],
         [None, ],
      ],
      [point_in_time, predefined_level],
   ],

#'''
#s2s/lfpw: warning: s2s.lfpw_msl_0.grib2, field 1 [mean_sea_level_pressure_sfc]: mean_sea_level_pressure_sfc maximum value 120427 is not in [98000,109000] xxx should be fixed by provider!!
#'''
   [
      "mean_sea_level_pressure_sfc.lfpw",
      85000,
      104000,
      98000,
      121000,
      [
         ["paramId", int, 151],
         ["centre", str, 1, "lfpw"],
         ["step", int, 0],

         ["discipline", int, 0],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 0],

         ["typeOfFirstFixedSurface", int, 101],
         [None, ],
      ],
      [point_in_time, predefined_level],
   ],

#'''
#s2s_devel, ecmf, 20141229, 00UTC, test, enfh, real:    s2s.2014122900.test.768.10.pf.20131229.pl.720.grib2, field 450 [geopotential_height_pl]: geopotential_height_pl minimum value 30321.6 is not in [-850,30000]
#warning: s2s.2015082000.prod.1104.50.pf.pl.648.grib2, field 2241 [geopotential_height_pl]: geopotential_height_pl minimum value -876.714 is not in [-850,30500]
#s2s/lfpw: warning: s2s.lfpw_gh_1000.grib2, field 1 [geopotential_height_pl]: geopotential_height_pl minimum value -1199.08 is not in [-1000,30500]
#s2s/egrr: s2s.z_s2s_c_ukmo_20160102000000_glob_prod_pf_1440_002.rt.pl.grib2, field 1211 [geopotential_height_pl]: geopotential_height_pl minimum value 30506.8 is not in [-1300,30500]
#'''
   [
      "geopotential_height_pl",
      -5000,
      30600,
      200,
      35000,
      [
         ["discipline", int, 0],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 5],

         ["typeOfFirstFixedSurface", int, 100],
         [None, ],
      ],
      [point_in_time, given_level, pressure_level],
   ],

   [
      "geopotential_pl",
      -5000,
      306000,
      2000,
      350000,
      [
         ["discipline", int, 0],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 4],

         ["typeOfFirstFixedSurface", int, 100],
         [None, ],
      ],
      [point_in_time, given_level, pressure_level],
   ],


#'''
#warning: s2s.lfpw_t_10.grib2, field 61 [temperature_pl]: temperature_pl minimum value 159.934 is not in [160,260]
#s2s/egrr: warning: s2s.z_s2s_c_ukmo_19960417000000_glob_prod_pf_1440_002.hc.pl.grib2, field 450 [temperature_pl]: temperature_pl minimum value 260.687 is not in [150,260]
#s2s/egrr-enfo warning: s2s.z_s2s_c_ukmo_20160520000000_glob_prod_pf_1440_003.rt.pl.grib2, field 450 [temperature_pl]: temperature_pl minimum value 270.611 is not in [150,270]
#'''

   [
      "temperature_pl",
      150,
      275,
      200,
      330,
      [
         ["model", str, 0, "glob"],

         ["paramId", int, 130],

         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 0],

         ["typeOfFirstFixedSurface", int, 100],
         [None, ],
      ],
      [point_in_time, given_level, pressure_level],
   ],
#''' 
#   S2S/ammc: warning: s2s.t_20150906_21.grib2, field 11 [temperature_pl]: temperature_pl minimum value 44.6657 is not in [50,260]
#   S2S/ammc: warning: s2s.t_20150906_24.grib2, field 321 [temperature_pl]: temperature_pl minimum value -48.9135 is not in [50,260]
#   S2S/ammc: warning: s2s.t_20160403_16.grib2, field 571 [temperature_pl.ammc]: temperature_pl.ammc maximum value 343.462 is not in [200,340]
#'''
   [
      "temperature_pl.ammc",
      -999,
      260,
      200,
      350,
      [
         ["model", str, 0, "glob"],

         ["paramId", int, 130],
         ["centre", str, 1, "ammc"],

         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 0],

         ["typeOfFirstFixedSurface", int, 100],
         [None, ],
      ],
      [point_in_time, given_level, pressure_level],
   ],
#''' 
#   S2S/CAWCR: u_velocity_pl minimum value -137.331 is not in [-120,-10]
#   S2S/CAWCR: u_velocity_pl minimum value -8.77315 is not in [-120,-10]
#   s2s/ammc: warning: s2s.u_20150910_1.grib2, field 270 [u_velocity_pl]: u_velocity_pl minimum value -0.81584 is not in [-150,-1]
#   s2s/ammc: warning: s2s.u_20150906_28.grib2, field 430 [u_velocity_pl]: u_velocity_pl minimum value -1.09782 is not in [-150,-5]
#   s2s_devel, ecmf, 20150101, 00UTC, test, enfh, real: warning: s2s.2015010100.test.768.10.pf.20140101.pl.240.grib2, field 120 [u_velocity_pl]: u_velocity_pl maximum value 154.069 is not in [10,150]
#warning: s2s.z_tigge_c_kwbc_20020817000000_ncep_prod_pf_pl_0000_003_0010_u.grib2, field 3 [u_velocity_pl]: u_velocity_pl maximum value 170.9 is not in [10,170]
#   s2s/ammc: warning: s2s.u_20150913_31.grib2, field 550 [u_velocity_pl]: u_velocity_pl minimum value 0.352796 is not in [-150,-0.001]
#   s2s/ammc: warning: s2s.u_20151101_13.grib2, field 401 [u_velocity_pl]: u_velocity_pl minimum value -195.645 is not in [-180,1]
#   uerra/edzw-an: warning: /tmp/marm/uerra/cosmo/sample2/grib2/an.200812020800.u.pl.grib2, field 1 [u_velocity_pl]: u_velocity_pl minimum value 1.41138 is not in [-200,1]
#   s2s, ammc-enfo: s2s.u_20161222_4.pl.grib2, field 261 [u_velocity_pl]: u_velocity_pl minimum value -223.937 is not in [-200,-1]
#'''
   [
      "u_velocity_pl",
      -250,
      5,
      1,
      250,
      [
         ["paramId", int, 131],

         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 2],

         ["typeOfFirstFixedSurface", int, 100],
         [None, ],
      ],
      [point_in_time, given_level, pressure_level],
   ],


#''' 
#   S2S/CAWCR: v_velocity_pl maximum value 8.54936 is not in [10,150]
#   S2S/CAWCR: v_velocity_pl minimum value -128.209 is not in [-120,-10]
#   ammc-s2s-enfo: warning: s2s.v_20160131_0.grib2, field 430 [v_velocity_pl]: v_velocity_pl minimum value -4.84592 is not in [-190,-5]
#   ammc-s2s-enfo: warning: s2s.v_20160324_7.grib2, field 160 [v_velocity_pl]: v_velocity_pl maximum value 3.79724 is not in [4,190]
#   ammc-s2s-enfo: warning: s2s.v_20160526_0.grib2, field 611 [v_velocity_pl]: v_velocity_pl minimum value -194.691 is not in [-190,-2]
#'''
   [
      "v_velocity_pl",
      -200,
      -2,
      2,
      200,
      [
         ["model", str, 0, "glob"],

         ["paramId", int, 132],

         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 3],

         ["typeOfFirstFixedSurface", int, 100],
         [None, ],
      ],
      [point_in_time, given_level, pressure_level],
   ],

   [
      "u_velocity_pv",
      -120,
      -30,
      70,
      120,
      [
         ["model", str, 0, "glob"],
         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 2],
         ["typeOfFirstFixedSurface", int, 109],
         [None, ],
      ],
      [point_in_time, given_level, potential_vorticity_level],
   ],

   [
      "v_velocity_pv",
      -120,
      -50,
      55,
      120,
      [
         ["model", str, 0, "glob"],
         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 3],
         ["typeOfFirstFixedSurface", int, 109],
         [None, ],
      ],
      [point_in_time, given_level, potential_vorticity_level],
   ],
#'''
#   s2s_devel, ecmf, 20150101, 00UTC, test, enfh, warning: s2s.2015010100.test.768.10.pf.20020101.pl.0.grib2, field 372 [w_vertical_velocity_pl]: w_vertical_velocity_pl minimum value -5.02998 is not in [-5,0] 
#warning: s2s.z_tigge_c_kwbc_20150817000000_ncep_prod_pf_pl_0000_015_0500_w.grib2, field 3 [w_vertical_velocity_pl]: w_vertical_velocity_pl minimum value -7.25731 is not in [-6,0]
#  s2s/kwbc/enfo: warning: s2s.z_tigge_c_kwbc_20151114000000_ncep_prod_pf_pl_0000_011_0500_w.grib2, field 7 [w_vertical_velocity_pl]: w_vertical_velocity_pl minimum value -10.202 is not in [-10,0]
#  s2s/cwao/enfo: warning: s2s.z_s2s_c_cwao_20160512000000_glob_prod_??_pl_00_384_003.grib2, field 28 [w_vertical_velocity_pl]: w_vertical_velocity_pl minimum value -19.8681 is not in [-12,0]
#  s2s/rksl/enfh: warning: s2s.002.pl.grib2, field 2489 [w_vertical_velocity_pl]: w_vertical_velocity_pl maximum value -1.23174 is not in [-1,25]

#'''
   [
      "w_vertical_velocity_pl",
      -25,
        0,
       -2,
       25,
      [
         ["paramId", int, 135],

         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 8],

         ["typeOfFirstFixedSurface", int, 100],
         [None, ],
      ],
      [point_in_time, given_level, pressure_level],
   ],

   [
      "soil_type_sfc",
      0,
      1,
      5,
      10,
      [
         ["model", str, 0, "glob"],

         ["paramId", int, 43],

         ["discipline", int, 2],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 0],

         ["typeOfFirstFixedSurface", int, 1],

         [None, ],
      ],
      [point_in_time, predefined_level, has_bitmap],
   ],
#'''
#s2s_devel, ecmf, 20141229, 00UTC, test, enfh, real:  s2s.2014122900.test.768.10.pf.19941229.sl.168.grib2, field 21 [surface_pressure_sfc]: surface_pressure_sfc maximum value 102851 is not in [102900,110000]
#uerra, eswi-an: an.sp.sfc.grib2, field 1 [surface_pressure_sfc]: surface_pressure_sfc minimum value 66482.1 is not in [48000,55000]
#'''
   [
      "surface_pressure_sfc",
      48000,
      80000,
      101500,
      115000,
      [
         ["model", str, 0, "glob"],

         ["paramId", int, 134],

         ["discipline", int, 0],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 0],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level],
   ],

##todo limits
   [
      "eastward_turbulent_surface_stress_sfc",
      -1.5e+6,
       1.5e+6,
      -1.5e+6,
       1.5e+6,
      [
         ["model", str, 0, "glob"],

         ["paramId", int, 180],

         ["discipline", int,0],
         ["parameterCategory", int,2],
         ["parameterNumber", int,38],

         ["typeOfStatisticalProcessing", int, 1],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

##todo limits
   [
      "northward_turbulent_surface_stress_sfc",
      -1.5e+6,
       1.5e+6,
      -1.5e+6,
       1.5e+6,
      [
         ["model", str, 0, "glob"],

         ["paramId", int, 181],

         ["discipline", int,0],
         ["parameterCategory", int,2],
         ["parameterNumber", int,37],

         ["typeOfStatisticalProcessing", int, 1],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],


   [
      "water_runoff_sfc",
      -0.001,
       5,
       0.3,
       30,
      [
         ["model", str, 0, "glob"],

         ["paramId", int, 228205],

         ["discipline", int,2],
         ["parameterCategory", int,0],
         ["parameterNumber", int,33],

         ["typeOfStatisticalProcessing", int, 1],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level, has_bitmap],
   ],

   [
      "sea_ice_cover_sfc.glob",
      -1.5e+6,
       1.5e+6,
      -1.5e+6,
       1.5e+6,
      [
         ["model", str, 0, "glob"],

         ["paramId", int, 31],

         ["discipline", int, 10],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 0],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level, has_bitmap],
   ],

   [
      "snow_density_sfc.glob",
      -1.5e+6,
       1.5e+6,
      -1.5e+6,
       1.5e+6,
      [
         ["model", str, 0, "glob"],

         ["paramId", int, 33],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 61],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level, has_bitmap],
   ],

   [
      "sea_surface_temperature_sfc.glob",
       200,
       290,
       260,
       320,
      [
         ["model", str, 0, "glob"],

         ["paramId", int, 34],

         ["discipline", int, 10],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 0],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level, has_bitmap],
   ],

#''' 
#  s2s/rums/enfo: warning: s2s.z_s2s_c_rhmc_20170301000000_glob_prod_00.sl.grib2, field 141 [sea_surface_temperature_sfc.glob.s2]: sea_surface_temperature_sfc.glob.s2 minimum value 0 is not in [200,290]

#  SHOULD be fixed now!

#   [
#      "sea_surface_temperature_sfc.glob.s2s.rums",
#       0,
#       290,
#       260,
#       320,
#      [
#         ["model", str, 0, "glob"],
#         ["class", str, 0, "s2"],
#         ["centre", str, 1, "rums"],

#         ["paramId", int, 34],

#         ["discipline", int, 10],
#         ["parameterCategory", int, 3],
#         ["parameterNumber", int, 0],

#         ["typeOfFirstFixedSurface", int, 1],
#         [None, ],
#      ],
#      [daily_average, predefined_level, has_bitmap],
#   ],
#'''

   [
      "convective_available_potential_energy_sfc.glob.s2",
      0,
      10,
      0,
      17000,
      [
         ["model", str, 0, "glob"],
         ["class", str, 0, "s2"],

         ["paramId", int, 59],

         ["discipline", int, 0],
         ["parameterCategory", int, 7],
         ["parameterNumber", int, 6],

         ["typeOfStatisticalProcessing", int, 0],

         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 8],
         [None, ],
      ],
      [daily_average, predefined_thickness, resolution_s2s],
   ],
#''' 
#   S2S/CAWCR: total_column_water_sfc.glob minimum value 0.00832421 is not in [0.01,1]
#warning: s2s.z_tigge_c_kwbc_19990817000000_ncep_prod_cf_sl_0024_000_0000_tcw.grib2, field 33 [total_column_water_sfc.glob]: total_column_water_sfc.glob minimum value -0.168614 is not in [0.001,1]
#warning: s2s.z_tigge_c_kwbc_20090829000000_ncep_prod_pf_sl_0024_003_0000_tcw.grib2, field 11 [total_column_water_sfc.glob]: total_column_water_sfc.glob minimum value -2.00987 is not in [-2,1]
#  lfpw/enfo: warning: s2s.lfpw_tcw_0.grib2, field 10 [total_column_water_sfc.glob.s2]: total_column_water_sfc.glob.s2 minimum value 1.01153 is not in [-3,1]
#  uerra, eswi-an: an.tcw.sfc.grib2, field 1 [total_column_water_sfc]: total_column_water_sfc maximum value 37.9248 is not in [50,150]
#'''
   [
      "total_column_water_sfc.s2",
      -3.0,
      2,
      30,
      150,
      [
         ["model", str, 0, "glob"],
         ["class", str, 0, "s2"],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 51],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 8],
         [None, ],
      ],
      [daily_average, predefined_thickness, resolution_s2s],
   ],

   [
      "total_column_water_sfc",
      -3.0,
      2,
      30,
      150,
      [
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 51],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 8],
         [None, ],
      ],
      [point_in_time, predefined_thickness],
   ],

#'''
#s2s/rums warning: s2s.z_s2s_c_rhmc_20150819000000_glob_prod_0336_017.sl.grib2, field 4 [surface_air_temperature_sfc.glob]: surface_air_temperature_sfc.glob minimum value 177.17 is not in [180,290]
#s2s/ammc: warning: s2s.2t_20151224_26.grib2, field 12 [surface_air_temperature_sfc.glob.s2]: surface_air_temperature_sfc.glob.s2 maximum value 353.017 is not in [270,350]
#'''

   [
      "surface_air_temperature_sfc.glob.s2",
      170,
      290,
      270,
      360,
      [
         ["model", str, 0, "glob"],
         ["class", str, 0, "s2"],

         ["paramId", int, 167],

         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 0],

         ["typeOfStatisticalProcessing", int, 0],

         ["typeOfFirstFixedSurface", int, 103],
         [None, ],
      ],
      [daily_average, given_level, resolution_s2s],
   ],

   [
      "surface_air_dew_point_temperature_sfc",
      30,
      290,
      270,
      350,
      [
         ["model", str, 0, "glob"],

         ["paramId", int, 168],

         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 6],

         ["typeOfFirstFixedSurface", int, 103],
         [None, ],
      ],
      [point_in_time, given_level],
   ],

#''' 
#   S2S/CAWCR: surface_air_dew_point_temperature_sfc.glob minimum value 32.4337 is not in [175,290]
#'''
   [
      "surface_air_dew_point_temperature_sfc.s2",
      30,
      290,
      270,
      350,
      [
         ["class", str, 0, "s2"],

         ["paramId", int, 168],

         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 6],

         ["typeOfStatisticalProcessing", int, 0],

         ["typeOfFirstFixedSurface", int, 103],
         [None, ],
      ],
      [daily_average, given_level, resolution_s2s],
   ],
#''' 
#   S2S/CAWCR: skin_temperature_sfc.glob maximum value 309.28 is not in [310,355]
#s2s/kwbc/enfh: warning: s2s.z_s2s_c_rhmc_20150819000000_glob_prod_1464_000.sl.grib2, field 17 [skin_temperature_sfc.glob]: skin_temperature_sfc.glob minimum value 237.261 is not in [
#s2s/rums/enfo warning: s2s.z_s2s_c_rhmc_20150826000000_glob_prod_1392_003.sl.grib2, field 15 [skin_temperature_sfc.glob]: skin_temperature_sfc.glob minimum value 240.467 is not in [180,240]
#s2s/ammc/enfo warning: warning: s2s.skt_20150920_4.grib2, field 12 [skin_temperature_sfc.glob]: skin_temperature_sfc.glob minimum value 179.087 is not in [180,245]
#s2s/ammc/enfo warning: warning: s2s.skt_20160410_21.grib2, field 57 [skin_temperature_sfc.glob.s2]: skin_temperature_sfc.glob.s2 minimum value 164.277 is not in [175,245]
#uerra/egrr/det/an: skin_temperature_sfc minimum value 266.875 is not in [160,250]
#'''
   [
      "skin_temperature_sfc.s2",
      160,
      300,
      300,
      355,
      [
         ["class", str, 0, "s2"],

         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 17],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [daily_average, predefined_level, resolution_s2s],
   ],

#''' 
#   S2S/CAWCR: soil_moisture_top_20_cm_sfc.glob maximum value 150 is not in [450,800]
#warning: s2s.z_s2s_c_babj_20150817000000_glob_prod_cf_1440_000.sl.grib2, field 1641 [soil_moisture_top_20_cm_sfc.glob]: soil_moisture_top_20_cm_sfc.glob minimum value 59.5781 is not in [-1e-17,0]
#'''

   [
      "soil_moisture_top_20_cm_sfc.glob",
      -1e-17,
      70,
      100,
      1500,
      [
         ["model", str, 0, "glob"],

         ["paramId", int, 228086],

         ["discipline", int, 2],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 22],

         ["typeOfStatisticalProcessing", int, 0],

         ["typeOfFirstFixedSurface", int, 106],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 0],

         ["typeOfSecondFixedSurface", int, 106],
         ["scaleFactorOfSecondFixedSurface", int, 1],
         ["scaledValueOfSecondFixedSurface", int, 2],
         [None, ],
      ],
      [daily_average, given_thickness, has_bitmap],
   ],

#'''
#warning: s2s.z_s2s_c_babj_20150901000000_glob_prod_pf_1440_002.sl.grib2, field 1621 [soil_moisture_top_100_cm_sfc.glob]: soil_moisture_top_100_cm_sfc.glob minimum value 60.1641 is not in [-1e-16,60]
#warning: s2s.z_s2s_c_babj_20150817000000_glob_prod_cf_1440_000.sl.grib2, field 1745 [soil_moisture_top_100_cm_sfc.glob]: soil_moisture_top_100_cm_sfc.glob maximum value 1382.83 is not in [450,800]
#warning: s2s.2015092100.prod.1104.10.pf.19980921.sl.48.grib2, field 220 [soil_moisture_top_100_cm_sfc.glob]: soil_moisture_top_100_cm_sfc.glob minimum value -1.07114e-16 is not in [-1e-16,60]
#s2s/rums warning: s2s.z_s2s_c_rhmc_20150819000000_glob_prod_1464_001.sl.grib2, field 17 [soil_moisture_top_100_cm_sfc.glob]: soil_moisture_top_100_cm_sfc.glob maximum value 413.812 is not in [450,1400]
#'''
   [
      "soil_moisture_top_100_cm_sfc.glob",
      -1e-15,
      70,
      380,
      1400,
      [
         ["model", str, 0, "glob"],

         ["paramId", int, 228087],

         ["discipline", int, 2],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 22],

         ["typeOfStatisticalProcessing", int, 0],

         ["typeOfFirstFixedSurface", int, 106],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 0],

         ["typeOfSecondFixedSurface", int, 106],
         ["scaleFactorOfSecondFixedSurface", int, 1],
         ["scaledValueOfSecondFixedSurface", int, 10],
         [None, ],
      ],
      [daily_average, given_thickness, has_bitmap],
   ],
#'''
#s2s_devel/ecmf/enfh/rea: warning: s2s.2015011200.test.768.10.cf.20100112.sl.24.grib2, field 25 [soil_temperature_top_20_cm_sfc.glob]: soil_temperature_top_20_cm_sfc.glob minimum value 199.519 is not in [200,230]
#s2s_prod/ammc/enfo:warning: s2s.st20_20151004_4.grib2, field 61 [soil_temperature_top_20_cm_sfc.glob]: soil_temperature_top_20_cm_sfc.glob minimum value 231.081 is not in [180,230]
#'''
   [
      "soil_temperature_top_20_cm_sfc.glob",
      180,
      240,
      300,
      350,
      [
         ["model", str, 0, "glob"],

         ["paramId", int, 228095],

         ["discipline", int, 2],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 2],

         ["typeOfStatisticalProcessing", int, 0],

         ["typeOfFirstFixedSurface", int, 106],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 0],

         ["typeOfSecondFixedSurface", int, 106],
         ["scaleFactorOfSecondFixedSurface", int, 1],
         ["scaledValueOfSecondFixedSurface", int, 2],
         [None, ],
      ],
      [daily_average, given_thickness, has_bitmap],
   ],

#'''
#   s2s/rums warning: s2s.z_s2s_c_rhmc_20150819000000_glob_prod_0024_000.sl.grib2, field 26 [soil_temperature_top_20_cm_sfc.glob]: soil_temperature_top_20_cm_sfc.glob minimum value 0 is not in [180,230] xxx must be fiexed!!!
#   s2s/rums warning: warning: s2s.z_s2s_c_rhmc_20151021000000_glob_prod_0336_019.sl.grib2, field 24 [soil_temperature_top_20_cm_sfc.glob]: soil_temperature_top_20_cm_sfc.glob minimum value 238.514 is not in [0,230]
#'''
   [
      "soil_temperature_top_20_cm_sfc.glob.rums",
      0,
      250,
      300,
      350,
      [
         ["model", str, 0, "glob"],
         ["centre", str, 1, "rums"],

         ["paramId", int, 228095],

         ["discipline", int, 2],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 2],

         ["typeOfStatisticalProcessing", int, 0],

         ["typeOfFirstFixedSurface", int, 106],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 0],

         ["typeOfSecondFixedSurface", int, 106],
         ["scaleFactorOfSecondFixedSurface", int, 1],
         ["scaledValueOfSecondFixedSurface", int, 2],
         [None, ],
      ],
      [daily_average, given_thickness, has_bitmap],
   ],


#''' 
#   S2S/babj: warning: s2s.z_s2s_c_babj_20150908000000_glob_prod_cf_1440_000.sl.grib2, field 1816 [soil_temperature_top_100_cm_sfc.glob]: soil_temperature_top_100_cm_sfc.glob minimum value 199.941 is not in [200,240]
#'''
   [
      "soil_temperature_top_100_cm_sfc.glob",
      190,
      240,
      300,
      350,
      [
         ["model", str, 0, "glob"],

         ["paramId", int, 228096],

         ["discipline", int, 2],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 2],

         ["typeOfStatisticalProcessing", int, 0],

         ["typeOfFirstFixedSurface", int, 106],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 0],

         ["typeOfSecondFixedSurface", int, 106],
         ["scaleFactorOfSecondFixedSurface", int, 1],
         ["scaledValueOfSecondFixedSurface", int, 10],
         [None, ],
      ],
      [daily_average, given_thickness, has_bitmap],
   ],

#''' 
#   S2S/rums: warning: s2s.z_s2s_c_rhmc_20150819000000_glob_prod_0024_000.sl.grib2, field 25 [soil_temperature_top_100_cm_sfc.glob]: soil_temperature_top_100_cm_sfc.glob minimum value 0 is not in [200,240]  xxx must be fixed!!!
#   S2S/rums: warning: s2s.z_s2s_c_rhmc_20151021000000_glob_prod_0360_019.sl.grib2, field 23 [soil_temperature_top_100_cm_sfc.glob.s2.rums]: soil_temperature_top_100_cm_sfc.glob.s2.rums minimum value 240.084 is not in [0,240]
#'''
   [
      "soil_temperature_top_100_cm_sfc.glob.s2.rums",
      0,
      250,
      300,
      350,
      [
         ["model", str, 0, "glob"],
         ["class", str, 0, "s2"],
         ["centre", str, 1, "rums"],

         ["paramId", int, 228096],

         ["discipline", int, 2],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 2],

         ["typeOfStatisticalProcessing", int, 0],

         ["typeOfFirstFixedSurface", int, 106],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 0],

         ["typeOfSecondFixedSurface", int, 106],
         ["scaleFactorOfSecondFixedSurface", int, 1],
         ["scaledValueOfSecondFixedSurface", int, 10],
         [None, ],
      ],
      [daily_average, given_thickness, has_bitmap, resolution_s2s],
   ],
#''' 
#   S2S/CAWCR: snow_depth_water_equivalent_sfc.glob maximum value 9066.25 is not in [10000,15000]
#warning: s2s.z_tigge_c_kwbc_19990817000000_ncep_prod_cf_sl_0024_000_0000_sd.grib2, field 19 [snow_depth_water_equivalent_sfc.glob]: snow_depth_water_equivalent_sfc.glob maximum value 219.94 is not in [9000,15000]
#  s2s/isac:warning: s2s.z_s2s_c_isac_201510190000_glob_prod_cf_0744_00.sl.grib2, field 25 [snow_depth_water_equivalent_sfc.glob]: snow_depth_water_equivalent_sfc.glob maximum value 118.824
#'''
   [
      "snow_depth_water_equivalent_sfc.glob.s2",
      -0.00001,
      0,
      100,
      15000,
      [
         ["model", str, 0, "glob"],
         ["class", str, 0, "s2"],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 60],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [daily_average, predefined_level, resolution_s2s],
   ],

#'''s2s/isac:warning: s2s.z_s2s_c_isac_201510190000_glob_prod_cf_0744_00.sl.grib2, field 25 [snow_depth_water_equivalent_sfc.glob]: snow_depth_water_equivalent_sfc.glob maximum value 118.824
#  s2s/cwao:warning: warning: s2s.z_s2s_c_cwao_20130211000000_glob_prod_sl_000.grib2, field 23 [snow_depth_water_equivalent_sfc.glob.s2]: snow_depth_water_equivalent_sfc.glob.s2 maximum value 30452.5 is not in [100,15000]
#'''
   [
      "snow_depth_water_equivalent_sfc.glob.s2.cwao",
      -4e-19,
      0,
      100,
      40000,
      [
         ["model", str, 0, "glob"],
         ["class", str, 0, "s2"],
         ["centre", str, 1, "cwao"],

         ["paramId", int, 228141],

         ["typeOfStatisticalProcessing", int, 0],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 60],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [daily_average, predefined_level, resolution_s2s],
   ],

# '''
#warning: s2s.z_tigge_c_kwbc_20150817000000_ncep_prod_cf_sl_0024_000_0000_tcc.grib2, field 2 [total_cloud_cover_sfc.glob]: total_cloud_cover_sfc.glob maximum value 100.716 is not in [99.99,100.01]
#warning: s2s.z_s2s_c_babj_20150817000000_glob_prod_cf_1440_000.sl.grib2, field 2582 [total_cloud_cover_sfc.glob]: total_cloud_cover_sfc.glob maximum value 94.4214 is not in [99.99,100.01]
#warning: s2s.z_tigge_c_kwbc_20150817000000_ncep_prod_pf_sl_0024_009_0000_tcc.grib2, field 1 [total_cloud_cover_sfc.glob]: total_cloud_cover_sfc.glob maximum value 100.503 is not in [90,100.1]
#s2s/lfpw: warning: s2s.lfpw_tcc_0.grib2, field 60 [total_cloud_cover_sfc.glob]: total_cloud_cover_sfc.glob minimum value -0.0300206 is not in [0,5]
#s2s/ammc/enfo:s2s.tcc_20151004_9.grib2, field 21 [total_cloud_cover_sfc.glob]: total_cloud_cover_sfc.glob maximum value 128 is not in [90,101]
# '''
   [
      "total_cloud_cover_sfc.glob.s2",
      -0.1,
      5,
      90.,
      101.,
      [
         ["model", str, 0, "glob"],
         ["class", str, 0, "s2"],

         ["paramId", int, 228164],

         ["typeOfStatisticalProcessing", int, 0],

         ["discipline", int, 0],
         ["parameterCategory", int, 6],
         ["parameterNumber", int, 1],

         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 8],
         [None, ],
      ],
      [daily_average, predefined_thickness, resolution_s2s],
   ],

#'''
#   s2s/lfpw warning: s2s.lfpw_tcc_0.grib2, field 1 [total_cloud_cover_sfc.glob]: total_cloud_cover_sfc.glob maximum value 75 is not in [90,101] xxx should be fixed by provider!!
#'''

   [
      "total_cloud_cover_sfc.glob.s2.lfpw",
      -0.1,
      5,
      70.,
      101.,
      [
         ["model", str, 0, "glob"],
         ["class", str, 0, "s2"],
         ["centre", str, 1, "lfpw"],
         ["step", str, 1, "0-24"],

         ["paramId", int, 228164],

         ["typeOfStatisticalProcessing", int, 0],

         ["discipline", int, 0],
         ["parameterCategory", int, 6],
         ["parameterNumber", int, 1],

         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 8],
         [None, ],
      ],
      [daily_average, predefined_thickness, resolution_s2s],
   ],

   [
      "convective_precipitation_sfc.glob",
      -0.05,
      0.1,
      0.,
      100.,
      [
         ["model", str, 0, "glob"],

         ["paramId", int, 228143],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 37],

         ["typeOfStatisticalProcessing", int, 1],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

   [
      "sea_ice_cover_sfc.glob.s2",
      -1.5e+6,
       1.5e+6,
      -1.5e+6,
       1.5e+6,
      [
         ["model", str, 0, "glob"],
         ["class", str, 0, "s2"],

         ["paramId", int, 31],
         ["typeOfStatisticalProcessing", int, 0],

         ["discipline", int, 10],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 0],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [daily_average, predefined_level, has_bitmap, resolution_s2s],
   ],

   [
      "snow_density_sfc.glob.s2",
      -1.5e+6,
       1.5e+6,
      -1.5e+6,
       1.5e+6,
      [
         ["model", str, 0, "glob"],
         ["class", str, 0, "s2"],

         ["paramId", int, 33],

         ["typeOfStatisticalProcessing", int, 0],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 61],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [daily_average, predefined_level, resolution_s2s],
   ],

#'''
#  s2s/ammc/enfo: warning: s2s.sst_20170223_4.sl.grib2, field 59 [sea_surface_temperature_sfc.glob.s2]: sea_surface_temperature_sfc.glob.s2 minimum value 194.496 is not in [200,290]
#'''

   [
      "sea_surface_temperature_sfc.glob.s2",
       180,
       290,
       260,
       320,
      [
         ["model", str, 0, "glob"],
         ["class", str, 0, "s2"],

         ["paramId", int, 34],

         ["typeOfStatisticalProcessing", int, 0],

         ["discipline", int, 10],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 0],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [daily_average, predefined_level, has_bitmap, resolution_s2s],
   ],

   [
      "snow_albedo_sfc.glob",
      -1.5e+6,
       1.5e+6,
      -1.5e+6,
       1.5e+6,
      [
         ["model", str, 0, "glob"],

         ["paramId", int, 228032],

         ["typeOfStatisticalProcessing", int, 0],

         ["discipline", int, 0],
         ["parameterCategory", int, 19],
         ["parameterNumber", int, 19],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [daily_average, predefined_level, has_bitmap],
   ],

## UERRA 
   [
      "high_cloud_cover_sfc",
      0,
      1e-10,
      0.9999,
      100.00001,
      [
         ["discipline", int, 0],
         ["parameterCategory", int, 6],
         ["parameterNumber", int, 5],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 8],
         [None, ],
      ],
      [point_in_time, predefined_thickness],
   ],
   [
      "medium_cloud_cover_sfc",
      0,
      1e-10,
      0.9999,
      100.00001,
      [
         ["discipline", int, 0],
         ["parameterCategory", int, 6],
         ["parameterNumber", int, 4],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 8],
         [None, ],
      ],
      [point_in_time, predefined_thickness],
   ],
   [
      "low_cloud_cover_sfc",
      0,
      1e-10,
      0.9999,
      100.00001,
      [
         ["discipline", int, 0],
         ["parameterCategory", int, 6],
         ["parameterNumber", int, 3],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 8],
         [None, ],
      ],
      [point_in_time, predefined_thickness],
   ],
#''' 

#uerra/egrr (something like ad hoc 1 grid-point issue (similarly grid-point storms..)): warning: enda.2009-01-20.sfc.grib2, field 831 [low_cloud_cover_sfc]: low_cloud_cover_sfc maximum value 317.188 is not in [0.9999,100]
#'''
   [
      "low_cloud_cover_sfc.egrr",
      0,
      1e-10,
      0.9999,
      400.00001,
      [
         ["discipline", int, 0],
         ["parameterCategory", int, 6],
         ["parameterNumber", int, 3],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 8],
         [None, ],
      ],
      [point_in_time, predefined_thickness],
   ],


   # uerra model levels 
   [
      "pressure_ml",
      100,
      100000,
      100,
      108000,
      [
         ["paramId", int, 54],
         ["discipline", int, 0],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 105],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level], # check model levels?? 
   ],
   [
      "pressure_ml.edzw",
      100,
      100000,
      100,
      108000,
      [
         ["paramId", int, 54],
         ["origin", str, 0, "edzw"],

         ["discipline", int, 0],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 118],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level], # check model levels?? 
   ],

   [
      "specific_humidity_ml",
      -0.1,
      0.01,
         0,
       0.1,
      [
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 105],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level], # check model levels?? 
   ],
   [
      "specific_humidity_ml.edzw",
      -0.1,
      0.01,
         0,
       0.1,
      [
         ["paramId", int, 133],
         ["origin", str, 0, "edzw"],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 118],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level], # check model levels?? 
   ],

   [
      "temperature_ml",
      150,
      300,
      200,
      330,
      [
         ["paramId", int, 130],
         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 105],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level], # check model levels?? 
   ],
   [
      "temperature_ml.edzw",
      150,
      300,
      200,
      330,
      [
         ["paramId", int, 130],
         ["origin", str, 0, "edzw"],

         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 118],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level], # check model levels?? 
   ],

#'''
#  uerra, eswi-an: an.200812020000+0.ml.grib2, field 3 [u_velocity_ml]: u_velocity_ml minimum value 1.55574 is not in [-200,1]
#  uerra, egrr-det-fc: u_velocity_ml maximum value 0.625 is not in [1,200]
#'''
   [
      "u_velocity_ml",
      -200,
        10,
       0.1,
       200,
      [
         ["paramId", int, 131],
         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 2],
         ["typeOfFirstFixedSurface", int, 105],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level], # check model levels?? 
   ],
   [
      "u_velocity_ml.edzw",
      -200,
        10,
       0.1,
       200,
      [
         ["paramId", int, 131],
         ["origin", str, 0, "edzw"],

         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 2],
         ["typeOfFirstFixedSurface", int, 118],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level], # check model levels?? 
   ],

   [
      "v_velocity_ml",
      -200,
      -1,
      1,
      200,
      [
         ["paramId", int, 132],
         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 3],
         ["typeOfFirstFixedSurface", int, 105],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level], # check model levels?? 
   ],
   [
      "v_velocity_ml.edzw",
      -200,
      -1,
      1,
      200,
      [
         ["paramId", int, 132],
         ["origin", str, 0, "edzw"],

         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 3],
         ["typeOfFirstFixedSurface", int, 118],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level], # check model levels?? 
   ],

   [
      "cloud_cover_ml",
      0,
      1e-10,
      0,
      100.00001,
      [
         ["discipline", int, 0],
         ["parameterCategory", int, 6],
         ["parameterNumber", int, 22],
         ["typeOfFirstFixedSurface", int, 105],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level], # check model levels?? 
   ],
   [
      "cloud_cover_ml.edzw",
      0,
      1e-10,
      0,
      100.00001,
      [
         ["paramId", int, 260257],
         ["origin", str, 0, "edzw"],

         ["discipline", int, 0],
         ["parameterCategory", int, 6],
         ["parameterNumber", int, 22],
         ["typeOfFirstFixedSurface", int, 118],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level], # check model levels?? 
   ],

   [
      "specific_cloud_ice_water_content_pl",
       0,
       0.001,
       0,
       0.01,
      [
         ["paramId", int, 247],
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 84],
         ["typeOfFirstFixedSurface", int, 100],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level, pressure_level],
   ],

   [
      "cloud_cover_pl.glob",
      0,
      1e-10,
      100,
      100.00001,
      [
         ["paramId", int, 260257],
         ["discipline", int, 0],
         ["parameterCategory", int, 6],
         ["parameterNumber", int, 22],
         ["typeOfFirstFixedSurface", int, 100],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level, pressure_level],
   ],
   [
      "specific_cloud_liquid_water_content_pl",
       0,
       1e+5,
       0,
       1e+6,
      [
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 83],
         ["typeOfFirstFixedSurface", int, 100],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level, pressure_level],
   ],

   [
      "specific_cloud_ice_water_content_ml",
       0,
       0.001,
       0,
       0.01,
      [
         ["paramId", int, 247],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 84],
         ["typeOfFirstFixedSurface", int, 105],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level], # check model levels?? 
   ],
   [
      "specific_cloud_ice_water_content_ml.edzw",
       0,
       0.001,
       0,
       0.01,
      [
         ["paramId", int, 247],
         ["origin", str, 0, "edzw"],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 84],
         ["typeOfFirstFixedSurface", int, 118],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level], # check model levels?? 
   ],

   [
      "specific_cloud_liquid_water_content_ml",
       0,
       1e+5,
       0,
       1e+6,
      [
         ["paramId", int, 246],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 83],
         ["typeOfFirstFixedSurface", int, 105],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level], # check model levels?? 
   ],
   [
      "specific_cloud_liquid_water_content_ml.edzw",
       0,
       1e+5,
       0,
       1e+6,
      [
         ["paramId", int, 246],
         ["origin", str, 0, "edzw"],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 83],
         ["typeOfFirstFixedSurface", int, 118],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level], # check model levels?? 
   ],

#'''
#  uerra/eggr  warning: oper.2010-03-13.pl.grib2, field 69 [relative_humidity_pl]: relative_humidity_pl maximum value 169 is not in [0,160]

#'''
   [
      "relative_humidity_pl",
       0,
       30,
       0,
       180,
      [
         ["paramId", int, 157],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 1],
         ["typeOfFirstFixedSurface", int, 100],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level, pressure_level],
   ],

   # uerra height levels 

   [
      "cloud_cover_hl",
      0,
      1e-10,
      80,
      100.00001,
      [
         ["discipline", int, 0],
         ["parameterCategory", int, 6],
         ["parameterNumber", int, 22],
         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level, height_level],
   ],
   [
      "pressure_hl",
      100,
      100000,
      100,
      108000,
      [
         ["discipline", int, 0],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level, height_level],
   ],
   [
      "specific_cloud_liquid_water_content_hl",
       0,
       1e+5,
       0,
       1e+6,
      [
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 83],
         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level, height_level],
   ],
   [
      "specific_cloud_ice_water_content_hl",
       0,
       0.001,
       0,
       0.01,
      [
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 84],
         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level, height_level],
   ],
   [
      "relative_humidity_hl",
      0,
      40,
      1,
      160,
      [
         ["paramId", int, 157],
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 1],
         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level, height_level],
   ],
   [
      "temperature_hl",
      150,
      300,
      200,
      330,
      [
         ["paramId", int, 130],
         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level, height_level],
   ],
   [
      "wind_speed_hl",
      0,
      10,
      10,
      150,
      [
         ["paramId", int, 10],
         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 1],
         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level, height_level],
   ],
   [
      "wind_direction_hl",
      0,
      1,
      359,
      360.1,
      [
         ["paramId", int, 3031],
         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level, height_level],
   ],

   # uerra single level (surface) 

#'''
#  uerra, eswi-fc: percolation_sfc maximum value 0.971001 is not in [1,30]
#'''
   [
      "percolation_sfc",
      0,
      1,
      0.8,
      30,
      [
         ["paramId", int, 260430],
         ["discipline", int, 1],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 16],
         ["typeOfStatisticalProcessing", int, 1],
         ["typeOfFirstFixedSurface", int, 177],
         [None, ],
      ],
       [from_start, predefined_level],
   ],
   [
      "2_metre_relative_humidity",
      0,
      25,
      90,
      160,
      [
         ["paramId", int, 260242],
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 1],
         ["typeOfFirstFixedSurface", int, 103],
         [None, ],
      ],
      [point_in_time, given_level],
   ],

#'''
#  s2s, babj-enfo: surface_runoff maximum value 0.479167 is not in [1,100]
#'''
   [
      "surface_runoff",
      -0.001,
      1,
      0.1,
      100,
      [
         ["paramId", int, 174008],
         ["discipline", int, 2],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 34],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfStatisticalProcessing", int, 1],
         [None, ],
      ],
      [from_start, predefined_level, has_bitmap],
   ],

#'''
#  uerra, cosmo-fc:albedo_sfc maximum value 70 is not in [80,100]
#'''
   [
      "albedo_sfc",
      0,
      20,
      60,
      100,
      [
         ["paramId", int, 260509],
         ["discipline", int, 0],
         ["parameterCategory", int, 19],
         ["parameterNumber", int, 1],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level, has_bitmap],
   ],
#'''
#  uerra, egrr:  The albedo is 0 at night because it is dependent on solar radiation
#'''
   [
      "albedo_sfc.uerra-egrr",
      0,
      20,
      0,
      100,
      [
         ["class", str, 0, "ur"],
         ["centre", str, 1, "egrr"],
         ["paramId", int, 260509],
         ["discipline", int, 0],
         ["parameterCategory", int, 19],
         ["parameterNumber", int, 1],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level, has_bitmap],
   ],
   [
      "time_integrated_surface_clear-sky_solar_radiation_downwards",
      -0.1,
      1e+08,
      0,
      1e+09,
      [
         ["paramId", int, 260423],
         ["discipline", int, 0],
         ["parameterCategory", int, 4],
         ["parameterNumber", int, 52],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfStatisticalProcessing", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],
   [
      "time_integrated_surface_clear-sky_solar_radiation_upwards",
      -0.1,
      1e+08,
      0,
      1e+09,
      [
         ["paramId", int, 260427],
         ["discipline", int, 0],
         ["parameterCategory", int, 4],
         ["parameterNumber", int, 53],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfStatisticalProcessing", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],
   [
      "time_integrated_surface_clear-sky_thermal_radiation_downwards",
      -0.1,
      1e+08,
      0,
      1e+09,
      [
         ["paramId", int, 260428],
         ["discipline", int, 0],
         ["parameterCategory", int, 5],
         ["parameterNumber", int, 8],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfStatisticalProcessing", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

#'''
#  uerra, eswi-fc: fc.tidirswrf.sfc.grib2, field 6 [time_integrated_surface_direct_solar_radiation]: time_integrated_surface_direct_solar_radiation minimum value 58442 is not in [-0.1,20000]
#'''
   [
      "time_integrated_surface_direct_solar_radiation",
      -10,
      1e+08,
      0,
      1e+09,
      [
         ["paramId", int, 260264],
         ["discipline", int, 0],
         ["parameterCategory", int, 4],
         ["parameterNumber", int, 13],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfStatisticalProcessing", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

   [
      "time_integrated_surface_net_solar_radiation_sfc.lam",
      -0.1,
      1e+08,
      0,
      1e+09,
      [
         ["paramId", int, 176],
         ["discipline", int, 0],
         ["parameterCategory", int, 4],
         ["parameterNumber", int, 9],
         ["typeOfStatisticalProcessing", int, 1],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

   [
      "10_metre_wind_speed",
      0,
      10,
      10,
      300,
      [
         ["paramId", int, 207],
         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 1],
         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 10],
         [None, ],
      ],
      [point_in_time, given_level],
   ],
#'''
#  uerra, cosmo-fc: 10_metre_wind_direction maximum value 360.001 is not in [359,360]
#'''
   [
      "10_metre_wind_direction",
      0,
      0.1,
      359.,
      360.01,
      [
         ["paramId", int, 260260],
         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 10],
         [None, ],
      ],
      [point_in_time, given_level],
   ],
   [
      "10_metre_wind_gust_since_pp",
      0.001,
      10,
      10,
      150,
      [
         ["paramId", int, 49],

         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 22],

         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 10],

         ["typeOfStatisticalProcessing", int, 2],
         [None, ],
      ],
      [since_prev_pp, given_level],
   ],
   [
      "2_metre_maximum_temperature",
      200,
      340,
      200,
      340,
      [
         ["paramId", int, 201],
         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 103],
         ["typeOfStatisticalProcessing", int, 2],
         [None, ],
      ],
      [since_prev_pp, given_level],
   ],
   [
      "2_metre_minimum_temperature",
      200,
      340,
      200,
      340,
      [
         ["paramId", int, 202],
         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 103],
         ["typeOfStatisticalProcessing", int, 3],
         [None, ],
      ],
      [since_prev_pp, given_level],
   ],
   [
      "evaporation_sfc",
      -10,
       0,
       0,
       5,
      [
         ["paramId", int, 260259],
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 79],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfStatisticalProcessing", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],
   [
      "snow_depth_sfc",
       0,
       0,
       0,
       5,
      [
         ["paramId", int, 3066],
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 11],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level],
   ],

#'''
#  uerra, cosmo-det-an: surface_roughness_sfc maximum value 9.36719 is not in [1.3,1.8]
#  uerra, egrr:  surface roughness is fixed at 0.5 over land and is close to 0 over sea
#'''
   [
      "surface_roughness_sfc",
       0,
       0.001,
       0.5,
       10,
      [
         ["paramId", int, 173],
         ["discipline", int, 2],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 1],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level],
   ],
   [
      "liquid_non-frozen_soil_moisture_level",
      0,
      0.1,
      0.1,
      1,
      [
         ["paramId", int, 260210],
         ["discipline", int, 2],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 10],
         ["typeOfFirstFixedSurface", int, 151],
         [None, ],
      ],
      [point_in_time, given_level, has_bitmap, has_soil_level],
   ],
   [
      "liquid_non-frozen_soil_moisture_layer",
      0,
      0.1,
      0.1,
      1,
      [
         ["paramId", int, 260210],
         ["discipline", int, 2],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 10],
         ["typeOfFirstFixedSurface", int, 151],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["typeOfSecondFixedSurface", int, 151],
         ["scaleFactorOfSecondFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_thickness, has_bitmap, has_soil_layer],
   ],
   [
      "volumetric_soil_moisture_level",
      0,
      0.1,
      0.1,
      1,
      [
         ["paramId", int, 260199],
         ["discipline", int, 2],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 25],
         ["typeOfFirstFixedSurface", int, 151],
         [None, ],
      ],
      [point_in_time, given_level, has_bitmap, has_soil_level],
   ],
   [
      "volumetric_soil_moisture_layer",
      0,
      0.1,
      0.1,
      1,
      [
         ["paramId", int, 260199],
         ["discipline", int, 2],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 25],
         ["typeOfFirstFixedSurface", int, 151],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["typeOfSecondFixedSurface", int, 151],
         ["scaleFactorOfSecondFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_thickness, has_bitmap, has_soil_layer],
   ],
   [
      "soil_heat_flux_sfc",
      -1000,
        -10,
         10,
       1000,
      [
         ["paramId", int, 260364],
         ["discipline", int, 2],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 26],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level],
   ],

#'''
#  uerra, cosmo-an: soil_temperature_level maximum value 296.188 is not in [300,350]
#  uerra, eswi: soil_temperature_level minimum value 199.649 is not in [200,270]
#'''
   [
      "soil_temperature_level",
      180,
      270,
      280,
      350,
      [
         ["paramId", int, 260360],
         ["discipline", int, 2],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 18],
         ["typeOfFirstFixedSurface", int, 151],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level, has_bitmap, has_soil_level],
   ],

#'''
#  uerra, egrr-an-enda: soil_temperature_layer minimum value 273.125 is not in [200,230]
#'''
   [
      "soil_temperature_layer",
      200,
      280,
      285,
      350,
      [
         ["paramId", int, 260360],
         ["discipline", int, 2],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 18],
         ["typeOfFirstFixedSurface", int, 151],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["typeOfSecondFixedSurface", int, 151],
         ["scaleFactorOfSecondFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_thickness, has_bitmap, has_soil_layer],
   ],

   [
      "cloud_cover_pl.lam",
      0,
      1e-10,
      0,
      100,
      [
         ["paramId", int, 260257],
         ["discipline", int, 0],
         ["parameterCategory", int, 6],
         ["parameterNumber", int, 22],
         ["typeOfFirstFixedSurface", int, 100],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level, pressure_level],
   ],

#'''
# ========================
# this skin_temperature_sfc  must be matched by tigge and uerra (not s2s!) 
# ========================

# uerra, cosmo-an: skin_temperature_sfc minimum value 245.905 is not in [160,245]
# uerra, eswi-fc: skin_temperature_sfc maximum value 298.942 is not in [300,355]
#'''
   [
      "skin_temperature_sfc",
      160,
      300,
      280,
      355,
      [
         ["paramId", int, 235],
         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 17],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level],
   ],

#'''
#  uerra, egrr-det-an: total_column_water_vapour_sfc minimum value 5.57326 is not in [-3,2]
#'''
   [
      "total_column_water_vapour_sfc",
      -3.0,
      10,
      30,
      150,
      [
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 64],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 8],
         [None, ],
      ],
      [point_in_time, predefined_thickness],
   ],

# '''
#uerra, eswi-enfo:total_cloud_cover_sfc maximum value 96.4844 is not in [100,100]
# '''
   [
      "total_cloud_cover_sfc.ur.eswi",
      0,
      2e-10,
      90.,
      100.,
      [
         ["class", str, 0, "ur"],
         ["centre", str, 1, "eswi"],

         ["discipline", int, 0],
         ["parameterCategory", int, 6],
         ["parameterNumber", int, 1],

         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 8],
         [None, ],
      ],
      [point_in_time, predefined_thickness],
   ],
   [
      "soil_depth",
      0.005,
      100,
      0.005,
      100,
      [
         ["paramId", int, 260367],
         ["discipline", int, 2],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 27],
         ["typeOfFirstFixedSurface", int, 151],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level, has_bitmap, has_soil_level],
   ],

   [
      "volumetric_field_capacity",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260211],
         ["discipline", int, 2],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 11],
         [None, ],
      ],
      [point_in_time, has_bitmap],
   ],

   [
      "volumetric_wilting_point",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260200],
         ["discipline", int, 2],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 27],
         [None, ],
      ],
      [point_in_time, has_bitmap],
   ],
#'''
#  carra / cerra
#'''
   [
      "specific_rain_water_content_ml",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 75],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 85],
         ["typeOfFirstFixedSurface", int, 105],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level], # check model levels?? 
   ],

   [
      "specific_snow_water_content_ml",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 76],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 86],
         ["typeOfFirstFixedSurface", int, 105],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level], # check model levels?? 
   ],

   [
      "graupel_ml",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260028],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 32],
         ["typeOfFirstFixedSurface", int, 105],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level], # check model levels?? 
   ],

   [
      "turbulent_kinetic_energy_ml",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260155],

         ["discipline", int, 0],
         ["parameterCategory", int, 19],
         ["parameterNumber", int, 11],
         ["typeOfFirstFixedSurface", int, 105],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level], # check model levels?? 
   ],

   [
      "specific_rain_water_content_pl",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 75],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 85],
         ["typeOfFirstFixedSurface", int, 100],
         [None, ],
      ],
      [point_in_time, given_level, pressure_level],
   ],

   [
      "specific_snow_water_content_pl",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 76],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 86],
         ["typeOfFirstFixedSurface", int, 100],
         [None, ],
      ],
      [point_in_time, given_level, pressure_level],
   ],

   [
      "graupel_pl",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260028],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 32],
         ["typeOfFirstFixedSurface", int, 100],
         [None, ],
      ],
      [point_in_time, given_level, pressure_level],
   ],

   [
      "pseudo-adiabatic_potential_temperature_pl",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 3014],

         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 3],
         ["typeOfFirstFixedSurface", int, 100],
         [None, ],
      ],
      [point_in_time, given_level, pressure_level],
   ],

   [
      "geometric_vertical_velocity_pl",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260238],

         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 9],
         ["typeOfFirstFixedSurface", int, 100],
         [None, ],
      ],
      [point_in_time, given_level, pressure_level],
   ],

   [
      "potential_vorticity_pl",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 60],

         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 14],
         ["typeOfFirstFixedSurface", int, 100],
         [None, ],
      ],
      [point_in_time, given_level, pressure_level],
   ],

   [
      "visibility_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 3020],

         ["discipline", int, 0],
         ["parameterCategory", int, 19],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level],
   ],

   [
      "cloud_base_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260107],

         ["discipline", int, 0],
         ["parameterCategory", int, 6],
         ["parameterNumber", int, 11],
         [None, ],
      ],
      [point_in_time, predefined_level],
   ],

   [
      "cloud_top_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260108],

         ["discipline", int, 0],
         ["parameterCategory", int, 6],
         ["parameterNumber", int, 12],
         [None, ],
      ],
      [point_in_time, predefined_level],
   ],

   [
      "sea_ice_cover_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 31],

         ["discipline", int, 10],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 0],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level, has_bitmap],
   ],

   [
      "sea_surface_temperature_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 34],

         ["discipline", int, 10],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 0],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level, has_bitmap],
   ],

  [
      "precipitation_type_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260015],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 19],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level],
   ],

   [
      "specific_rain_water_content_hl",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 75],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 85],
         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level, height_level],
   ],

   [
      "specific_snow_water_content_hl",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 76],

         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 86],
         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level, height_level],
   ],

   [
      "turbulent_kinetic_energy_hl",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260155],

         ["discipline", int, 0],
         ["parameterCategory", int, 19],
         ["parameterNumber", int, 11],
         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level, height_level],
   ],
   [
      "2_metre_specific_humidity_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 174096],
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 103],
         [None, ],
      ],
      [point_in_time, given_level],
   ],
  [
      "time_integral_of_rain_flux_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 235015],
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 65],
         ["typeOfStatisticalProcessing", int, 1],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],
   [
      "total_column_cloud_liquid_water_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 78],
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 69],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 8],
         [None, ],
      ],
      [point_in_time, predefined_thickness],
   ],
   [
      "total_column_cloud_ice_water_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 79],
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 70],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 8],
         [None, ],
      ],
      [point_in_time, predefined_thickness],
   ],
   [
      "total_column_graupel_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260001],
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 74],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 8],
         [None, ],
      ],
      [point_in_time, predefined_thickness],
   ],
   [
      "direct_solar_radiation_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 47],
         ["discipline", int, 0],
         ["parameterCategory", int, 4],
         ["parameterNumber", int, 54],
         ["typeOfStatisticalProcessing", int, 1],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],
   [
      "time_integral_of_top_net_solar_radiation_flux_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 178],
         ["discipline", int, 0],
         ["parameterCategory", int, 4],
         ["parameterNumber", int, 1],
         ["typeOfStatisticalProcessing", int, 1],
         ["typeOfFirstFixedSurface", int, 8],
         [None, ],
      ],
      [from_start, predefined_level],
   ],
   [
      "time_integral_of_surface_latent_heat_evaporation_flux_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 235019],
         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 30],
         ["typeOfStatisticalProcessing", int, 1],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],
   [
      "time_integral_of_surface_latent_heat_sublimation_flux_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 235071],
         ["discipline", int, 0],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 31],
         ["typeOfStatisticalProcessing", int, 1],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],
   [
      "time_integral_of_surface_eastward_momentum_flux_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 235017],
         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 17],
         ["typeOfStatisticalProcessing", int, 1],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],
   [
      "time_integral_of_surface_northward_momentum_flux_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 235018],
         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 18],
         ["typeOfStatisticalProcessing", int, 1],
         ["typeOfFirstFixedSurface", int, 1], 
         [None, ],
      ], 
      [from_start, predefined_level],
   ],
   [
      "time_integral_of_total_solid_precipitation_flux_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260645],
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 128],
         ["typeOfStatisticalProcessing", int, 1],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],
   [
      "time_integral_of_snow_evaporation_flux_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 235072],
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 192],
         ["typeOfStatisticalProcessing", int, 1],
         ["typeOfFirstFixedSurface", int, 1],
         ["localTablesVersion", int, 1],
         [None, ],
      ], 
      [from_start, predefined_level, has_bitmap],
   ],
   [
      "10_metre_eastward_wind_gust_since_pp_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260646],
         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 23],
         ["typeOfStatisticalProcessing", int, 2],
         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 10],
         [None, ],
      ],
      [since_prev_pp, given_level],
   ],
   [
      "10_metre_northward_wind_gust_since_pp_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260647],
         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 24],
         ["typeOfStatisticalProcessing", int, 2],
         ["typeOfFirstFixedSurface", int, 103],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 10],
         [None, ],
      ],
      [since_prev_pp, given_level],
   ],
   [
      "fog_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260648],
         ["discipline", int, 0],
         ["parameterCategory", int, 6],
         ["parameterNumber", int, 50],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level],
   ],
   [
      "snow_on_ice_total_depth_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260650],
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 11],
         ["typeOfFirstFixedSurface", int, 174],
         [None, ],
      ],
      [point_in_time, predefined_level, has_bitmap],
   ],
   [
      "fraction_of_snow_cover_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260289],
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 121],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level, has_bitmap],
   ],
   [
      "snow_albedo_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 228032],
         ["discipline", int, 0],
         ["parameterCategory", int, 19],
         ["parameterNumber", int, 19],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level, has_bitmap],
   ],
   [
      "temperature_of_snow_layer_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 238],
         ["discipline", int, 2],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 28],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level, has_bitmap],
   ],
   [
      "sea_ice_thickness_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 174098],
         ["discipline", int, 10],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 1],
         ["typeOfFirstFixedSurface", int, 160],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_level, has_bitmap],
   ],
   [
      "sea_ice_surface_temperature_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260649],
         ["discipline", int, 10],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 8],
         ["typeOfFirstFixedSurface", int, 174],
         [None, ],
      ],
      [point_in_time, predefined_level, has_bitmap],
   ],
   [
      "surface_roughness_length_for_heat",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260651],
         ["discipline", int, 2],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 192],
         ["typeOfFirstFixedSurface", int, 1],
         ["localTablesVersion", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level, has_bitmap],
   ],
   [
      "volumetric_soil_ice_layer",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260644],
         ["discipline", int, 2],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 38],
         ["typeOfFirstFixedSurface", int, 151],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["typeOfSecondFixedSurface", int, 151],
         ["scaleFactorOfSecondFixedSurface", int, 0],
         [None, ],
      ],
      [point_in_time, given_thickness, has_bitmap, has_soil_layer],
   ],

#'''
#  cerra
#'''
  [
      "time_integral_of_evapotranspiration_flux_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 235073],
         ["discipline", int, 2],
         ["parameterCategory", int, 0],
         ["parameterNumber", int, 39],
         ["typeOfStatisticalProcessing", int, 1],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level, has_bitmap],
   ],
   [
      "snow_melt_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 3099],
         ["discipline", int, 0],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 16],
         ["typeOfStatisticalProcessing", int, 1],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level, has_bitmap],
   ],
   [
      "lake_total_layer_temperature_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 228011],
         ["discipline", int, 1],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 1],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 162],
         [None, ],
      ],
      [point_in_time, predefined_thickness, has_bitmap],
   ],
   [
      "lake_mix_layer_temperature_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 228008],
         ["discipline", int, 1],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 1],
         ["typeOfFirstFixedSurface", int, 166],
         [None, ],
      ],
      [point_in_time, predefined_level, has_bitmap],
   ],
   [
      "lake_mix_layer_depth_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 228009],
         ["discipline", int, 1],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 166],
         [None, ],
      ],
      [point_in_time, predefined_level, has_bitmap],
   ],
   [
      "lake_bottom_temperature_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 228010],
         ["discipline", int, 1],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 1],
         ["typeOfFirstFixedSurface", int, 162],
         [None, ],
      ],
      [point_in_time, predefined_level, has_bitmap],
   ],
   [
      "lake_shape_factor_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 228012],
         ["discipline", int, 1],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 10],
         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [point_in_time, predefined_level, has_bitmap],
   ],
   [
      "lake_ice_surface_temperature_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 228013],
         ["discipline", int, 1],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 6],
         ["typeOfFirstFixedSurface", int, 174],
         [None, ],
      ],
      [point_in_time, predefined_level, has_bitmap],
   ],
   [
      "lake_ice_total_depth_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 228014],
         ["discipline", int, 1],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 5],
         ["typeOfFirstFixedSurface", int, 174],
         ["typeOfSecondFixedSurface", int, 176],
         [None, ],
      ],
      [point_in_time, predefined_thickness, has_bitmap],
   ],
   [
      "lake_total_depth_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 228007],
         ["discipline", int, 1],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 0],
         ["typeOfFirstFixedSurface", int, 1],
         ["typeOfSecondFixedSurface", int, 162],
         [None, ],
      ],
      [point_in_time, predefined_thickness, has_bitmap],
   ],
  [
      "momentum_flux_u_component_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260062],

         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 17],

         ["typeOfStatisticalProcessing", int, 1],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

  [
      "momentum_flux_v_component_sfc",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260063],

         ["discipline", int, 0],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 18],

         ["typeOfStatisticalProcessing", int, 1],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

  [
      "time_integrated_surface_clear-sky_net_solar_radiation",
      -0.1,
      1e+08,
      0,
      1e+09,
      [
         ["paramId", int, 210],

         ["discipline", int, 0],
         ["parameterCategory", int, 4],
         ["parameterNumber", int, 11],

         ["typeOfStatisticalProcessing", int, 1],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

  [
      "time_integrated_surface_clear-sky_net_thermal_radiation",
      -0.1,
      1e+08,
      0,
      1e+09,
      [
         ["paramId", int, 211],

         ["discipline", int, 0],
         ["parameterCategory", int, 5],
         ["parameterNumber", int, 6],

         ["typeOfStatisticalProcessing", int, 1],

         ["typeOfFirstFixedSurface", int, 1],
         [None, ],
      ],
      [from_start, predefined_level],
   ],

   [
      "turbulent_kinetic_energy_pl",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["paramId", int, 260155],

         ["discipline", int, 0],
         ["parameterCategory", int, 19],
         ["parameterNumber", int, 11],
         ["typeOfFirstFixedSurface", int, 100],
         [None, ],
      ],
      [point_in_time, given_level, pressure_level],
   ],

 #'''
 # s2s ocean parameters
 #'''

   [
      "depth_of_20_C_isotherm_o2d.s2",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["class", str, 0, "s2"],

         ["paramId", int, 151163],
         ["discipline", int, 10],
         ["parameterCategory", int, 4],
         ["parameterNumber", int, 14],

         ["typeOfFirstFixedSurface", int, 20],
         ["scaleFactorOfFirstFixedSurface", int, 2],
         ["scaledValueOfFirstFixedSurface", int, 29315],
         [None, ],
      ],
      [daily_average, given_level, has_bitmap, resolution_s2s_ocean],
   ],
   [
      "average_salinity_in_the_upper_300_m_o2d.s2",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["class", str, 0, "s2"],

         ["paramId", int, 151175],
         ["discipline", int, 10],
         ["parameterCategory", int, 4],
         ["parameterNumber", int, 21],

         ["typeOfFirstFixedSurface", int, 160],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 0],

         ["typeOfSecondFixedSurface", int, 160],
         ["scaleFactorOfSecondFixedSurface", int, 0],
         ["scaledValueOfSecondFixedSurface", int, 300],
         [None, ],
      ],
      [daily_average, given_thickness, has_bitmap, resolution_s2s_ocean],
   ],
   [
      "mean_sea_water_temperature_in_the_upper_300_m_o2d.s2",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["class", str, 0, "s2"],

         ["paramId", int, 151127],
         ["discipline", int, 10],
         ["parameterCategory", int, 4],
         ["parameterNumber", int, 15],

         ["typeOfFirstFixedSurface", int, 160],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 0],

         ["typeOfSecondFixedSurface", int, 160],
         ["scaleFactorOfSecondFixedSurface", int, 0],
         ["scaledValueOfSecondFixedSurface", int, 300],
         [None, ],
      ],
      [daily_average, given_thickness, has_bitmap, resolution_s2s_ocean],
   ],
   [
      "mean_sea_water_potential_temperature_in_the_upper_300_m_o2d.s2",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["class", str, 0, "s2"],

         ["paramId", int, 151126],
         ["discipline", int, 10],
         ["parameterCategory", int, 4],
         ["parameterNumber", int, 18],

         ["typeOfFirstFixedSurface", int, 160],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 0],

         ["typeOfSecondFixedSurface", int, 160],
         ["scaleFactorOfSecondFixedSurface", int, 0],
         ["scaledValueOfSecondFixedSurface", int, 300],
         [None, ],
      ],
      [daily_average, given_thickness, has_bitmap, resolution_s2s_ocean],
   ],
   [
      "ocean_mixed_layer_thickness_defined_by_sigma_theta_0.01_kg/m3_o2d.s2",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["class", str, 0, "s2"],

         ["paramId", int, 151225],
         ["discipline", int, 10],
         ["parameterCategory", int, 4],
         ["parameterNumber", int, 14],

         ["typeOfFirstFixedSurface", int, 169],
         ["scaleFactorOfFirstFixedSurface", int, 2],
         ["scaledValueOfFirstFixedSurface", int, 1],

         [None, ],
      ],
      [daily_average, given_level, has_bitmap, resolution_s2s_ocean],
   ],
   [
      "eastward_sea_water_velocity_o2d.s2",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["class", str, 0, "s2"],

         ["paramId", int, 151131],
         ["discipline", int, 10],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 2],

         ["typeOfFirstFixedSurface", int, 160],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 0],

         [None, ],
      ],
      [daily_average, given_level, has_bitmap, resolution_s2s_ocean],
   ],
   [
      "northward_sea_water_velocity_o2d.s2",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["class", str, 0, "s2"],

         ["paramId", int, 151132],
         ["discipline", int, 10],
         ["parameterCategory", int, 1],
         ["parameterNumber", int, 3],

         ["typeOfFirstFixedSurface", int, 160],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 0],

         [None, ],
      ],
      [daily_average, given_level, has_bitmap, resolution_s2s_ocean],
   ],
   [
      "sea-ice_thickness_o2d.s2",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["class", str, 0, "s2"],

         ["paramId", int, 174098],
         ["discipline", int, 10],
         ["parameterCategory", int, 2],
         ["parameterNumber", int, 1],

         ["typeOfFirstFixedSurface", int, 160],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 0],

         [None, ],
      ],
      [daily_average, given_level, has_bitmap, resolution_s2s_ocean],
   ],
   [
      "sea_surface_height_o2d.s2",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["class", str, 0, "s2"],

         ["paramId", int, 151145],
         ["discipline", int, 10],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 1],

         ["typeOfFirstFixedSurface", int, 160],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 0],

         [None, ],
      ],
      [daily_average, given_level, has_bitmap, resolution_s2s_ocean],
   ],
   [
      "sea_surface_practical_salinity_o2d.s2",
      -1e+8,
       1e+8,
      -1e+8,
       1e+8,
      [
         ["class", str, 0, "s2"],

         ["paramId", int, 151219],
         ["discipline", int, 10],
         ["parameterCategory", int, 3],
         ["parameterNumber", int, 3],

         ["typeOfFirstFixedSurface", int, 160],
         ["scaleFactorOfFirstFixedSurface", int, 0],
         ["scaledValueOfFirstFixedSurface", int, 0],

         [None, ],
      ],
      [daily_average, given_level, has_bitmap, resolution_s2s_ocean],
   ],

];


