from router import Router


test_requests = [
    # Research - 3
    {
        "request": "Find news about Acme",
        "expected": "research",
    },
    {
        "request": "Research the latest AI trends",
        "expected": "research",
    },
    {
        "request": "Find information about Microsoft",
        "expected": "research",
    },

    # Writing - 3
    {
        "request": "Write a follow-up email",
        "expected": "writing",
    },
    {
        "request": "Draft a professional message to my manager",
        "expected": "writing",
    },
    {
        "request": "Rewrite this customer email",
        "expected": "writing",
    },

    # Data lookup - 3
    {
        "request": "How many open tickets?",
        "expected": "data-lookup",
    },
    {
        "request": "How many employees are in IT?",
        "expected": "data-lookup",
    },
    {
        "request": "Check the customer data for customer 1001",
        "expected": "data-lookup",
    },
]


def main():

    router = Router()

    correct = 0
    total = len(test_requests)

    print("=" * 60)
    print("WEEK 6 - DAY 3 - TASK 1")
    print("ROUTER PATTERN")
    print("=" * 60)

    for test in test_requests:

        request = test["request"]
        expected = test["expected"]

        selected_agent, result = router.route(request)

        print()
        print(f"Request : {request}")
        print(f"Expected: {expected}")
        print(f"Chosen  : {selected_agent}")
        print(f"Result  : {result}")

        if selected_agent == expected:
            correct += 1
            print("Status  : PASS")
        else:
            print("Status  : FAIL")

    accuracy = (correct / total) * 100

    print()
    print("=" * 60)
    print("ROUTING RESULTS")
    print("=" * 60)

    print(f"Correct routes    : {correct}/{total}")
    print(f"Routing accuracy  : {accuracy:.0f}%")

    if accuracy >= 90:
        print("PASS - Routing accuracy is above 90%")
    else:
        print("FAIL - Router needs improvement")

    # Fallback test
    print()
    print("=" * 60)
    print("FALLBACK TEST")
    print("=" * 60)

    unknown_request = "Tell me a joke about a robot"

    selected_agent, result = router.route(unknown_request)

    print(f"Request : {unknown_request}")
    print(f"Chosen  : {selected_agent}")
    print(f"Result  : {result}")


if __name__ == "__main__":
    main()