def calculate_score(row):
    score = 0

    # Role Fit
    if "Director" in row["Title"] or "Head" in row["Title"]:
        score += 30

    # Company Funding
    if row["Funding"] in ["Series A", "Series B"]:
        score += 20

    # Technographic
    if row["Tech_Used"] == "Yes":
        score += 15

    # Scientific Intent
    if row["Recent_Paper"] == "Yes":
        score += 40

    return min(score, 100)
