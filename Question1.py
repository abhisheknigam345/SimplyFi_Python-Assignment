def convert_to_indian_currency(value: int):
    if len(str(value)) <= 3:    # values lesser 1000
        return value
    elif 3 < len(str(value)) <= 5: # values lesser than 100000
        return f'{str(value)[:-3]},{str(value)[-3:]}'
    else:   # values greater and equal 100000
        trim = str(value)[:-3]
        lst = []
        while trim:
            lst.append(trim[-2:])
            trim = trim[:-2]
        lst = lst[::-1]
        result = ",".join(lst)
        return f'{result},{str(value)[-3:]}'

def main():
    value1 = int(input())
    if value1 < 0:
        print(f'-{convert_to_indian_currency(int(str(value1)[1:]))}')
    else:
        print(convert_to_indian_currency(value1))

if __name__ == "__main__":
    main()