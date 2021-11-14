# <center> Arrowstreet Capital </center>

---

## <center> Portfolio Management Tool </center>

---

### General Information
<b>Author:</b> Pranav H. Deo <i>{ phd24@umd.edu }</i> <br>
<b>Date:</b> 11/13/2021 <br>
<b>Note:</b> This project is purely for demonstration of DevOps & Full-Stack development skills. It should
not be used in distribution or logical or algorithmic implementations. <br>
<b>Plagiarism:</b> This project guarantees 0% plagiarism.

---

### Opensource Software / Tools used
a. Pycharm Editor <br>
b. Docker <br>
c. Python3.9 <br>
d. Ubuntu 20.04 <br>

---

### Python libraries used
a. Python-Flask (Web-GUI) <br>
b. PyYaml (YAML reader) <br>
c. Requests (API request catch) <br>
d. Random (Random no. generator) <br>

---

### About the Application
* This application uses `Python-Flask` for Web-front (GUI)
* It renders `HTML` scripts on GUI
* `config` directory contains `.txt` & `.yaml` files.
  * `asc_trx_data.txt` contains the data written after reading the `JSON` API from `https://www.styvio.com/api/*`
  * `transaction_data.txt` was used for testing with hard-coded data (Ignored by application).
  * `company_tracker.yaml` contains the `URLs` for different companies. One can add / remove companies from here to monitor the stocks.
* `modules` directory contains 2 python scripts: `analyzer.py` & `apiReader.py`.
  * `analyzer.py` is used to analyze the data read from the API. This script contains functions to compute Stocks, Profit/Loss and Balance etc.
  * `apiReader.py` is used to read live API from `https://www.styvio.com/api/*`. It translates the `JSON` data to `.txt` data for `analyzer.py` to analyze.
* `static` directory contains `image` directory which contains the various company images for Web-GUI display.
* `template` directory contains 4 `HTML` templates - `HomePage.html`, 'Login.html', 'Register.html' & `Investments.html`.
  * `Login.html` contains the script for user login
  * `Register.html` contains the script for user registration
  * `HomePage.html` contains the script for rendering landing page of the web application
  * `Investments.html` contains the cards to display various companies and their live analyzed stats.
* `WebApp.py` contains the routing logic for `Flask` Web-App.

---

### Additional Scope
* RDS DB for Login/Registration/Caching etc.
* CloudFormation Deployment across EC2 instances (End-2-End).
* Polling Live Data logic with auto-refresh and live graphical stats.
* Intelligent logic on shares to sell / buy.
* Adding new company via GUI for monitoring stats.

---
---