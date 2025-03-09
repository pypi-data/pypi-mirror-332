import hors

# Распознавание фиксированной даты и времени
r = hors.process_phrase('3 числа мы слушали Шуфутинского')
print(r.dates[0].type)  # <DateTimeTokenType.FIXED: 1>
print(f"{r.dates[0].date_from} | {r.dates[0].date_to}")
# ????-??-03 00:00:00.000000 | ????-??-03 00:00:00.000000 + 23:59:59.999999
