from sub_agents import (
    ResearchAgent,
    DraftAgent,
    ReviewAgent,
)


class Orchestrator:

    def __init__(self):
        self.research_agent = ResearchAgent()
        self.draft_agent = DraftAgent()
        self.review_agent = ReviewAgent()

    def create_plan(self, goal):

        return [
            {
                "step": 1,
                "task": "research",
                "description": "Research the target company",
            },
            {
                "step": 2,
                "task": "draft",
                "description": "Create an outreach brief",
            },
            {
                "step": 3,
                "task": "review",
                "description": "Review and approve the brief",
            },
        ]

    def run(self, goal):

        print("=" * 60)
        print("ORCHESTRATOR")
        print("=" * 60)

        print(f"Goal: {goal}")

        # Create plan
        plan = self.create_plan(goal)

        print("\nPLAN")
        for step in plan:
            print(
                f"{step['step']}. "
                f"{step['task']} - "
                f"{step['description']}"
            )

        # Extract company from goal
        company = goal.replace(
            "Prepare an outreach brief for company ",
            ""
        ).strip()

        # --------------------------------------------------
        # STEP 1 - RESEARCH
        # Only company is passed.
        # Full conversation/history is NOT passed.
        # --------------------------------------------------

        print("\n--- STEP 1: RESEARCH ---")

        research_context = {
            "company": company
        }

        research_output = self.research_agent.run(
            research_context["company"]
        )

        print("Research output:")
        print(research_output)

        # --------------------------------------------------
        # STEP 2 - DRAFT
        # Only required research context is passed.
        # --------------------------------------------------

        print("\n--- STEP 2: DRAFT ---")

        draft_context = {
            "company": research_output["company"],
            "industry": research_output["industry"],
            "focus": research_output["focus"],
            "target_area": research_output["target_area"],
        }

        draft_output = self.draft_agent.run(
            company,
            draft_context
        )

        print("Draft output:")
        print(draft_output["draft"])

        # --------------------------------------------------
        # STEP 3 - REVIEW
        # Only the draft is passed.
        # Research output and full history are NOT passed.
        # --------------------------------------------------

        print("\n--- STEP 3: REVIEW ---")

        review_context = {
            "draft": draft_output["draft"]
        }

        review_output = self.review_agent.run(
            review_context
        )

        print("Review output:")
        print(review_output["review"])

        # --------------------------------------------------
        # FINAL BRIEF
        # --------------------------------------------------

        final_brief = {
            "company": company,
            "research": research_output,
            "draft": draft_output,
            "review": review_output,
        }

        return final_brief