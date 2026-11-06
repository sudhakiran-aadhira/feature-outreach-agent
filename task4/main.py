from prospect_loader import load_prospects
from tool_registry import (
    TOOL_REGISTRY,
    execute_tool,
)


def main():

    print("=" * 60)
    print("MULTI-STEP SALES OUTREACH AGENT")
    print("WEEK 6 - DAY 3 - TASK 4")
    print("=" * 60)

    # ----------------------------------------
    # Load prospects
    # ----------------------------------------

    prospects = load_prospects(
        "data/prospects.csv"
    )

    print(
        f"\nValid prospect count: {len(prospects)}"
    )

    # ----------------------------------------
    # Show registered tools
    # ----------------------------------------

    print("\nRegistered Tools:")

    for name, tool in TOOL_REGISTRY.items():

        print(
            f"- {name} "
            f"(Risk: {tool['risk_level']})"
        )

    # ----------------------------------------
    # Test mock web search
    # ----------------------------------------

    print("\nTesting search_company('Acme')")

    result = execute_tool(
        "search_company",
        "Acme"
    )

    print("\nsearch_company('Acme') ->")
    print(result)


if __name__ == "__main__":
    main()