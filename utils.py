def parse_input(input_str):
    try:
        return list(map(int,input_str.strip().split()))
    except:
        return[]