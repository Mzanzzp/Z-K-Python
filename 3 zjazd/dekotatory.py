from functools import wraps

def bol(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)
        return f"<b>{result}</b>"

    return wrapper



@bol
def paragraph(text):
    return  f"<p>{text}</p>"

print(paragraph("ala"))
assert paragraph("aaa") == "<b><p>aaa</p></b>"