import csv
import re


REQUIRED_FIELDS = [
    "company",
    "contact_name",
    "email",
    "industry",
    "size",
]


def valid_email(email):
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(pattern, email) is not None


def validate_row(row, row_number):

    errors = []

    # Required field validation
    for field in REQUIRED_FIELDS:
        if not row.get(field, "").strip():
            errors.append(f"Missing {field}")

    # Email validation
    email = row.get("email", "").strip()

    if email and not valid_email(email):
        errors.append("Invalid email")

    if errors:
        return False, errors

    return True, []


def load_prospects(file_path):

    valid_prospects = []
    invalid_rows = []

    with open(
    "task4/data/prospects.csv",
    "r",
    encoding="utf-8"
) as file:

        reader = csv.DictReader(file)

        for row_number, row in enumerate(reader, start=2):

            is_valid, errors = validate_row(
                row,
                row_number
            )

            if is_valid:
                valid_prospects.append(row)

            else:
                invalid_rows.append({
                    "row": row_number,
                    "data": row,
                    "errors": errors,
                })

    print(
        f"Loaded {len(valid_prospects)} prospects "
        f"({len(invalid_rows)} invalid row skipped)"
    )

    if invalid_rows:

        print("\nInvalid rows:")

        for item in invalid_rows:

            print(
                f"Row {item['row']}: "
                f"{', '.join(item['errors'])}"
            )

    return valid_prospects


if __name__ == "__main__":

    prospects = load_prospects(
        "data/prospects.csv"
    )

    print("\nValid prospects:")

    for prospect in prospects:
        print(
            f"{prospect['company']} - "
            f"{prospect['contact_name']} - "
            f"{prospect['email']}"
        )