def calculate_decision():
    print("=== Sim Companies Executive Decision Calculator ===\n")

    # --- INPUTS ---
    to_employees = float(input("Current 'To Employees' cost per day: "))
    base_ao = float(input("Base Administration Overhead % (before executive reductions): "))
    exec_reduction_before = float(input("Total Executive Reduction % (BEFORE executive leaves): "))
    exec_reduction_after = float(input("Total Executive Reduction % (AFTER executive leaves): "))

    current_exec_salary = float(input("Current executive salary per day: "))
    exec_offer = float(input("Rival salary offer you must match to keep executive: "))

    training_comp = float(input("Training compensation you receive if he leaves (upfront): "))
    royalties = float(input("Royalties per day you receive if he leaves: "))

    # --- CONVERSIONS ---
    base_ao /= 100
    exec_reduction_before /= 100
    exec_reduction_after /= 100

    final_ao_before = base_ao - exec_reduction_before
    final_ao_after = base_ao - exec_reduction_after

    # --- BASE WAGE CALCULATION ---
    base_wages = to_employees / (1 + final_ao_before)

    # --- SCENARIO A: KEEP EXEC (MATCH OFFER) ---
    wages_keep = base_wages - current_exec_salary + exec_offer
    ao_cost_keep = wages_keep * final_ao_before
    total_daily_keep = wages_keep + ao_cost_keep  # No royalties, no upfront

    # --- SCENARIO B: LET EXEC GO ---
    wages_leave = base_wages - current_exec_salary
    ao_cost_leave = wages_leave * final_ao_after
    total_daily_leave = wages_leave + ao_cost_leave - royalties
    upfront_gain = training_comp

    # --- OUTPUT ---
    print("\n===== RESULTS =====")
    print(f"Base wages (calculated): ${base_wages:,.2f}/day\n")

    print("---- If You KEEP the Executive ----")
    print(f"New wage bill:        ${wages_keep:,.2f}/day")
    print(f"Admin overhead cost:  ${ao_cost_keep:,.2f}/day")
    print(f"TOTAL daily cost:     ${total_daily_keep:,.2f}/day\n")

    print("---- If You LET the Executive GO ----")
    print(f"Wage bill without exec:   ${wages_leave:,.2f}/day")
    print(f"Admin overhead cost:      ${ao_cost_leave:,.2f}/day")
    print(f"Royalties received:       ${royalties:,.2f}/day")
    print(f"TOTAL daily cost:         ${total_daily_leave:,.2f}/day")
    print(f"UPFRONT cash received:    ${upfront_gain:,.2f}\n")

    print("===== COMPARISON =====")
    daily_diff = total_daily_keep - total_daily_leave
    print(f"Daily savings if he leaves: ${daily_diff:,.2f}/day")

    if total_daily_keep > total_daily_leave:
        print("👉 Financially BETTER to LET HIM GO.")
    elif total_daily_keep < total_daily_leave:
        print("👉 Financially BETTER to KEEP him.")
    else:
        print("Both choices cost the same daily.")

    # Break-even analysis:
    print("\n===== EXTRA ANALYSIS =====")
    print(f"If you let him go, you gain ${upfront_gain:,.2f} immediately.")
    print(f"Your long-term daily benefit of letting him go is ${daily_diff:,.2f}/day.")
    if daily_diff > 0:
        days_to_match_upfront = upfront_gain / daily_diff
        print(f"This daily advantage repays the upfront bonus in {days_to_match_upfront:,.1f} days.")
    else:
        print("There is no upfront recovery period because keeping him is cheaper or equal.")


# Run calculator
calculate_decision()