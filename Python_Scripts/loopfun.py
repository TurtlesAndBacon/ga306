body_parts = ['left-arm', 'right-arm', 'left-leg', 'right-leg']

#
# def add_functionNum(body_parts):
#     new_bp = [ x + add_func for x in body_parts]
#     for index, new_bp in enumerate(new_bp):
#         print(new_bp + str(index))
#
# add_functionNum(body_parts)

# def add_functionNum(body_parts):
#         add_functionNum = []
#         counter = 0
#         for thing in body_parts:
#             counter += 1
#             thing = thing + '.function' + str(counter)
#             body_parts.append(thing)
#         return updated_lst
#
# add_functionNum(body_parts)
# print(updated_lst)


def loopingfunction(loop_list):
    for k in range(len(loop_list)):
        loop_list[k] = loop_list[k] + '.function' + str(k+1)
    return loop_list

print(loopingfunction(body_parts))
