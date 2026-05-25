# ReqRes API Test Framework
> REST API automation suite built with Python · Pytest · Requests

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pytest](https://img.shields.io/badge/Pytest-8.x-green)
![Tests](https://img.shields.io/badge/Tests-10%20Passing-brightgreen)
![API](https://img.shields.io/badge/API-ReqRes.in-orange)
![CI](https://github.com/Aferuza/reqres.api-test-framework-/actions/workflows/test.yml/badge.svg)

---

## 📌 Overview

This framework automates REST API testing for [ReqRes.in](https://reqres.in) —
a real, hosted API used to validate professional test automation frameworks.

Built as a portfolio project demonstrating:
- Structured Pytest test suite with shared fixtures
- Full CRUD coverage across REST endpoints
- Negative and edge case testing
- Clean, maintainable Python test code

---

## ✅ Test Coverage — 10 Tests

| # | Test | Method | Endpoint | Type |
|---|------|--------|----------|------|
| 1 | `test_list_users_pagination` | GET | `/users?page=2` | Happy path |
| 2 | `test_single_user_found` | GET | `/users/2` | Schema validation |
| 3 | `test_single_user_not_found` | GET | `/users/23` | Negative — 404 |
| 4 | `test_list_resource_colors` | GET | `/unknown` | Schema validation |
| 5 | `test_create_user_successful` | POST | `/users` | Happy path |
| 6 | `test_update_user_via_put` | PUT | `/users/2` | Full update |
| 7 | `test_update_user_via_patch` | PATCH | `/users/2` | Partial update |
| 8 | `test_delete_user_successful` | DELETE | `/users/2` | REST spec — 204 |
| 9 | `test_register_user_successful` | POST | `/register` | Auth — token |
| 10 | `test_login_user_missing_password` | POST | `/login` | Negative — 400 |

---

## 📁 Project Structure

```
reqres.api-test-framework/
│
├── config.py            # Base URL, timeout, token config
├── conftest.py          # Shared fixtures — api_client session
├── test_reqres.py       # All 10 test cases
├── requirements.txt     # Pinned dependencies
└── README.md
```

---

## 🛠️ Tech Stack

| Tool | Version | Purpose |
|------|---------|---------|
| Python | 3.11 | Primary language |
| Pytest | 8.x | Test framework and runner |
| Requests | 2.31 | HTTP client |
| pytest-html | 4.x | HTML test reports |

---

## ⚡ Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/Aferuza/reqres.api-test-framework-.git
cd reqres.api-test-framework-
```

### 2. Create and activate virtual environment
```bash
python3 -m venv venv
source venv/bin/activate       # Mac/Linux
# venv\Scripts\activate        # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run all tests
```bash
pytest -v
```

### 5. Run with HTML report
```bash
pytest -v --html=report.html --self-contained-html
open report.html
```

---

## 🧪 What Each Test Validates

**Test 1 — List Users Pagination**
Confirms the `/users` endpoint returns paginated data with correct
page number, non-empty data array, and valid structure.

**Test 2 — Single User Found**
Validates structural data integrity — correct user ID returned,
email field present, first_name matches expected value.

**Test 3 — Single User Not Found**
Negative path — confirms 404 response and clean empty JSON body
`{}` for a non-existent user ID (23).

**Test 4 — List Resource Colors**
Validates the `/unknown` resource endpoint returns correct schema
including `pantone_value` and `color` fields in first data item.

**Test 5 — Create User**
POST mutation test — confirms 201 status, name and job persisted
correctly, `id` and `createdAt` fields present in response.

**Test 6 — Update User via PUT**
Full update validation — confirms job field updated to new value,
`updatedAt` timestamp present in response.

**Test 7 — Update User via PATCH**
Incremental update — confirms single field mutation via PATCH
returns 200 with updated job value.

**Test 8 — Delete User**
REST spec compliance — confirms DELETE returns 204 No Content
with empty response body as per HTTP specification.

**Test 9 — Register User**
Auth flow — confirms successful registration returns both `id`
and `token` in response payload.

**Test 10 — Login Missing Password**
Negative auth test — confirms 400 Bad Request returned with
`"Missing password"` error message when password field omitted.

---

## 📊 Sample Output

```
collected 10 items

test_reqres.py::test_list_users_pagination        PASSED
test_reqres.py::test_single_user_found            PASSED
test_reqres.py::test_single_user_not_found        PASSED
test_reqres.py::test_list_resource_colors         PASSED
test_reqres.py::test_create_user_successful       PASSED
test_reqres.py::test_update_user_via_put          PASSED
test_reqres.py::test_update_user_via_patch        PASSED
test_reqres.py::test_delete_user_successful       PASSED
test_reqres.py::test_register_user_successful     PASSED
test_reqres.py::test_login_user_missing_password  PASSED

========================= 10 passed in 3.09s seconds ==========================
```

---

## ⚙️ CI/CD — GitHub Actions

Tests run automatically on every push and pull request via GitHub Actions.

```yaml
name: ReqRes API Test Suite

on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]
  schedule:
    - cron: '0 8 * * *'

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Set up Python 3.11
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Create artifacts directory
        run: mkdir -p artifacts

      - name: Run test suite
        run: |
          pytest test_reqres.py -v \
            --html=artifacts/report.html \
            --self-contained-html \
            --junitxml=artifacts/results.xml

      - name: Upload test report
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: test-report
          path: artifacts/
          retention-days: 30
```

---

## 🗺️ Roadmap — Coming Next

- [ ] Parametrized tests for multiple user IDs and status codes
- [ ] Response time / performance threshold validation
- [ ] Extended edge case coverage (boundary values, special characters)
- [x] GitHub Actions CI/CD — auto-run on every push ✅
- [ ] Allure report integration

---

## 👤 Author

**Aferuza**
QA Automation Engineer | 6+ years experience
Python · Pytest · REST API Testing · CI/CD

- QA Engineer — Android Auto Infotainment (Google via Virtusa)
- Available for QA automation contracts on Upwork
- [GitHub](https://github.com/Aferuza) | [LinkedIn](https://linkedin.com/in/feruza-askar)

---