def calculate_final_score(
    semantic_score,
    resume_skills,
    jd_skills,
    retrieved_chunks
):

    if len(jd_skills) == 0:
        skill_score = 0

    else:
        skill_score = (
            len(
                set(resume_skills)
                &
                set(jd_skills)
            )
            /
            len(jd_skills)
        ) * 100

    retrieval_score = min(
        len(retrieved_chunks) * 30,
        100
    )

    final_score = (
        0.4 * semantic_score
        +
        0.3 * skill_score
        +
        0.3 * retrieval_score
    )

    return round(
        final_score,
        2
    )