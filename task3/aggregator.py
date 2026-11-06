async def aggregate_results(company, results):

    successful_sources = []
    missing_sources = []

    news = ""
    products = ""
    leadership = ""

    for result in results:

        if result["status"] == "success":

            successful_sources.append(result["source"])

            if result["source"] == "company_news":
                news = result["data"]

            elif result["source"] == "products":
                products = result["data"]

            elif result["source"] == "leadership":
                leadership = result["data"]

        else:
            missing_sources.append(result["source"])

    summary = f"""
OUTREACH SUMMARY - {company}

Company News:
{news if news else "Missing"}

Products:
{products if products else "Missing"}

Leadership:
{leadership if leadership else "Missing"}

Sources available:
{len(successful_sources)}/3
"""

    if missing_sources:
        summary += (
            "\nMissing information: "
            + ", ".join(missing_sources)
        )

    return summary.strip()