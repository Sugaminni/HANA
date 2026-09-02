from typing import Optional
from pydantic import BaseModel

# Optional so HANA doesn't just guess things

class DealProfile(BaseModel):
    # Identification
    deal_name: Optional[str] = None
    property_name: Optional[str] = None
    property_type: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    market: Optional[str] = None
    submarket: Optional[str] = None

    # Property
    units: Optional[int] = None
    square_feet: Optional[float] = None
    year_built: Optional[int] = None
    occupancy_rate: Optional[float] = None

    # Transaction
    asking_price: Optional[float] = None
    price_per_unit: Optional[float] = None
    price_per_square_foot: Optional[float] = None
    cap_rate: Optional[float] = None

    # Financials
    annual_revenue: Optional[float] = None
    operating_expenses: Optional[float] = None
    noi: Optional[float] = None

    # Debt / Financing
    loan_amount: Optional[float] = None
    interest_rate: Optional[float] = None
    ltv: Optional[float] = None
    loan_term_years: Optional[int] = None

    # Sponsor
    sponsor_name: Optional[str] = None
    sponsor_equity: Optional[float] = None
    sponsor_track_record: Optional[str] = None

    # Deal Context
    investment_strategy: Optional[str] = None
    business_plan: Optional[str] = None

    # Data Quality
    missing_information: list[str] = []
    conflicting_information: list[str] = []