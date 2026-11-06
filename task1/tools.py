def research_tool(request):
    return f"Researching: {request}"


def writing_tool(request):
    return f"Writing content for: {request}"


def data_lookup_tool(request):
    return f"Looking up data for: {request}"


def fallback_tool(request):
    return f"Unable to identify a specialist for: {request}"