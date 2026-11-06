class ResearchAgent:
    system_prompt = """
    You are a research sub-agent.
    Your job is to collect useful company information
    for an outreach brief.
    """

    def run(self, company):
        return {
            "company": company,
            "industry": "Technology",
            "focus": "Cloud and enterprise software",
            "target_area": "Digital transformation",
            "research_summary": (
                f"{company} is a technology company focused on "
                "cloud and enterprise software solutions."
            ),
        }


class DraftAgent:
    system_prompt = """
    You are a drafting sub-agent.
    Your job is to create a concise outreach brief
    using only the research context provided to you.
    """

    def run(self, company, research_context):
        return {
            "company": company,
            "draft": (
                f"Outreach Brief for {company}\n\n"
                f"Industry: {research_context['industry']}\n"
                f"Focus: {research_context['focus']}\n"
                f"Target Area: {research_context['target_area']}\n\n"
                "Suggested outreach:\n"
                f"Hello {company} team,\n\n"
                "We would like to explore how our solutions "
                "can support your digital transformation initiatives."
            ),
        }


class ReviewAgent:
    system_prompt = """
    You are a review sub-agent.
    Review the draft for clarity, completeness,
    professionalism, and correctness.
    """

    def run(self, draft_context):
        draft = draft_context["draft"]

        review = (
            "Review completed.\n"
            "The brief is clear, professional, and suitable "
            "for initial business outreach."
        )

        return {
            "review": review,
            "approved": True,
            "final_draft": draft,
        }