import re
match_mode = re.compile(r"(\d\d\d)-(\d\d\d)")
result = match_mode.search("13456123-456798-123")
print(result)
