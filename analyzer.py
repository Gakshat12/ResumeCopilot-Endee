def generate_feedback(score, missing_skills):

    feedback = []

    if score >= 80:
        feedback.append(
            "Strong match for the role."
        )

    elif score >= 60:
        feedback.append(
            "Moderate match. Improve a few skills."
        )

    else:
        feedback.append(
            "Low match. Resume needs significant improvements."
        )

    if missing_skills:

        feedback.append(
            "Missing Skills:"
        )

        for skill in missing_skills:
            feedback.append(
                f"- {skill}"
            )

    return feedback