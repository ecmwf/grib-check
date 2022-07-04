parameters = [
    {
        'name': "10_meter_u_velocity_sfc.glob",
        'min1': -100,
        'min2': -1,
        'max1': 1,
        'max2': 100,
        'pairs': [
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

            {'key':"paramId", 'key_type':"int", 'value_long':165, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':2, 'value_string':''},

            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'],
    },

    {
        'name': "10_meter_u_velocity_sfc.lam",
        'min1': -100,
        'min2': -1,
        'max1': 1,
        'max2': 100,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"lam"},

            {'key':"paramId", 'key_type':"int", 'value_long':165, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':2, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':10, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'],
    },

#''' 
#   MOGREPS (origin = 1(mogreps-mo-eua))
#   2014-01-10: minimum limit for 10_meter_u_velocity_sfc changed to <-100,5> because of 2014010715_00+0000
#   2014-31-03: maximum changed from <1,100> because of forecasts from 27-31.3...
#   2014-31-03: minimum  maximum changed for u,v components changed to reflect better small UK domain..
#'''
    {
        'name': "10_meter_u_velocity_sfc.lam.mogreps-mo-eua",
        'min1': -100,
        'min2': 10,
        'max1': -10,
        'max2': 100,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"lam"},
            {'key':"suiteName", 'key_type':"str", 'value_long':1, 'value_string':"mogreps-mo-eua"},

            {'key':"paramId", 'key_type':"int", 'value_long':165, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':2, 'value_string':''},

            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'],
    },

    {
        'name': "10_meter_v_velocity_sfc.glob",
        'min1': -100,
        'min2': -1,
        'max1': 1,
        'max2': 100,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':166, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':3, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':10, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'],
    },

#''' 
    #   MOGREPS (origin = 1(mogreps-mo-eua))  set up for 10_meter_u_velocity_sfc
#   2014-01-08: minimum limit for 10_meter_v_velocity_sfc changed to <-100,10> because of one early January forecast..
#   2014-31-03: minimum  maximum changed for u,v components changed to reflect better small UK domain..
#'''
    {
        'name': "10_meter_v_velocity_sfc.lam.mogreps-mo-eua",
        'min1': -100,
        'min2': 10,
        'max1': -10,
        'max2': 100,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"lam"},
            {'key':"suiteName", 'key_type':"str", 'value_long':1, 'value_string':"mogreps-mo-eua"},

            {'key':"paramId", 'key_type':"int", 'value_long':166, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':3, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':10, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'],
    },

    {
        'name': "convective_available_potential_energy_sfc.glob",
        'min1': 0,
        'min2': 10,
        'max1': 0,
        'max2': 17000,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':7, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':6, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_thickness'],
    },

#'''
#    2014-07-24: upper limit for cape minimum changed to <0,100> due to tigge_lam.LAEF_4tigge_08+0036.grib2, field 2 [convective_available_potential_energy_sfc.lam]: convective_available_potential_energy_sfc.lam minimum value 16.2219 is not in [0,10]
#'''

    {
        'name': "convective_available_potential_energy_sfc.lam",
        'min1': 0,
        'min2': 100,
        'max1': 0,
        'max2': 17000,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"lam"},

            {'key':"paramId", 'key_type':"int", 'value_long':59, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':7, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':6, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_thickness'],
    },

    {
        'name': "convective_available_potential_energy_sfc.lam.glameps-hirlamcons-eu",
        'min1': -1000,
        'min2': 10,
        'max1': 0,
        'max2': 17000,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"lam"},
            {'key':"suiteName", 'key_type':"str", 'value_long':9, 'value_string':"glameps-hirlamcons-eu"},

            {'key':"paramId", 'key_type':"int", 'value_long':59, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':7, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':6, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_thickness'],
    },

    {
        'name': "convective_inhibition_sfc.glob",
        'min1': -60000,
        'min2': 0,
        'max1': -10,
        'max2': 5,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':7, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':7, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},

            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_thickness'],
    },
    #''' 
    #   eggr                  (centre=74, model=1) cin max ~ -30000
    #   aladinhuneps-omsz-eu  (origin=12) cin max ~ <-60000,1>
    #   aladinlaef-zamg-eu    (origin=)   cin max ~ <-...,1>
    #   cosmodeeps-dwd-eu (origin=7)
    #   2014-07-24: max upper limit change to <0, 4000> => tigge_lam.2014062818_slevels_lfff00000000.m011.grib2: convective_inhibition_sfc.lam.cosmodeeps-dwd-eu maximum value 3041.35 is not in [0,2000]
    #'''
    {
        'name': "convective_inhibition_sfc.lam",
        'min1': -60000,
        'min2': 1,
        'max1': -10,
        'max2': 4000,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"lam"},

            {'key':"paramId", 'key_type':"int", 'value_long':228001, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':7, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':7, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_thickness'],
    },

    {
        'name': "field_capacity_sfc",
        'min1': 1e99,
        'min2': -1e99,
        'max1': 99,
        'max2': -99,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':12, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaleFactorOfSecondFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfSecondFixedSurface", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':106, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':106, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_thickness', 'has_bitmap'],
    },

    {
        'name': "land_sea_mask_sfc.glob",
        'min1': 0,
        'min2': 0,
        'max1': 1,
        'max2': 1,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':172, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level'],
    },

    {
        'name': "land_sea_mask_sfc.lam.hirlam-dmi-eu",
        'min1': -0.001,
        'min2': 0,
        'max1': 1,
        'max2': 1.11,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"lam"},
            {'key':"suiteName", 'key_type':"str", 'value_long':11, 'value_string':"hirlam-dmi-eu"},

            {'key':"paramId", 'key_type':"int", 'value_long':172, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level'],
    },

    #''' 
    #   MOGREPS (origin = 1(mogreps-mo-eua))
    #   2014-01-08: limits for orog changed to <1000,8888>
    #'''

    {
        'name': "orography_sfc",
        'min1': -1300,
        'min2': 0,
        'max1': 1000,
        'max2': 8888,
        'pairs':[
        {'key':"paramId", 'key_type':"int", 'value_long':228002, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':5, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level'],
    },


    {
        'name': "potential_temperature_pv",
        'min1': 220,
        'min2': 265,
        'max1': 380,
        'max2': 1200,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':109, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'potential_vorticity_level'],
    },

    {
        'name': "potential_vorticity_pt",
        'min1': -0.005,
        'min2': -1e-6,
        'max1': 1e-6,
        'max2': 0.002,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':14, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':320, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':107, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'potential_temperature_level'],
    },

    {
        'name': "snow_depth_water_equivalent_sfc",
        'min1': 0,
        'min2': 0,
        'max1': 100,
        'max2': 15000,
        'pairs':[

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':60, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level'],
    },

    {
        'name': "snow_fall_water_equivalent_sfc",
        'min1': -1.5e+6,
        'min2':  1.5e+6,
        'max1': -1.5e+6,
        'max2':  1.5e+6,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"paramId", 'key_type':"int", 'value_long':228144, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':53, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

    {
        'name': "soil_moisture_sfc",
        'min1': -1e-19,
        'min2': 0,
        'max1': 450,
        'max2': 800,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':22, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaleFactorOfSecondFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfSecondFixedSurface", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':106, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':106, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_thickness', 'has_bitmap'],
    },

    {
        'name': "soil_temperature_sfc",
        'min1': 200,
        'min2': 230,
        'max1': 300,
        'max2': 350,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaleFactorOfSecondFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfSecondFixedSurface", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':106, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':106, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_thickness'],
    },
#''' 
#   S2S/CAWCR: specific_humidity_pl minimum value -0.0108485 is not in [-0.01,0.001]
#   s2s/ammc: warning: s2s.q_20160623_4.grib2, field 288 [specific_humidity_pl]: specific_humidity_pl minimum value -0.0209212 is not in [-0.02,0.001]
#   s2s/ammc: warning: s2s.q_20160717_21.grib2, field 99 [specific_humidity_pl]: specific_humidity_pl maximum value 0.0820876 is not in [5e-05,0.08]
#'''
    {
        'name': "specific_humidity_pl",
        'min1': -1e-1,
        'min2': 1.e-3,
        'max1': 5e-5,
        'max2': 1e-1,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':100, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'pressure_level'],
    },

    {
        'name': "sunshine_duration_sfc",
        'min1': 0,
        'min2': 0,
        'max1': 3600.00000001,
        'max2': 3600.00000001,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':6, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':24, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

    {
        'name': "surface_air_temperature_sfc.glob",
        'min1': 180,
        'min2': 290,
        'max1': 270,
        'max2': 350,
        'pairs':[
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'],
    },

#''' 
#   cosmodeeps-dwd-eu (origin=7)
#   2014-01-08: minimum limit for surface_air_dew_point_temperature_sfc changed to <160,290>
#   2014-11-06: glameps: tigge_lam.20141106_00+042.mem012.grib2, surface_air_dew_point_temperature_sfc.lam minimum value 128.003 is not in [160,290]
#     => [128.003,290]
#'''
    {
        'name': "surface_air_dew_point_temperature_sfc.lam",
        'min1': 110,
        'min2': 290,
        'max1': 270,
        'max2': 350,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"lam"},

            {'key':"paramId", 'key_type':"int", 'value_long':168, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':6, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':2, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'],
    },

# mogreps specific set up! => 1.5m instead of 2m measurements 
    {
        'name': "surface_air_dew_point_temperature_sfc.lam",
        'min1': 110,
        'min2': 290,
        'max1': 270,
        'max2': 350,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"lam"},
            {'key':"suiteName", 'key_type':"str", 'value_long':1, 'value_string':"mogreps-mo-eua"},

            {'key':"paramId", 'key_type':"int", 'value_long':168, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':6, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':15, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'],
    },
#''' 
        #   S2S/CAWCR: surface_air_maximum_temperature_sfc maximum value 359.388 is not in [300,330]
#s2s/kwbc/enfh: warning: s2s.z_s2s_c_rhmc_20150819000000_glob_prod_0006_000.sl.grib2, field 2 [surface_air_maximum_temperature_sfc]: surface_air_maximum_temperature_sfc minimum value 179.427 is not in [190,240]
#s2s/kwbc/enfh: warning: s2s.z_tigge_c_kwbc_20071002000000_ncep_prod_pf_sl_0006_001_0000_mx2t6.grib2, field 146 [surface_air_maximum_temperature_sfc]: surface_air_maximum_temperature_sfc minimum value 240.208 is not in [175,240]
#s2s/isac/enfo: warning: z_s2s_c_isac_201510190000_glob_prod_pf_0744_05.sl.grib2, field 513 [surface_air_maximum_temperature_sfc]: surface_air_maximum_temperature_sfc minimum value 245.143 is not in [175,245]
#s2s/lfpw/enfo: warning: s2s.lfpw_mx2t6_2.grib2, field 86 [surface_air_maximum_temperature_sfc]: surface_air_maximum_temperature_sfc minimum value 250.116 is not in [160,250]
#'''
    {
        'name': "surface_air_maximum_temperature_sfc",
        'min1': 160,
        'min2': 255,
        'max1': 300,
        'max2': 380,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"paramId", 'key_type':"int", 'value_long':121, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':2, 'value_string':''},
        ],
        'checks': ['six_hourly', 'given_level'],
    },
#'''
        #s2s_devel, ecmf, 20141222, 00UTC, test, enfo, real warning: s2s.2014122200.test.768.50.pf.sl.516.grib2, field 57 [surface_air_minimum_temperature_sfc]: surface_air_minimum_temperature_sfc maximum value 320.122 is not in [300,320]
#warning: s2s.z_tigge_c_kwbc_20090817000000_ncep_prod_pf_sl_0006_002_0000_mn2t6.grib2, field 100 [surface_air_minimum_temperature_sfc]: surface_air_minimum_temperature_sfc minimum value 188.577 is not in [190,240]
#s2s/kwbc/enfh: warning: s2s.z_s2s_c_rhmc_20150819000000_glob_prod_0006_000.sl.grib2, field 1 [surface_air_minimum_temperature_sfc]: surface_air_minimum_temperature_sfc minimum value 179.642 is not in [183,240]
#s2s/ammc/enfo: warning: s2s.mn2t6_20150917_24.grib2, field 1 [surface_air_minimum_temperature_sfc]: surface_air_minimum_temperature_sfc minimum value 167.556 is not in [175,240]
#s2s/isac/enfo: warning: z_s2s_c_isac_201510190000_glob_prod_pf_0744_24.sl.grib2, field 671 [surface_air_minimum_temperature_sfc]: surface_air_minimum_temperature_sfc minimum value 241.292 is not in [160,240]
#s2s/rums/enfh: warning: s2s.z_s2s_c_rhmc_19910316000000_glob_prod_009.sl.grib2, field 2204 [surface_air_minimum_temperature_sfc]: surface_air_minimum_temperature_sfc maximum value 325.122 is not in [300,325]
#s2s/lfpw/enfo: warning: s2s.lfpw_mn2t6_2.grib2, field 82 [surface_air_minimum_temperature_sfc]: surface_air_minimum_temperature_sfc minimum value 250.259 is not in [160,250]
#'''

    {
        'name': "surface_air_minimum_temperature_sfc",
        'min1': 160,
        'min2': 260,
        'max1': 300,
        'max2': 330,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"paramId", 'key_type':"int", 'value_long':122, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':3, 'value_string':''},
        ],
    'checks': ['six_hourly', 'given_level'],
    },

#'''
#s2s/ammc: warning: s2s.mx2t6_20150910_4.grib2, field 200 [surface_air_maximum_temperature_sfc.ammc]: surface_air_maximum_temperature_sfc.ammc maximum value 1516.03 is not in [300,1500]
#s2s/ammc: warning: s2s.mx2t6_20151224_26.grib2, field 47 [surface_air_maximum_temperature_sfc.ammc]: surface_air_maximum_temperature_sfc.ammc maximum value 6963.63 is not in [300,5000]
#'''
    {
        'name': "surface_air_maximum_temperature_sfc.ammc",
        'min1': 175,
        'min2': 240,
        'max1': 300,
        'max2': 10000,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"centre", 'key_type':"str", 'value_long':1, 'value_string':"ammc"},
            {'key':"paramId", 'key_type':"int", 'value_long':121, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':2, 'value_string':''},
        ],
        'checks': ['six_hourly', 'given_level'],
    },

    {
        'name': "time_integrated_top_net_thermal_radiation_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':179, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':5, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':5, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

    {
        'name': "time_integrated_surface_latent_heat_flux_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':147, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },
#'''
        # s2s/enfh/rums: warning: s2s.z_s2s_c_rhmc_19850217000000_glob_prod_1296_000.sl.grib2, field 24 [time_integrated_surface_net_solar_radiation_sfc]: time_integrated_surface_net_solar_radiation_sfc minimum value 20718.7 is not in [-0.1,20000]
# s2s/enfo/ammc: warning: s2s.ssr_20160807_25.grib2, field 62 [time_integrated_surface_net_solar_radiation_sfc]: time_integrated_surface_net_solar_radiation_sfc minimum value 10280.6 is not in [-0.1,10000]
# '''
    {
        'name': "time_integrated_surface_net_solar_radiation_sfc.glob",
        'min1': -10,
        'min2': 1e+05,
        'max1': 1e+05,
        'max2': 1e+07,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':176, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':4, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':9, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

    {
        'name': "time_integrated_surface_net_solar_radiation_downwards_sfc",
        'min1': -10,
        'min2': 1e+07,
        'max1': 1e+05,
        'max2': 1e+09,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':169, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':4, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':7, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

    {
        'name': "time_integrated_surface_net_thermal_radiation_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"paramId", 'key_type':"int", 'value_long':177, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':5, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':5, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

    {
        'name': "time_integrated_surface_net_thermal_radiation_downwards_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"paramId", 'key_type':"int", 'value_long':175, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':5, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

    {
        'name': "time_integrated_surface_sensible_heat_flux_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"paramId", 'key_type':"int", 'value_long':146, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':11, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

    {
        'name': "total_cloud_cover_sfc",
        'min1': 0,
        'min2': 1e-10,
        'max1': 100,
        'max2': 100.00001,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':6, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_thickness'],
    },

#'''
#   hourly extreems for cumulated parameters!

#   - TBD: the problem is that for tigge/tigge-lam there are cumulated parameters from step 0 and
#          the limits for e.g. 0-3 period should be very different to ones for e.g. 0-120 even
#          the value is divided by the period length in hours!
#'''

    {
        'name': "total_precipitation_sfc.glob",
        'min1': -0.05,
        'min2': 0.1,
        'max1': 0.,
        'max2': 100.,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

            {'key':"paramId", 'key_type':"int", 'value_long':228228, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':52, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

#'''
#    2013-xx-yy: maximum changed to <0,133> because of cosmo-de boundary effects when coupled with IFS ..
#    glameps: warning: tigge_lam.20160814_00+006.mem026.grib2, field 6 [total_precipitation_sfc.lam]: total_precipitation_sfc.lam maximum value 361.151 is not in [0,350]
#'''

    {
        'name': "total_precipitation_sfc.lam",
        'min1': -0.05,
        'min2': 0.1,
        'max1': 0.,
        'max2': 400.,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"lam"},

            {'key':"paramId", 'key_type':"int", 'value_long':228228, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':52, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

#hourly extreems for cumulated parameters! 
    {
        'name': "large_scale_precipitation_sfc.glob",
        'min1': -0.05,
        'min2': 0.1,
        'max1': 0.0,
        'max2': 100.,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':54, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},

            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':255, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

#'''
#   glameps-hirlamcons-eu: warning: tigge_lam.20160814_00+009.mem026.grib2, field 7 [large_scale_precipitation_sfc.lam]: large_scale_precipitation_sfc.lam maximum value 370.829 is not in [0,350]
#'''
    {
        'name': "large_scale_precipitation_sfc.lam",
        'min1': -0.05,
        'min2': 0.1,
        'max1': 0.0,
        'max2': 400.,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"lam"},

            {'key':"paramId", 'key_type':"int", 'value_long':3062, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':54, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

    {
        'name': "wilting_point_sfc",
        'min1': 1e99,
        'min2': -1e99,
        'max1': 99,
        'max2': -99,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':26, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaleFactorOfSecondFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfSecondFixedSurface", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':106, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':106, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_thickness', 'has_bitmap'],
    },

#''' 
#   cosmoleps-arpasimc-eu 20140323, 12UTC, prod: tigge_lam.vmax_10m.9999.grib2, field 11 [maximum_wind_gust.lam]: maximum_wind_gust.lam maximum value 106.861 is not in [0,100] 
#'''

    {
        'name': "maximum_wind_gust.lam",
        'min1': 0,
        'min2': 15,
        'max1': 0,
        'max2': 150,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"lam"},

            {'key':"paramId", 'key_type':"int", 'value_long':228028, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':22, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':2, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':10, 'value_string':''},
        ],
        'checks': ['three_hourly', 'given_level'],
    },

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

    {
        'name': "maximum_wind_gust.lam.mogreps",
        'min1': 0,
        'min2': 20,
        'max1': 0,
        'max2': 800,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"lam"},
            {'key':"suiteName", 'key_type':"str", 'value_long':1, 'value_string':"mogreps-mo-eua"},

            {'key':"paramId", 'key_type':"int", 'value_long':228028, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':22, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':2, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':10, 'value_string':''},
        ],
        'checks': ['three_hourly', 'given_level'],
    },

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
    {
        'name': "mean_sea_level_pressure_sfc",
        'min1': 88000,
        'min2': 104000,
        'max1': 98000,
        'max2': 115000,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':151, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':101, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level'],
    },

#'''
#s2s/lfpw: warning: s2s.lfpw_msl_0.grib2, field 1 [mean_sea_level_pressure_sfc]: mean_sea_level_pressure_sfc maximum value 120427 is not in [98000,109000] xxx should be fixed by provider!!
#'''
    {
        'name': "mean_sea_level_pressure_sfc.lfpw",
        'min1': 85000,
        'min2': 104000,
        'max1': 98000,
        'max2': 121000,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':151, 'value_string':''},
            {'key':"centre", 'key_type':"str", 'value_long':1, 'value_string':"lfpw"},
            {'key':"step", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':101, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level'],
    },

#'''
#s2s_devel, ecmf, 20141229, 00UTC, test, enfh, real:    s2s.2014122900.test.768.10.pf.20131229.pl.720.grib2, field 450 [geopotential_height_pl]: geopotential_height_pl minimum value 30321.6 is not in [-850,30000]
#warning: s2s.2015082000.prod.1104.50.pf.pl.648.grib2, field 2241 [geopotential_height_pl]: geopotential_height_pl minimum value -876.714 is not in [-850,30500]
#s2s/lfpw: warning: s2s.lfpw_gh_1000.grib2, field 1 [geopotential_height_pl]: geopotential_height_pl minimum value -1199.08 is not in [-1000,30500]
#s2s/egrr: s2s.z_s2s_c_ukmo_20160102000000_glob_prod_pf_1440_002.rt.pl.grib2, field 1211 [geopotential_height_pl]: geopotential_height_pl minimum value 30506.8 is not in [-1300,30500]
#'''
    {
        'name': "geopotential_height_pl",
        'min1': -5000,
        'min2': 30600,
        'max1': 200,
        'max2': 35000,
        'pairs':[
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':5, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':100, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'pressure_level'],
    },

    {
        'name': "geopotential_pl",
        'min1': -5000,
        'min2': 306000,
        'max1': 2000,
        'max2': 350000,
        'pairs':[
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':4, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':100, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'pressure_level'],
    },


#'''
#warning: s2s.lfpw_t_10.grib2, field 61 [temperature_pl]: temperature_pl minimum value 159.934 is not in [160,260]
#s2s/egrr: warning: s2s.z_s2s_c_ukmo_19960417000000_glob_prod_pf_1440_002.hc.pl.grib2, field 450 [temperature_pl]: temperature_pl minimum value 260.687 is not in [150,260]
#s2s/egrr-enfo warning: s2s.z_s2s_c_ukmo_20160520000000_glob_prod_pf_1440_003.rt.pl.grib2, field 450 [temperature_pl]: temperature_pl minimum value 270.611 is not in [150,270]
#'''

    {
        'name': "temperature_pl",
        'min1': 150,
        'min2': 275,
        'max1': 200,
        'max2': 330,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

            {'key':"paramId", 'key_type':"int", 'value_long':130, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':100, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'pressure_level'],
    },
#''' 
#   S2S/ammc: warning: s2s.t_20150906_21.grib2, field 11 [temperature_pl]: temperature_pl minimum value 44.6657 is not in [50,260]
#   S2S/ammc: warning: s2s.t_20150906_24.grib2, field 321 [temperature_pl]: temperature_pl minimum value -48.9135 is not in [50,260]
#   S2S/ammc: warning: s2s.t_20160403_16.grib2, field 571 [temperature_pl.ammc]: temperature_pl.ammc maximum value 343.462 is not in [200,340]
#'''
    {
    'name': "temperature_pl.ammc",
    'min1': -999,
    'min2': 260,
    'max1': 200,
    'max2': 350,
    'pairs':[
        {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

        {'key':"paramId", 'key_type':"int", 'value_long':130, 'value_string':''},
        {'key':"centre", 'key_type':"str", 'value_long':1, 'value_string':"ammc"},

        {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
        {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
        {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},

        {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':100, 'value_string':''},
    ],
    'checks': ['point_in_time', 'given_level', 'pressure_level'],
},
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
    {
        'name': "u_velocity_pl",
        'min1': -250,
        'min2': 5,
        'max1': 1,
        'max2': 250,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':131, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':2, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':100, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'pressure_level'],
    },


#''' 
#   S2S/CAWCR: v_velocity_pl maximum value 8.54936 is not in [10,150]
#   S2S/CAWCR: v_velocity_pl minimum value -128.209 is not in [-120,-10]
#   ammc-s2s-enfo: warning: s2s.v_20160131_0.grib2, field 430 [v_velocity_pl]: v_velocity_pl minimum value -4.84592 is not in [-190,-5]
#   ammc-s2s-enfo: warning: s2s.v_20160324_7.grib2, field 160 [v_velocity_pl]: v_velocity_pl maximum value 3.79724 is not in [4,190]
#   ammc-s2s-enfo: warning: s2s.v_20160526_0.grib2, field 611 [v_velocity_pl]: v_velocity_pl minimum value -194.691 is not in [-190,-2]
#'''
    {
        'name': "v_velocity_pl",
        'min1': -200,
        'min2': -2,
        'max1': 2,
        'max2': 200,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

            {'key':"paramId", 'key_type':"int", 'value_long':132, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':3, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':100, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'pressure_level'],
    },

    {
        'name': "u_velocity_pv",
        'min1': -120,
        'min2': -30,
        'max1': 70,
        'max2': 120,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':109, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'potential_vorticity_level'],
    },

    {
        'name': "v_velocity_pv",
        'min1': -120,
        'min2': -50,
        'max1': 55,
        'max2': 120,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':109, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'potential_vorticity_level'],
    },
#'''
#   s2s_devel, ecmf, 20150101, 00UTC, test, enfh, warning: s2s.2015010100.test.768.10.pf.20020101.pl.0.grib2, field 372 [w_vertical_velocity_pl]: w_vertical_velocity_pl minimum value -5.02998 is not in [-5,0] 
#warning: s2s.z_tigge_c_kwbc_20150817000000_ncep_prod_pf_pl_0000_015_0500_w.grib2, field 3 [w_vertical_velocity_pl]: w_vertical_velocity_pl minimum value -7.25731 is not in [-6,0]
#  s2s/kwbc/enfo: warning: s2s.z_tigge_c_kwbc_20151114000000_ncep_prod_pf_pl_0000_011_0500_w.grib2, field 7 [w_vertical_velocity_pl]: w_vertical_velocity_pl minimum value -10.202 is not in [-10,0]
#  s2s/cwao/enfo: warning: s2s.z_s2s_c_cwao_20160512000000_glob_prod_??_pl_00_384_003.grib2, field 28 [w_vertical_velocity_pl]: w_vertical_velocity_pl minimum value -19.8681 is not in [-12,0]
#  s2s/rksl/enfh: warning: s2s.002.pl.grib2, field 2489 [w_vertical_velocity_pl]: w_vertical_velocity_pl maximum value -1.23174 is not in [-1,25]

#'''
    {
        'name': "w_vertical_velocity_pl",
        'min1': -25,
        'min2': 0,
        'max1': -2,
        'max2': 25,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':135, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':8, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':100, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'pressure_level'],
    },

    {
        'name': "soil_type_sfc",
        'min1': 0,
        'min2': 1,
        'max1': 5,
        'max2': 10,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

            {'key':"paramId", 'key_type':"int", 'value_long':43, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level', 'has_bitmap'],
    },
#'''
#s2s_devel, ecmf, 20141229, 00UTC, test, enfh, real:  s2s.2014122900.test.768.10.pf.19941229.sl.168.grib2, field 21 [surface_pressure_sfc]: surface_pressure_sfc maximum value 102851 is not in [102900,110000]
#uerra, eswi-an: an.sp.sfc.grib2, field 1 [surface_pressure_sfc]: surface_pressure_sfc minimum value 66482.1 is not in [48000,55000]
#'''
    {
        'name': "surface_pressure_sfc",
        'min1': 48000,
        'min2': 80000,
        'max1': 101500,
        'max2': 115000,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

            {'key':"paramId", 'key_type':"int", 'value_long':134, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level'],
    },

##todo limits
    {
        'name': "eastward_turbulent_surface_stress_sfc",
        'min1': -1.5e+6,
        'min2': 1.5e+6,
        'max1': -1.5e+6,
        'max2': 1.5e+6,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

            {'key':"paramId", 'key_type':"int", 'value_long':180, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':38, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

##todo limits
    {
        'name': "northward_turbulent_surface_stress_sfc",
        'min1': -1.5e+6,
        'min2': 1.5e+6,
        'max1': -1.5e+6,
        'max2': 1.5e+6,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

            {'key':"paramId", 'key_type':"int", 'value_long':181, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':37, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },


    {
        'name': "water_runoff_sfc",
        'min1': -0.001,
        'min2': 5,
        'max1': 0.3,
        'max2': 30,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

            {'key':"paramId", 'key_type':"int", 'value_long':228205, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':33, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level', 'has_bitmap'],
    },

    {
        'name': "sea_ice_cover_sfc.glob",
        'min1': -1.5e+6,
        'min2': 1.5e+6,
        'max1': -1.5e+6,
        'max2': 1.5e+6,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

            {'key':"paramId", 'key_type':"int", 'value_long':31, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level', 'has_bitmap'],
    },

    {
        'name': "snow_density_sfc.glob",
        'min1': -1.5e+6,
        'min2': 1.5e+6,
        'max1': -1.5e+6,
        'max2': 1.5e+6,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

            {'key':"paramId", 'key_type':"int", 'value_long':33, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':61, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level', 'has_bitmap'],
    },

    {
        'name': "sea_surface_temperature_sfc.glob",
        'min1': 200,
        'min2': 290,
        'max1': 260,
        'max2': 320,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

            {'key':"paramId", 'key_type':"int", 'value_long':34, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level', 'has_bitmap'],
    },

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
#         {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
#         {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},
#         {'key':"centre", 'key_type':"str", 'value_long':1, 'value_string':"rums"},

#         {'key':"paramId", 'key_type':"int", 'value_long':34, 'value_string':''},

#         {'key':"discipline", 'key_type':"int", 'value_long':10, 'value_string':''},
#         {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
#         {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},

#         {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
#         [None, ],
#      ],
#      'checks': ['daily_average', 'predefined_level', 'has_bitmap'],
#   ],
#'''

    {
        'name': "convective_available_potential_energy_sfc.glob.s2",
        'min1': 0,
        'min2': 10,
        'max1': 0,
        'max2': 17000,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},

            {'key':"paramId", 'key_type':"int", 'value_long':59, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':7, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':6, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['daily_average', 'predefined_thickness', 'resolution_s2s'],
    },
#''' 
#   S2S/CAWCR: total_column_water_sfc.glob minimum value 0.00832421 is not in [0.01,1]
#warning: s2s.z_tigge_c_kwbc_19990817000000_ncep_prod_cf_sl_0024_000_0000_tcw.grib2, field 33 [total_column_water_sfc.glob]: total_column_water_sfc.glob minimum value -0.168614 is not in [0.001,1]
#warning: s2s.z_tigge_c_kwbc_20090829000000_ncep_prod_pf_sl_0024_003_0000_tcw.grib2, field 11 [total_column_water_sfc.glob]: total_column_water_sfc.glob minimum value -2.00987 is not in [-2,1]
#  lfpw/enfo: warning: s2s.lfpw_tcw_0.grib2, field 10 [total_column_water_sfc.glob.s2]: total_column_water_sfc.glob.s2 minimum value 1.01153 is not in [-3,1]
#  uerra, eswi-an: an.tcw.sfc.grib2, field 1 [total_column_water_sfc]: total_column_water_sfc maximum value 37.9248 is not in [50,150]
#'''
    {
        'name': "total_column_water_sfc.s2",
        'min1': -3.0,
        'min2': 2,
        'max1': 30,
        'max2': 150,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':51, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['daily_average', 'predefined_thickness', 'resolution_s2s'],
    },

    {
        'name': "total_column_water_sfc",
        'min1': -3.0,
        'min2': 2,
        'max1': 30,
        'max2': 150,
        'pairs':[
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':51, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_thickness'],
    },

#'''
#s2s/rums warning: s2s.z_s2s_c_rhmc_20150819000000_glob_prod_0336_017.sl.grib2, field 4 [surface_air_temperature_sfc.glob]: surface_air_temperature_sfc.glob minimum value 177.17 is not in [180,290]
#s2s/ammc: warning: s2s.2t_20151224_26.grib2, field 12 [surface_air_temperature_sfc.glob.s2]: surface_air_temperature_sfc.glob.s2 maximum value 353.017 is not in [270,350]
#'''

    {
        'name': "surface_air_temperature_sfc.glob.s2",
        'min1': 170,
        'min2': 290,
        'max1': 270,
        'max2': 360,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},

            {'key':"paramId", 'key_type':"int", 'value_long':167, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
        ],
        'checks': ['daily_average', 'given_level', 'resolution_s2s'],
    },

    {
        'name': "surface_air_dew_point_temperature_sfc",
        'min1': 30,
        'min2': 290,
        'max1': 270,
        'max2': 350,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

            {'key':"paramId", 'key_type':"int", 'value_long':168, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':6, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'],
    },

#''' 
#   S2S/CAWCR: surface_air_dew_point_temperature_sfc.glob minimum value 32.4337 is not in [175,290]
#'''
    {
        'name': "surface_air_dew_point_temperature_sfc.s2",
        'min1': 30,
        'min2': 290,
        'max1': 270,
        'max2': 350,
        'pairs':[
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},

            {'key':"paramId", 'key_type':"int", 'value_long':168, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':6, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
        ],
        'checks': ['daily_average', 'given_level', 'resolution_s2s'],
    },
#''' 
#   S2S/CAWCR: skin_temperature_sfc.glob maximum value 309.28 is not in [310,355]
#s2s/kwbc/enfh: warning: s2s.z_s2s_c_rhmc_20150819000000_glob_prod_1464_000.sl.grib2, field 17 [skin_temperature_sfc.glob]: skin_temperature_sfc.glob minimum value 237.261 is not in [
#s2s/rums/enfo warning: s2s.z_s2s_c_rhmc_20150826000000_glob_prod_1392_003.sl.grib2, field 15 [skin_temperature_sfc.glob]: skin_temperature_sfc.glob minimum value 240.467 is not in [180,240]
#s2s/ammc/enfo warning: warning: s2s.skt_20150920_4.grib2, field 12 [skin_temperature_sfc.glob]: skin_temperature_sfc.glob minimum value 179.087 is not in [180,245]
#s2s/ammc/enfo warning: warning: s2s.skt_20160410_21.grib2, field 57 [skin_temperature_sfc.glob.s2]: skin_temperature_sfc.glob.s2 minimum value 164.277 is not in [175,245]
#uerra/egrr/det/an: skin_temperature_sfc minimum value 266.875 is not in [160,250]
#'''
    {
        'name': "skin_temperature_sfc.s2",
        'min1': 160,
        'min2': 300,
        'max1': 300,
        'max2': 355,
        'pairs':[
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':17, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['daily_average', 'predefined_level', 'resolution_s2s'],
    },

#''' 
#   S2S/CAWCR: soil_moisture_top_20_cm_sfc.glob maximum value 150 is not in [450,800]
#warning: s2s.z_s2s_c_babj_20150817000000_glob_prod_cf_1440_000.sl.grib2, field 1641 [soil_moisture_top_20_cm_sfc.glob]: soil_moisture_top_20_cm_sfc.glob minimum value 59.5781 is not in [-1e-17,0]
#'''

    {
        'name': "soil_moisture_top_20_cm_sfc.glob",
        'min1': -1e-17,
        'min2': 70,
        'max1': 100,
        'max2': 1500,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

            {'key':"paramId", 'key_type':"int", 'value_long':228086, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':22, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':106, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':106, 'value_string':''},
            {'key':"scaleFactorOfSecondFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"scaledValueOfSecondFixedSurface", 'key_type':"int", 'value_long':2, 'value_string':''},
        ],
        'checks': ['daily_average', 'given_thickness', 'has_bitmap'],
    },

#'''
#warning: s2s.z_s2s_c_babj_20150901000000_glob_prod_pf_1440_002.sl.grib2, field 1621 [soil_moisture_top_100_cm_sfc.glob]: soil_moisture_top_100_cm_sfc.glob minimum value 60.1641 is not in [-1e-16,60]
#warning: s2s.z_s2s_c_babj_20150817000000_glob_prod_cf_1440_000.sl.grib2, field 1745 [soil_moisture_top_100_cm_sfc.glob]: soil_moisture_top_100_cm_sfc.glob maximum value 1382.83 is not in [450,800]
#warning: s2s.2015092100.prod.1104.10.pf.19980921.sl.48.grib2, field 220 [soil_moisture_top_100_cm_sfc.glob]: soil_moisture_top_100_cm_sfc.glob minimum value -1.07114e-16 is not in [-1e-16,60]
#s2s/rums warning: s2s.z_s2s_c_rhmc_20150819000000_glob_prod_1464_001.sl.grib2, field 17 [soil_moisture_top_100_cm_sfc.glob]: soil_moisture_top_100_cm_sfc.glob maximum value 413.812 is not in [450,1400]
#'''
    {
        'name': "soil_moisture_top_100_cm_sfc.glob",
        'min1': -1e-15,
        'min2': 70,
        'max1': 380,
        'max2': 1400,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

            {'key':"paramId", 'key_type':"int", 'value_long':228087, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':22, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':106, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':106, 'value_string':''},
            {'key':"scaleFactorOfSecondFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"scaledValueOfSecondFixedSurface", 'key_type':"int", 'value_long':10, 'value_string':''},
        ],
        'checks': ['daily_average', 'given_thickness', 'has_bitmap'],
    },
#'''
#s2s_devel/ecmf/enfh/rea: warning: s2s.2015011200.test.768.10.cf.20100112.sl.24.grib2, field 25 [soil_temperature_top_20_cm_sfc.glob]: soil_temperature_top_20_cm_sfc.glob minimum value 199.519 is not in [200,230]
#s2s_prod/ammc/enfo:warning: s2s.st20_20151004_4.grib2, field 61 [soil_temperature_top_20_cm_sfc.glob]: soil_temperature_top_20_cm_sfc.glob minimum value 231.081 is not in [180,230]
#'''
    {
    'name': "soil_temperature_top_20_cm_sfc.glob",
    'min1': 180,
    'min2': 240,
    'max1': 300,
    'max2': 350,
    'pairs':[
        {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

        {'key':"paramId", 'key_type':"int", 'value_long':228095, 'value_string':''},

        {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
        {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
        {'key':"parameterNumber", 'key_type':"int", 'value_long':2, 'value_string':''},

        {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':0, 'value_string':''},

        {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':106, 'value_string':''},
        {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},

        {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':106, 'value_string':''},
        {'key':"scaleFactorOfSecondFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        {'key':"scaledValueOfSecondFixedSurface", 'key_type':"int", 'value_long':2, 'value_string':''},
    ],
    'checks': ['daily_average', 'given_thickness', 'has_bitmap'],
},

#'''
#   s2s/rums warning: s2s.z_s2s_c_rhmc_20150819000000_glob_prod_0024_000.sl.grib2, field 26 [soil_temperature_top_20_cm_sfc.glob]: soil_temperature_top_20_cm_sfc.glob minimum value 0 is not in [180,230] xxx must be fiexed!!!
#   s2s/rums warning: warning: s2s.z_s2s_c_rhmc_20151021000000_glob_prod_0336_019.sl.grib2, field 24 [soil_temperature_top_20_cm_sfc.glob]: soil_temperature_top_20_cm_sfc.glob minimum value 238.514 is not in [0,230]
#'''
    {
    'name': "soil_temperature_top_20_cm_sfc.glob.rums",
    'min1': 0,
    'min2': 250,
    'max1': 300,
    'max2': 350,
    'pairs':[
        {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
        {'key':"centre", 'key_type':"str", 'value_long':1, 'value_string':"rums"},

        {'key':"paramId", 'key_type':"int", 'value_long':228095, 'value_string':''},

        {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
        {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
        {'key':"parameterNumber", 'key_type':"int", 'value_long':2, 'value_string':''},

        {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':0, 'value_string':''},

        {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':106, 'value_string':''},
        {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},

        {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':106, 'value_string':''},
        {'key':"scaleFactorOfSecondFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        {'key':"scaledValueOfSecondFixedSurface", 'key_type':"int", 'value_long':2, 'value_string':''},
    ],
    'checks': ['daily_average', 'given_thickness', 'has_bitmap'],
},


#''' 
#   S2S/babj: warning: s2s.z_s2s_c_babj_20150908000000_glob_prod_cf_1440_000.sl.grib2, field 1816 [soil_temperature_top_100_cm_sfc.glob]: soil_temperature_top_100_cm_sfc.glob minimum value 199.941 is not in [200,240]
#'''
    {
    'name': "soil_temperature_top_100_cm_sfc.glob",
    'min1': 190,
    'min2': 240,
    'max1': 300,
    'max2': 350,
    'pairs':[
        {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

        {'key':"paramId", 'key_type':"int", 'value_long':228096, 'value_string':''},

        {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
        {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
        {'key':"parameterNumber", 'key_type':"int", 'value_long':2, 'value_string':''},

        {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':0, 'value_string':''},

        {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':106, 'value_string':''},
        {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},

        {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':106, 'value_string':''},
        {'key':"scaleFactorOfSecondFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        {'key':"scaledValueOfSecondFixedSurface", 'key_type':"int", 'value_long':10, 'value_string':''},
    ],
    'checks': ['daily_average', 'given_thickness', 'has_bitmap'],
},

#''' 
#   S2S/rums: warning: s2s.z_s2s_c_rhmc_20150819000000_glob_prod_0024_000.sl.grib2, field 25 [soil_temperature_top_100_cm_sfc.glob]: soil_temperature_top_100_cm_sfc.glob minimum value 0 is not in [200,240]  xxx must be fixed!!!
#   S2S/rums: warning: s2s.z_s2s_c_rhmc_20151021000000_glob_prod_0360_019.sl.grib2, field 23 [soil_temperature_top_100_cm_sfc.glob.s2.rums]: soil_temperature_top_100_cm_sfc.glob.s2.rums minimum value 240.084 is not in [0,240]
#'''
    {
        'name': "soil_temperature_top_100_cm_sfc.glob.s2.rums",
        'min1': 0,
        'min2': 250,
        'max1': 300,
        'max2': 350,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},
            {'key':"centre", 'key_type':"str", 'value_long':1, 'value_string':"rums"},

            {'key':"paramId", 'key_type':"int", 'value_long':228096, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':2, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':106, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':106, 'value_string':''},
            {'key':"scaleFactorOfSecondFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"scaledValueOfSecondFixedSurface", 'key_type':"int", 'value_long':10, 'value_string':''},
        ],
        'checks': ['daily_average', 'given_thickness', 'has_bitmap', 'resolution_s2s'],
    },
#''' 
#   S2S/CAWCR: snow_depth_water_equivalent_sfc.glob maximum value 9066.25 is not in [10000,15000]
#warning: s2s.z_tigge_c_kwbc_19990817000000_ncep_prod_cf_sl_0024_000_0000_sd.grib2, field 19 [snow_depth_water_equivalent_sfc.glob]: snow_depth_water_equivalent_sfc.glob maximum value 219.94 is not in [9000,15000]
#  s2s/isac:warning: s2s.z_s2s_c_isac_201510190000_glob_prod_cf_0744_00.sl.grib2, field 25 [snow_depth_water_equivalent_sfc.glob]: snow_depth_water_equivalent_sfc.glob maximum value 118.824
#'''
    {
        'name': "snow_depth_water_equivalent_sfc.glob.s2",
        'min1': -0.00001,
        'min2': 0,
        'max1': 100,
        'max2': 15000,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':60, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['daily_average', 'predefined_level', 'resolution_s2s'],
    },

#'''s2s/isac:warning: s2s.z_s2s_c_isac_201510190000_glob_prod_cf_0744_00.sl.grib2, field 25 [snow_depth_water_equivalent_sfc.glob]: snow_depth_water_equivalent_sfc.glob maximum value 118.824
#  s2s/cwao:warning: warning: s2s.z_s2s_c_cwao_20130211000000_glob_prod_sl_000.grib2, field 23 [snow_depth_water_equivalent_sfc.glob.s2]: snow_depth_water_equivalent_sfc.glob.s2 maximum value 30452.5 is not in [100,15000]
#'''
    {
        'name': "snow_depth_water_equivalent_sfc.glob.s2.cwao",
        'min1': -4e-19,
        'min2': 0,
        'max1': 100,
        'max2': 40000,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},
            {'key':"centre", 'key_type':"str", 'value_long':1, 'value_string':"cwao"},

            {'key':"paramId", 'key_type':"int", 'value_long':228141, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':60, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['daily_average', 'predefined_level', 'resolution_s2s'],
    },

# '''
#warning: s2s.z_tigge_c_kwbc_20150817000000_ncep_prod_cf_sl_0024_000_0000_tcc.grib2, field 2 [total_cloud_cover_sfc.glob]: total_cloud_cover_sfc.glob maximum value 100.716 is not in [99.99,100.01]
#warning: s2s.z_s2s_c_babj_20150817000000_glob_prod_cf_1440_000.sl.grib2, field 2582 [total_cloud_cover_sfc.glob]: total_cloud_cover_sfc.glob maximum value 94.4214 is not in [99.99,100.01]
#warning: s2s.z_tigge_c_kwbc_20150817000000_ncep_prod_pf_sl_0024_009_0000_tcc.grib2, field 1 [total_cloud_cover_sfc.glob]: total_cloud_cover_sfc.glob maximum value 100.503 is not in [90,100.1]
#s2s/lfpw: warning: s2s.lfpw_tcc_0.grib2, field 60 [total_cloud_cover_sfc.glob]: total_cloud_cover_sfc.glob minimum value -0.0300206 is not in [0,5]
#s2s/ammc/enfo:s2s.tcc_20151004_9.grib2, field 21 [total_cloud_cover_sfc.glob]: total_cloud_cover_sfc.glob maximum value 128 is not in [90,101]
# '''
    {
        'name': "total_cloud_cover_sfc.glob.s2",
        'min1': -0.1,
        'min2': 5,
        'max1': 90.,
        'max2': 101.,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},

            {'key':"paramId", 'key_type':"int", 'value_long':228164, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':6, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':1, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['daily_average', 'predefined_thickness', 'resolution_s2s'],
    },

#'''
#   s2s/lfpw warning: s2s.lfpw_tcc_0.grib2, field 1 [total_cloud_cover_sfc.glob]: total_cloud_cover_sfc.glob maximum value 75 is not in [90,101] xxx should be fixed by provider!!
#'''

    {
        'name': "total_cloud_cover_sfc.glob.s2.lfpw",
        'min1': -0.1,
        'min2': 5,
        'max1': 70.,
        'max2': 101.,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},
            {'key':"centre", 'key_type':"str", 'value_long':1, 'value_string':"lfpw"},
            {'key':"step", 'key_type':"str", 'value_long':1, 'value_string':"0-24"},

            {'key':"paramId", 'key_type':"int", 'value_long':228164, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':6, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':1, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['daily_average', 'predefined_thickness', 'resolution_s2s'],
    },

    {
        'name': "convective_precipitation_sfc.glob",
        'min1': -0.05,
        'min2': 0.1,
        'max1': 0.,
        'max2': 100.,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

            {'key':"paramId", 'key_type':"int", 'value_long':228143, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':37, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

    {
        'name': "sea_ice_cover_sfc.glob.s2",
        'min1': -1.5e+6,
        'min2':  1.5e+6,
        'max1': -1.5e+6,
        'max2':  1.5e+6,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},

            {'key':"paramId", 'key_type':"int", 'value_long':31, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['daily_average', 'predefined_level', 'has_bitmap', 'resolution_s2s'],
    },

    {
        'name': "snow_density_sfc.glob.s2",
        'min1': -1.5e+6,
        'min2':  1.5e+6,
        'max1': -1.5e+6,
        'max2':  1.5e+6,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},

            {'key':"paramId", 'key_type':"int", 'value_long':33, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':61, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['daily_average', 'predefined_level', 'resolution_s2s'],
    },

#'''
#  s2s/ammc/enfo: warning: s2s.sst_20170223_4.sl.grib2, field 59 [sea_surface_temperature_sfc.glob.s2]: sea_surface_temperature_sfc.glob.s2 minimum value 194.496 is not in [200,290]
#'''

    {
        'name': "sea_surface_temperature_sfc.glob.s2",
        'min1':  180,
        'min2':  290,
        'max1':  260,
        'max2':  320,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},

            {'key':"paramId", 'key_type':"int", 'value_long':34, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['daily_average', 'predefined_level', 'has_bitmap', 'resolution_s2s'],
    },

    {
        'name': "snow_albedo_sfc.glob",
        'min1': -1.5e+6,
        'min2':  1.5e+6,
        'max1': -1.5e+6,
        'max2':  1.5e+6,
        'pairs':[
            {'key':"model", 'key_type':"str", 'value_long':0, 'value_string':"glob"},

            {'key':"paramId", 'key_type':"int", 'value_long':228032, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':19, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':19, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['daily_average', 'predefined_level', 'has_bitmap'],
    },

## UERRA 
    {
        'name': "high_cloud_cover_sfc",
        'min1': 0,
        'min2': 1e-10,
        'max1': 0.9999,
        'max2': 100.00001,
        'pairs':[
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':6, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':5, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_thickness'],
    },
    {
        'name': "medium_cloud_cover_sfc",
        'min1': 0,
        'min2': 1e-10,
        'max1': 0.9999,
        'max2': 100.00001,
        'pairs':[
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':6, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':4, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_thickness'],
    },
    {
        'name': "low_cloud_cover_sfc",
        'min1': 0,
        'min2': 1e-10,
        'max1': 0.9999,
        'max2': 100.00001,
        'pairs':[
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':6, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_thickness'],
    },
#''' 

#uerra/egrr (something like ad hoc 1 grid-point issue (similarly grid-point storms..)): warning: enda.2009-01-20.sfc.grib2, field 831 [low_cloud_cover_sfc]: low_cloud_cover_sfc maximum value 317.188 is not in [0.9999,100]
#'''
    {
        'name': "low_cloud_cover_sfc.egrr",
        'min1': 0,
        'min2': 1e-10,
        'max1': 0.9999,
        'max2': 400.00001,
        'pairs':[
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':6, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_thickness'],
    },


# uerra model levels 
    {
        'name': "pressure_ml",
        'min1': 100,
        'min2': 100000,
        'max1': 100,
        'max2': 108000,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':54, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':105, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'], # check model levels?? 
    },
    {
        'name': "pressure_ml.edzw",
        'min1': 100,
        'min2': 100000,
        'max1': 100,
        'max2': 108000,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':54, 'value_string':''},
            {'key':"origin", 'key_type':"str", 'value_long':0, 'value_string':"edzw"},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':118, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'], # check model levels?? 
    },

    {
        'name': "specific_humidity_ml",
        'min1': -0.1,
        'min2': 0.01,
        'max1': 0,
        'max2': 0.1,
        'pairs':[
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':105, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'], # check model levels?? 
    },
    {
        'name': "specific_humidity_ml.edzw",
        'min1': -0.1,
        'min2': 0.01,
        'max1': 0,
        'max2': 0.1,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':133, 'value_string':''},
            {'key':"origin", 'key_type':"str", 'value_long':0, 'value_string':"edzw"},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':118, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'], # check model levels?? 
    },

    {
        'name': "temperature_ml",
        'min1': 150,
        'min2': 300,
        'max1': 200,
        'max2': 330,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':130, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':105, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'], # check model levels?? 
    },
    {
        'name': "temperature_ml.edzw",
        'min1': 150,
        'min2': 300,
        'max1': 200,
        'max2': 330,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':130, 'value_string':''},
            {'key':"origin", 'key_type':"str", 'value_long':0, 'value_string':"edzw"},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':118, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'], # check model levels?? 
    },

#'''
#  uerra, eswi-an: an.200812020000+0.ml.grib2, field 3 [u_velocity_ml]: u_velocity_ml minimum value 1.55574 is not in [-200,1]
#  uerra, egrr-det-fc: u_velocity_ml maximum value 0.625 is not in [1,200]
#'''
    {
        'name': "u_velocity_ml",
        'min1': -200,
        'min2': 10,
        'max1': 0.1,
        'max2': 200,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':131, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':105, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'], # check model levels?? 
    },
    {
        'name': "u_velocity_ml.edzw",
        'min1': -200,
        'min2': 10,
        'max1': 0.1,
        'max2': 200,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':131, 'value_string':''},
            {'key':"origin", 'key_type':"str", 'value_long':0, 'value_string':"edzw"},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':118, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'], # check model levels?? 
    },

    {
        'name': "v_velocity_ml",
        'min1': -200,
        'min2': -1,
        'max1': 1,
        'max2': 200,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':132, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':105, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'], # check model levels?? 
    },
    {
        'name': "v_velocity_ml.edzw",
        'min1': -200,
        'min2': -1,
        'max1': 1,
        'max2': 200,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':132, 'value_string':''},
            {'key':"origin", 'key_type':"str", 'value_long':0, 'value_string':"edzw"},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':118, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'], # check model levels?? 
    },

    {
        'name': "cloud_cover_ml",
        'min1': 0,
        'min2': 1e-10,
        'max1': 0,
        'max2': 100.00001,
        'pairs':[
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':6, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':22, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':105, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'], # check model levels?? 
    },
    {
        'name': "cloud_cover_ml.edzw",
        'min1': 0,
        'min2': 1e-10,
        'max1': 0,
        'max2': 100.00001,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260257, 'value_string':''},
            {'key':"origin", 'key_type':"str", 'value_long':0, 'value_string':"edzw"},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':6, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':22, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':118, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'], # check model levels?? 
    },

    {
        'name': "specific_cloud_ice_water_content_pl",
        'min1': 0,
        'min2': 0.001,
        'max1': 0,
        'max2': 0.01,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':247, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':84, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':100, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'pressure_level'],
    },

    {
        'name': "cloud_cover_pl.glob",
        'min1': 0,
        'min2': 1e-10,
        'max1': 100,
        'max2': 100.00001,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260257, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':6, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':22, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':100, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'pressure_level'],
    },
    {
        'name': "specific_cloud_liquid_water_content_pl",
        'min1': 0,
        'min2': 1e+5,
        'max1': 0,
        'max2': 1e+6,
        'pairs':[
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':83, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':100, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'pressure_level'],
    },

    {
        'name': "specific_cloud_ice_water_content_ml",
        'min1': 0,
        'min2': 0.001,
        'max1': 0,
        'max2': 0.01,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':247, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':84, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':105, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'], # check model levels?? 
    },
    {
        'name': "specific_cloud_ice_water_content_ml.edzw",
        'min1': 0,
        'min2': 0.001,
        'max1': 0,
        'max2': 0.01,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':247, 'value_string':''},
            {'key':"origin", 'key_type':"str", 'value_long':0, 'value_string':"edzw"},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':84, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':118, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'], # check model levels?? 
    },

    {
        'name': "specific_cloud_liquid_water_content_ml",
        'min1': 0,
        'min2': 1e+5,
        'max1': 0,
        'max2': 1e+6,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':246, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':83, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':105, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'], # check model levels?? 
    },
    {
        'name': "specific_cloud_liquid_water_content_ml.edzw",
        'min1': 0,
        'min2': 1e+5,
        'max1': 0,
        'max2': 1e+6,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':246, 'value_string':''},
            {'key':"origin", 'key_type':"str", 'value_long':0, 'value_string':"edzw"},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':83, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':118, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'], # check model levels?? 
    },

    #'''
    #  uerra/eggr  warning: oper.2010-03-13.pl.grib2, field 69 [relative_humidity_pl]: relative_humidity_pl maximum value 169 is not in [0,160]

    #'''
    {
        'name': "relative_humidity_pl",
        'min1': 0,
        'min2': 30,
        'max1': 0,
        'max2': 180,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':157, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':100, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'pressure_level'],
    },

    # uerra height levels 

    {
        'name': "cloud_cover_hl",
        'min1': 0,
        'min2': 1e-10,
        'max1': 80,
        'max2': 100.00001,
        'pairs':[
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':6, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':22, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'height_level'],
    },
    {
        'name': "pressure_hl",
        'min1': 100,
        'min2': 100000,
        'max1': 100,
        'max2': 108000,
        'pairs':[
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'height_level'],
    },
    {
        'name': "specific_cloud_liquid_water_content_hl",
        'min1': 0,
        'min2': 1e+5,
        'max1': 0,
        'max2': 1e+6,
        'pairs':[
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':83, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'height_level'],
    },
    {
        'name': "specific_cloud_ice_water_content_hl",
        'min1': 0,
        'min2': 0.001,
        'max1': 0,
        'max2': 0.01,
        'pairs':[
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':84, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'height_level'],
    },
    {
        'name': "relative_humidity_hl",
        'min1': 0,
        'min2': 40,
        'max1': 1,
        'max2': 160,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':157, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'height_level'],
    },
    {
        'name': "temperature_hl",
        'min1': 150,
        'min2': 300,
        'max1': 200,
        'max2': 330,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':130, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'height_level'],
    },
    {
        'name': "wind_speed_hl",
        'min1': 0,
        'min2': 10,
        'max1': 10,
        'max2': 150,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'height_level'],
    },
    {
        'name': "wind_direction_hl",
        'min1': 0,
        'min2': 1,
        'max1': 359,
        'max2': 360.1,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':3031, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'height_level'],
    },

# uerra single level (surface) 

#'''
#  uerra, eswi-fc: percolation_sfc maximum value 0.971001 is not in [1,30]
#'''
    {
        'name': "percolation_sfc",
        'min1': 0,
        'min2': 1,
        'max1': 0.8,
        'max2': 30,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260430, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':16, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':177, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },
    {
        'name': "2_metre_relative_humidity",
        'min1': 0,
        'min2': 25,
        'max1': 90,
        'max2': 160,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260242, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'],
    },

#'''
#  s2s, babj-enfo: surface_runoff maximum value 0.479167 is not in [1,100]
#'''
    {
        'name': "surface_runoff",
        'min1': -0.001,
        'min2': 1,
        'max1': 0.1,
        'max2': 100,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':174008, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':34, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level', 'has_bitmap'],
    },

#'''
#  uerra, cosmo-fc:albedo_sfc maximum value 70 is not in [80,100]
#'''
    {
        'name': "albedo_sfc",
        'min1': 0,
        'min2': 20,
        'max1': 60,
        'max2': 100,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260509, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':19, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level', 'has_bitmap'],
    },
#'''
#  uerra, egrr:  The albedo is 0 at night because it is dependent on solar radiation
#'''
    {
        'name': "albedo_sfc.uerra-egrr",
        'min1': 0,
        'min2': 20,
        'max1': 0,
        'max2': 100,
        'pairs':[
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"ur"},
            {'key':"centre", 'key_type':"str", 'value_long':1, 'value_string':"egrr"},
            {'key':"paramId", 'key_type':"int", 'value_long':260509, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':19, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level', 'has_bitmap'],
    },
    {
        'name': "time_integrated_surface_clear-sky_solar_radiation_downwards",
        'min1': -0.1,
        'min2': 1e+08,
        'max1': 0,
        'max2': 1e+09,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260423, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':4, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':52, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },
    {
        'name': "time_integrated_surface_clear-sky_solar_radiation_upwards",
        'min1': -0.1,
        'min2': 1e+08,
        'max1': 0,
        'max2': 1e+09,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260427, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':4, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':53, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },
    {
        'name': "time_integrated_surface_clear-sky_thermal_radiation_downwards",
        'min1': -0.1,
        'min2': 1e+08,
        'max1': 0,
        'max2': 1e+09,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260428, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':5, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':8, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

#'''
#  uerra, eswi-fc: fc.tidirswrf.sfc.grib2, field 6 [time_integrated_surface_direct_solar_radiation]: time_integrated_surface_direct_solar_radiation minimum value 58442 is not in [-0.1,20000]
#'''
    {
        'name': "time_integrated_surface_direct_solar_radiation",
        'min1': -10,
        'min2': 1e+08,
        'max1': 0,
        'max2': 1e+09,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260264, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':4, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':13, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

    {
        'name': "time_integrated_surface_net_solar_radiation_sfc.lam",
        'min1': -0.1,
        'min2': 1e+08,
        'max1': 0,
        'max2': 1e+09,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':176, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':4, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':9, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

    {
        'name': "10_metre_wind_speed",
        'min1': 0,
        'min2': 10,
        'max1': 10,
        'max2': 300,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':207, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':10, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'],
    },
#'''
#  uerra, cosmo-fc: 10_metre_wind_direction maximum value 360.001 is not in [359,360]
#'''
    {
        'name': "10_metre_wind_direction",
        'min1': 0,
        'min2': 0.1,
        'max1': 359.,
        'max2': 360.01,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260260, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':10, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'],
    },
    {
        'name': "10_metre_wind_gust_since_pp",
        'min1': 0.001,
        'min2': 10,
        'max1': 10,
        'max2': 150,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':49, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':22, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':10, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':2, 'value_string':''},
        ],
        'checks': ['since_prev_pp', 'given_level'],
    },
    {
        'name': "2_metre_maximum_temperature",
        'min1': 200,
        'min2': 340,
        'max1': 200,
        'max2': 340,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':201, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':2, 'value_string':''},
        ],
        'checks': ['since_prev_pp', 'given_level'],
    },
    {
        'name': "2_metre_minimum_temperature",
        'min1': 200,
        'min2': 340,
        'max1': 200,
        'max2': 340,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':202, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':3, 'value_string':''},
        ],
        'checks': ['since_prev_pp', 'given_level'],
    },
    {
        'name': "evaporation_sfc",
        'min1': -10,
        'min2': 0,
        'max1': 0,
        'max2': 5,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260259, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':79, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },
    {
        'name': "snow_depth_sfc",
        'min1': 0,
        'min2': 0,
        'max1': 0,
        'max2': 5,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':3066, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':11, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level'],
    },

#'''
#  uerra, cosmo-det-an: surface_roughness_sfc maximum value 9.36719 is not in [1.3,1.8]
#  uerra, egrr:  surface roughness is fixed at 0.5 over land and is close to 0 over sea
#'''
    {
        'name': "surface_roughness_sfc",
        'min1': 0,
        'min2': 0.001,
        'max1': 0.5,
        'max2': 10,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':173, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level'],
    },
    {
        'name': "liquid_non-frozen_soil_moisture_level",
        'min1': 0,
        'min2': 0.1,
        'max1': 0.1,
        'max2': 1,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260210, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':151, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'has_bitmap', 'has_soil_level'],
    },
    {
        'name': "liquid_non-frozen_soil_moisture_layer",
        'min1': 0,
        'min2': 0.1,
        'max1': 0.1,
        'max2': 1,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260210, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':151, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':151, 'value_string':''},
            {'key':"scaleFactorOfSecondFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_thickness', 'has_bitmap', 'has_soil_layer'],
    },
    {
        'name': "volumetric_soil_moisture_level",
        'min1': 0,
        'min2': 0.1,
        'max1': 0.1,
        'max2': 1,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260199, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':25, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':151, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'has_bitmap', 'has_soil_level'],
    },
    {
        'name': "volumetric_soil_moisture_layer",
        'min1': 0,
        'min2': 0.1,
        'max1': 0.1,
        'max2': 1,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260199, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':25, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':151, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':151, 'value_string':''},
            {'key':"scaleFactorOfSecondFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_thickness', 'has_bitmap', 'has_soil_layer'],
    },
    {
        'name': "soil_heat_flux_sfc",
        'min1': -1000,
        'min2': -10,
        'max1': 10,
        'max2': 1000,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260364, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':26, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level'],
    },

#'''
#  uerra, cosmo-an: soil_temperature_level maximum value 296.188 is not in [300,350]
#  uerra, eswi: soil_temperature_level minimum value 199.649 is not in [200,270]
#'''
    {
        'name': "soil_temperature_level",
        'min1': 180,
        'min2': 270,
        'max1': 280,
        'max2': 350,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260360, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':18, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':151, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'has_bitmap', 'has_soil_level'],
    },

#'''
#  uerra, egrr-an-enda: soil_temperature_layer minimum value 273.125 is not in [200,230]
#'''
    {
        'name': "soil_temperature_layer",
        'min1': 200,
        'min2': 280,
        'max1': 285,
        'max2': 350,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260360, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':18, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':151, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':151, 'value_string':''},
            {'key':"scaleFactorOfSecondFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_thickness', 'has_bitmap', 'has_soil_layer'],
    },

    {
        'name': "cloud_cover_pl.lam",
        'min1': 0,
        'min2': 1e-10,
        'max1': 0,
        'max2': 100,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260257, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':6, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':22, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':100, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'pressure_level'],
    },

#'''
# ========================
# this skin_temperature_sfc  must be matched by tigge and uerra (not s2s!) 
# ========================

# uerra, cosmo-an: skin_temperature_sfc minimum value 245.905 is not in [160,245]
# uerra, eswi-fc: skin_temperature_sfc maximum value 298.942 is not in [300,355]
#'''
    {
        'name': "skin_temperature_sfc",
        'min1': 160,
        'min2': 300,
        'max1': 280,
        'max2': 355,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':235, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':17, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level'],
    },

#'''
#  uerra, egrr-det-an: total_column_water_vapour_sfc minimum value 5.57326 is not in [-3,2]
#'''
    {
        'name': "total_column_water_vapour_sfc",
        'min1': -3.0,
        'min2': 10,
        'max1': 30,
        'max2': 150,
        'pairs':[
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':64, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_thickness'],
    },

# '''
#uerra, eswi-enfo:total_cloud_cover_sfc maximum value 96.4844 is not in [100,100]
# '''
    {
        'name': "total_cloud_cover_sfc.ur.eswi",
        'min1': 0,
        'min2': 2e-10,
        'max1': 90.,
        'max2': 100.,
        'pairs':[
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"ur"},
            {'key':"centre", 'key_type':"str", 'value_long':1, 'value_string':"eswi"},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':6, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':1, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_thickness'],
    },
    {
        'name': "soil_depth",
        'min1': 0.005,
        'min2': 100,
        'max1': 0.005,
        'max2': 100,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260367, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':27, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':151, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'has_bitmap', 'has_soil_level'],
    },

    {
        'name': "volumetric_field_capacity",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260211, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':11, 'value_string':''},
        ],
        'checks': ['point_in_time', 'has_bitmap'],
    },

    {
        'name': "volumetric_wilting_point",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260200, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':27, 'value_string':''},
        ],
        'checks': ['point_in_time', 'has_bitmap'],
    },
#'''
#  carra / cerra
#'''
    {
        'name': "specific_rain_water_content_ml",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':75, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':85, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':105, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'], # check model levels?? 
    },

    {
        'name': "specific_snow_water_content_ml",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':76, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':86, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':105, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'], # check model levels?? 
    },

    {
        'name': "graupel_ml",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260028, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':32, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':105, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'], # check model levels?? 
    },

    {
        'name': "turbulent_kinetic_energy_ml",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260155, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':19, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':11, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':105, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'], # check model levels?? 
    },

    {
        'name': "specific_rain_water_content_pl",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':75, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':85, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':100, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'pressure_level'],
    },

    {
        'name': "specific_snow_water_content_pl",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':76, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':86, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':100, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'pressure_level'],
    },

    {
        'name': "graupel_pl",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260028, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':32, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':100, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'pressure_level'],
    },

    {
        'name': "pseudo-adiabatic_potential_temperature_pl",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':3014, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':100, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'pressure_level'],
    },

    {
        'name': "geometric_vertical_velocity_pl",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260238, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':9, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':100, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'pressure_level'],
    },

    {
        'name': "potential_vorticity_pl",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':60, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':14, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':100, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'pressure_level'],
    },

    {
        'name': "visibility_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':3020, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':19, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level'],
    },

    {
        'name': "cloud_base_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260107, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':6, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':11, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level'],
    },

    {
        'name': "cloud_top_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260108, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':6, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':12, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level'],
    },

    {
        'name': "sea_ice_cover_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':31, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level', 'has_bitmap'],
    },

    {
        'name': "sea_surface_temperature_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':34, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level', 'has_bitmap'],
    },

    {
        'name': "precipitation_type_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260015, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':19, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level'],
    },

    {
        'name': "specific_rain_water_content_hl",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':75, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':85, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'height_level'],
    },

    {
        'name': "specific_snow_water_content_hl",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':76, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':86, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'height_level'],
    },

    {
        'name': "turbulent_kinetic_energy_hl",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260155, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':19, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':11, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'height_level'],
    },
    {
        'name': "2_metre_specific_humidity_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':174096, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level'],
    },
    {
        'name': "time_integral_of_rain_flux_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':235015, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':65, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },
    {
        'name': "total_column_cloud_liquid_water_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':78, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':69, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_thickness'],
    },
    {
        'name': "total_column_cloud_ice_water_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':79, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':70, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_thickness'],
    },
    {
        'name': "total_column_graupel_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260001, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':74, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_thickness'],
    },
    {
        'name': "direct_solar_radiation_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':47, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':4, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':54, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },
    {
        'name': "time_integral_of_top_net_solar_radiation_flux_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':178, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':4, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':8, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },
    {
        'name': "time_integral_of_surface_latent_heat_evaporation_flux_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':235019, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':30, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },
    {
        'name': "time_integral_of_surface_latent_heat_sublimation_flux_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':235071, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':31, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },
    {
        'name': "time_integral_of_surface_eastward_momentum_flux_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':235017, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':17, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },
    {
        'name': "time_integral_of_surface_northward_momentum_flux_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':235018, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':18, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''}, 
        ],
        'checks': ['from_start', 'predefined_level'],
    },
    {
        'name': "time_integral_of_total_solid_precipitation_flux_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260645, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':128, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },
    {
        'name': "time_integral_of_snow_evaporation_flux_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':235072, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':192, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"localTablesVersion", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level', 'has_bitmap'],
    },
    {
        'name': "10_metre_eastward_wind_gust_since_pp_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260646, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':23, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':10, 'value_string':''},
        ],
        'checks': ['since_prev_pp', 'given_level'],
    },
    {
        'name': "10_metre_northward_wind_gust_since_pp_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260647, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':24, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':103, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':10, 'value_string':''},
        ],
        'checks': ['since_prev_pp', 'given_level'],
    },
    {
        'name': "fog_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260648, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':6, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':50, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level'],
    },
    {
        'name': "snow_on_ice_total_depth_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260650, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':11, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':174, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level', 'has_bitmap'],
    },
    {
        'name': "fraction_of_snow_cover_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260289, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':121, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level', 'has_bitmap'],
    },
    {
        'name': "snow_albedo_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':228032, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':19, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':19, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level', 'has_bitmap'],
    },
    {
        'name': "temperature_of_snow_layer_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':238, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':28, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level', 'has_bitmap'],
    },
    {
        'name': "sea_ice_thickness_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':174098, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':160, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'has_bitmap'],
    },
    {
        'name': "sea_ice_surface_temperature_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260649, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':8, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':174, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level', 'has_bitmap'],
    },
    {
        'name': "surface_roughness_length_for_heat",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260651, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':192, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"localTablesVersion", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level', 'has_bitmap'],
    },
    {
        'name': "volumetric_soil_ice_layer",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260644, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':38, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':151, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':151, 'value_string':''},
            {'key':"scaleFactorOfSecondFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_thickness', 'has_bitmap', 'has_soil_layer'],
    },

#'''
#  cerra
#'''
    {
        'name': "time_integral_of_evapotranspiration_flux_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':235073, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':39, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level', 'has_bitmap'],
    },
    {
        'name': "snow_melt_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':3099, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':16, 'value_string':''},
            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level', 'has_bitmap'],
    },
    {
        'name': "lake_total_layer_temperature_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':228011, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':162, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_thickness', 'has_bitmap'],
    },
    {
        'name': "lake_mix_layer_temperature_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':228008, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':166, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level', 'has_bitmap'],
    },
    {
        'name': "lake_mix_layer_depth_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':228009, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':166, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level', 'has_bitmap'],
    },
    {
        'name': "lake_bottom_temperature_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':228010, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':162, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level', 'has_bitmap'],
    },
    {
        'name': "lake_shape_factor_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':228012, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level', 'has_bitmap'],
    },
    {
        'name': "lake_ice_surface_temperature_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':228013, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':6, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':174, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_level', 'has_bitmap'],
    },
    {
        'name': "lake_ice_total_depth_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':228014, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':5, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':174, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':176, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_thickness', 'has_bitmap'],
    },
    {
        'name': "lake_total_depth_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':228007, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':162, 'value_string':''},
        ],
        'checks': ['point_in_time', 'predefined_thickness', 'has_bitmap'],
    },
    {
        'name': "momentum_flux_u_component_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260062, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':17, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

    {
        'name': "momentum_flux_v_component_sfc",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260063, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':18, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

    {
        'name': "time_integrated_surface_clear-sky_net_solar_radiation",
        'min1': -0.1,
        'min2': 1e+08,
        'max1': 0,
        'max2': 1e+09,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':210, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':4, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':11, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

    {
        'name': "time_integrated_surface_clear-sky_net_thermal_radiation",
        'min1': -0.1,
        'min2': 1e+08,
        'max1': 0,
        'max2': 1e+09,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':211, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':5, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':6, 'value_string':''},

            {'key':"typeOfStatisticalProcessing", 'key_type':"int", 'value_long':1, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['from_start', 'predefined_level'],
    },

    {
        'name': "turbulent_kinetic_energy_pl",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"paramId", 'key_type':"int", 'value_long':260155, 'value_string':''},

            {'key':"discipline", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':19, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':11, 'value_string':''},
            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':100, 'value_string':''},
        ],
        'checks': ['point_in_time', 'given_level', 'pressure_level'],
    },

#'''
# s2s ocean parameters
#'''

    {
        'name': "depth_of_20_C_isotherm_o2d.s2",
        'min1': -1e+8,
        'min2':  1e+8,
        'max1': -1e+8,
        'max2':  1e+8,
        'pairs':[
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},

            {'key':"paramId", 'key_type':"int", 'value_long':151163, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':4, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':14, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':20, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':29315, 'value_string':''},
        ],
        'checks': ['daily_average', 'given_level', 'has_bitmap', 'resolution_s2s_ocean'],
    },
    {
        'name': "average_salinity_in_the_upper_300_m_o2d.s2",
        'min1':  -1e+8,
        'min2':  1e+8,
        'max1':  -1e+8,
        'max2':  1e+8,
        'pairs': [
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},

            {'key':"paramId", 'key_type':"int", 'value_long':151175, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':4, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':21, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':160, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':160, 'value_string':''},
            {'key':"scaleFactorOfSecondFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfSecondFixedSurface", 'key_type':"int", 'value_long':300, 'value_string':''},
        ],
        'checks': ['daily_average', 'given_thickness', 'has_bitmap', 'resolution_s2s_ocean'],
    },
    {
        'name': "mean_sea_water_temperature_in_the_upper_300_m_o2d.s2",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},

            {'key':"paramId", 'key_type':"int", 'value_long':151127, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':4, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':15, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':160, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':160, 'value_string':''},
            {'key':"scaleFactorOfSecondFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfSecondFixedSurface", 'key_type':"int", 'value_long':300, 'value_string':''},
        ],
        'checks': ['daily_average', 'given_thickness', 'has_bitmap', 'resolution_s2s_ocean'],
    },
    {
        'name': "mean_sea_water_potential_temperature_in_the_upper_300_m_o2d.s2",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},

            {'key':"paramId", 'key_type':"int", 'value_long':151126, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':4, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':18, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':160, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},

            {'key':"typeOfSecondFixedSurface", 'key_type':"int", 'value_long':160, 'value_string':''},
            {'key':"scaleFactorOfSecondFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfSecondFixedSurface", 'key_type':"int", 'value_long':300, 'value_string':''},
        ],
        'checks': ['daily_average', 'given_thickness', 'has_bitmap', 'resolution_s2s_ocean'],
    },
    {
        'name': "ocean_mixed_layer_thickness_defined_by_sigma_theta_0.01_kg/m3_o2d.s2",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},

            {'key':"paramId", 'key_type':"int", 'value_long':151225, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':4, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':14, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':169, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':1, 'value_string':''},
        ],
        'checks': ['daily_average', 'given_level', 'has_bitmap', 'resolution_s2s_ocean'],
    },
    {
        'name': "eastward_sea_water_velocity_o2d.s2",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},

            {'key':"paramId", 'key_type':"int", 'value_long':151131, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':2, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':160, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['daily_average', 'given_level', 'has_bitmap', 'resolution_s2s_ocean'],
    },
    {
        'name': "northward_sea_water_velocity_o2d.s2",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},

            {'key':"paramId", 'key_type':"int", 'value_long':151132, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':1, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':3, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':160, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['daily_average', 'given_level', 'has_bitmap', 'resolution_s2s_ocean'],
    },
    {
        'name': "sea-ice_thickness_o2d.s2",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},

            {'key':"paramId", 'key_type':"int", 'value_long':174098, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':2, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':1, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':160, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['daily_average', 'given_level', 'has_bitmap', 'resolution_s2s_ocean'],
    },
    {
        'name': "sea_surface_height_o2d.s2",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},

            {'key':"paramId", 'key_type':"int", 'value_long':151145, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':1, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':160, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['daily_average', 'given_level', 'has_bitmap', 'resolution_s2s_ocean'],
    },
    {
        'name': "sea_surface_practical_salinity_o2d.s2",
        'min1': -1e+8,
        'min2': 1e+8,
        'max1': -1e+8,
        'max2': 1e+8,
        'pairs':[
            {'key':"class", 'key_type':"str", 'value_long':0, 'value_string':"s2"},

            {'key':"paramId", 'key_type':"int", 'value_long':151219, 'value_string':''},
            {'key':"discipline", 'key_type':"int", 'value_long':10, 'value_string':''},
            {'key':"parameterCategory", 'key_type':"int", 'value_long':3, 'value_string':''},
            {'key':"parameterNumber", 'key_type':"int", 'value_long':3, 'value_string':''},

            {'key':"typeOfFirstFixedSurface", 'key_type':"int", 'value_long':160, 'value_string':''},
            {'key':"scaleFactorOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
            {'key':"scaledValueOfFirstFixedSurface", 'key_type':"int", 'value_long':0, 'value_string':''},
        ],
        'checks': ['daily_average', 'given_level', 'has_bitmap', 'resolution_s2s_ocean'],
    },
]


