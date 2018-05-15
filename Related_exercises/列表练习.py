# names=['alex','jack',2,'rain',2,'mack',2,'racheal','shanshan']

# count=0
# for i in names:
#     print(count,i)
#     count+=1
# enumerate枚举

# for index,i in enumerate(names):
#     print(index,i)

# for index,i in enumerate(names):
#     if index%2==0:
#         names[index]==-1
#         print(index,i)
# print(names)


names=['alex','jack',2,'rain',2,'mack',2,'racheal','shanshan']
first_index=names.index(2)
names2=names[names.index(2)+1:]
second_index=names2.index(2)
val=names[first_index+second_index+1]
print(val)