#**Algorithms**

##author srt-2000


##Introduction

    This is a CLI app.
    It shows a results of working
    an algorithms described in a book "Grokking Algorithms".


##Content

    - data - repository with data files used as stdin data
    - src - repository with python modules, as ussual it's a Class code
    - main.py - main code with click commands


##Requirements

It made with PYTHON 3.12

For using this app you need install python packages:

    bitarray==3.0.0
    click==8.1.7
    contourpy==1.3.0
    cycler==0.12.1
    fonttools==4.54.1
    kiwisolver==1.4.7
    matplotlib==3.9.2
    numpy==2.1.2
    packaging==24.1
    pillow==11.0.0
    pyparsing==3.2.0
    PyQt6==6.7.1
    PyQt6-Qt6==6.7.3
    PyQt6_sip==13.8.0
    python-dateutil==2.9.0.post0
    scipy==1.14.1
    six==1.16.0


##Installation

To install - you have copy this repo and create .venv with requirement packages.


##Using

###START in terminal:

            When you are inside your project and venv try command:

                ~/xx/xx$: python main.py [name of command (see 'the main commands')]

            or try help command to read all commands in terminal

                ~/xx/xx$: python main.py --help

    
###The main commands:

      bf   Bloom filter algorithm
            It's show how works a Bloom filter for negative IP address.

            No options or arguments for this command.


      bs   binary search algorithm
            It's shows how binary search works - to find our char index.

            Options:

                --mx   
                INTEGER  You have to enter max value of list

                --find 
                INTEGER  You have to enter the value what index you want to find


      bt   binary tree parsing
            It show a result of different types of parsing for binary tree.

            Options:

                --ptype 
                use only [pre|post|in]  
                You have to enter max the parsing type, choose pre, post or in.


      cr   Countdown function with recursion
            Shows a countdown result used recursion algorithm.

            Options:

                --rng 
                INTEGER  You have to enter maximum value of countdown range


      dc   Dynamic programming algorithm
            It's presents solution for select the most expensive things into the backpack. 
 
            No options or arguments for this command.


      dh   Diffie–Hellman algorithm
            Shows how works classic encryption algorithm.

            Options:

              --p 
              INTEGER  You have to input a number = public key P

              --g 
              INTEGER  You have to input a number = public key G


      dk   Dijkstra algorithm
            We are using the DSA Dijkstra's Algorithm to find our minimal trip.

            No options or arguments for this command.


      fc   Factorial calculating function with recursion
    
            Options:

             --fn 
             INTEGER  You have to enter the number for factorial calculating.


      fr   Fourier transform
            We are filtering and normalising the signal.
            It shows interesting figures.

            No options or arguments for this command.        


      gr   Greedy algorithm
            We are solving a hard task to fin the path for postman.

            No options or arguments for this command.  


      ht1  Hash tables version 1
            It presents a check voters process.

            Options:
             --qnt 
             INTEGER  You have input a planned quantity of voters.


      ht2  Hash tables version 2
            It's presents like test for cash.
            Input urls from given list and see from where you have a response.

            No options or arguments for this command. 


      ih   Inverted index algorithm
            It finds all pages with inputed word.

            Options:
             --word 
             only [hi|there|adit|we|go]  
             Input word from phrases and fin the pages


      mm   Array multiplicative function
            It multiplicate inputed array with itself.
            You have to input array in line, and separat numbers by space.

            No options or arguments for this command. 


      mp   Map function
            Shows how map function works.

            No options or arguments for this command. 


      nn   Nearest neighbours algorithm
            Presents some prediction for sales using NN algorithm.

            No options or arguments for this command. 


      qsr  Sorting function with recursion
            Simple sorting.

            No options or arguments for this command. 


      rc   Reduce function
            A functools.reduce function.

            No options or arguments for this command. 


      sm   Sum function with recursion
            Sum all elements in the list.
            You have to input array in line, and separat numbers by space.

            No options or arguments for this command. 

      ws   Width search algorithm
             Find a mango-seller (name has '-m' at tne end) in friends circle.

            Options:

            --name 
            only [Viva|Max|Demon|Leo|Alex|Denis|Dima|Ann|Andrey|you]
            Enter the name you want to check

##Thanks for your attention.