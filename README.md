# Loan Qualifier API

A **Flask-based API** that evaluates whether a business qualifies for a loan based on requested loan amount, annual revenue, and credit score.  

This API automates loan eligibility decisions and provides actionable recommendations for applicants.

---

## Features

- Evaluates loan eligibility based on:
  - Credit score
  - Annual business revenue
  - Loan-to-revenue ratio
- Returns eligibility status:
  - `Eligible to apply`
  - `Wait 6 months and try again` (if credit score < 650 or revenue too low)
- Suggests a **recommended loan amount** if the requested amount exceeds 10% of revenue
- Easy to integrate with web applications or other APIs

---

## Requirements

- Python 3.8+
- Flask

Install dependencies with:

```bash
pip install Flask

```

## Usage
1. Run the API: \
python loan_qualifier_api.py


2. Send a POST request to /evaluate: \
ex: {
  "name": "Alicia Patel",
  "loan_amount": 40000,
  "annual_revenue": 300000,
  "credit_score": 700
}


3. Response
- Eligible \
{
  "eligible": true,
  "reason": "Eligible to apply",
  "applicant": "Alicia Patel"
}

- If the credit score is below 650: \
{
  "eligible": true,
  "reason": "Eligible to apply",
  "applicant": "Alicia Patel"
}

- If the loan amount is too high relative to revenue:\
{
  "eligible": false,
  "reason": "Loan amount exceeds 10% of revenue. Suggested maximum: $30,000.00",
  "applicant": "Alicia Patel"
}