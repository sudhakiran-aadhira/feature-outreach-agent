from specialist_agents import (
    ResearchAgent,
    WritingAgent,
    DataLookupAgent,
    FallbackAgent,
)


class Router:

    def __init__(self):
        self.research_agent = ResearchAgent()
        self.writing_agent = WritingAgent()
        self.data_lookup_agent = DataLookupAgent()
        self.fallback_agent = FallbackAgent()

    def classify(self, request):

        text = request.lower()

        # Writing classification
        writing_keywords = [
            "write",
            "draft",
            "email",
            "message",
            "rewrite",
            "compose",
            "follow-up",
        ]

        if any(keyword in text for keyword in writing_keywords):
            return "writing"

        # Data lookup classification
        data_keywords = [
            "how many",
            "count",
            "number of",
            "open tickets",
            "employee data",
            "customer data",
            "order data",
            "lookup",
            "balance",
        ]

        if any(keyword in text for keyword in data_keywords):
            return "data-lookup"

        # Research classification
        research_keywords = [
            "news",
            "research",
            "search",
            "find information",
            "latest",
            "information about",
            "investigate",
        ]

        if any(keyword in text for keyword in research_keywords):
            return "research"

        return "unknown"

    def route(self, request):

        category = self.classify(request)

        if category == "research":
            agent = self.research_agent

        elif category == "writing":
            agent = self.writing_agent

        elif category == "data-lookup":
            agent = self.data_lookup_agent

        else:
            agent = self.fallback_agent

        result = agent.run(request)

        return category, result