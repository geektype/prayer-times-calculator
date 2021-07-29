BASE_URL = "http://api.aladhan.com/v1/"

TIMINGS_URL = BASE_URL + "timings"

CALCULATION_METHODS = {
	"jafari": 0,
	"karachi": 1,
	"isna": 2,
	"mwl": 3,
	"makkah": 4,
	"egypt": 5,
	"tehran": 7,
	"gulf": 8,
	"kuwait": 9,
	"qatar": 10,
	"singapore": 11,
	"france": 12,
	"turkey": 13,
	"russia": 14,
	"custom": 99,
}

SCHOOLS = {"shafi": 0, "hanafi": 1}

MIDNIGHT_MODES = {"standard": 0, "jafari": 1}

LAT_ADJ_METHODS = {"middle of the night": 1, "one seventh": 2, "angle based": 3}