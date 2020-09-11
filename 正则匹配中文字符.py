import re

text = "hello 你好 世界！ world!"

pattern  = re.compile(r'[\u4e00-\u9fa5]+')
result = pattern.findall(text)
print(result)
