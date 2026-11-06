from orchestrator import Orchestrator


def main():

    goal = "Prepare an outreach brief for company Acme"

    orchestrator = Orchestrator()

    result = orchestrator.run(goal)

    print("\n")
    print("=" * 60)
    print("FINAL OUTREACH BRIEF")
    print("=" * 60)

    print(f"\nCompany: {result['company']}")

    print("\nResearch:")
    print(result["research"]["research_summary"])

    print("\nDraft:")
    print(result["draft"]["draft"])

    print("\nReview:")
    print(result["review"]["review"])

    print("\nApproved:")
    print(result["review"]["approved"])

    print("\n")
    print("=" * 60)
    print("MULTI-AGENT vs SINGLE-AGENT")
    print("=" * 60)

    print(
        "1. Multi-agent systems are better when a task contains "
        "different specialized activities."
    )

    print(
        "2. Different agents can use different tools and system "
        "prompts for their specific responsibilities."
    )

    print(
        "3. Context isolation reduces unnecessary information "
        "being passed between agents."
    )

    print(
        "4. Multi-agent workflows can improve reliability by "
        "separating research, generation, and review."
    )


if __name__ == "__main__":
    main()