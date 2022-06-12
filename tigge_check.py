#!/usr/bin/env python3.9

import eccodes
import sys
from pathlib import Path



def scan(name: str):
    print(name)
    for path in Path(name).rglob('*'):
        print(path)
        validate(path);


def NUMBER(a):
    sizeof(a) / sizeof(a[0])

def CHECK(a):  
    #check(a,a)
    check(a)

class pair:
    key: str
    key_type: int
    value_long: int
    value_string: str

class parameter:
    name: str
    min1: float
    min2: float
    max1: float
    max2: float
    #pair   pairs[15];
    pairs: list
    #check_proc checks[5];
    checks: list


error: int = 0
filename: str = 0
field: int = 0
warning: int = 0
valueflg: int = 0
param: str = "unknown"
warnflg: int = 0
zeroflg: int = 0
is_lam: int = 0
is_s2s: int = 0
is_s2s_refcst: int = 0
is_uerra: int = 0
is_crra: int = 0

good: str = None
bad: str = None

#FILE* fgood = NULL;
#FILE* fbad  = NULL;

#def check(name: str, a: int):
def check(a: int):
    if a != 0:
        #print("%s, field %d [%s]: %s failed\n", filename, field, param, name)
        print("%s, field %d [%s]: failed\n", filename, field, param)
        error = error + 1

#/*
#def warn(const char* name,int a)
#{
    #if(!a) {
        #printf("%s, field %d [%s]: %s failed\n",filename,field,param,name);
        #warning++;
    #}
#}
#*/

#def save(grib_handle* h, const char *name,FILE* f)
#{
    #size_t size;
    #const void *buffer;
    #int e;

    #if(!f) return;

    #if((e = grib_get_message(h,&buffer,&size)) != GRIB_SUCCESS)
    #{
        #printf("%s, field %d [%s]: cannot get message: %s\n",filename,field,param,grib_get_error_message(e));
        #exit(1);
    #}

    #if(fwrite(buffer,1,size,f) != size)
    #{
        #perror(name);
        #exit(1);
    #}
#}

def save(h, name:str, f):
    buffer = grib_get_message(h)
    f.write(bytearray(buffer))

def get(h, what: str) -> int:
    val = eccodes.grib_get_long(h, what)
    return val;

def dget(h, what: str) -> float:
    val = eccodes.grib_get_double(h, what)
    return val;

def missing(h, what: str) -> int:
    return eccodes.grib_is_missing(h, what);

def eq(h, what: str, value: int) -> int:
    return get(h, what) == value;

def ne(h, what: str, value: int) -> int:
    return get(h,what) != value;

def ge(h, what: str, value: int) -> int:
    return get(h, what) >= value;

def le(h, what: str, value: int) -> int:
    return get(h, what) <= value;

def DBL_EQUAL(d1: float, d2: float, tolerance: float) -> int:
    return fabs(d1 - d2) <= tolerance;


def static_vars(**kwargs):
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate

@static_vars(values=None, last_n=0)
def gaussian_grid(h):
    tolerance: float = 1.0/1000000.0; # angular tolerance for grib2: micro degrees
    n: int = get(h,"numberOfParallelsBetweenAPoleAndTheEquator"); # This is the key N
    #static double* values = NULL;
    #static long last_n = 0;

    north: float = dget(h,"latitudeOfFirstGridPointInDegrees");
    south: float = dget(h,"latitudeOfLastGridPointInDegrees");

    west: float = dget(h,"longitudeOfFirstGridPointInDegrees");
    east: float = dget(h,"longitudeOfLastGridPointInDegrees");

    if n != last_n:
        gaussian_grid.values = grib_get_gaussian_latitudes(n,gaussian_grid.values)
        last_n = n;

    if gaussian_grid.values == None:
        assert(0)
        return

    if gaussian_grid.values != None:
        gaussian_grid.values[0] = rint(gaussian_grid.values[0]*1e6)/1e6;

    if not DBL_EQUAL(north, gaussian_grid.values[0], tolerance) or not DBL_EQUAL(south, -gaussian_grid.values[0], tolerance):
        print("N=%ld north=%f south=%f v(=gauss_lat[0])=%f north-v=%0.30f south-v=%0.30f\n" % (n, north, south, gaussian_grid.values[0], north-gaussian_grid.values[0], south+gaussian_grid.values[0]))

    CHECK(DBL_EQUAL(north, gaussian_grid.values[0], tolerance))
    CHECK(DBL_EQUAL(south, -gaussian_grid.values[0], tolerance))

    if(missing(h,"numberOfPointsAlongAParallel")): # same as key Ni 
        # If missing, this is a REDUCED gaussian grid 
        MAXIMUM_RESOLUTION: int = 640;
        CHECK(get(h,"PLPresent"))
        CHECK(DBL_EQUAL(west, 0.0, tolerance))
        if n > MAXIMUM_RESOLUTION:
            printf("Gaussian number N (=%ld) cannot exceed %ld\n", n, MAXIMUM_RESOLUTION)
            CHECK(n <= MAXIMUM_RESOLUTION)
    else:
        # REGULAR gaussian grid 
        l_west: int = get(h,"longitudeOfFirstGridPoint")
        l_east: int = get(h,"longitudeOfLastGridPoint")
        parallel: int = get(h,"numberOfPointsAlongAParallel")
        we: int = get(h,"iDirectionIncrement")
        dwest: float  = dget(h,"longitudeOfFirstGridPointInDegrees")
        deast: float  = dget(h,"longitudeOfLastGridPointInDegrees")
        dwe: float = dget(h,"iDirectionIncrementInDegrees")
        # printf("parallel=%ld east=%ld west=%ld we=%ld\n",parallel,east,west,we)

        CHECK(parallel == (l_east-l_west)/we + 1)
        CHECK(abs((deast-dwest)/dwe + 1 - parallel) < 1e-10)
        CHECK(not get(h,"PLPresent"))

    CHECK(ne(h,"Nj",0))

    get(h,"PLPresent")

    i: int = 0
    count: int = eccodes.grib_get_size(h,"pl")
    expected_lon2: float = 0
    total: int = 0
    max_pl: int = 0
    numberOfValues: int = get(h,"numberOfValues")
    numberOfDataPoints: int = get(h,"numberOfDataPoints")


    pl = grib_get_double_array(h,"pl")

    if len(pl) != count:
        print("len(pl)=%ld count=%ld\n" % (len(pl), count))

    CHECK(len(pl) == count)
    CHECK(len(pl) == 2*n)

    total = 0;
    max_pl = pl[0]; #  max elem of pl array = num points at equator

    for p in pl:
        total = total + p
        if p > max_pl: 
            max_pl = p


    # Do not assume maximum of pl array is 4N! not true for octahedral

    expected_lon2 = 360.0 - 360.0/max_pl;
    if not DBL_EQUAL(expected_lon2, east, tolerance):
        printf("east actual=%g expected=%g diff=%g\n",east, expected_lon2, expected_lon2-east)

    CHECK(DBL_EQUAL(expected_lon2, east, tolerance))

    if numberOfDataPoints != total:
        print("GAUSS numberOfValues=%ld numberOfDataPoints=%ld sum(pl)=%ld\n" & (
                numberOfValues,
                numberOfDataPoints,
                total))

    CHECK(numberOfDataPoints == total)

    CHECK(missing(h,"iDirectionIncrement"))
    CHECK(missing(h,"iDirectionIncrementInDegrees"))

    CHECK(eq(h,"iDirectionIncrementGiven",0))
    CHECK(eq(h,"jDirectionIncrementGiven",1))

    CHECK(eq(h,"resolutionAndComponentFlags1",0))
    CHECK(eq(h,"resolutionAndComponentFlags2",0))
    CHECK(eq(h,"resolutionAndComponentFlags6",0))
    CHECK(eq(h,"resolutionAndComponentFlags7",0))
    CHECK(eq(h,"resolutionAndComponentFlags8",0))

def check_validity_datetime(h):
    # If we just set the stepRange (for non-instantaneous fields) to its
    # current value, then this causes the validity date and validity time
    # keys to be correctly computed.
    # Then we can compare the previous (possibly wrongly coded) value with
    # the newly computed one
    
    stepType = grib_get_string(h, "stepType")

    if stepType != "instant": # not instantaneous
        # Check only applies to accumulated, max etc.
        stepRange = grib_get_string(h, "stepRange")

        saved_validityDate = get(h, "validityDate")
        saved_validityTime = get(h, "validityTime")

        grib_set_string(h, "stepRange", stepRange);

        validityDate = get(h, "validityDate");
        validityTime = get(h, "validityTime");
        if validityDate!=saved_validityDate or validityTime!=saved_validityTime:
            printf("warning: %s, field %d [%s]: invalid validity Date/Time (Should be %ld and %ld)\n" & filename, field, param, validityDate, validityTime)
            warning = warning + 1

def check_range(h, p: parameter, min_value: float, max_value: float):
    missing: float = 0;
    if not valueflg:
        return

    missing = dget(h,"missingValue")

    # See ECC-437
    if not get(h,"bitMapIndicator") == 0 and min_value == missing and max_value == missing:
        if min_value < p.min1 or min_value > p.min2: 
            print("warning: %s, field %d [%s]: %s minimum value %g is not in [%g,%g]\n" % (filename, field, param, p.name, min_value, p.min1, p.min2))
            print("  => [%g,%g]\n" % (min_value if min_value < p.min1 else p.min1, min_value if min_value > p.min2 else p.min2))
            warning = warning + 1

        if max_value < p.max1 or max_value > p.max2:
            print("warning: %s, field %d [%s]: %s maximum value %g is not in [%g,%g]\n" & (filename, field, param, p.name, max_value, p.max1, p.max2))
            print("  => [%g,%g]\n" % (max_value if max_value < p.max1 else p.max1, max_value if max_value > p.max2 else p.max2))
            warning = warning + 1


def point_in_time(h, p: parameter, min_value: float, max_value: float):
    #switch(get(h,"typeOfProcessedData"))
    topd = get(h,"typeOfProcessedData")
    
    if topd == 0: # Analysis
        if is_uerra:
            CHECK(eq(h,"productDefinitionTemplateNumber",0) or eq(h,"productDefinitionTemplateNumber",1))
        if get(h,"productDefinitionTemplateNumber") == 1:
            CHECK(ne(h,"numberOfForecastsInEnsemble",0))
            CHECK(le(h,"perturbationNumber",get(h,"numberOfForecastsInEnsemble")))

    elif topd == 1: # Forecast
        if is_uerra:
            CHECK(eq(h,"productDefinitionTemplateNumber",0) or eq(h,"productDefinitionTemplateNumber",1))
        if get(h,"productDefinitionTemplateNumber") == 1:
            CHECK(ne(h,"numberOfForecastsInEnsemble",0))
            CHECK(le(h,"perturbationNumber",get(h,"numberOfForecastsInEnsemble")))

    elif topd == 2: # Analysis and forecast products
        CHECK(eq(h,"productDefinitionTemplateNumber",0))

    elif topd == 3: # Control forecast products 
        CHECK(eq(h,"perturbationNumber",0))
        CHECK(ne(h,"numberOfForecastsInEnsemble",0))
        if is_s2s_refcst:
            CHECK(eq(h,"productDefinitionTemplateNumber",60))
        elif is_s2s:
            # CHECK(eq(h,"productDefinitionTemplateNumber",60) or eq(h,"productDefinitionTemplateNumber",11) or eq(h,"productDefinitionTemplateNumber",1))
            CHECK(eq(h,"productDefinitionTemplateNumber",1))
        else:
            CHECK(eq(h,"productDefinitionTemplateNumber",1))

    elif topd == 4: # Perturbed forecast products
        CHECK(ne(h,"perturbationNumber",0))
        CHECK(ne(h,"numberOfForecastsInEnsemble",0))
        if is_s2s_refcst:
            CHECK(eq(h,"productDefinitionTemplateNumber",60))
        elif is_s2s:
            # CHECK(eq(h,"productDefinitionTemplateNumber",60) or eq(h,"productDefinitionTemplateNumber",11) or eq(h,"productDefinitionTemplateNumber",1))
            CHECK(eq(h,"productDefinitionTemplateNumber",1))
        else:
            CHECK(eq(h,"productDefinitionTemplateNumber",1));
        if is_lam:
            CHECK(le(h,"perturbationNumber", get(h,"numberOfForecastsInEnsemble")))
        else:
            # Is there always cf in tigge global datasets??
            CHECK(le(h,"perturbationNumber",get(h,"numberOfForecastsInEnsemble")-1))

    else:
        print("Unsupported typeOfProcessedData %ld\n" % get(h,"typeOfProcessedData"))
        CHECK(0)

    if is_lam:
        if get(h,"indicatorOfUnitOfTimeRange") == 10: # three hours
            # Three hourly is OK 
            pass
        else:
            CHECK(eq(h,"indicatorOfUnitOfTimeRange",1)) # Hours
            CHECK((get(h,"forecastTime") % 3) == 0) # Every three hours
    elif is_uerra:
        if(get(h,"indicatorOfUnitOfTimeRange") == 1): #hourly
            CHECK((eq(h,"forecastTime",1) or eq(h,"forecastTime",2) or eq(h,"forecastTime",4) or eq(h,"forecastTime",5)) or (get(h,"forecastTime") % 3) == 0)
    else:
        if get(h,"indicatorOfUnitOfTimeRange") == 11: #six hour
            # Six hourly is OK
            pass
        else:
            CHECK(eq(h,"indicatorOfUnitOfTimeRange",1)) # Hours
            CHECK((get(h,"forecastTime") % 6) == 0) # Every six hours

    check_range(h, p, min_value, max_value)

def height_level(h, p: parameter, min_value: float, max_value:float):
    level: int = get(h, "level");
    levels = [15, 30, 50, 75, 100, 150, 200, 250, 300, 400, 500]
    if is_uerra:
        if level in levels:
            pass
        else:
            print("%s, field %d [%s]: invalid height level %ld\n" % (filename, field, param, level))
            error = error + 1

def pressure_level(h, p: parameter, min_value: float, max_value: float):
    level: int = get(h,"level");

    if is_uerra and not is_crra:
        if level in [1000, 975, 950, 925, 900, 875, 850, 825, 800, 750, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 20, 10]:
            pass
        else:
            print("%s, field %d [%s]: invalid pressure level %ld\n" % (filename, field, param, level))
            error = error + 1
    elif is_uerra and is_crra:
        if level in [1000, 975, 950, 925, 900, 875, 850, 825, 800, 750, 700, 600, 500, 400, 300, 250, 200, 150, 100, 70, 50, 30, 20, 10, 7, 5, 3, 2, 1]:
            pass
        else:
            print("%s, field %d [%s]: invalid pressure level %ld\n" % (filename, field, param, level))
            error = error + 1
    elif is_s2s:
        if level in [1000, 925, 850, 700, 500, 300, 200, 100, 50, 10]:
            pass
        else:
            print("%s, field %d [%s]: invalid pressure level %ld\n" % (filename, field, param, level))
            error = error + 1
    else:
        if level in [1000, 200, 250, 300, 500, 700, 850, 925, 50]:
            pass
        else:
            print("%s, field %d [%s]: invalid pressure level %ld\n" % (filename, field, param, level))
            error = error + 1

def potential_vorticity_level(h, p: parameter, min_value: float, max_value: float):
    level: int = get(h, "level")
    if level == 2:
        pass
    else:
        print("%s, field %d [%s]: invalid potential vorticity level %ld\n" % (filename, field, param, level))
        error = error + 1

def potential_temperature_level(h, p:parameter, min_value: float, max_value: float):
    level: int = get(h, "level")
    if level == 320:
        pass
    else:
        print("%s, field %d [%s]: invalid potential temperature level %ld\n" % (filename, field, param, level))
        error = error + 1

def statistical_process(h, p:parameter, min_value: float, max_value: float):
    topd = get(h, "typeOfProcessedData")
    
    if topd ==  0: # Analysis
        if is_uerra:
            CHECK(eq(h,"productDefinitionTemplateNumber",8) or eq(h,"productDefinitionTemplateNumber",11))
    elif topd == 1: # Forecast
        if is_uerra:
            CHECK(eq(h,"productDefinitionTemplateNumber",8) or eq(h,"productDefinitionTemplateNumber",11))
    elif topd == 2: # Analysis and forecast products
        CHECK(eq(h,"productDefinitionTemplateNumber",8))
    elif topd == 3: # Control forecast products
        if not is_s2s_refcst:
            CHECK(eq(h,"productDefinitionTemplateNumber",11))
        else:
            CHECK(eq(h,"productDefinitionTemplateNumber",61))
    elif topd == 4: # Perturbed forecast products
        if not is_s2s_refcst:
            CHECK(eq(h,"productDefinitionTemplateNumber",11))
        else:
            CHECK(eq(h,"productDefinitionTemplateNumber",61))
    else:
        print("Unsupported typeOfProcessedData %ld\n" % (get(h,"typeOfProcessedData")))
        error = error + 1
        return;

    if is_lam:
        if get(h,"indicatorOfUnitOfTimeRange") == 10: # three hours
            # Three hourly is OK
            pass
        else:
            CHECK(eq(h,"indicatorOfUnitOfTimeRange",1)) # Hours
            CHECK((get(h,"forecastTime") % 3) == 0); # Every three hours
    elif is_uerra:
#  forecastTime for uerra might be all steps decreased by 1 i.e 0,1,2,3,4,5,8,11...29 too many... */
        if get(h,"indicatorOfUnitOfTimeRange") == 1:
            CHECK(le(h,"forecastTime",30))
    else:
        if get(h,"indicatorOfUnitOfTimeRange") == 11: # six hours
            # Six hourly is OK
            pass
        else:
            CHECK(eq(h,"indicatorOfUnitOfTimeRange",1)); # Hours
            CHECK((get(h,"forecastTime") % 6) == 0); # Every six hours

    CHECK(eq(h,"numberOfTimeRange",1))
    CHECK(eq(h,"numberOfMissingInStatisticalProcess",0))
    CHECK(eq(h,"typeOfTimeIncrement",2))
    # CHECK(eq(h,"indicatorOfUnitOfTimeForTheIncrementBetweenTheSuccessiveFieldsUsed",255))

    if is_s2s:
        if get(h,"typeOfStatisticalProcessing") == 0:
            CHECK(eq(h,"timeIncrementBetweenSuccessiveFields",1) or eq(h,"timeIncrementBetweenSuccessiveFields",4))
        else:
            CHECK(eq(h,"timeIncrementBetweenSuccessiveFields",0))
    else:
        CHECK(eq(h,"timeIncrementBetweenSuccessiveFields",0))

    CHECK(eq(h,"minuteOfEndOfOverallTimeInterval",0))
    CHECK(eq(h,"secondOfEndOfOverallTimeInterval",0))

    if is_uerra:
        CHECK((eq(h,"endStep",1) or eq(h,"endStep",2) or eq(h,"endStep",4) or eq(h,"endStep",5)) or (get(h,"endStep") % 3) == 0)
    elif is_lam:
        CHECK((get(h,"endStep") % 3) == 0);  # Every three hours
    else:
        CHECK((get(h,"endStep") % 6) == 0); # Every six hours

    if get(h,"indicatorOfUnitForTimeRange") == 11:
        # Six hourly is OK
        CHECK(get(h,"lengthOfTimeRange")*6 + get(h,"startStep") == get(h,"endStep"))
    elif get(h,"indicatorOfUnitForTimeRange") == 10:
        # Three hourly is OK
        CHECK(get(h,"lengthOfTimeRange")*3 + get(h,"startStep") == get(h,"endStep"))
    else:
        CHECK(eq(h,"indicatorOfUnitForTimeRange",1)) # Hours
        CHECK(get(h,"lengthOfTimeRange") + get(h,"startStep") == get(h,"endStep"))

def has_bitmap(h, p: parameter, min_value: float, max_value: float):
    # printf("bitMapIndicator %ld\n",get(h,"bitMapIndicator"))
    CHECK(eq(h,"bitMapIndicator",0))

def has_soil_level(h, p: parameter, min_value: float, max_value: float):
    CHECK(get(h,"topLevel") == get(h,"bottomLevel"))
    CHECK(le(h,"level",14)); # max in UERRA

def has_soil_layer(h, p: parameter, min_value: float, max_value: float):
    CHECK(get(h,"topLevel") == get(h,"bottomLevel") - 1)
    CHECK(le(h,"level",14)); # max in UERRA

def resolution_s2s(h, p: parameter, min_value: float, max_value: float):
    CHECK(eq(h,"iDirectionIncrement",1500000))
    CHECK(eq(h,"jDirectionIncrement",1500000))

def resolution_s2s_ocean(h, p: parameter, min_value: float, max_value: float):
    CHECK(eq(h,"iDirectionIncrement",1000000))
    CHECK(eq(h,"jDirectionIncrement",1000000))

def six_hourly(h, p: parameter, min_value: float, max_value: float):
    statistical_process(h,p,min_value,max_value);

    if get(h,"indicatorOfUnitForTimeRange") == 11:
        CHECK(eq(h,"lengthOfTimeRange",1))
    else:
        CHECK(eq(h,"lengthOfTimeRange",6))

    CHECK(get(h,"endStep") == get(h,"startStep") + 6)
    check_range(h,p,min_value,max_value)

def since_prev_pp(h, p: parameter, min_value: float, max_value: float):
    statistical_process(h,p,min_value,max_value)
    CHECK(eq(h,"indicatorOfUnitForTimeRange",1))
    CHECK(get(h,"endStep") == get(h,"startStep") + get(h,"lengthOfTimeRange"))
    check_range(h,p,min_value,max_value)

def three_hourly(h, p: parameter, min_value: float, max_value: float):
    statistical_process(h,p,min_value,max_value)

    if get(h,"indicatorOfUnitForTimeRange") == 11:
        CHECK(eq(h,"lengthOfTimeRange",1))
    else:
        CHECK(eq(h,"lengthOfTimeRange",3))

    CHECK(get(h,"endStep") == get(h,"startStep") + 3)
    check_range(h,p,min_value,max_value)

def from_start(h, p: parameter, min_value: float, max_value: float):
    step: int = get(h,"endStep")
    statistical_process(h,p,min_value,max_value)
    CHECK(eq(h,"startStep",0))

    if step == 0:
        if not is_uerra:
            CHECK(min_value == 0 and max_value == 0); # ??? xxx
    else:
        check_range(h,p,min_value/step,max_value/step)

def daily_average(h, p: parameter, min_value: float, max_value: float):
    step: int = get(h,"endStep")
    CHECK(get(h,"startStep") == get(h,"endStep") - 24)
    statistical_process(h,p,min_value,max_value)

    if step == 0:
        CHECK(min_value == 0 and max_value == 0)
    else:
        check_range(h,p,min_value,max_value)

def given_level(h, p: parameter, min_value: float, max_value: float):
    CHECK(ne(h,"typeOfFirstFixedSurface",255))
    CHECK(not missing(h,"scaleFactorOfFirstFixedSurface"))
    CHECK(not missing(h,"scaledValueOfFirstFixedSurface"))

    CHECK(eq(h,"typeOfSecondFixedSurface",255))
    CHECK(missing(h,"scaleFactorOfSecondFixedSurface"))
    CHECK(missing(h,"scaledValueOfSecondFixedSurface"))

def predefined_level(h, p: parameter, min_value: float, max_value: float):
    CHECK(ne(h,"typeOfFirstFixedSurface",255))
    CHECK(missing(h,"scaleFactorOfFirstFixedSurface"))
    CHECK(missing(h,"scaledValueOfFirstFixedSurface"))

    CHECK(eq(h,"typeOfSecondFixedSurface",255))
    CHECK(missing(h,"scaleFactorOfSecondFixedSurface"))
    CHECK(missing(h,"scaledValueOfSecondFixedSurface"))

def predefined_thickness(h, p: parameter, min_value: float, max_value: float):
    CHECK(ne(h,"typeOfFirstFixedSurface",255))
    CHECK(missing(h,"scaleFactorOfFirstFixedSurface"))
    CHECK(missing(h,"scaledValueOfFirstFixedSurface"))

    CHECK(ne(h,"typeOfSecondFixedSurface",255))
    CHECK(missing(h,"scaleFactorOfSecondFixedSurface"))
    CHECK(missing(h,"scaledValueOfSecondFixedSurface"))

def given_thickness(h, p: parameter, min_value: float, max_value: float):
    CHECK(ne(h,"typeOfFirstFixedSurface",255))
    CHECK(not missing(h,"scaleFactorOfFirstFixedSurface"))
    CHECK(not missing(h,"scaledValueOfFirstFixedSurface"))

    CHECK(ne(h,"typeOfSecondFixedSurface",255))
    CHECK(not missing(h,"scaleFactorOfSecondFixedSurface"))
    CHECK(not missing(h,"scaledValueOfSecondFixedSurface"))

def latlon_grid(h):
    tolerance: float = 1.0/1000000.0; # angular tolerance for grib2: micro degrees
    data_points: int = get(h,"numberOfDataPoints")
    meridian: int    = get(h,"numberOfPointsAlongAMeridian")
    parallel: int    = get(h,"numberOfPointsAlongAParallel")

    north: int = get(h,"latitudeOfFirstGridPoint")
    south: int = get(h,"latitudeOfLastGridPoint")
    west: int  = get(h,"longitudeOfFirstGridPoint")
    east: int  = get(h,"longitudeOfLastGridPoint")

    ns: int = get(h,"jDirectionIncrement")
    we: int = get(h,"iDirectionIncrement")

    dnorth: float = dget(h,"latitudeOfFirstGridPointInDegrees")
    dsouth: float = dget(h,"latitudeOfLastGridPointInDegrees")
    dwest: float  = dget(h,"longitudeOfFirstGridPointInDegrees")
    deast: float  = dget(h,"longitudeOfLastGridPointInDegrees")

    dns: float = dget(h,"jDirectionIncrementInDegrees")
    dwe: float = dget(h,"iDirectionIncrementInDegrees")

    if eq(h,"basicAngleOfTheInitialProductionDomain",0):
        CHECK(missing(h,"subdivisionsOfBasicAngle"))
    else:
        # long basic    = get(h,"basicAngleOfTheInitialProductionDomain")
        # long division = get(h,"subdivisionsOfBasicAngle")
        CHECK(not missing(h,"subdivisionsOfBasicAngle"))
        CHECK(not eq(h,"subdivisionsOfBasicAngle",0))

    if missing(h,"subdivisionsOfBasicAngle"):
        CHECK(eq(h,"basicAngleOfTheInitialProductionDomain",0))

    CHECK(meridian*parallel == data_points)

    CHECK(eq(h,"resolutionAndComponentFlags1",0))
    CHECK(eq(h,"resolutionAndComponentFlags2",0))
    CHECK(eq(h,"resolutionAndComponentFlags6",0))
    CHECK(eq(h,"resolutionAndComponentFlags7",0))
    CHECK(eq(h,"resolutionAndComponentFlags8",0))

    CHECK(eq(h,"iDirectionIncrementGiven",1))
    CHECK(eq(h,"jDirectionIncrementGiven",1))

    CHECK(eq(h,"numberOfOctectsForNumberOfPoints",0))
    CHECK(eq(h,"interpretationOfNumberOfPoints",0))

    if get(h,"iScansNegatively") != 0:
        tmp: int    = east
        dtmp: float = deast

        east = west
        west = tmp

        deast = dwest
        dwest = dtmp

    if get(h,"jScansPositively") != 0:
        tmp: int  = north
        dtmp: float = dnorth

        north = south
        south = tmp

        dnorth = dsouth
        dsouth = dtmp

    if not (is_lam or is_uerra):
        CHECK(north > south)
        CHECK(east  > west)

        # Check that the grid is symmetrical */
        CHECK(north == -south)
        CHECK( DBL_EQUAL(dnorth, -dsouth, tolerance) )
        CHECK(parallel == (east-west)/we + 1)
        CHECK(fabs((deast-dwest)/dwe + 1 - parallel) < 1e-10)
        CHECK(meridian == (north-south)/ns + 1)
        CHECK(fabs((dnorth-dsouth)/dns + 1 - meridian) < 1e-10 )

        # Check that the field is global */
        area: float  = (dnorth-dsouth) * (deast-dwest)
        globe: float = 360.0*180.0
        CHECK(area <= globe)
        CHECK(area >= globe*0.95)

    # GRIB2 requires longitudes are always positive */
    CHECK(east >= 0)
    CHECK(west >= 0)

      #printf("meridian=%ld north=%ld south=%ld ns=%ld \n",meridian,north,south,ns)
      #printf("meridian=%ld north=%f south=%f ns=%f \n",meridian,dnorth,dsouth,dns)
      #printf("parallel=%ld east=%ld west=%ld we=%ld \n",parallel,east,west,we)
      #printf("parallel=%ld east=%f west=%f we=%f \n",parallel,deast,dwest,dwe)

#define X(x) printf("%s=%ld ",#x,get(h,#x))
def X(x):
    pass
    #print("%s=%ld ",#x,get(h,#x))
    #print("%s=%ld ",#x,get(h,#x))

def check_parameter(h, min_value: float, max_value: float):
    #int err;
    best: int = -1;
    match: int = -1;
    i: int = 0;

    #for (i = 0; i < NUMBER(parameters); i++):
    for parameter in parameters:
        j: int = 0;
        matches: int = 0;

        #while(parameter.pairs[j].key != NULL)
        for pair in parameter.pairs:
            val: int = -1;
            ktype: int = pair.key_type;
            if ktype == GRIB_TYPE_LONG:
                val = grib_get_long(h, pair.key)
                if val == GRIB_SUCCESS:
                    if pair.value_long == val:
                        matches = matches + 1
            elif ktype == GRIB_TYPE_STRING:
                #char strval[256]={0,};
                #len: int = 256;

                if is_uerra and strcasecmp(pair.key, "model") == 0:
                    # print("Skipping model keyword for UERRA class\n")
                    matches = matches + 1 # xxx hack to pretend that model key was matched.
                else:
                    if strcasecmp(pair.value_string, "MISSING") == 0:
                        is_miss: int = grib_is_missing(h, pair.key)
                        if is_miss != 0:
                            matches = matches + 1
                    elif grib_get_string(h,pair.key):
                        strval = grib_get_string(h, pair.key)
                        if pair.value_string == strval:
                            matches = matches + 1
            else:
                assert("Unknown key type")
            j = j + 1
#if 0
            #print("%s %s %ld val -> %d %d %d\n" % (
                    #pair.key,
                    #pair.value_string,
                    #val,
                    #matches,
                    #j,
                    #best))
#endif

        if matches == j and matches > best:
            best = matches
            match = i
        i = i + 1

    if match >= 0:
        # int j = 0;
        param = parameters[match].name
        i = 0
        while parameters[match].checks[i]:
            (parameters[match].checks[i])(h, parameters[match], min_value, max_value)
            i = i + 1
                #printf("=========================\n");
                #printf("%s -> %d %d\n",param, match, best);
                #while(parameters[match].pairs[j].key != NULL)
                #{
                #     printf("%s val -> %ld %d\n",parameters[match].pairs[j].key,parameters[match].pairs[j].value,j);
                #     j++;
                #}
                #printf("matched parameter: %s\n", param);
    else:
        print("%s, field %d [%s]: cannot match parameter\n" % (filename, field, param))
        #X(origin)
        #X(discipline)
        #X(parameterCategory)
        #X(parameterNumber)
        #X(typeOfFirstFixedSurface)
        #X(scaleFactorOfFirstFixedSurface)
        #X(scaledValueOfFirstFixedSurface)
        #X(typeOfSecondFixedSurface)
        #X(scaleFactorOfSecondFixedSurface)
        #X(scaledValueOfSecondFixedSurface)
        print("\n")
        error = error + 1

def check_packing(h):
    # ECC-1009: Warn if not using simple packing
    expected_packingType: str = "grid_simple";
    packingType = grib_get_string(h, "packingType")

    if packingType == expected_packingType:
        print("warning: %s, field %d [%s]: invalid packingType %s (Should be %s)\n" %(filename, field, param, packingType, expected_packingType))
        warning = warning + 1

def verify(h):
    min_value: float = 0
    max_value: float = 0

    CHECK(eq(h,"editionNumber",2))
    CHECK(missing(h,"reserved") or eq(h,"reserved",0))

    if valueflg:
        #n: int
        count: int= grib_get_size(h,"values")
        #double *values;
        #size_t i;
        try:
            bitmap: int = not eq(h,"bitMapIndicator",255);
        except Exception as e:
            printf("%s, field %d [%s]: cannot number of values: %s\n",file,field,param,grib_get_error_message(e))
            error = error = 1
            return;

        CHECK(eq(h,"numberOfDataPoints",count));

        n = count;
        try:
            values = grib_get_double_array(h,"values")
        except Exception as e:
            print("%s, field %d [%s]: cannot get values: %s\n" % (filename, field, param, grib_get_error_message(e)))
            error = error + 1
            return

        if n != count:
            print("%s, field %d [%s]: value count changed %ld -> %ld\n" % (filename, field, param, count, n))
            error = error + 1
            return

        if bitmap:
            missing: float = dget(h,"missingValue")

            min_value = max_value = missing;

            for value in values:
                if (min_value == missing) or ((value != missing) and (min_value > value)):
                    min_value = value
                if (max_value == missing) or ((value != missing) and (max_value < value)):
                    max_value = value
        else:
            min_value = max_value = values[0]
            for value in values:
                if min_value > value:
                    min_value = value
                if max_value < value: 
                    max_value = value;

    check_parameter(h, min_value, max_value);
    check_packing(h);

    # Section 1

    CHECK(ge(h,"gribMasterTablesVersionNumber",4))
    CHECK(eq(h,"versionNumberOfGribLocalTables",0)) # Local tables not used

    CHECK(eq(h,"significanceOfReferenceTime",1)); # Start of forecast

    if not is_s2s:
        # todo check for how many years back the reforecast is done? Is it coded in the grib???
        # Check if the date is OK
        date: int = get(h,"date");
        # CHECK(date > 20060101);
        CHECK( (date / 10000)         == get(h,"year"))
        CHECK( ((date % 10000) / 100) == get(h,"month"))
        CHECK( ((date % 100))         == get(h,"day"))

    if is_uerra:
        CHECK(le(h,"hour",24))
    elif is_lam:
        CHECK(eq(h,"hour",0) or eq(h,"hour",3) or eq(h,"hour",6) or eq(h,"hour",9) or eq(h,"hour",12) or eq(h,"hour",15) or eq(h,"hour",18) or eq(h,"hour",21))
    else:
    # Only 00, 06 12 and 18 Cycle OK 
        CHECK(eq(h,"hour",0) or eq(h,"hour",6) or eq(h,"hour",12) or eq(h,"hour",18))

    CHECK(eq(h,"minute",0))
    CHECK(eq(h,"second",0))
    CHECK(ge(h,"startStep",0))

    if is_s2s:
        CHECK(eq(h,"productionStatusOfProcessedData",6) or eq(h,"productionStatusOfProcessedData",7)) #S2S prod or test
        CHECK(le(h,"endStep",100*24))
    elif not is_uerra:
        CHECK(eq(h,"productionStatusOfProcessedData",4) or eq(h,"productionStatusOfProcessedData",5)) # TIGGE prod or test
        CHECK(le(h,"endStep",30*24))

    if is_uerra:
        CHECK((eq(h,"step",1) or eq(h,"step",2) or eq(h,"step",4) or eq(h,"step",5)) or (get(h,"step") % 3) == 0)
    elif is_lam:
        CHECK((get(h,"step") % 3) == 0)
    else:
        CHECK((get(h,"step") % 6) == 0)

    if is_uerra:
        if is_crra:
            CHECK(eq(h,"productionStatusOfProcessedData",10) or eq(h,"productionStatusOfProcessedData",11)) # CRRA prodortest
        else:
            CHECK(eq(h,"productionStatusOfProcessedData",8) or eq(h,"productionStatusOfProcessedData",9)); #  UERRA prodortest
        CHECK(le(h,"endStep",30))
        # 0 = analysis , 1 = forecast
        CHECK(eq(h,"typeOfProcessedData",0) or eq(h,"typeOfProcessedData",1))
        if get(h,"typeOfProcessedData") == 0:
            CHECK(eq(h,"step",0))
        else:
            CHECK((eq(h,"step",1) or eq(h,"step",2) or eq(h,"step",4) or eq(h,"step",5)) or (get(h,"step") % 3) == 0)
    else:
        # 2 = analysis or forecast , 3 = control forecast, 4 = perturbed forecast
        CHECK(eq(h,"typeOfProcessedData",2) or eq(h,"typeOfProcessedData",3) or eq(h,"typeOfProcessedData",4));

    # TODO: validate local usage. Empty for now xxx
    # CHECK(eq(h,"section2.sectionLength",5))

    # Section 3

    CHECK(eq(h,"sourceOfGridDefinition",0)) # Specified in Code table 3.1 

    dtn = get(h,"gridDefinitionTemplateNumber")
    
    if dtn in [0, 1]:
        # dtn == 1: rotated latlon
        latlon_grid(h);
    elif dtn == 30: #Lambert conformal
        # lambert_grid(h); # TODO xxx
        # print("warning: Lambert grid - geometry checking not implemented yet!\n")
        # CHECK(eq(h,"scanningMode",64));*/ /* M-F data used to have it wrong.. but it might depends on other projection set up as well!
        pass
    elif dtn == 40: # gaussian grid (regular or reduced)
        gaussian_grid(h)
    else:
        print("%s, field %d [%s]: Unsupported gridDefinitionTemplateNumber %ld\n" %
                (filename, field, param, get(h,"gridDefinitionTemplateNumber")))
        error = error + 1
        return;

    # If there is no bitmap, this should be true
    # CHECK(eq(h,"bitMapIndicator",255))

    if eq(h,"bitMapIndicator",255):
        CHECK(get(h,"numberOfValues") == get(h,"numberOfDataPoints"))
    else:
        CHECK(get(h,"numberOfValues") <= get(h,"numberOfDataPoints"))

    # Check values 
    CHECK(eq(h,"typeOfOriginalFieldValues",0)) # Floating point 

    check_validity_datetime(h)

    # do not store empty values e.g. fluxes at step 0
    #    todo ?? now it's allowed in the code here!
    #    if not missing(h,"typeOfStatisticalProcessing"):
    #      CHECK(ne(h,"stepRange",0))

def validate(path: str):
    #FILE *f = fopen(path,"rb");
    with GribFile as grib:
        #grib_handle *h = 0;
        #int err;
        count: int = 0;

        #file  = path;
        field: int = 0;

        #if(!f) {
            #printf("%s: %s\n",path,strerror(errno));
            #error++;
            #return;
        #}

        #while( (h= grib_handle_new_from_file(0,f,&err)) != NULL)
        for msg in grib:
            last_error: int    = error;
            last_warning: int  = warning;

            field = field + 1
            #verify(h);

            if (last_error != error) or (warnflg and (last_warning != warning)):
                save(h,bad,fbad)
            else:
                save(h,good,fgood)

            #grib_handle_delete(h)
            count = count + 1
            param = "unknown"

        #if(err) {
            #printf("%s: grib_handle_new_from_file: %s\n",path,grib_get_error_message(err));
            #error++;
            #return;
        #}

        if count == 0:
            print("%s does not contain any GRIBs\n" % path)
            error = error + 1
            return

def usage():
    print("tigge_check [options] grib_file grib_file ...\n")
    print("   -l: check local area model fields\n")
    print("   -v: check value ranges\n")
    print("   -w: warnings are treated as errors\n")
    print("   -g: write good gribs\n")
    print("   -b: write bad  gribs\n")
    print("   -z: return 0 to calling shell\n")
    print("   -s: check s2s fields\n")
    print("   -r: check s2s reforecast fields\n")
    print("   -u: check uerra fields\n")
    print("   -c: check crra fields (-u must be also used in this case)\n")
    sys.exit(1)


if __name__ == "__main__":
    from tigge_check_parameters import parameters 

    fgood = None
    fbad = None

    argc = len(sys.argv)

    iargv = iter(sys.argv)
    i = 1

    for arg in iargv:
        if arg[0] == '-':
            param = arg[1]
            if param == 'w':
                warnflg = warndflg + 1
            elif param == 'z':
                zeroflg = zeroflg + 1
            elif param == 'v':
                valueflg = zeroflg + 1
            elif param == 'g':
                i = i + 1
                if i == argc:
                    usage()
                good = next(iargv)
                fgood = open(good,"w")
                #if not fgood:
                    #perror(good)
                    #sys.exit(1)
            elif param == 'b':
                i = i + 1
                if i == argc:
                    usage()
                bad = next(iargv)
                fbad = open(bad,"w")
                #if not fbad:
                    #perror(bad);
                    #sys.exit(1)
            elif param == 'l':
                is_lam=1
            elif param == 's':
                is_s2s=1
            elif param == 'r':
                is_s2s_refcst=1
            elif param == 'u':
                is_uerra=1
            elif param == 'c':
                is_crra=1
            else:
                usage()
        else:
            break

    if i == argc:
        usage()

    for arg in iargv:
        error = 0
        scan(arg)
        if error:
            err = 1
        if warning and warnflg:
            err = 1

    if fgood and close(fgood):
        perror(good)
        sys.exit(1)
    if fbad and close(fbad):
        perror(bad )
        sys.exit(1)

    #return 0 if zeroflg else err
