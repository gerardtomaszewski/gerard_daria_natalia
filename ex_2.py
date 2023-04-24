def policz_studentow(studenci) -> int:
    stringi = [element for element in studenci if isinstance(element, str)]
    return len(stringi)
