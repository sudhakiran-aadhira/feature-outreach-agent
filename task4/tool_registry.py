from tools.mock_web_search import search_company


TOOL_REGISTRY = {
    "search_company": {
        "function": search_company,
        "risk_level": "READ",
        "description": (
            "Search mock company information including "
            "news, products and pain points."
        ),
    }
}


def execute_tool(tool_name, input_data):

    if tool_name not in TOOL_REGISTRY:
        raise ValueError(
            f"Unknown tool: {tool_name}"
        )

    tool = TOOL_REGISTRY[tool_name]

    print(
        f"Executing tool: {tool_name} "
        f"| Risk: {tool['risk_level']}"
    )

    return tool["function"](input_data)