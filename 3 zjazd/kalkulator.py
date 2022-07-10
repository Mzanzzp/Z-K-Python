import logging

logging.basicConfig(level=logging.INFO, filename="log_kal.logs")
logger = logging.getLogger(__name__)

def add(a, b):
    logger.info(f"wywolanie add z argumantami: {a} {b}")
    return a + b


def sub(a, b):
    logger.info(f"wywolanie sub z argumantami: {a} {b}")
    return a - b


def div(a, b):
    logger.info(f"wywolanie div z argumantami: {a} {b}")
    if a == 0 or b == 0:
        logger.critical(f"dzielenie przez zero  {a} {b}")
        print("Nie dziel przez zero")
    else:
        return a / b


def multi(a, b):
    logger.info(f"wywolanie multi z argumantami: {a} {b}") #, stack_info=True daje ewentualny error
    return a * b


def get_data():
    operator = input("jaka operecje chcesz wykonac? [1-add, 2-sub, 3-div, 4-multi]")
    a = int(input("podaj argument a: "))
    b = int(input("podaj argument b: "))
    return operator, a, b


def main():
    op, a, b = get_data()
    result = operations[op](a, b)
    print("wynik to", result)
    return result


operations = {"1": add, "2": sub, "3": div, "4": multi}
if __name__ == "__main__":
    main()

