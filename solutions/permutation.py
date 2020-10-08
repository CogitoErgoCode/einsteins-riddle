from itertools import permutations

def main():
    variables = {
        'colors' : ['red'     , 'green'  , 'white' , 'yellow'    , 'blue'  ],
        'races'  : ['brit'    , 'swede'  , 'dane'  , 'norwegian' , 'german'],
        'drinks' : ['tea'     , 'coffee' , 'milk'  , 'beer'      , 'water' ],
        'smokes' : ['pallMall', 'dunhill', 'blends', 'blueMaster', 'prince'],
        'pets'   : ['dogs'    , 'birds'  , 'cats'  , 'horses'    , 'fish'  ]
    }

    equals  = lambda a,b: a == b
    next_to = lambda a,b: a == b - 1 or a == b + 1
    left_of = lambda a,b: a == b - 1
                        
    perm = list(permutations(range(1, 5+1)))
    for red, green, white, yellow, blue in perm:
        if not left_of(green, white):
            continue
        for brit, swede, dane, norwegian, german in perm:
            # if not ( equals(brit, red) and next_to(norwegian, blue) ):
            if not all([equals(brit, red), next_to(norwegian, blue)]):
                continue
            for tea, coffee, milk, beer, water in perm:
                # if not ( equals(dane, tea) and equals(green, coffee) and \
                #          milk == 3         and norwegian == 1 ):
                if not all([ equals(dane, tea), equals(green, coffee), 
                             milk == 3, norwegian == 1 ]):
                    continue
                for pallMall, dunhill, blends, blueMaster, prince in perm:
                    # if not ( equals(yellow, dunhill) and equals(blueMaster, beer) and \
                    #          equals(german, prince)  and next_to(blends, water) ):
                    if not all([ equals(yellow, dunhill), equals(blueMaster, beer), 
                                 equals(german, prince), next_to(blends, water) ]):
                        continue
                    for dogs, birds, cats, horses, fish in perm:
                        # if not ( equals(swede, dogs)   and equals(pallMall, birds) and \
                        #          next_to(blends, cats) and next_to(horses, dunhill) ):
                        if not all([ equals(swede, dogs), equals(pallMall, birds), 
                                     next_to(blends, cats), next_to(horses, dunhill) ]):
                            continue

                        g = lambda oldLst,newPos: [i for i,j in sorted(zip(oldLst, newPos), key=lambda x: x[1])]
                        
                        # iterate through the solved positions sorting each tuple of solutions as we print
                        for (k,v), new in zip(variables.items(), (
                            [red     , green  , white , yellow    , blue  ],
                            [brit    , swede  , dane  , norwegian , german],
                            [tea     , coffee , milk  , beer      , water ],
                            [pallMall, dunhill, blends, blueMaster, prince],
                            [dogs    , birds  , cats  , horses    , fish  ]
                        )):
                            print("{:6s}: {:10s} {:10s} {:10s} {:10s} {:10s}".format(k, *g(v, new)))

if __name__ == "__main__":
    main()