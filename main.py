# import libs and modules
import click
import json

from src.binary_search import PositionFinder
from src.bloom import BloomFilter
from src.binary_tree import TreeNode
from src.dh import DHProtocol
from src.dijkstra import BestPath
from src.dynamic import DynamicSelection
from src.greedy import PathFinder
from src.hash_tables1 import VoteChecker
from src.hash_tables2 import CashTest
from src.inverted import WordFinder
from src.map import Sqr
from src.nn import NNPrediction
from src.quick_sort1 import QuickSort
from src.quick_sort2 import MultipleMatrix
from src.quick_sum import Summator
from src.recurtion1 import CountDown
from src.recurtion2 import FactorialCalculate
from src.reduce import RedFun
from src.width_search import MSearcher


# create command's group
@click.group
def app_commands():
    pass


# binary search algorithm command
@click.command(help="binary search algorithm")
@click.option(
    "--mx",
    type=int,
    prompt="Hello!"
           "\nI'm the binary search algorithm"
           "\nI'll find the index of item you want very fast"
           "\n\nEnter the maximum number of sorted array",
    help="You have to enter max value of list"
)
@click.option(
    "--find",
    type=int,
    prompt="Enter the digit we want to find",
    help="You have to enter the value what index you want to find"
)
def bs(mx, find):
    my_list = [n for n in range(1, mx + 1)]
    click.echo(f"\nWe have a  sorted list from 0 to {mx}")
    position = PositionFinder()
    click.echo(f"\nFIND!!!\n{position.bin_search(my_list, find)} is position of {find}")


# binary Tree algorithm command
@click.command(help="binary tree parsing")
@click.option(
    "--ptype",
    prompt="\nWe've created a Perfect Binary Tree with 7 nodes"
           "\nEnter the parsing type for our binary tree",
    type=click.Choice(["pre", "post", "in"]),
    help="You have to enter max the parsing type, choose pre, post or in"
)
def bt(ptype):
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)
    tree.right.left = TreeNode(6)
    tree.right.right = TreeNode(7)

    if ptype == "pre":
        click.echo("\nBinary-Tree Pre-order parsing:")
        tree.pre_order(tree)
        click.echo("\n")
    elif ptype == "post":
        click.echo("\nBinary-Tree Post-order parsing:")
        tree.post_order(tree)
        click.echo("\n")
    elif ptype == "in":
        click.echo("\nBinary-Tree In-order parsing")
        tree.in_order(tree)
        click.echo("\n")


# Bloom filter algorithm command
@click.command(help="Bloom filter algorithm")
def bf():
    bloom_filter = BloomFilter(1000000, 100000)
    base_ip = "192.168.1."
    bloom_filter.add_to_filter(base_ip + str(1))
    bloom_filter.add_to_filter(base_ip + str(98))
    bloom_filter.add_to_filter(base_ip + str(101))
    click.echo(
        f"A Bloom filter for negative IP address.\nWe have a base IP:{base_ip}"
        "\nAnd we add some sample ens for 3 addresses in filter: 1, 98, 101"
        "\nIf we have a very large massive with 100000 IP,"
        "\nand we have to find IPs which are not allowed,"
        "\nwe use Bloom filter:\n"
    )

    for i in range(1, 100000):
        if not bloom_filter.check_is_not_in_filter(base_ip + str(i)):
            click.echo(base_ip + str(i))


# Diffie–Hellman algorithm
@click.command(help="Diffie–Hellman algorithm")
@click.option(
    "--p",
    type=int,
    prompt="It's a Diffie Hellman algorithm.\n"
           "Alice and Bob agree upon the public keys G and P\n"
           "Input a number = public key P",
    help="You have to input a number = public key P"
)
@click.option(
    "--g",
    type=int,
    prompt="Input a number = public key G",
    help="You have to input a number = public key G"
)
def dh(p, g):
    d_h = DHProtocol()
    d_h.dh_calculate(p, g)


# Dijkstra algorithm
@click.command(help="Dijkstra algorithm")
def dk():
    with open("data/7_1_graph_data.json", "r") as file1:
        graph = json.load(file1)
    with open("data/7_1_costs_data.json", "r") as file2:
        costs = json.load(file2)
    costs["fin"] = float("inf")
    with open("data/7_1_parents_data.json", "r") as file3:
        parents = json.load(file3)

    a = BestPath()
    path = a.dsa(graph, costs, parents)

    click.echo(f"We have a graph with different paths to get our point:\n {graph} \n")
    click.echo("I've used the DSA Dijkstra's Algorithm and found our minimal trip\n"
               f"{['start'] + path[:(path.index("fin") + 1):]}")


# dynamic programming
@click.command(help="Dynamic programming algorithm")
def dc():
    with open("data/9_1_data.json", "r") as file:
        items = json.load(file)
    for i in items:
        items[i] = tuple(items[i])

    click.echo(
        "Hi, I'm a dynamic programming algorithm.\n"
        "Let's select the most expensive things into my backpack.\n"
        f"\nWe have things (weight, cost):\n{items}\n"
        "My backpack weight limit is 4 kg.\n"
    )
    a = DynamicSelection()
    select = a.get_selected_items(items)
    click.echo(f"And I've chosen the best combination for us:\n{select}")


# Fourier transform
@click.command(help="Fourier transform")
def fr():
    import src.fourier


# greedy algorithm
@click.command(help="Greedy algorithm")
def gr():
    with open("data/8_1_data.json", "r") as file:
        street = json.load(file)

    for key, value in street.items():
        click.echo(f"distance from house, {key}, {value}")

    b = PathFinder()
    b.find_postman_path(street)


# hash tables version 1
@click.command(help="Hash tables version 1")
@click.option(
    "--qnt",
    type=int,
    prompt="I'm a check voted function with hash table"
           "\nI'll control and check the list of voters"
           "\nInput how many people have come to vote",
    help="You have input a planned quantity of voters"
)
def ht1(qnt):
    voted = {}
    checker = VoteChecker(voted)

    click.echo("Please, input the name of voter")
    while len(voted) < qnt:
        voter_name = input()
        checker.check_vote(voter_name)
    click.echo(f"\nOur voted list\n{voted}")


# hash tables version 1
@click.command(help="Hash tables version 2")
def ht2():
    with open("data/5_2_data.json", "r") as file:
        page = json.load(file)
    click.echo(
        f"We have urls: {list(page.keys())}"
        "\nYou have 6 attempts"
        "\nInput url to make a CASH test"
    )
    tester = CashTest()
    for i in range(6):
        url = input()
        print(tester.get_cache(url, page))
    click.echo("\nYou've done all of your attempts")


# inverted index algorithm example
@click.command(help="Inverted index algorithm")
@click.option(
    "--word",
    prompt="Inverted index algorithm"
           "\nWe have"
           f"\npage a with phrase: hi there"
           f"\npage b with phrase: hi adit"
           f"\npage c with phrase: there we go"
           "\nInput word from phrases and fin the pages",
    type=click.Choice(["hi", "there", "adit", "we", "go"]),
    help="Input word from phrases and fin the pages"
)
def ih(word):
    with open("data/11_2_data.json", "r") as file:
        inv_hash = json.load(file)
    f = WordFinder()
    f.find_world(word, inv_hash)


# map function
@click.command(help="Map function")
def mp():
    with open("data/11_4_data.json", "r") as file:
        a = json.load(file)

    b = Sqr()
    click.echo(
        "A map function"
        f"\nWe have an array:{a}"
        f"\nAnd we've powered every element with map function:{b.sqr_arr(a)}"
    )


# nearest neighbours algorithm
@click.command(help="Nearest neighbours algorithm")
@click.argument("condition", type=list, default=[4, 1, 0])
@click.argument("neighbours_number", type=int, default=3)
def nn(condition, neighbours_number):
    with open("data/10_1_data.json", "r") as file:
        bread_stat = json.load(file)
    bread_stat = {int(k): v for k, v in bread_stat.items()}
    a = NNPrediction()
    click.echo(
        "Nearest neighbours algorithm"
        "\nLet's make prediction for bread sales\n"
        "\nWe have a statistics (bread quantity: day condition)"
        f"\n{bread_stat}"
        "\nWe have our today's condition:"
        f"\n{condition}\n"
        "\nAnd we predict to sale about"
        f"\n{a.predict_bread_sales(bread_stat, condition, neighbours_number)} breads"
    )


# Sorting function with recursion
@click.command(help="Sorting function with recursion")
def qsr():
    click.echo("The quick sort function with recursion algorithm")
    a = [int(n) for n in input("Enter the list you want to sort:").split()]
    b = QuickSort()
    click.echo(f"Here is your sorted array: {b.sorted(a)}")


# Array multiplicative function
@click.command(help="Array multiplicative function")
def mm():
    click.echo("Multiplication array function")
    a = [int(n) for n in input("Enter the array you want to multiplicate with itself:").split()]
    b = MultipleMatrix()
    click.echo(f"Here is your multiplicated matrix: {b.mult_matrix(a)}")


# Sum function with recursion
@click.command(help="Sum function with recursion")
def sm():
    click.echo("Sum function with recursion algorithm.")
    a = [int(n) for n in input("\nEnter the list numbers you want to summing:").split()]
    b = Summator()
    click.echo(f"The sum of your array is: {b.array_sum(a)}")


# Countdown function with recursion
@click.command(help="Countdown function with recursion")
@click.option(
    "--rng",
    type=int,
    prompt="Countdown function with recursion algorithm"
           "\nEnter the countdown range",
    help="You have to enter maximum value of countdown range"
)
def cr(rng):
    c = CountDown()
    c.down_row(rng)


# Factorial calculating function with recursion
@click.command(help="Factorial calculating function with recursion")
@click.option(
    "--fn",
    type=int,
    prompt="Factorial calculating function with recursion"
           "\nEnter the number to calculate it factorial",
    help="You have to enter the number for factorial calculating"
)
def fc(fn):
    f = FactorialCalculate()
    click.echo(f"The factorial of {fn} is {f.fa_calc(fn)}")


# Reduce function
@click.command(help="Reduce function")
def rc():
    with open("data/11_5_data.json", "r") as file:
        test_list = json.load(file)
    l = RedFun()

    click.echo(
        f"A functools.reduce function.\nWe have an array:{test_list}"
        f"\nThe sum of elements in test_list is:{l.arr_sum(test_list)}"
        f"\nThe maximum element in test_list is:{l.arr_max(test_list)}"
    )


# Width search algorithm
@click.command(help="Width search algorithm")
@click.option(
    "--name",
    prompt="I'm a finder if a mango-seller (name has 'm' at tne end) in friends circle"
           "\nPlease, have a look on this list"
           "\nAnd enter the name you want to check",
    type=click.Choice(["Viva", "Max", "Demon", "Leo", "Alex", "Denis", "Dima", "Ann", "Andrey", "you"]),
    help="Enter the name you want to check"
)
def ws(name):
    with open("data/6_1_data.json", "r") as data:
        graph = json.load(data)

    b = MSearcher()
    b.search_mango_seller(name, graph)


# adding commands into group
app_commands.add_command(bf)
app_commands.add_command(bs)
app_commands.add_command(bt)
app_commands.add_command(dh)
app_commands.add_command(dk)
app_commands.add_command(dc)
app_commands.add_command(fr)
app_commands.add_command(gr)
app_commands.add_command(ht1)
app_commands.add_command(ht2)
app_commands.add_command(ih)
app_commands.add_command(mp)
app_commands.add_command(nn)
app_commands.add_command(qsr)
app_commands.add_command(mm)
app_commands.add_command(sm)
app_commands.add_command(cr)
app_commands.add_command(fc)
app_commands.add_command(rc)
app_commands.add_command(ws)

if __name__ == '__main__':
    app_commands()
