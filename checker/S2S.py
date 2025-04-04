from Assert import Le, Lt, Gt, Ge, Ne, Eq, Fail, IsIn, IsMultipleOf, EqDbl
from Report import Report
from checker.TiggeBasicChecks import TiggeBasicChecks


class S2S(TiggeBasicChecks):
    def __init__(self, param_file=None, valueflg=False):
        super().__init__(param_file, valueflg=valueflg)

    def _basic_checks(self, message, p):
        reports = super()._basic_checks(message, p)
        report = Report(f"{__class__.__name__}._basic_checks")

        # todo check for how many years back the reforecast is done? Is it coded in the grib???
        # Check if the date is OK
        date = message["date"]
        # report.add(Ge(message["date"], 20060101))
        
        report.add(Eq((date / 10000).to_int(), message["year"], "int(date / 10000) == message.get('year')"))
        report.add(Eq(((date % 10000) / 100).to_int(), message["month"], "int((date % 10000) / 100) == message.get('month')"))
        report.add(Eq((date % 100).to_int(), message["day"], "int(date % 100) == message.get('day')"))
        report.add(IsIn(message["productionStatusOfProcessedData"], [6, 7]))
        report.add(IsMultipleOf(message["step"], 6))

        return reports + [report]


    # not registered in the lookup table
    def _statistical_process(self, message, p):
        report = Report(f"{__class__.__name__}.statistical_process")

        topd = message.get("typeOfProcessedData", int)

        if topd in [0, 1, 2]: # Analysis, Forecast, Analysis and forecast products
            pass
        elif topd in [3, 4]: # Control forecast products, Perturbed forecast products
            report.add(Eq(message["productDefinitionTemplateNumber"], 11))
        else:
            report.add(Fail(f"Unsupported typeOfProcessedData {topd}"))
            return [report]

        if message["indicatorOfUnitOfTimeRange"] == 11: # six hours
            # Six hourly is OK
            pass
        else:
            report.add(Eq(message["indicatorOfUnitOfTimeRange"], 1))
            report.add(IsMultipleOf(message["forecastTime"], 6))

        report.add(Eq(message["timeIncrementBetweenSuccessiveFields"], 0))
        report.add(IsMultipleOf(message["endStep"], 6))

        reports = super()._statistical_process(message, p)
        return reports + [report]

    def _from_start(self, message, p):
        reports = super()._from_start(message, p)
        if message["endStep"] != 0:
            reports += self._check_range(message, p)
        return reports

    def _point_in_time(self, message, p):
        reports = super()._point_in_time(message, p)

        report = Report()
        topd = message.get("typeOfProcessedData", int)
        if topd in [0, 1]: # Analysis, Forecast
            if message["productDefinitionTemplateNumber"] == 1:
                report.add(Ne(message["numberOfForecastsInEnsemble"], 0))
                report.add(Le(message["perturbationNumber"], message["numberOfForecastsInEnsemble"]))
        elif topd == 2: # Analysis and forecast products
            pass
        elif topd == 3: # Control forecast products 
            # check.add(IsIn(message["productDefinitionTemplateNumber"], [60, 11, 1]))
            report.add(Eq(message["productDefinitionTemplateNumber"], 1))
        elif topd == 4: # Perturbed forecast products
            # check.add(IsIn(message["productDefinitionTemplateNumber"], [60, 11, 1]))
            report.add(Eq(message["productDefinitionTemplateNumber"], 1))
            report.add(Eq(message["perturbationNumber"], message["numberOfForecastsInEnsemble"]- 1, "perturbationNumber == numberOfForecastsInEnsemble - 1"))
        else:
            report.add(Fail(f'Unsupported typeOfProcessedData {message["typeOfProcessedData"]}'))

        if message["indicatorOfUnitOfTimeRange"] == 11:
            # Six hourly is OK
            pass
        else:
            report.add(Eq(message["indicatorOfUnitOfTimeRange"], 1))
            report.add(IsMultipleOf(message["forecastTime"], 6))

        return reports + [report]

    def _latlon_grid(self, message):
        report = Report(f"{__class__.__name__}.latlon_grid")

        tolerance = 1.0/1000000.0 # angular tolerance for grib2: micro degrees
        meridian = message["numberOfPointsAlongAMeridian"]
        parallel = message["numberOfPointsAlongAParallel"]

        north = message["latitudeOfFirstGridPoint"]
        south = message["latitudeOfLastGridPoint"]
        west = message["longitudeOfFirstGridPoint"]
        east = message["longitudeOfLastGridPoint"]

        ns= message["jDirectionIncrement"]
        we= message["iDirectionIncrement"]

        dnorth = message.get("latitudeOfFirstGridPointInDegrees", float)
        dsouth = message.get("latitudeOfLastGridPointInDegrees", float)
        dwest = message.get("longitudeOfFirstGridPointInDegrees", float)
        deast = message.get("longitudeOfLastGridPointInDegrees", float)

        dns = message.get("jDirectionIncrementInDegrees", float)
        dwe = message.get("iDirectionIncrementInDegrees", float)


        report.add(Gt(north, south, "north > south"))
        report.add(Gt(east, west, "east > west"))

        # Check that the grid is symmetrical */
        report.add(Eq(north, -south, "north == -south"))
        report.add(EqDbl(dnorth, -dsouth, tolerance, "dnorth == -dsouth"))
        report.add(Eq(parallel, (east-west) / we + 1, "parallel == (east - west) / we + 1"))
        report.add(Lt(((deast - dwest) / dwe + 1 - parallel).abs(), 1e-10, "math.fabs((deast - dwest) / dwe + 1 - parallel) < 1e-10"))
        report.add(Eq(meridian, (north - south) / ns + 1, "meridian == (north - south) / ns + 1"))
        report.add(Lt(((dnorth - dsouth) / dns + 1 - meridian).abs(), 1e-10, "math.fabs((dnorth - dsouth) / dns + 1 - meridian) < 1e-10 "))

        # Check that the field is global */
        area = (dnorth - dsouth) * (deast - dwest)
        globe = 360.0 * 180.0
        report.add(Le(area, globe, "area <= globe"))
        report.add(Ge(area, globe * 0.95, "area >= globe*0.95"))

        reports = super()._latlon_grid(message)
        return reports + [report]

    def _pressure_level(self, message, p):
        report = Report()
        levels = [1000, 925, 850, 700, 500, 300, 200, 100, 50, 10]
        report.add(IsIn(message["level"], levels, 'check pressure level'))
        return [report]
