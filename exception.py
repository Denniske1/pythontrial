# # my name ="eMobilis"
# #
# # for i in my name:
# #     if i != k:
# #         print(i)
#
# # jina= ['banana','mangoes','apples']
# #
# # for i in range(5)
# #      print(i,jina[i])
# try:
#     jina = ['banana', 'mangoes', 'apples']
#
#     for i in range(5):
#         print(i,jina[i])
#     # # code that might raise exception
#     # result = 1 / 0
# # except ZeroDivisionError as e:
# #     # code to handle exception
# #      print(f"An error occurred: {e}")
# finally:
#     # code that runs no matter what
#      print("This will always be printed")

try:
    jina=['banana','oranges','mangoes']
    for i in range(5):
        print(i,jina[i])
except:
    print("index out of range")
finally:
    print("This will always run")