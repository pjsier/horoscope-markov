import sys
from datetime import date, timedelta

SIGN_IDS = list(range(1, 13))


if __name__ == "__main__":
    start_date = date(2019, 1, 1)
    end_date = date.today()
    for date_diff in range(0, (end_date - start_date).days + 1):
        date_str = (start_date + timedelta(days=date_diff)).strftime("%Y%m%d")
        for sign_id in SIGN_IDS:
            sys.stdout.write(f"{date_str}/{sign_id}\n")
