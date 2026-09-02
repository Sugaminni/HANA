from deal_profile import DealProfile

deal = DealProfile(
    deal_name="Test Multifamily Deal",
    property_name="HANA Apartments",
    property_type="Multifamily",
    city="Atlanta",
    state="GA",
    units=250,
    asking_price=42_000_000,
    occupancy_rate=0.94,
    noi=2_400_000
)

print(deal)
print()
print(deal.model_dump())