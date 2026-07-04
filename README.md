# 🚀 API Testing Automation Framework using Playwright & Python

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Playwright](https://img.shields.io/badge/Playwright-API%20Testing-45ba4b?style=for-the-badge&logo=playwright)
![Pytest](https://img.shields.io/badge/Pytest-Automation-green?style=for-the-badge&logo=pytest)
![REST API](https://img.shields.io/badge/REST-API-orange?style=for-the-badge)
![JSON](https://img.shields.io/badge/JSON-Validation-yellow?style=for-the-badge)
![Faker](https://img.shields.io/badge/Faker-Test%20Data-purple?style=for-the-badge)

</p>

---

# 📌 Project Overview

Modern applications rely heavily on REST APIs to power business-critical workflows.

This repository demonstrates a **scalable API Automation Framework** built using **Playwright with Python**, showcasing practical automation techniques used in enterprise software testing.

The framework goes beyond simple status code validation by covering authentication, CRUD operations, schema validation, cookies, headers, dynamic test data generation, and maintainable automation practices.

Whether you're a QA Engineer, SDET, Automation Tester, or Hiring Manager evaluating automation skills, this repository highlights real-world API testing capabilities.

---

# 🎯 Project Objectives

This framework demonstrates how to:

- ✅ Design scalable API automation solutions
- ✅ Automate REST API validation using Playwright
- ✅ Validate business-critical CRUD workflows
- ✅ Implement Authentication & Authorization testing
- ✅ Perform Schema Validation
- ✅ Verify Headers & Cookies
- ✅ Generate dynamic test data using Faker
- ✅ Build reusable and maintainable test scripts
- ✅ Follow automation best practices used in enterprise projects

---

# 🏗 Framework Structure

```
apitesting_using_playwright_python
│
├── APITesting
│   ├── Test_Auth.py
│   ├── Test_Booking_crude2e.py
│   ├── Test_Cookies.py
│   ├── Test_CreateBooking.py
│   ├── Test_CreateBookingusingfaker.py
│   ├── Test_CreateBookingusingjson.py
│   ├── Test_Schemavalidation.py
│   ├── Test_headers.py
│
├── TestData
│
├── Test_Codegen.py
├── Test_ShadowDom.py
│
└── README.md
```

---

# 🚀 Framework Highlights

## 🔐 Authentication Testing

Implemented authentication workflows including:

- Token Generation
- Authorization Validation
- Secure API Access
- Response Verification

---

## 📦 CRUD API Testing

Complete end-to-end API validation including:

- Create Resource
- Read Resource
- Update Resource
- Delete Resource

Business workflow validation ensures APIs behave correctly across the entire lifecycle.

---

## 📄 JSON Data-Driven Testing

Supports external JSON payloads for:

- Multiple test scenarios
- Easy maintenance
- Better scalability
- Reusable test data

---

## 🎲 Dynamic Test Data

Using the **Faker** library, the framework generates realistic test data dynamically.

Example:

```python
firstname = fake.first_name()
lastname = fake.last_name()
```

Benefits include:

- Reduced duplicate data failures
- More realistic test execution
- Improved test reliability

---

## ✅ JSON Schema Validation

Response validation includes:

- Mandatory field verification
- Data type validation
- API contract validation
- Response structure verification

Ensures API responses remain consistent even when HTTP status codes indicate success.

---

## 🍪 Cookie Validation

Framework validates:

- Session Cookies
- Cookie Attributes
- Security Values
- Cookie Availability

---

## 📬 Header Validation

Verifies response headers including:

- Content-Type
- Authorization
- Cache-Control
- Response Metadata

---

# 💻 Technology Stack

| Technology | Purpose |
|------------|----------|
| Python | Programming Language |
| Playwright | API Automation |
| Pytest | Test Execution |
| Faker | Dynamic Test Data |
| JSON | Test Data Management |
| Git | Version Control |
| GitHub | Repository Hosting |

---

# 🧪 Test Coverage

### Authentication

- Token Validation
- Login Authentication
- Authorization

### CRUD Operations

- Create Booking
- Retrieve Booking
- Update Booking
- Delete Booking

### Validation

- Headers
- Cookies
- JSON Schema
- Response Body
- Status Codes

### Test Data

- JSON Files
- Faker Library
- Dynamic Payloads

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/ArpitChoubey/apitesting_using_playwright_python.git
```

## Navigate

```bash
cd apitesting_using_playwright_python
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Execute All Tests

```bash
pytest
```

## Execute Individual Test

```bash
pytest APITesting/Test_Auth.py
```

---

# 📈 Skills Demonstrated

### API Automation

- REST API Testing
- CRUD Operations
- Authentication
- Authorization
- Schema Validation

### Programming

- Python
- Object-Oriented Programming
- Modular Framework Design
- Reusable Components

### Quality Engineering

- API Validation
- Test Strategy
- Automation Best Practices
- Data-Driven Testing

### Software Engineering

- Git
- Version Control
- Clean Code
- Maintainable Test Design

---

# 🌟 Why This Repository Matters

Unlike basic API automation examples that only verify status codes, this framework demonstrates how enterprise QA teams validate business-critical APIs.

It showcases:

- Real-world automation scenarios
- Maintainable framework design
- Practical Python programming
- API quality engineering
- Scalable automation architecture

---

# 🚀 Future Enhancements

Planned improvements include:

- Allure Reports
- HTML Reporting
- GitHub Actions
- Jenkins CI/CD
- Docker Support
- Parallel Test Execution
- Environment Configuration
- API Mocking
- Database Validation

---

# 💼 Recruiter Snapshot

### This repository demonstrates practical experience with:

- ✅ Python
- ✅ Playwright
- ✅ API Automation
- ✅ REST API Testing
- ✅ CRUD Validation
- ✅ Authentication Testing
- ✅ JSON Schema Validation
- ✅ Data-Driven Testing
- ✅ Dynamic Test Data
- ✅ Automation Framework Design
- ✅ Quality Engineering Practices

---

# 🎯 Ideal Audience

This repository is designed for:

- QA Automation Engineers
- Software Development Engineers in Test (SDETs)
- API Automation Engineers
- Manual Testers transitioning to Automation
- Developers learning API testing
- Hiring Managers evaluating automation portfolios

---

# 👨‍💻 About Me

## Arpit Choubey

**Senior QA Automation Engineer | SDET | API Automation | Playwright | Python | Selenium | REST Assured | Java**

I enjoy building scalable automation frameworks, improving software quality, and sharing practical learning through open-source projects.

---

# 🌐 Connect With Me

### GitHub

https://github.com/ArpitChoubey

### LinkedIn

https://www.linkedin.com/in/arpitchoubey/

### Medium

https://medium.com/@ArpitChoubey9

---

# ⭐ Support

If you found this repository useful:

⭐ Star this repository

🍴 Fork the project

💬 Share feedback

🤝 Connect with me

Your support encourages me to continue building practical automation projects for the QA community.

---

# 💡 Key Takeaway

> **"Effective API automation is more than checking status codes—it's about validating business workflows, ensuring data integrity, and building confidence in every release."**
