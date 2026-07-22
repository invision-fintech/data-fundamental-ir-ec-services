"""Checks for the three functions in retirement_model.py.

Run them as you work — they're the same reference numbers quoted in the
docstrings, and they'll tell you when each function is right.

    python test_retirement_model.py     # no extra installs
    pytest test_retirement_model.py     # if you'd rather use pytest

Before you've written anything, every check fails with "not implemented yet".
That's expected — that's your starting state.

These pin the *answers*, not the approach. There's more than one reasonable way
to write the code behind them, and passing these is the floor, not the whole
task — the screenshot and the write-up are what the review actually turns on.
"""

import retirement_model as model

CLIENT_ALLOCATION = {
    'cash': 0.10,
    'bonds': 0.10,
    'equities': 0.50,
    'precious_metals': 0.10,
    'real_estate': 0.20,
}


def close(actual, expected, tolerance=0.5):
    return abs(actual - expected) <= tolerance


def test_blended_return_matches_the_client_portfolio():
    """The client's allocation against DEFAULT_RETURNS is exactly 6.1%."""
    result = model.blended_return(CLIENT_ALLOCATION, model.DEFAULT_RETURNS)
    assert close(result, 0.061, 1e-9), f'expected 0.061, got {result}'


def test_blended_return_of_a_single_asset_is_that_assets_return():
    """100% equities should just be the equities number — no weighting subtleties."""
    all_equities = {k: (1.0 if k == 'equities' else 0.0) for k in model.DEFAULT_RETURNS}
    result = model.blended_return(all_equities, model.DEFAULT_RETURNS)
    assert close(result, 0.08, 1e-9), f'expected 0.08, got {result}'


def test_projected_value_reference_scenario():
    """Age 30 to 65, $20k saved, $8k/yr, 6.1% nominal, 2.5% inflation."""
    result = model.project_portfolio_value(20_000, 8_000, 0.061, 0.025, 35)
    assert close(result, 601_625), (
        f'expected ~601_625, got {result:,.0f}.\n'
        '        If you got ~450_684, you compounded at the nominal rate and deflated the\n'
        '        result at the end. That answers a different question - see the docstring.'
    )


def test_projected_value_survives_a_zero_real_return():
    """When the nominal return equals inflation the real return is exactly 0.

    The annuity formula divides by that rate, so this is the edge case the
    docstring asks you to handle. Nothing grows in real terms: you end up with
    what you put in.
    """
    result = model.project_portfolio_value(20_000, 8_000, 0.025, 0.025, 35)
    assert close(result, 300_000), f'expected 300_000, got {result:,.0f}'


def test_projected_value_with_no_contributions_is_pure_compounding():
    result = model.project_portfolio_value(20_000, 0, 0.061, 0.025, 35)
    assert close(result, 66_947), f'expected ~66_947, got {result:,.0f}'


def test_projected_value_at_zero_years_is_todays_savings():
    result = model.project_portfolio_value(20_000, 8_000, 0.061, 0.025, 0)
    assert close(result, 20_000), f'expected 20_000, got {result:,.0f}'


def test_sustainable_withdrawal_splits_annual_and_monthly():
    annual, monthly = model.sustainable_withdrawal(601_625, 0.04)
    assert close(annual, 24_065), f'expected annual ~24_065, got {annual:,.0f}'
    assert close(monthly, 2_005), f'expected monthly ~2_005, got {monthly:,.0f}'


if __name__ == '__main__':
    tests = [v for k, v in sorted(globals().items()) if k.startswith('test_')]
    passed, pending, failed = 0, 0, []
    for test in tests:
        try:
            test()
            passed += 1
            print(f'  PASS  {test.__name__}')
        except NotImplementedError:
            pending += 1
            print(f'  TODO  {test.__name__}')
        except AssertionError as e:
            failed.append(test.__name__)
            print(f'  FAIL  {test.__name__}\n        {e}')

    print(f'\n{passed} passed, {pending} not implemented yet, {len(failed)} failed')
    if pending and not failed:
        print("Nothing's wrong - you just haven't filled in retirement_model.py yet.")
    raise SystemExit(1 if failed else 0)
