"""
loan_qualifier_api.py
-----------------
Business Loan Qualification API

Evaluates loan eligibility based on:
  - Loan amount requested
  - Annual business revenue
  - Credit score

Alicia Patel — Python Loan Qualifier API
"""

from dataclasses import dataclass
from flask import Flask, request, jsonify


@dataclass
class Applicant:
    name: str
    loan_amount: float
    annual_revenue: float
    credit_score: int


# Decision Function
def check_eligibility(applicant: Applicant) -> dict:
    # Credit Check
    if applicant.credit_score < 650:
        return {
            "eligible": False,
            "reason": "Credit score below minimum 650. Wait 6 months and try again."
        }

    # Minimum Revenue
    if applicant.annual_revenue < 50_000:
        return {
            "eligible": False,
            "reason": "Annual revenue below $50,000. Wait 6 months and try again."
        }

    # Loan-to-revenue check
    max_loan = applicant.annual_revenue * 0.10

    if applicant.loan_amount <= max_loan:
        return {
            "eligible": True,
            "reason": "Eligible to apply."
        }
    else:
        return {
            "eligible": False,
            "reason": f"Loan amount too high. Based on your revenue, an eligible loan amount is ${max_loan:,.2f}."
        }


# Flask app
app = Flask(__name__)


@app.route("/evaluate", methods=["POST"])
def evaluate_loan():
    data = request.get_json()

    # Validate input
    try:
        applicant = Applicant(
            name=data["name"],
            loan_amount=float(data["loan_amount"]),
            annual_revenue=float(data["annual_revenue"]),
            credit_score=int(data["credit_score"])
        )
    except (KeyError, ValueError, TypeError):
        return jsonify({"error": "Invalid input. Provide name, loan_amount, annual_revenue, credit_score"}), 400

    result = check_eligibility(applicant)
    result["applicant"] = applicant.name
    return jsonify(result), 200


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
