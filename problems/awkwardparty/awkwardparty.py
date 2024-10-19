n = int(input())

guest_languages = list(map(int, input().split()))

last_index_of_language = {}

m = n
last_index_of_language[guest_languages[0]] = 0

for i in range(1, len(guest_languages)):
    lang = guest_languages[i]
    if lang in last_index_of_language:
        m = min(m, abs(last_index_of_language[lang] - i))

    last_index_of_language[lang] = i

print(m)