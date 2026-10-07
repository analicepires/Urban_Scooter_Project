# Final Project – Urban Routes

![Web Testing](https://img.shields.io/badge/Test-Web-blue)
![API Testing](https://img.shields.io/badge/Test-API-orange)
![Manual Testing](https://img.shields.io/badge/Test-Manual-green)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?logo=selenium&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?logo=pytest&logoColor=white)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/analice-pires/)

---

## 📌 Project Overview

This final project was developed as part of **Sprint 9** of the **QA course at TripleTen**.  
It demonstrates the full cycle of **planning**, **executing**, and **documenting** functional tests for a **Web application** and **API endpoints** within the **Urban Routes** ecosystem.

The Web tests were **automated with Python + Selenium + Pytest**, developed in **VS Code** using the **Page Object Model** pattern.

The project simulates a real-world QA scenario involving writing detailed test cases, running tests under time constraints, logging and tracking bugs in **JIRA**, and consolidating all results and evidence in **Google Sheets**.

Initially, the scope included **mobile app testing**, but due to technical issues with the app build, the mobile tests could not be executed and were postponed for future improvement.

---

## 🎯 Project Goal

- Plan, write, and execute functional test cases for the Web application and its API.
- Automate the Web test cases with **Selenium WebDriver** and **Python**.
- Log and track bugs effectively in **JIRA**.
- Consolidate results, test cases, and bug reports in **Google Sheets**.
- Deliver clear evidence for identified issues.

> **Note:** Mobile app testing was planned but could not be executed due to a technical issue with the app build. This remains an opportunity for future execution.

---

## 🔧 Technologies and Tools

- **Manual Testing**
- **Python** — Test automation language
- **Selenium WebDriver** — Web UI automation (Chrome)
- **Pytest** — Test runner, parametrized test cases and failure evidence
- **VS Code** — Development environment
- **Postman** — API Testing
- **JIRA** — Bug Tracking and Reporting
- **Google Sheets** — Test Case Management and Execution Results

---

## ▶️ How to Execute

### 🖥️ **Web Application (Automated — Selenium + Python)**

The automated suite covers the **First name**, **Last name**, and **Phone** fields of the first step of the *Order* form (20 test cases, CT-01 to CT-20).

1. Launch the Urban Routes server and update `URBAN_SCOOTER_URL` in `web-tests/data.py` if the URL changed.
2. Open the `web-tests` folder in **VS Code** and create/activate a virtual environment:
   ```bash
   cd web-tests
   python -m venv .venv
   .venv\Scripts\activate      # Windows
   # source .venv/bin/activate  # Linux/macOS
   ```
3. Install the dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Run the tests:
   ```bash
   python -m pytest -v
   ```
5. Selenium opens Chrome at **1280x720**, runs the 20 scenarios, and closes the browser.
6. When a test fails, a screenshot (`.png`) and a report (`.txt`) are saved in `web-tests/evidencias/` to be used as evidence for the bug in JIRA.

### 🔗 **API**
1. Run the backend server.
2. Review the API documentation (apiDoc).
3. Use **Postman** to send POST and DELETE requests.
4. Validate API responses and database updates.
5. Report any issues found in JIRA.

> **Note:** The **Urban Routes** server must be running for the tests to run properly.

---

## 🧾 Results

- **96** Web test cases were created and executed.
- **43** API test cases were created and executed.
- A total of **35 bugs** were identified and tracked in **JIRA**.

---

## 📚 What I Learned

- Planning and prioritizing tests effectively under tight deadlines.
- Hands-on experience with multi-platform testing (Web, Mobile, API).
- Clear and traceable bug reporting using JIRA.
- Web UI automation with Selenium WebDriver, Pytest parametrization, and the Page Object Model.
- Organizing execution evidence in collaborative tools like Google Sheets.

---

## 💡 Future Improvements

- Extend tests to cover the **Mobile app** version.
- Expand the Selenium suite to cover the remaining steps of the order flow.
- Automate API scenarios using **Python + Requests**.
- Integrate automated tests into a **CI/CD pipeline**.
- Expand exploratory test coverage for edge cases.

---

## 🗂️ Project Structure

```
Urban_Scooter_Project/
├── api-tests/              # Postman globals for API tests
├── docs/                   # Requirements and server guide (PDF)
├── mobile-tests/           # Mobile app build (APK)
└── web-tests/              # Selenium + Python automation
    ├── bug-screenshots/    # Evidence of the bugs found
    ├── conftest.py         # Saves screenshot + report when a test fails
    ├── data.py             # URL and valid test data
    ├── pages.py            # Page Object Model and locators
    ├── requirements.txt    # selenium, pytest
    └── test_urban_scooter.py  # Parametrized test cases (CT-01 to CT-20)
```

---

## 📂 Project Files

- [📄 Google Sheets — Test Cases and Execution Results](https://docs.google.com/spreadsheets/d/1lzxzIyFdUGPFFqEZinuH5yliMmmpbv5SyC1AKtSI7Cg/edit?usp=sharing)
- [🐞 JIRA — Bug Reports](https://analicesworkspace-43077494.atlassian.net/?continue=https%3A%2F%2Fanalicesworkspace-43077494.atlassian.net%2Fwelcome%2Fsoftware%3FprojectId%3D10001&atlOrigin=eyJpIjoiM2Y1Y2Q0ZDlkNzRlNDAzZThiYmNjZjMzOGI3NDk1OWQiLCJwIjoiamlyYS1zb2Z0d2FyZSJ9)

---
