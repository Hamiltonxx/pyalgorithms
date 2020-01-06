dgt = {"zero":"00","one":"01","two":"04","three":"09","four":"16","five":"25","six":"36","seven":"49",
"eight":"64","nine":"81","ten":"00","eleven":"21","twelve":"44","thirteen":"69","fourteen":"96","fifteen":"25",
"sixteen":"56","seventeen":"89","eighteen":"24","nineteen":"61","twenty":"00",
"a":"01","both":"04","another":"04","first":"01","second":"04","third":"09"}

words = input().split()
a = []
for x in words:
    if x in dgt:
        a.append(dgt[x])
a.sort()

res = int("".join(a)) if a else 0
print(res)