import asyncio


async def company_news_agent(company):
    await asyncio.sleep(3.0)

    return {
        "source": "company_news",
        "status": "success",
        "data": (
            f"{company} recently announced expansion of its "
            "cloud technology business."
        ),
    }


async def products_agent(company):
    await asyncio.sleep(2.5)

    return {
        "source": "products",
        "status": "success",
        "data": (
            f"{company} offers cloud infrastructure, "
            "enterprise software, and analytics products."
        ),
    }


async def leadership_agent(company, fail=False):
    await asyncio.sleep(3.2)

    if fail:
        raise Exception("Leadership service unavailable")

    return {
        "source": "leadership",
        "status": "success",
        "data": (
            f"{company}'s leadership team is focused on "
            "cloud growth and enterprise customers."
        ),
    }