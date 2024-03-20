# Treść zadania: zaprogramuj grę, która będzie weryfikować, czy dla wybranego przez gracza numeru
# suma lub iloczyn dowolnej pary unikatowych liczb z nieznanego graczowi NIU (numeru identyfikacyjnego studenta)
# jest równa wybranej przez gracza liczbie.

def check_number(niu:list):
    # Wybieram unikatowe wartości z listy.
    unique_niu = set(niu)
    # I konwertuję zbiór z powrotem na listę, by mieć zapewnioną indeksowalność.
    unique_niu = list(unique_niu)
    number = input('Wybierz numer :-)\n')

    # Zmienne kontrolujące, ile razy spełnione zostały założenia modułów gry.
    # Zainicjalizowane jako listy, ponieważ typ integer jest w Pythonie immutable.
    matching_pairs_sum = [0]
    matching_pairs_multip = [0]

    for list_element in unique_niu:
        elements_index = unique_niu.index(list_element)
        look_for_sum(elements_index, number, list_element, unique_niu, matching_pairs_sum)
        look_for_multiplication(elements_index, number, list_element, unique_niu, matching_pairs_multip)

    print('------\nWYNIK\n------')
    if matching_pairs_sum[0] == 0 and matching_pairs_multip[0] == 0:
        print('Wybrana liczba nie spełnia żadnych z założen dla tego NIU.\nSpróbuj jeszcze raz!')
    else:
        print(
            f"Liczba pasujących par dla sumy: {matching_pairs_sum[0]}\n"
            f"Liczba pasujących par dla iloczynu: {matching_pairs_multip[0]}")

def look_for_sum(elements_index, number, list_element, unique_niu, matching_pairs_sum):
    # Sprawdzanie elementów występujących w liście po elemencie z obecnej iteracji.
    for other_element in range(elements_index + 1, len(unique_niu)):
        if matching_pairs_sum[0] > 0 and int(number) == unique_niu[other_element] + list_element:
            matching_pairs_sum[0] += 1
            print(
                f"Wow, jest ich jeszcze więcej!\nTe elementy to {unique_niu[other_element]} i {list_element}"
            )
        elif int(number) == unique_niu[other_element] + list_element:
            matching_pairs_sum[0] += 1
            print(
                f"Hurray!! Istnieje suma elementów równa podanej liczbie.\n"
                f"Te elementy to: {unique_niu[other_element]} i {list_element}"
            )

def look_for_multiplication(elements_index, number, list_element, unique_niu, matching_pairs_multip):
    for other_element in range(elements_index + 1, len(unique_niu)):
        if matching_pairs_multip[0] > 0 & int(number) == unique_niu[other_element] * list_element:
            matching_pairs_multip[0] += 1
            print(
                f"Wow, jest ich jeszcze więcej!\nTe elementy to {unique_niu[other_element]} i {list_element}"
            )
        elif int(number) == unique_niu[other_element] * list_element:
            matching_pairs_multip[0] += 1
            print(
                f"Hurray!! Istnieje iloczyn elementów równa podanej liczbie.\n"
                f"Te elementy to: {unique_niu[other_element]} i {list_element}"
            )

check_number(niu=[4, 1, 0, 5, 6, 7, 1, 0, 2,])