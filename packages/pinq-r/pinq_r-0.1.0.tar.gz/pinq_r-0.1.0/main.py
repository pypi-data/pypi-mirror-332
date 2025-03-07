from pinq import PinqSeq

li = PinqSeq([1, 14, 'g', 2, 3, 4, 5])

if __name__ == "__main__":
    squares_grouped = (
        li
        .of_type(int).where(lambda x: x % 2 == 0)
        .select(lambda x: x ** 2)
        .order_by(lambda x: x).rev()
        .group_by(lambda x: x % 5)
        .select(lambda x: (x[0], x[-1].list())).at(-1)
    )

    print(squares_grouped)
