"""Retirement projection math, kept separate from the Streamlit UI in app.py
so it stays independently readable/testable/reusable.

Deliberately deterministic compound-growth math, not a Monte Carlo /
sequence-of-returns simulation — that's a much bigger model than this task
calls for.
"""

# Long-run nominal annual return assumptions per asset class. These are
# reasonable historical-average ballparks (broad equity/bond indices,
# short-term cash instruments, gold, diversified real estate), not a live
# feed — state in your write-up whether you'd revise any of them and why.
DEFAULT_RETURNS = {
    'cash': 0.02,
    'bonds': 0.04,
    'equities': 0.08,
    'precious_metals': 0.03,
    'real_estate': 0.06,
}

DEFAULT_INFLATION = 0.025


def blended_return(allocation: dict, returns_by_asset: dict) -> float:
    """Weighted-average expected annual return across the portfolio.

    Args:
        allocation: e.g. {'cash': 0.10, 'bonds': 0.10, 'equities': 0.50,
            'precious_metals': 0.10, 'real_estate': 0.20} — fractions summing to 1.0.
        returns_by_asset: expected nominal annual return per asset class,
            same keys as allocation (see DEFAULT_RETURNS).

    Returns:
        The blended nominal annual return, as a fraction (e.g. 0.061 for 6.1%).
    """
    raise NotImplementedError('TODO: weighted sum of allocation * returns_by_asset')


def project_portfolio_value(
    current_savings: float,
    annual_contribution: float,
    blended_return: float,
    inflation: float,
    years_to_retirement: int,
) -> float:
    """Projects portfolio value at retirement, in today's real dollars.

    Convert the nominal blended_return to a real (inflation-adjusted) return
    first, then compound current_savings for years_to_retirement years and
    add the future value of annual_contribution as an ordinary annuity
    (contribution made at the end of each year).

    Handle the edge case where the real return is ~0 — the annuity formula
    divides by the real return rate, which blows up at exactly zero.

    Returns:
        Projected portfolio value at retirement, in today's real dollars.
    """
    raise NotImplementedError('TODO: real-return compounding + annuity future value')


def sustainable_withdrawal(portfolio_value: float, withdrawal_rate: float) -> tuple:
    """Annual and monthly withdrawal at the given rate of the portfolio value.

    Returns:
        (annual_withdrawal, monthly_withdrawal)
    """
    raise NotImplementedError('TODO: portfolio_value * withdrawal_rate, and /12 for monthly')
