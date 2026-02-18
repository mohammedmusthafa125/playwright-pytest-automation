🚀 Playwright Pytest Automation Framework
📌 Overview

This project is a scalable UI automation framework built using Python, Playwright, and Pytest.
It follows the Page Object Model (POM) design pattern and integrates reporting and CI/CD to simulate a real-world automation environment.

The framework demonstrates:

Structured test architecture

Smoke and Regression execution control

Retry logic for flaky tests

Allure reporting integration

GitHub Actions CI pipeline

Screenshot capture on failure

This repository reflects practical automation practices used in modern QA teams.

🛠 Tech Stack

Language: Python

Automation Tool: Playwright

Test Runner: Pytest

Design Pattern: Page Object Model (POM)

Reporting: Allure Reports

CI/CD: GitHub Actions

Version Control: Git & GitHub

project structure:

playwright-pytest-automation/
│
├── pages/                 # Page Object classes
├── tests/                 # Test cases
├── testdata/              # Test files and data
├── utils/                 # Configurations and helpers
├── conftest.py            # Pytest fixtures
├── pytest.ini             # Pytest configuration
├── requirements.txt       # Dependencies
├── .github/workflows/     # CI pipeline
└── README.md


✅ Implemented Test Scenarios

Login (valid credentials)

Login (negative scenarios)

Logout functionality

Dynamic content loading

File upload validation

API GET & POST validation


Test Markers

@pytest.mark.smoke → Critical path validation

@pytest.mark.regression → Full test suite validation

pytest -m smoke

pytest -m regression

📊 Allure Reporting

Generate Allure results:

pytest --alluredir=allure-results


Serve report:

allure serve allure-results


The report includes:

Test execution status

Step-level visibility

Failure screenshots

Retry attempts

🔁 Retry Logic

Configured using:

--reruns 1


This helps stabilize flaky UI tests and simulates real-world framework behavior.

📸 Screenshot on Failure

If a test fails, a screenshot is automatically captured and stored for debugging purposes.

🔄 CI/CD Integration

The project includes a GitHub Actions workflow that:

Installs dependencies

Installs Playwright browsers

Runs tests in headless mode

Publishes Allure results as artifacts

Pipeline ensures the framework runs successfully in a Linux environment.

▶️ How to Run the Project Locally
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Install Playwright browsers
playwright install

3️⃣ Run tests
pytest

🎯 Purpose of This Project

This framework demonstrates practical QA automation knowledge, including:

Structured framework design

Real-world execution control

CI/CD readiness

Maintainability and scalability practices

It is designed to reflect industry-standard automation engineering workflows.

👨‍💻 Author

Mohammed Musthafa
QA Automation Engineer (Aspiring)
Python | Playwright | Pytest | CI/CD