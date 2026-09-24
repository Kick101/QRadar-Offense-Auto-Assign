# QRadar-Offense-Auto-Assign
Automates offense assignment in IBM QRadar using Playwright. Runs on a schedule, assigns offenses to the logged-in analyst.

> ⚠️ Note: This is a personal automation project. It is not affiliated with or endorsed by IBM. Test thoroughly in a non-production QRadar environment before deploying.

## How it works

1. Attaches to a Chromium instance running with remote debugging enabled (`localhost:9222`)
1. Finds the tab whose title contains "Offense Manager"
1. Clicks refresh in the rightPane iframe, scrapes the offense table to offenses.html
1. Parses the HTML into offenses.json
1. Bulk-selects every offense with no assigned user
1. Opens Actions → Assign, picks a random username from `qradar-usernames.txt`, and saves

The script does not launch a browser or handle login. You must have a Chromium session already open and logged into QRadar.


## Installation
```
git clone https://github.com/Kick101/QRadar-UI-automation-via-Playwright.git
cd QRadar-UI-automation-via-Playwright

python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

pip install -r requirements.txt

# Playwright browsers are NOT installed by pip — this step is required
playwright install
```

## Critical setup: the Chromium session
This script uses connect_over_cdp, so Playwright attaches to a browser you start yourself. You must start Chromium with the remote debugging port open before running the script.

1. Edit `launch_browser.bat` with the correct browser binary location
2. Example:
```
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
```


## Usage
1. After editing the `launch_browser.bat`. Double-click `launch_browser.bat` to launch the browser with remote debugging enabled
2. Add your QRadar username to `qradar-usernames.txt`
3. Run once:

```
python qradar-offense-auto-assign.py
```

4. Run on a schedule (every 10 minutes):
```
python qradar-offense-auto-assign-scheduler.py
```
