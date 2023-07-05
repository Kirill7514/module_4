def strcounter(s, str):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym, 0) + 1

    print(syms_counter)