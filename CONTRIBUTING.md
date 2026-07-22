# Contributing

## The one rule
**Never commit secrets.** Not an API key, not a `.env` file, not a credentials
file. The `gitleaks` workflow will fail your PR if it finds one.

If you accidentally pushed a secret: rotate it immediately (assume it's
compromised), then [purge from history](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).
Don't just delete the file in a follow-up commit — git history retains it.

## Workflow

This repo doesn't grant direct push access to non-`core` contributors, so
**everyone** goes through a fork:

1. Fork the repo to your own account.
2. Branch from `main`: `git checkout -b your-name/short-description`.
3. Commit small, push often. One working PR is fine; a few incremental ones are
   also fine.
4. Open a PR from your fork against `invision-fintech/data-fundamental-ir-ec-services:main`,
   referencing the relevant issue. The `gitleaks` check must be green and one approval is
   required before merge. If `gitleaks` fails, read the run log — it names the file and
   commit it flagged. If it looks like a false positive, say so in the PR rather than
   working around it; a reviewer will sort it out.
5. Squash-merge into `main`.

## Naming
- Branches: `<your-name>/<description>`, e.g. `jdoe/mini-pipeline`.

## Reviews
PRs auto-request review from `@invision-devs`/`@invision-fintech/core` via
`CODEOWNERS`.
