from datetime import date

def main():
    today = date.today().strftime("%B %d, %Y")
    print(f"Hello Earth! Today's date is {today}.")


if __name__ == "__main__":
    main()
