import circle
import square
import triangle

fig_modules = {
    "circle": circle,
    "square": square,
    "triangle": triangle,
}

figs = ["circle", "square", "triangle"]
funcs = ["perimeter", "area"]
sizes = {
    "circle-area": 1,
    "circle-perimeter": 1,
    "square-area": 1,
    "square-perimeter": 1,
    "triangle-area": 3,
    "triangle-perimeter": 3,
}


def calc(fig, func, size):
    assert fig in fig_modules, "Invalid figure"
    assert func in funcs, "Invalid function"

    key = f"{fig}-{func}"
    args = sizes.get(key)
    assert args is not None
    assert len(size) == args

    module = fig_modules[fig]
    func_to_call = getattr(module, func)
    result = func_to_call(*size)
    return result


if __name__ == "__main__":
    func = ""
    fig = ""
    size = []

    while fig not in figs:
        fig = input(f"Enter figure name, available are {figs}: \n")

    while func not in funcs:
        func = input(f"Enter function name, available are {funcs}: \n")

    while len(size) != sizes.get(f"{fig}-{func}", 1):
        size = list(
            map(
                int,
                input(
                    "Input figure sizes separated by space, "
                    "1 for circle and square:\n"
                ).split(),
            )
        )

    result = calc(fig, func, size)
    print(f"Result: {result}")
