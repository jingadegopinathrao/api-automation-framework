# 🚀 API Automation Testing Framework

A robust and scalable API Automation Testing Framework built using **Python, Pytest, Requests, Allure Reports, and BDD (pytest-bdd)**.
This project demonstrates real-world API testing practices including data-driven testing, logging, reporting, and CI-ready structure.

---

## 📌 Features

* ✅ REST API Testing using Python & Requests
* ✅ Pytest Framework with Fixtures
* ✅ Data-Driven Testing (JSON-based)
* ✅ BDD Support using pytest-bdd
* ✅ Allure Reporting with Auto Attachments
* ✅ Centralized API Client (Class-based Design)
* ✅ Logging using Loguru
* ✅ Multiple Environment Support (JSONPlaceholder & ReqRes)
* ✅ Clean & Scalable Project Structure
* ✅ Ready for CI/CD Integration

---

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** Pytest
* **API Library:** Requests
* **Reporting:** Allure
* **BDD:** pytest-bdd
* **Logging:** Loguru
* **Version Control:** Git & GitHub

---

## 📂 Project Structure

```
API_Automation_Project/
│
├── utils/
│   ├── api_client.py        # Class-based API client
│   ├── config.py            # Base URLs & config
│   ├── logger.py            # Loguru logging setup
│   ├── data_reader.py       # JSON data reader
│
├── tests/
│   ├── test_get_users.py
│   ├── test_create_post.py
│   ├── test_posts_api.py
│   ├── step_definitions/    # BDD step definitions
│   ├── features/            # BDD feature files
│
├── data/
│   ├── post_test_data.json
│
├── logs/
│   ├── api_tests.log
│
├── allure-results/
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run the Project

### 1️⃣ Clone Repository

```
git clone https://github.com/jingadegopinathrao/api-automation-framework
cd API-Automation-Project
```

---

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 3️⃣ Run Tests

```
pytest
```

---

### 4️⃣ Generate Allure Report

```
pytest --alluredir=allure-results
allure serve allure-results
```

---

## 📊 Allure Report Features

* Request URL
* Request Payload
* Response Status
* Response Body
* Step-wise execution
* Test categorization (Smoke, Regression)

---

## 🧪 Sample Test Types

* ✅ GET API Testing
* ✅ POST API Testing
* ✅ Data-Driven Tests
* ✅ BDD Test (Login/Register)

---

## 🔥 Key Highlights

* Designed using **Object-Oriented Programming (OOP)**
* Centralized API handling for better maintainability
* Automatic logging and reporting for debugging
* Clean separation of test logic and API logic
* Industry-level framework design

---

## 📌 Future Enhancements

* 🔄 Add Retry Mechanism
* 🔐 Add Authentication Handling (Token-based)
* 🌍 Environment-based execution (dev/qa/prod)
* ⚙️ CI/CD Integration using GitHub Actions
* 📈 Advanced reporting dashboard

---

## 👨‍💻 Author

**Gopi Nath**
API Automation Tester | Python | Pytest

---

## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

---
