def cubesquare_details(num):
    square = num * num
    cube = num * num * num
    return {
        "num": num,
        "square": square,
        "cube": cube
    }

if __name__ == "__main__":
    num = int(input("Enter the number: "))
    print(cubesquare_details(num))
