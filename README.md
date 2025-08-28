# Test task
This repo is used to showcase test approach for Playwright + pytest.<br>
It uses [OrangeHRM](https://ddec1-0-en-ctp.trendmicro.com/wis/clicktime/v1/query?url=https%3a%2f%2fopensource%2ddemo.orangehrmlive.com%2fweb%2findex.php%2fauth%2flogin&umid=cdcc023c-bb19-4239-a913-67085e30709e&rct=1751307249&auth=764ac1ebf8525e86559591b5649e04916e63728b-0b105689ebceb390b5f855f57f5f524eb523e611) to define several test cases.<br>
Tests are running in parallel, collect logs and screenshots and generate html report.

## Getting Started
To run the tests for this project, follow the steps below:

### 1. Clone the Repository

```bash
git clone https://github.com/dvts1471/ui_test_fw_playwright.git
cd ui_test_fw_playwright
```

### 2. Install required packages:
```bash
pip install -r requirements.txt
```

### 3. Install playwright:
```bash
playwright install
```

###	4. Run tests using pytest:
```bash
pytest
```

### 5. Analyze test results:
HTML report is created in ./test_results dir.<br>
Every verification has screenshot evidence (path to the screenshot can be found in logs).