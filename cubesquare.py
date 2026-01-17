def cubesquare_details(num):
    square = num * num
    cube = num * num * num
    return {
        "num": num,
        "square": square,
        "cube": cube
    }

if __name__ == "__main__":
    num = 5
    print(cubesquare_details(num))
