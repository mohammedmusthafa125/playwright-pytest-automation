Playwright + PyTest Automation Framework (Python)
📌 Project Overview

This project is a UI test automation framework built using Python, Playwright, and PyTest, following industry-standard practices such as Page Object Model (POM), configuration handling, data-driven testing, and reporting.

The framework automates the login functionality of a sample web application and is designed to be scalable, maintainable, and CI-friendly.

🛠 Tech Stack Used

Programming Language: Python

Automation Tool: Playwright (Sync API)

Test Framework: PyTest

Design Pattern: Page Object Model (POM)

Reporting: Allure Reports

Version Control: Git

📂 Project Structure
project/
├── pages/
│   ├── __init__.py
│   └── Login_Page.py
│
├── tests/
│   ├── __init__.py
│   └── test_login.py
│
├── utils/
│   ├── __init__.py
│   └── config.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md

🧱 Framework Highlights
✅ Page Object Model (POM)

Page logic is separated from test logic

Improves maintainability and reusability

✅ Configuration Handling

Browser type, URL, headless mode, and timeouts are managed via config.py

Environment changes do not require test code changes

✅ Data-Driven Testing

Login tests are executed with multiple data sets

Same test covers both positive and negative scenarios

✅ PyTest Fixtures

Browser and page lifecycle handled using fixtures

Clean setup and teardown for every test run

✅ Allure Reporting

Generates interactive HTML reports

Shows test status, execution time, and results clearly

🧪 Test Scenarios Covered

✔ Valid login with correct credentials

❌ Invalid login with incorrect credentials

Assertions based on success and failure messages

▶️ How to Run the Tests
1️⃣ Clone the Repository
git clone <your-github-repo-url>
cd project

2️⃣ Create and Activate Virtual Environment
python -m venv .venv
.venv\Scripts\activate   # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Tests
pytest

📊 Generate Allure Report
1️⃣ Run Tests with Allure Enabled
pytest --alluredir=allure-results

2️⃣ Open Allure Report
allure serve allure-results

🔧 Configuration Control

All execution-related settings are managed in:

utils/config.py


You can easily change:

Browser (chromium, firefox, webkit)

Headless mode

Base URL

Timeout values

🎯 Why This Project?

This project demonstrates:

Strong understanding of automation fundamentals

Ability to structure real-world automation frameworks

Hands-on experience with Playwright + PyTest

Clean, readable, and maintainable test code

🚀 Future Enhancements

Cross-browser execution

Screenshot capture on failure

CI/CD integration

More test modules and pages

👤 Author

Mohammed Musthafa
Aspiring QA Automation Engineer
Skilled in Python, Playwright, and PyTest