def calculate_tax(earnings):
    """
    Calculates the tax based on the given earnings, using a progressive tax system.

    Tax Brackets:
    - Earnings <= 12,000 per year: 0% tax
    - Earnings between 12,001 and 36,000 per year: 20% tax on this portion
    - Earnings > 36,000 per year: 40% tax on this portion
    """
    tax = 0

    # First bracket: Earnings up to 12,000 (0% tax)
    # If earnings fall within or below this bracket, no tax is applied.
    if earnings <= 12000:
        return 0
    # Second bracket: Earnings from 12,001 to 36,000 (20% tax on this portion)
    elif earnings <= 36000:
        # Calculate the amount of earnings that fall into this bracket
        taxable_amount_second_bracket = earnings - 12000
        # Add the tax from this bracket to the total tax
        tax += taxable_amount_second_bracket * 0.20
        return tax
    # Third bracket: Earnings greater than 36,000 (40% tax on this portion)
    else: # earnings > 36000
        # First, calculate the maximum tax from the second bracket, as it's fully utilized
        # (36000 - 12000) = 24000 is the full range of the second bracket
        tax_from_second_bracket = (36000 - 12000) * 0.20 # 24000 * 0.20 = 4800
        tax += tax_from_second_bracket

        # Calculate the amount of earnings that fall into the third bracket
        taxable_amount_third_bracket = earnings - 36000
        # Add the tax from this bracket to the total tax
        tax += taxable_amount_third_bracket * 0.40
        return tax

