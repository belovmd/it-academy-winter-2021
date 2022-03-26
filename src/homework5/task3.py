# Realise function get_ranges that get list of non-recurring numbers, sorted in
# ascending and rolls it up.
# !!!!! Я знаю, что код получился очень С-подобным и замысловатым,
# просто я пытался сделать мимальную О-нотацию и сделать всё за один проход
# по списку, вроде так и получилось, не считая одного len. Простите :(

def get_ranges(lst):
    str_ = f'{lst[0]}'
    step = 1
    length = len(lst)
    while step < length:
        if lst[step] - lst[step - 1] == 1:
            str_ += '-'
            if step == length - 1:
                str_ += f'{lst[step]}'
                break
            if lst[step + 1] - lst[step] != 1:
                if str_[-1] != '-':
                    str_ += f'{lst[step]},{lst[step + 1]}'
                else:
                    str_ += f'{lst[step]},{lst[step + 1]}'
            while lst[step] - lst[step - 1] == 1:
                step += 1
            if str(lst[step - 1]) not in str_:
                str_ += f'{lst[step - 1]},'
            step += 1
            if lst[step] == lst[-1] and lst[step] - lst[step - 1] == 1:
                str_ += f'-{lst[step]}'
                break
            if lst[step + 1] - lst[step] != 1 and str_[-1]:
                str_ += f'{lst[step]},'
            step += 1
        else:
            if step == length - 1:
                str_ += str(lst[step])
                step += 1
            elif step == 1:
                str_ += f',{lst[step]},'
                step += 1
            else:
                str_ += f'{lst[step]},'
                step += 1

    return str_


print(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]))
print(get_ranges([4, 7, 10]))
print(get_ranges([2, 3, 8, 9]))
