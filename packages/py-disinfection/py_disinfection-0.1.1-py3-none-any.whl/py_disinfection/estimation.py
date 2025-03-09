import math
from typing import List, Tuple

from py_disinfection.tables import (
    giardia_ct_chloramines,
    giardia_ct_chlorinedioxide,
    giardia_ct_freechlorine,
    virus_ct_chloramines,
    virus_ct_chlorinedioxide,
    virus_ct_freechlorine,
)

# Conservative Method
"""
This function calculates the conservatively estimated CT value for 3-log Giardia inactivation using free chlorine.
The function takes the temperature, pH, and free chlorine concentration as input and returns the CT value.
"""


def conservative_giardia_ct(temp: float, ph: float, chlorine_conc: float) -> float:
    rounded_temp = max(t for t in giardia_ct_freechlorine.keys() if t <= temp)
    rounded_chlorine = min(
        c for c in giardia_ct_freechlorine[rounded_temp].keys() if c >= chlorine_conc
    )
    rounded_ph = min(
        p
        for p in giardia_ct_freechlorine[rounded_temp][rounded_chlorine].keys()
        if p >= ph
    )
    return giardia_ct_freechlorine[rounded_temp][rounded_chlorine][rounded_ph]


# Interpolation Method
def interpolate_giardia_ct(temp: float, ph: float, chlorine_conc: float) -> float:
    def linear_interpolate(
        x1: float, x2: float, y1: float, y2: float, x: float
    ) -> float:
        return y1 + (y2 - y1) * ((x - x1) / (x2 - x1)) if x2 != x1 else y1

    def find_next_lowest_and_highest(
        values: List[float], target: float
    ) -> Tuple[float, float]:
        lower = max([v for v in values if v <= target], default=values[0])
        upper = min([v for v in values if v >= target], default=values[-1])
        return lower, upper

    temp_low, temp_high = find_next_lowest_and_highest(
        list(giardia_ct_freechlorine.keys()), temp
    )
    chlorine_low, chlorine_high = find_next_lowest_and_highest(
        list(giardia_ct_freechlorine[temp_low].keys()), chlorine_conc
    )
    ph_low, ph_high = find_next_lowest_and_highest(
        list(giardia_ct_freechlorine[temp_low][chlorine_low].keys()), ph
    )

    # Step 1: Interpolate CT between pH values at the next lowest temp & next lowest chlorine residual
    ct1_low_cl = linear_interpolate(
        ph_low,
        ph_high,
        giardia_ct_freechlorine[temp_low][chlorine_low][ph_low],
        giardia_ct_freechlorine[temp_low][chlorine_low][ph_high],
        ph,
    )

    # Step 2: Interpolate CT between pH values at the next highest temp & next lowest chlorine residual
    ct2_low_cl = linear_interpolate(
        ph_low,
        ph_high,
        giardia_ct_freechlorine[temp_high][chlorine_low][ph_low],
        giardia_ct_freechlorine[temp_high][chlorine_low][ph_high],
        ph,
    )

    # Step 3: Interpolate CT between temp values from Steps 1 & 2
    ct_low_cl = linear_interpolate(temp_low, temp_high, ct1_low_cl, ct2_low_cl, temp)

    # Step 4: Interpolate CT between pH values at the next lowest temp & next highest chlorine residual
    ct1_high_cl = linear_interpolate(
        ph_low,
        ph_high,
        giardia_ct_freechlorine[temp_low][chlorine_high][ph_low],
        giardia_ct_freechlorine[temp_low][chlorine_high][ph_high],
        ph,
    )

    # Step 5: Interpolate CT between pH values at the next highest temp & next highest chlorine residual
    ct2_high_cl = linear_interpolate(
        ph_low,
        ph_high,
        giardia_ct_freechlorine[temp_high][chlorine_high][ph_low],
        giardia_ct_freechlorine[temp_high][chlorine_high][ph_high],
        ph,
    )

    # Step 6: Interpolate CT between temp values from Steps 4 & 5
    ct_high_cl = linear_interpolate(temp_low, temp_high, ct1_high_cl, ct2_high_cl, temp)

    # Step 7: Final interpolation between chlorine residual values
    return linear_interpolate(
        chlorine_low, chlorine_high, ct_low_cl, ct_high_cl, chlorine_conc
    )


# Regression Method
def regression_giardia_ct(
    temp: float, ph: float, chlorine_conc: float, log_inactivation: int = 3
) -> float:
    if temp < 12.5:
        return (0.353 * log_inactivation) * (
            12.006 + math.exp(2.46 - 0.073 * temp + 0.125 * chlorine_conc + 0.389 * ph)
        )
    else:
        return (0.361 * log_inactivation) * (
            -2.261 + math.exp(2.69 - 0.065 * temp + 0.111 * chlorine_conc + 0.361 * ph)
        )


def conservative_giardia_chlorine_dioxide_ct(temp: float) -> float:
    rounded_temp = max(
        t for t in giardia_ct_chlorinedioxide.keys() if t <= temp
    )  # Round down temperature - take the highest value of the values less than or equal to the temperature
    return giardia_ct_chlorinedioxide[rounded_temp]


def conservative_giardia_chloramines_ct(temp: float) -> float:
    rounded_temp = max(
        t for t in giardia_ct_chloramines.keys() if t <= temp
    )  # Round down temperature - take the highest value of the values less than or equal to the temperature
    return giardia_ct_chloramines[rounded_temp]


# Viruses
def conservative_viruses_ct(temp: float, ph: float) -> float:
    rounded_temp = max(
        t for t in virus_ct_freechlorine.keys() if t <= temp
    )  # Round down temperature - take the highest value of the values less than or equal to the temperature
    rounded_ph = min(
        p for p in virus_ct_freechlorine[rounded_temp].keys() if p >= ph
    )  # Round up pH - take the lowest value of the values greater than or equal to the pH
    return virus_ct_freechlorine[rounded_temp][rounded_ph]


def conservative_viruses_chlorine_dioxide_ct(temp: float) -> float:
    rounded_temp = max(
        t for t in virus_ct_chlorinedioxide.keys() if t <= temp
    )  # Round down temperature - take the highest value of the values less than or equal to the temperature
    return virus_ct_chlorinedioxide[rounded_temp]


def conservative_viruses_chloramines_ct(temp: float) -> float:
    rounded_temp = max(
        t for t in virus_ct_chloramines.keys() if t <= temp
    )  # Round down temperature - take the highest value of the values less than or equal to the temperature
    return virus_ct_chloramines[rounded_temp]
