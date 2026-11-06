from tools import (
    research_tool,
    writing_tool,
    data_lookup_tool,
    fallback_tool,
)


class ResearchAgent:
    name = "research"

    system_prompt = """
    You are a research specialist.
    Handle news, research, searches, and information requests.
    """

    def run(self, request):
        result = research_tool(request)
        return result


class WritingAgent:
    name = "writing"

    system_prompt = """
    You are a writing specialist.
    Handle emails, messages, drafting, rewriting, and professional writing.
    """

    def run(self, request):
        result = writing_tool(request)
        return result


class DataLookupAgent:
    name = "data-lookup"

    system_prompt = """
    You are a data-lookup specialist.
    Handle questions requiring business, customer, employee,
    ticket, order, or other structured data.
    """

    def run(self, request):
        result = data_lookup_tool(request)
        return result


class FallbackAgent:
    name = "fallback"

    system_prompt = """
    You are a fallback agent.
    Handle requests that cannot confidently be classified
    as research, writing, or data-lookup.
    """

    def run(self, request):
        return fallback_tool(request)