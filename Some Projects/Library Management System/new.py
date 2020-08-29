stuLine = "xiaoxi，okok，白夜行，白夜行，三体"
stuName, stupassword, *others = stuLine.split('，')

print(others)
others.remove('三体')
print(others)
others.remove('三体')
print(others)
#result = stuName + '，' + stupassword + '，' + others + '\n'
#print(result)
