# Setup

Everything you need to get a task running. Written for Windows, and written assuming
you've never done this before — no prior setup, and no need to be comfortable with a
terminal.

**Pick one of the three paths below.** They all end in the same place. Then come back for
[Getting the code](#getting-the-code) onward.

If you get stuck, jump to [When something goes wrong](#when-something-goes-wrong) — it
covers the handful of things that actually trip people up on Windows. And if you're stuck
for more than about fifteen minutes, ask. That's faster than grinding, and if the
instructions are unclear we want to know.

---

## Path A — Nothing to install

Best if you're on a work laptop that blocks installing software, or you just don't want
to set anything up. Everything runs in your browser.

1. Go to the [repo](https://github.com/invision-fintech/data-fundamental-ir-ec-services).
2. Click the green **Code** button ▸ **Codespaces** tab ▸ **Create codespace on main**.
3. Wait a minute or two. It opens a full code editor in your browser with Python and
   every package already installed.

That's it — skip ahead to [Running your task](#running-your-task). There's no cloning and
no installing on this path; it's already done.

> Your personal GitHub account includes 120 core-hours of Codespaces per month at no
> cost, which is far more than a task needs. Close the browser tab when you're done and
> it stops counting.

Two tasks also have their own browser option, if you'd rather use those:
the notebook task opens in **Google Colab**, and the dashboard task deploys to
**Streamlit Community Cloud**. Each task's README has the link.

---

## Path B — On your PC, using apps

Best if you'd rather click buttons than type commands. You'll install two apps, and after
that everything is menus and buttons.

1. **Install [GitHub Desktop](https://desktop.github.com)** — manages the code for you.
2. **Install [Visual Studio Code](https://code.visualstudio.com)** — where you'll write and
   run things.
3. **Install [Python](https://www.python.org/downloads/windows/)** — download the latest
   "Windows installer (64-bit)".

   > **This one step matters.** On the installer's first screen, tick
   > **"Add python.exe to PATH"** at the bottom before clicking Install. It's easy to miss,
   > and skipping it is the single most common reason things don't work later.

Then continue to [Getting the code](#getting-the-code).

---

## Path C — On your PC, one command

Best if you're comfortable with a terminal. Open **PowerShell** from the Start menu and run:

```powershell
winget install Python.Python.3.12 Git.Git Microsoft.VisualStudioCode GitHub.GitHubDesktop
```

That installs all four at once, and handles the PATH setting from Path B automatically.

**Close PowerShell and open a new one afterwards** — a terminal only picks up newly
installed programs when it starts.

---

## Getting the code

*(Skip this if you used Path A — a Codespace already has the code.)*

**Using GitHub Desktop:**

1. **File ▸ Clone repository ▸ URL**
2. Paste: `https://github.com/invision-fintech/data-fundamental-ir-ec-services.git`
3. Click **Choose…** to pick where it goes — anywhere is fine, `Documents` is a
   reasonable default. **GitHub Desktop creates the folder for you**, so there's nothing
   to make beforehand.
4. Click **Clone**, then **Open in Visual Studio Code**.

**Or in PowerShell:**

```powershell
git clone https://github.com/invision-fintech/data-fundamental-ir-ec-services.git
code data-fundamental-ir-ec-services
```

The whole repo is about 20 KB, so this takes a second. You get every task, not just
yours — that's deliberate. Your task's README will tell you which folder is yours.

---

## Installing what the tasks need

Once, from the repo folder:

```powershell
python -m pip install -r requirements.txt
```

This covers **every** task, so you only ever do it once. If you're on Path A this already
ran for you.

> Use `python -m pip`, not plain `pip`. Both usually work, but the longer form keeps
> working in situations where `pip` on its own doesn't.

---

## Opening the right folder — without typing `cd`

Commands only work when the terminal is pointed at the right folder. You never have to
navigate there by typing. Easiest first:

| What you want | How |
|---|---|
| A terminal already inside a task folder | In VS Code's sidebar, **right-click the task folder ▸ Open in Integrated Terminal** |
| A terminal at the repo root | In VS Code, **Terminal ▸ New Terminal** |
| To jump straight to one task | In VS Code, **File ▸ Open Folder**, pick the task folder |
| A terminal from File Explorer | Right-click the folder ▸ **Open in Terminal** |

The first row is the one to remember. Right-click the folder, open a terminal there, and
whatever the task README tells you to type will just work.

To check you're in the right place, run `ls` — you should see the task's files listed.

---

## Running your task

From a terminal in your task's folder:

| Task | Command |
|---|---|
| `retirement-readiness-check` | `streamlit run app.py` |
| `filing-freshness-check` | Open `notebook.ipynb` in VS Code and click **Run All** |

A Streamlit app opens in your browser automatically. **Leave the terminal open** while
you use it — that window is running the app, and closing it stops the app. Press
`Ctrl+C` in the terminal when you actually want to stop.

Each task's README covers what to do from here.

---

## When something goes wrong

| What you see | What's happening | What to do |
|---|---|---|
| `Python was not found`, or the Microsoft Store opens instead | Windows ships a placeholder `python.exe` that pretends to be Python and just opens the Store. It's shadowing your real install. | **Settings ▸ Apps ▸ Advanced app settings ▸ App execution aliases** → switch off `python.exe` and `python3.exe`. Then open a new terminal. |
| `pip is not recognized` | pip is installed but Windows can't find it by that name | Use `python -m pip install ...` instead |
| You installed Python but the terminal still can't find it | The **"Add python.exe to PATH"** box was left unticked | Re-run the installer, choose **Modify**, and tick it. Or just use Path C. |
| `winget is not recognized` | Older Windows, or your workplace blocks it | Use Path B instead, or Path A |
| `Port 8501 is already in use` | A previous run is still going | `streamlit run app.py --server.port 8502` |
| The app went blank or stopped responding | The terminal running it was closed | Start it again, and leave the terminal open this time |
| `git is not recognized` | Git isn't installed | Path B (GitHub Desktop includes it) or Path C |

---

## A note on virtual environments

If you've read Python tutorials, you may expect to create a "virtual environment" first.
**You don't need one here.** The tasks share compatible packages, so installing them
normally is fine — and it avoids a whole category of confusing errors about activation
and the wrong Python being used.

If a future task ever needs a conflicting version, we'll add instructions then.
