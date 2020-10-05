from itertools import permutations

def main():
    variables = {
        'colors' : ['red'     , 'green'  , 'white' , 'yellow'    , 'blue'  ],
        'races'  : ['brit'    , 'swede'  , 'dane'  , 'norwegian' , 'german'],
        'drinks' : ['tea'     , 'coffee' , 'milk'  , 'beer'      , 'water' ],
        'smokes' : ['pallMall', 'dunhill', 'blends', 'blueMaster', 'prince'],
        'pets'   : ['dogs'    , 'birds'  , 'cats'  , 'horses'    , 'fish'  ]
    }

    equals  = lambda a,b: True if a == b else False
    next_to = lambda a,b: True if a == b - 1 or a == b +1 else False
    left_of = lambda a,b: True if a == b - 1 else False
                        
    perm = list(permutations(range(1, 5+1)))
    for red, green, white, yellow, blue in perm:
        if not left_of(green, white):
            continue
        for brit, swede, dane, norwegian, german in perm:
            if not ( equals(brit, red) and next_to(norwegian, blue) ):
                continue
            for tea, coffee, milk, beer, water in perm:
                if not ( equals(dane, tea) and equals(green, coffee) and \
                         milk == 3         and norwegian == 1 ):
                    continue
                for pallMall, dunhill, blends, blueMaster, prince in perm:
                    if not ( equals(yellow, dunhill) and equals(blueMaster, beer) and \
                             equals(german, prince)  and next_to(blends, water) ):
                        continue
                    for dogs, birds, cats, horses, fish in perm:
                        if not ( equals(swede, dogs)   and equals(pallMall, birds) and \
                                 next_to(blends, cats) and next_to(horses, dunhill) ):
                            continue

                        # combines old order strings to the newly ordered values then sorts them
                        # ('red'     , 3), ('green'  , 4), ('white' , 5), ('yellow'    , 1), ('blue'  , 2)
                        # ('brit'    , 3), ('swede'  , 5), ('dane'  , 2), ('norwegian' , 1), ('german', 4)
                        # ('tea'     , 2), ('coffee' , 4), ('milk'  , 3), ('beer'      , 5), ('water' , 1)
                        # ('pallMall', 3), ('dunhill', 1), ('blends', 2), ('blueMaster', 5), ('prince', 4)
                        # ('dogs'    , 5), ('birds'  , 3), ('cats'  , 1), ('horses'    , 2), ('fish'  , 4)
                        g = lambda x,y: [i for i,j in sorted(zip(x, y), key=lambda z: z[1])]

                        # iterate through solved positions
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