"""Retirement readiness dashboard — Streamlit app.

The sidebar inputs below already work. The results section calls into
retirement_model.py, which has 3 TODOs — until those are filled in, each
result panel shows a placeholder instead of crashing the whole page.
"""

import pandas as pd
import streamlit as st

import retirement_model as model

st.set_page_config(page_title='Retirement Readiness Check', layout='centered')
st.title('Retirement Readiness Check')
st.caption(
    "A private wealth client wants to know whether their current plan supports "
    "retirement. Adjust their numbers below and see the projection."
)

ASSET_CLASSES = ['cash', 'bonds', 'equities', 'precious_metals', 'real_estate']
ASSET_LABELS = {
    'cash': 'Cash',
    'bonds': 'Bonds',
    'equities': 'Equities',
    'precious_metals': 'Precious Metals',
    'real_estate': 'Real Estate',
}
DEFAULT_ALLOCATION = {'cash': 10, 'bonds': 10, 'equities': 50, 'precious_metals': 10, 'real_estate': 20}

with st.sidebar:
    st.header('Client profile')
    current_age = st.number_input('Current age', min_value=18, max_value=80, value=30)
    retirement_age = st.number_input('Target retirement age', min_value=19, max_value=90, value=65)
    current_savings = st.number_input('Current retirement savings ($)', min_value=0, value=20_000, step=1_000)
    annual_contribution = st.number_input('Annual contribution ($)', min_value=0, value=8_000, step=500)

    st.header('Portfolio allocation (%)')
    allocation_pct = {}
    for asset in ASSET_CLASSES:
        allocation_pct[asset] = st.slider(ASSET_LABELS[asset], 0, 100, DEFAULT_ALLOCATION[asset])
    allocation_total = sum(allocation_pct.values())
    if allocation_total != 100:
        st.caption(f'Allocations sum to {allocation_total}% — normalized to 100% below.')

    with st.expander('Return & inflation assumptions'):
        returns_by_asset = {}
        for asset in ASSET_CLASSES:
            returns_by_asset[asset] = st.slider(
                f'{ASSET_LABELS[asset]} expected return (%)', 0.0, 15.0,
                model.DEFAULT_RETURNS[asset] * 100, step=0.1,
            ) / 100
        inflation_pct = st.slider('Inflation (%)', 0.0, 10.0, model.DEFAULT_INFLATION * 100, step=0.1)

    st.header('Retirement income')
    target_income = st.number_input('Target annual retirement income ($, today\'s dollars)', min_value=0, value=50_000, step=1_000)
    withdrawal_rate_pct = st.slider('Withdrawal rate (%)', 1.0, 10.0, 4.0, step=0.1)

years_to_retirement = int(retirement_age) - int(current_age)
allocation = (
    {k: v / allocation_total for k, v in allocation_pct.items()}
    if allocation_total > 0 else {k: 0 for k in ASSET_CLASSES}
)
inflation = inflation_pct / 100
withdrawal_rate = withdrawal_rate_pct / 100

st.divider()

if years_to_retirement <= 0:
    st.warning('Retirement age must be after current age.')
    st.stop()

# br is computed once, outside the results/chart sections below, so a
# NotImplementedError here doesn't leave `br` undefined for the chart section
# (an undefined-variable NameError wouldn't be caught by `except NotImplementedError`
# and would crash the whole page instead of degrading gracefully).
br = None
try:
    br = model.blended_return(allocation, returns_by_asset)
except NotImplementedError as e:
    st.info(f'Results not available yet — {e}\n\nSee `retirement_model.py`.')

if br is not None:
    try:
        fv = model.project_portfolio_value(current_savings, annual_contribution, br, inflation, years_to_retirement)
        annual_withdrawal, monthly_withdrawal = model.sustainable_withdrawal(fv, withdrawal_rate)
        gap = target_income - annual_withdrawal

        col1, col2, col3 = st.columns(3)
        col1.metric('Blended return', f'{br:.1%}')
        col2.metric('Projected value at retirement', f'${fv:,.0f}')
        col3.metric('Sustainable withdrawal', f'${annual_withdrawal:,.0f}/yr', help=f'${monthly_withdrawal:,.0f}/month')

        if gap > 0:
            st.error(f'Funding gap: short by ${gap:,.0f}/yr against the ${target_income:,.0f} target.')
        else:
            st.success(f'On track: ${-gap:,.0f}/yr above the ${target_income:,.0f} target.')
    except NotImplementedError as e:
        st.info(f'Results not available yet — {e}\n\nSee `retirement_model.py`.')

st.subheader('Projected portfolio value over time')
if br is None:
    st.info('Chart not available yet — see `retirement_model.py`.')
else:
    try:
        years = list(range(1, years_to_retirement + 1))
        values = [
            model.project_portfolio_value(current_savings, annual_contribution, br, inflation, y)
            for y in years
        ]
        chart_df = pd.DataFrame({'years from now': years, 'projected value ($)': values}).set_index('years from now')
        st.line_chart(chart_df)
    except NotImplementedError as e:
        st.info(f'Chart not available yet — {e}\n\nSee `retirement_model.py`.')
