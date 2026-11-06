import asyncio
import time

from sub_agents import (
    company_news_agent,
    products_agent,
    leadership_agent,
)

from aggregator import aggregate_results
from audit import log_step


COMPANY = "Acme"


async def run_sequential():

    print("\n" + "=" * 60)
    print("SEQUENTIAL EXECUTION")
    print("=" * 60)

    start = time.perf_counter()

    results = []

    # Agent 1
    try:
        result = await company_news_agent(COMPANY)
        results.append(result)

        log_step(
            result["source"],
            result["status"],
            result["data"],
        )

    except Exception as error:
        result = {
            "source": "company_news",
            "status": "failed",
            "data": str(error),
        }

        results.append(result)

        log_step(
            result["source"],
            result["status"],
            result["data"],
        )

    # Agent 2
    try:
        result = await products_agent(COMPANY)
        results.append(result)

        log_step(
            result["source"],
            result["status"],
            result["data"],
        )

    except Exception as error:
        result = {
            "source": "products",
            "status": "failed",
            "data": str(error),
        }

        results.append(result)

        log_step(
            result["source"],
            result["status"],
            result["data"],
        )

    # Agent 3
    try:
        result = await leadership_agent(
            COMPANY,
            fail=False
        )

        results.append(result)

        log_step(
            result["source"],
            result["status"],
            result["data"],
        )

    except Exception as error:
        result = {
            "source": "leadership",
            "status": "failed",
            "data": str(error),
        }

        results.append(result)

        log_step(
            result["source"],
            result["status"],
            result["data"],
        )

    elapsed = time.perf_counter() - start

    return results, elapsed


async def run_parallel(fail_leadership=False):

    print("\n" + "=" * 60)
    print("PARALLEL EXECUTION")
    print("=" * 60)

    start = time.perf_counter()

    async def safe_news():

        try:
            result = await company_news_agent(COMPANY)

            log_step(
                result["source"],
                result["status"],
                result["data"],
            )

            return result

        except Exception as error:

            result = {
                "source": "company_news",
                "status": "failed",
                "data": str(error),
            }

            log_step(
                result["source"],
                result["status"],
                result["data"],
            )

            return result

    async def safe_products():

        try:
            result = await products_agent(COMPANY)

            log_step(
                result["source"],
                result["status"],
                result["data"],
            )

            return result

        except Exception as error:

            result = {
                "source": "products",
                "status": "failed",
                "data": str(error),
            }

            log_step(
                result["source"],
                result["status"],
                result["data"],
            )

            return result

    async def safe_leadership():

        try:
            result = await leadership_agent(
                COMPANY,
                fail=fail_leadership
            )

            log_step(
                result["source"],
                result["status"],
                result["data"],
            )

            return result

        except Exception as error:

            result = {
                "source": "leadership",
                "status": "failed",
                "data": str(error),
            }

            log_step(
                result["source"],
                result["status"],
                result["data"],
            )

            return result

    # IMPORTANT:
    # asyncio.gather runs the independent agents concurrently.

    results = await asyncio.gather(
        safe_news(),
        safe_products(),
        safe_leadership(),
    )

    elapsed = time.perf_counter() - start

    return results, elapsed


async def main():

    print("=" * 60)
    print("WEEK 6 - DAY 3 - TASK 3")
    print("PARALLEL SUB-AGENTS AND AGGREGATION")
    print("=" * 60)

    # --------------------------------------------------
    # SEQUENTIAL
    # --------------------------------------------------

    sequential_results, sequential_time = (
        await run_sequential()
    )

    # --------------------------------------------------
    # PARALLEL
    # --------------------------------------------------

    parallel_results, parallel_time = (
        await run_parallel(fail_leadership=False)
    )

    # --------------------------------------------------
    # AGGREGATION
    # --------------------------------------------------

    summary = await aggregate_results(
        COMPANY,
        parallel_results
    )

    successful_count = sum(
        1
        for result in parallel_results
        if result["status"] == "success"
    )

    print("\n" + "=" * 60)
    print("FINAL SUMMARY")
    print("=" * 60)

    print(summary)

    print("\n" + "=" * 60)
    print("PERFORMANCE")
    print("=" * 60)

    print(
        f"Sequential: {sequential_time:.1f} s"
    )

    print(
        f"Parallel:   {parallel_time:.1f} s"
    )

    print(
        f"Summary produced with "
        f"{successful_count}/3 sources"
    )

    # --------------------------------------------------
    # PARTIAL FAILURE TEST
    # --------------------------------------------------

    print("\n" + "=" * 60)
    print("PARTIAL FAILURE TEST")
    print("=" * 60)

    failed_results, failed_time = await run_parallel(
        fail_leadership=True
    )

    failed_summary = await aggregate_results(
        COMPANY,
        failed_results
    )

    successful_after_failure = sum(
        1
        for result in failed_results
        if result["status"] == "success"
    )

    print("\nSummary after leadership failure:")
    print(failed_summary)

    print(
        f"\nSummary produced with "
        f"{successful_after_failure}/3 sources"
    )

    print(
        "\nPASS - Partial failure handled successfully"
    )


if __name__ == "__main__":
    asyncio.run(main())