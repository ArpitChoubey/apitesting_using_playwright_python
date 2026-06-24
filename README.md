🚀 API Testing Automation Framework using Playwright + Python
<p align="center"> <img src="https://img.shields.io/badge/Automation-Testing-blue?style=for-the-badge" /> <img src="https://img.shields.io/badge/Playwright-Python-green?style=for-the-badge" /> <img src="https://img.shields.io/badge/API-Testing-orange?style=for-the-badge" /> <img src="https://img.shields.io/badge/Open%20Source-Learning-red?style=for-the-badge" /> </p>
🎯 Project Overview

Modern applications rely heavily on APIs. A single broken endpoint can impact multiple services, customers, and business workflows.

To strengthen API quality and demonstrate modern test automation practices, I built this API Testing Automation Framework using Playwright and Python.

This project showcases my ability to:

✅ Design scalable test automation frameworks

✅ Automate REST API validations

✅ Implement CRUD API testing

✅ Perform Authentication & Authorization testing

✅ Validate Headers, Cookies & Response Schemas

✅ Generate Dynamic Test Data using Faker

✅ Follow maintainable automation architecture

✅ Apply QA best practices used in enterprise projects

👨‍💻 About Me

I am a Senior QA Automation Engineer passionate about building reliable automation frameworks that improve software quality and accelerate delivery.

My expertise includes:

API Testing
Automation Framework Design
Playwright
Selenium
Python
Java
REST Assured
CI/CD Integration
Agile & Scrum Practices

I believe QA should be more than defect detection—it should actively contribute to product quality, faster releases, and better customer experiences.

🚀 Why This Project Matters

Many API automation projects only validate:

Status Code = 200

In real-world applications, that's not enough.

This framework validates:

Business Logic
Authentication
Response Structure
Data Integrity
Headers
Cookies
Schema Compliance
End-to-End CRUD Workflows

This approach mirrors how modern QA teams test APIs in production environments.

🏗 Framework Architecture
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
🧪 Test Scenarios Covered
🔐 Authentication Testing

Validates:

Token generation
Authentication success
Response verification
Authorization workflows
Why it matters

Authentication is the first line of defense in modern applications.

📦 CRUD API Testing
Create
Create Booking API
Dynamic payload validation
Read
Retrieve booking details
Verify response content
Update
Modify existing records
Validate updated responses
Delete
Remove records
Verify cleanup operations
Why it matters

CRUD operations represent the majority of business-critical API transactions.

🎲 Dynamic Test Data Generation

Using:

Faker

Benefits:

Unique test executions
Reduced duplicate data failures
Realistic user simulation

Example:

firstname = fake.first_name()
lastname = fake.last_name()
📄 JSON Data-Driven Testing

Supports:

Externalized test data
Multiple scenarios
Easy maintenance

Benefits:

Better scalability
Cleaner code
Faster test expansion
✅ Schema Validation

Validates:

Mandatory fields
Data types
API contracts
Response structure

Example:

{
  "firstname": "Arpit",
  "lastname": "Choubey"
}
Why it matters

A successful status code does not guarantee a valid response.

🍪 Cookie Validation

Checks:

Session cookies
Cookie attributes
Security-related values
📬 Header Validation

Validates:

Content-Type
Authorization
Cache-Control
Response Metadata
🛠 Technology Stack
Technology	Purpose
Python	Programming Language
Playwright	API Automation
Faker	Dynamic Test Data
JSON	Test Data Management
Git	Version Control
GitHub	Repository Hosting
🚀 How To Run
Clone Repository
git clone https://github.com/ArpitChoubey/apitesting_using_playwright_python.git
Navigate
cd apitesting_using_playwright_python
Install Dependencies
pip install -r requirements.txt
Execute Tests
pytest

Or run individual test files:

pytest Test_Auth.py
💼 Skills Demonstrated

This repository highlights practical experience in:

Test Automation
API Automation
Framework Design
Test Strategy
Programming
Python
Object-Oriented Programming
API Testing
REST APIs
CRUD Operations
Authentication
Quality Engineering
Validation Strategies
Test Data Management
Automation Best Practices
DevOps Awareness
Git
Version Control
Continuous Testing
📈 Future Enhancements

Planned improvements:

Pytest Framework Integration
Allure Reporting
HTML Reports
CI/CD Pipeline Integration
Jenkins Integration
GitHub Actions
Docker Support
Environment Management
Database Validation
Parallel Execution
API Mocking
🌟 What Recruiters, Hiring Managers & QA Leaders Can Expect

This project demonstrates my ability to:

✔ Build maintainable automation frameworks

✔ Apply real-world API testing techniques

✔ Write clean, reusable Python code

✔ Think beyond simple test execution

✔ Focus on software quality engineering

✔ Design scalable automation solutions

✔ Work with modern QA tooling

✔ Contribute effectively in Agile environments

🤝 Let's Connect

I'm always open to discussing:

QA Automation Opportunities
SDET Roles
API Testing Challenges
Automation Framework Design
Software Quality Engineering
LinkedIn

https://www.linkedin.com/in/arpitchoubey/

GitHub

https://github.com/ArpitChoubey

⭐ Support

If you found this project useful:

⭐ Star the repository

🍴 Fork the project

💬 Share feedback

🤝 Connect with me

📌 Key Takeaway

"Quality is not achieved by testing alone. It is achieved by designing automation that continuously validates business value."

🏷 Tags

Playwright Python API Testing Automation Testing QA Automation SDET REST API Software Testing Test Automation Quality Engineering Framework Design Automation Framework Continuous Testing GitHub Portfolio
