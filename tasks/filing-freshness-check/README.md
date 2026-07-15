# Filing freshness check

**Open question:** before anyone invests in automating a "data freshness"
signal off SEC filings, we want to know whether that's even a reliable thing
to measure — fiscal quarters don't line up with calendar quarters for every
company, and "the most recent filing" can quietly be months old. There's a
start on checking this for one company below; it needs finishing, and a
write-up the rest of the team can actually use.

## The notebook

Open **[`notebook.ipynb`](notebook.ipynb)** and run it top to bottom. The
early cells pull real data and already work; a few `TODO`s further down need
finishing before the rest runs.

**Fastest way to start (no install):** open it directly in Colab —
`https://colab.research.google.com/github/invision-fintech/data-fundamental-ir-ec-services/blob/main/tasks/filing-freshness-check/notebook.ipynb`

**Or locally:** `pip install requests pandas matplotlib jinja2`, then open
`notebook.ipynb` in Jupyter or VS Code.

## What "done" looks like

This should be readable by someone who never opens the notebook's code —
a teammate should get the finding just from skimming the top:

- The notebook runs top to bottom for a company of your choice, with all
  cells executed and their outputs (tables, chart) saved before you commit —
  nobody should have to re-run anything to see your result.
- The Executive Summary cell at the top is filled in (write it last, after
  you've done the analysis below it) — at least 500 words, covering: what you
  found, the actual numbers, anything that makes you trust or distrust the
  result, and whether this is worth extending to more companies.
- A chart of revenue by period and a table showing which periods are covered
  vs. missing/stale.

Open a PR with your notebook (see the repo's `CONTRIBUTING.md`) when you have
something working — partial/incremental is fine.

## A couple of notes

- Stick to a company with a plain January-December fiscal year to start
  (the notebook suggests a few) — some real companies use unusual fiscal
  calendars, which is a fun rabbit hole but not the point of this task.
- Optional stretch, not required: load your final table into a BigQuery
  dataset in your own GCP project instead of a CSV, if you want the extra
  practice.
