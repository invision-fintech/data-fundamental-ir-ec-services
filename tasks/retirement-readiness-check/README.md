# Retirement readiness check

**Open question:** a private wealth client wants to know whether their
current savings plan will actually support the retirement they want.
Right now that's a spreadsheet built fresh each time someone asks. There's a
start on a reusable dashboard below — the interactive shell works; the
actual projection math needs finishing.

The client's current portfolio: Cash 10% / Bonds 10% / Equities 50% /
Precious Metals 10% / Real Estate 20%.

## The app

Open **[`app.py`](app.py)** — it's a small [Streamlit](https://streamlit.io)
app. The sidebar (age, savings, contributions, allocation, return/inflation
assumptions, target income, withdrawal rate) already works. The results
panel and the growth chart call into **[`retirement_model.py`](retirement_model.py)**,
which has 3 functions left as `TODO`s — until those are filled in, the app
runs fine but shows a placeholder instead of numbers.

**Setting up:** see **[SETUP.md](../../SETUP.md)** — it covers installing
everything on Windows, and a browser-only option if you'd rather not install
anything. Once you're set up, from this folder: `streamlit run app.py`
(opens in your browser automatically).

**Or deploy it:** fork this repo and point
[Streamlit Community Cloud](https://streamlit.io/cloud) at your fork's
`tasks/retirement-readiness-check/app.py` (free tier, connects directly to
GitHub) — closest equivalent here to how the notebook task uses Colab.

**Checking your work:** `python test_retirement_model.py` from this folder
(no extra installs; `pytest` works too if you prefer it). It checks each
function against the reference numbers in the docstrings and tells you which
ones aren't right yet. Before you start, everything reports `TODO` — that's
your starting state, not a failure. Passing it is the floor, not the finish
line; the screenshot and the write-up are what the review actually turns on.

## What "done" looks like

This should be readable by someone who never opens `app.py` — a teammate
should get the finding from the screenshot and the write-up alone:

- All 3 functions in `retirement_model.py` are implemented (their docstrings
  describe the approach; `test_retirement_model.py` pins the numbers) and the
  app shows real numbers
  for a scenario of your choice: blended return, projected portfolio value
  at retirement, sustainable annual/monthly withdrawal, funding gap vs.
  target income, and the growth-over-time chart.
- A screenshot of that scenario, attached to the PR (the app has no saved
  "last run" state the way a notebook has saved cell outputs, so this is
  what lets a reviewer see the result without running it themselves).
- A short Methodology write-up in this README (below, or as a PR
  description) — at least 250 words: the scenario you used and why, whether
  you'd change any of the default return/inflation assumptions and why, what
  the funding gap means for this client, and what you'd add next if you kept
  going.

## A couple of notes

- Keep the compounding math deterministic (a single blended-return
  projection) — a full Monte Carlo / sequence-of-returns simulation is real,
  interesting work, but it's out of scope here.
- The default return/inflation assumptions in `retirement_model.py` are
  ballpark historical averages, not a live feed — no live market-data API
  is required or expected.
- Optional stretch, not required: any of spouse/dependents, mortgage or car
  loan paydown, major future expenses (education, home down payment,
  vehicle purchases), or government/workplace pension income as additional
  sidebar inputs feeding into the projection.

## Methodology

_(Fill this in as part of your PR — see "What done looks like" above.)_
