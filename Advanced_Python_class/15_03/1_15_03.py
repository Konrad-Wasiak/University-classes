my_niu = [8,3,8,3,7]

def niu_sorting(niu:list, ascending:bool):
    unique_niu = list(set(niu))
    unique_niu_copy = unique_niu
    warunek = [True]

    if ascending == True:
        while(warunek[0]):
            for element_index, element in enumerate(unique_niu):
                try:
                    if element > unique_niu[element_index + 1]:
                        unique_niu_copy[element_index], unique_niu_copy[element_index + 1] =\
                        (
                            unique_niu_copy[element_index + 1], unique_niu_copy[element_index]
                        )

                except IndexError:
                    continue

            if unique_niu == unique_niu_copy:
                warunek[0] = False
                unique_niu = unique_niu_copy
                print(f'Sortowanie rosnąco: {unique_niu}')
                return unique_niu

    else:
        while (warunek[0]):
            for element_index, element in enumerate(unique_niu):
                try:
                    if element < unique_niu[element_index + 1]:
                        unique_niu_copy[element_index], unique_niu_copy[element_index + 1] = \
                            (
                                unique_niu_copy[element_index + 1], unique_niu_copy[element_index]
                            )

                except IndexError:
                    continue

            if unique_niu == unique_niu_copy:
                warunek[0] = False
                unique_niu = unique_niu_copy
                print(f'Sortowanie malejąco: {unique_niu}')
                return unique_niu


sorted_niu = niu_sorting(my_niu, ascending = True)
sorted_niu = niu_sorting(my_niu, ascending = False)