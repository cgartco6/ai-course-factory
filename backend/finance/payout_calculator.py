def calculate_payout(total):
    return {
        "owner_fnb_35": total * 0.35,
        "african_bank_15": total * 0.15,
        "ai_fnb_20": total * 0.20,
        "reserve_fnb_20": total * 0.20,
        "retained_10": total * 0.10
    }
