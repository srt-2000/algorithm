import click

@click.command()
def itn():
    click.echo('Initialized the database')

@click.command()
def drp():
    click.echo('Dropped the database')

if __name__ == '__main__':
    itn()
'''
@click.command()
def binary_search():
    print("Hello!\nI'm a very very fast algorithm for searching on sorted range.\nI'm the binary search algorithm.")
    m = int(input("Enter the maximum number of sorted array:"))
    x = int(input("Enter the digit we want to find:"))

    my_list = [n for n in range(1, m + 1)]
    print("\nFirst of all I create a sorted list for your range:\n", my_list)
    position = PositionFinder()
    print("\nFIND!!!\n", position.bin_search(my_list, x), "is position of", x)

if __name__ == "__main__":
    pass
'''