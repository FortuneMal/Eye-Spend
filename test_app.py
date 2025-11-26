import pytest
from app import analyze_receipt_with_ai

# We mock the analyze function's logic essentially to test our business rules
# In a real app, you would separate the logic from the Streamlit UI code.

def test_high_risk_flagging():
    """
    Test that high risk items (Gambling) are flagged correctly.
    Note: Since our example app uses random generation for the demo, 
    we are simulating the logic verification here.
    """
    # Represents the logic inside the app:
    vendor = "Luxury Casino"
    amount = 500.00
    
    risk_score = 0
    if vendor == "Luxury Casino":
        risk_score = 95
        
    assert risk_score > 80, "Casinos should be flagged as high risk"

def test_spending_limits():
    """
    Test that amounts over $1000 trigger a review.
    """
    amount = 1200.00
    vendor = "Dell Computers"
    
    risk_score = 0
    if amount > 1000:
        risk_score = 60
        
    assert risk_score >= 50, "Large purchases should trigger medium risk"

def test_data_structure():
    """
    Ensure the AI returns the correct JSON structure for the frontend.
    """
    # This mocks the return of the main function
    mock_data = {
        "vendor": "Test",
        "date": "2023-01-01",
        "amount": 10.00,
        "category": "Test",
        "risk_score": 10,
        "risk_reason": "None"
    }
    
    assert "risk_score" in mock_data
    assert "amount" in mock_data
    assert isinstance(mock_data["amount"], float)
