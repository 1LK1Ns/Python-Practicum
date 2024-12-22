def counter(text):
    let = [i for i in sorted(set(text)) if i.isalpha()]
    for i in let:
        yield (i, text.count(i))