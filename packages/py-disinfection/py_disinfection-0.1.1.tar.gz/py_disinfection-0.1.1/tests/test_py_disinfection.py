import pytest

import py_disinfection.core as py_d
from py_disinfection.estimation import (
    conservative_giardia_ct,
    interpolate_giardia_ct,
    regression_giardia_ct,
)


@pytest.mark.parametrize(
    "temp, ph, chlorine_conc, expected",
    [
        (6.0, 6.7, 0.9, 149),
    ],
)
def test_conservative_ct(temp, ph, chlorine_conc, expected):
    assert conservative_giardia_ct(temp, ph, chlorine_conc) == expected


@pytest.mark.parametrize(
    "temp, ph, chlorine_conc, expected",
    [
        (6.0, 6.7, 0.9, 126.5),
    ],
)
def test_interpolate_ct(temp, ph, chlorine_conc, expected):
    assert (
        pytest.approx(interpolate_giardia_ct(temp, ph, chlorine_conc), rel=1e-2)
        == expected
    )


@pytest.mark.parametrize(
    "temp, ph, chlorine_conc, expected",
    [
        (6.0, 6.7, 0.9, 134),
    ],
)
def test_regression_ct(temp, ph, chlorine_conc, expected):
    assert (
        pytest.approx(regression_giardia_ct(temp, ph, chlorine_conc), rel=1e-2)
        == expected
    )


# @pytest.mark.parametrize(
#     "temp, ph, chlorine_conc",
#     [
#         (-13.0, 6.7, 0.9),
#     ],
# )
# def test_regression_oob_temp_low(temp, ph, chlorine_conc):
#     assert pytest.raises(ValueError, regression_ct(temp, ph, chlorine_conc))


# @pytest.mark.parametrize(
#     "temp, ph, chlorine_conc",
#     [
#         (133.0, 6.7, 0.9),
#     ],
# )
# def test_regression_oob_temp_high(temp, ph, chlorine_conc):
#     assert pytest.raises(ValueError, regression_ct(temp, ph, chlorine_conc))


@pytest.mark.parametrize(
    "gallons, flow, tdt",
    [
        (282000, 347, 813),
        (24000, 5000, 4.8),
        (80000, 5000, 16),
        (100000, 5000, 20),
        (45000, 5000, 9),
        (300000, 5000, 60),
        (31000, 5000, 6.2),
    ],
)
def test_tdt(gallons, flow, tdt):
    options = py_d.DisinfectionSegmentOptions(
        volume_gallons=gallons,
        peak_hourly_flow_gallons_per_minute=flow,
        baffling_factor=0.1,
        concentration_mg_per_liter=0.8,
        temperature_celsius=0.5,
        ph=6.0,
        agent=py_d.DisinfectantAgent.FREE_CHLORINE,
        ctreq_estimator=py_d.CTReqEstimator.CONSERVATIVE,
    )
    assert (
        pytest.approx(py_d.DisinfectionSegment(options).calculate_tdt(), rel=tdt / 100)
        == tdt
    )


@pytest.mark.parametrize(
    "gallons, flow, bf, contact_time",
    [
        (282000, 347, 0.1, 81.3),
        (24000, 5000, 0.1, 0.48),
        (80000, 5000, 0.1, 1.6),
        (100000, 5000, 0.5, 10),
        (45000, 5000, 0.7, 6.3),
        (300000, 5000, 0.7, 42),
        (31000, 5000, 1.0, 6.2),
    ],
)
def test_contact_time(gallons, flow, bf, contact_time):
    options = py_d.DisinfectionSegmentOptions(
        volume_gallons=gallons,
        peak_hourly_flow_gallons_per_minute=flow,
        baffling_factor=bf,
        concentration_mg_per_liter=0.8,
        temperature_celsius=0.5,
        ph=6.0,
        agent=py_d.DisinfectantAgent.FREE_CHLORINE,
        ctreq_estimator=py_d.CTReqEstimator.CONSERVATIVE,
    )
    assert (
        pytest.approx(
            py_d.DisinfectionSegment(options).calculate_contact_time(),
            rel=contact_time / 100,
        )
        == contact_time
    )


@pytest.mark.parametrize(
    "gallons, temp, ph, flow, bf, conc, ct",
    [
        (282000, 0.5, 6.0, 347, 0.1, 0.8, 65),
        (300000, 10, 7.5, 5000, 0.7, 1.2, 50),
    ],
)
def test_ct(gallons, temp, ph, flow, bf, conc, ct):
    options = py_d.DisinfectionSegmentOptions(
        volume_gallons=gallons,
        peak_hourly_flow_gallons_per_minute=flow,
        baffling_factor=bf,
        concentration_mg_per_liter=conc,
        temperature_celsius=temp,
        ph=ph,
        agent=py_d.DisinfectantAgent.FREE_CHLORINE,
        ctreq_estimator=py_d.CTReqEstimator.CONSERVATIVE,
    )
    assert (
        pytest.approx(py_d.DisinfectionSegment(options).calculate_ct(), rel=ct / 100)
        == ct
    )


def test_ct_required_giardia_free_chlorine():
    options = py_d.DisinfectionSegmentOptions(
        volume_gallons=282000,
        peak_hourly_flow_gallons_per_minute=347,
        baffling_factor=0.1,
        concentration_mg_per_liter=0.8,
        temperature_celsius=0.5,
        ph=6.0,
        agent=py_d.DisinfectantAgent.FREE_CHLORINE,
        ctreq_estimator=py_d.CTReqEstimator.CONSERVATIVE,
    )
    assert (
        pytest.approx(
            py_d.DisinfectionSegment(options).required_ct(
                target=py_d.DisinfectionTarget.GIARDIA
            ),
            rel=0.5,
        )
        == 145
    )


@pytest.mark.parametrize(
    "gallons, temp, ph, flow, bf, conc, ratio",
    [
        (282000, 0.5, 6.0, 347, 0.1, 0.8, 0.448),
        (300000, 10, 7.5, 5000, 0.7, 1.2, 0.368),
    ],
)
def test_calculate_giardia_log_inactivation_ratio(
    gallons, temp, ph, flow, bf, conc, ratio
):
    options = py_d.DisinfectionSegmentOptions(
        volume_gallons=gallons,
        peak_hourly_flow_gallons_per_minute=flow,
        baffling_factor=bf,
        concentration_mg_per_liter=conc,
        temperature_celsius=temp,
        ph=ph,
        agent=py_d.DisinfectantAgent.FREE_CHLORINE,
        ctreq_estimator=py_d.CTReqEstimator.CONSERVATIVE,
    )
    assert (
        pytest.approx(
            py_d.DisinfectionSegment(options).calculate_log_inactivation_ratio(
                target=py_d.DisinfectionTarget.GIARDIA
            ),
            rel=ratio / 100,
        )
        == ratio
    )


def test_calculate_giardia_log_inactivation():
    options = py_d.DisinfectionSegmentOptions(
        volume_gallons=282000,
        peak_hourly_flow_gallons_per_minute=347,
        baffling_factor=0.1,
        concentration_mg_per_liter=0.8,
        temperature_celsius=0.5,
        ph=6.0,
        agent=py_d.DisinfectantAgent.FREE_CHLORINE,
        ctreq_estimator=py_d.CTReqEstimator.CONSERVATIVE,
    )
    assert (
        pytest.approx(
            py_d.DisinfectionSegment(options).calculate_log_inactivation(
                target=py_d.DisinfectionTarget.GIARDIA
            ),
            rel=0.05,
        )
        == 1.34
    )


@pytest.mark.parametrize(
    "gallons, temp, ph, flow, bf, conc, ratio",
    [
        (282000, 0.5, 6.0, 347, 0.1, 0.8, 0.448),
        (300000, 10, 7.5, 5000, 0.7, 1.2, 0.368),
    ],
)
def test_full_results(gallons, temp, ph, flow, bf, conc, ratio):
    options = py_d.DisinfectionSegmentOptions(
        volume_gallons=gallons,
        peak_hourly_flow_gallons_per_minute=flow,
        baffling_factor=bf,
        concentration_mg_per_liter=conc,
        temperature_celsius=temp,
        ph=ph,
        agent=py_d.DisinfectantAgent.FREE_CHLORINE,
        ctreq_estimator=py_d.CTReqEstimator.CONSERVATIVE,
    )
    segment = py_d.DisinfectionSegment(options)
    results = segment.analyze()
    assert pytest.approx(results["giardia_ct_ratio"], rel=ratio / 100) == ratio


# def test_ct_required_viruses_free_chlorine():
#     options = py_d.DisinfectionSegmentOptions(
#         volume_gallons=282000,
#         peak_hourly_flow_gallons_per_minute=347,
#         baffling_factor=0.1,
#         concentration_mg_per_liter=0.8,
#         temperature_celsius=0.5,
#         ph=6.0,
#     )
#     assert (
#         pytest.approx(py_d.DisinfectionSegment(options)._required_ct_viruses(), rel=0.5)
#         == 145
#     )
