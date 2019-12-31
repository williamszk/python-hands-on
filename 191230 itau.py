#191230 itau
cienciadedados@itau-unibanco.com.br


# --------------------

listEmoji = ["🏦","🎲","🖥","📚","🚀"]
listHex = [ord(x) for x in listEmoji]
sum(listHex)

# --------------------

import emoji

sum_hex([x.Unicode.replace("U+","") for x in [🏦,🎲,🖥,📚,🚀]])

sum_hex([x.Unicode.replace("U+","") for x in [🏦,🎲,🖥,📚,🚀]])


listEmoji = [🏦,🎲,🖥,📚,🚀]
x.Unicode.replace("U+","") for x in [🏦,🎲,🖥,📚,🚀]

🏦.Unicode


"😀"
"U+1F600"
"1F600"
int("1F600",16)
ord("😀")

bank = "🏦"
ibrow = "🤨"

len(bank)
len(ibrow)
ord(bank)

sum_hex()

ibrow.encode("utf-8")
len(ibrow.encode("utf-8"))


# Calling list() on a bytes object gives you
# the decimal value for each byte
list(b'\xf0\x9f\xa4\xa8')


basehex = "12"
sechex = "11"

int("0",16)
int("1",16)
int("11",16)
int("9",16)
int("a",16)
int("b",16)
int("f",16)
int("F",16)
int("10",16)
int("11",16)
int("12",16)
int("13",16)



basehexin = int(basehex, 16)
sechexin = int(sechex, 16)



sum = basehexin - sechexin



print(hex(sum))