from constraint import *

def main():
    problem = Problem()

    variables = {
        'houses' : ['red'     , 'green'  , 'white' , 'yellow'    , 'blue'  ],
        'races'  : ['brit'    , 'swede'  , 'dane'  , 'norwegian' , 'german'],
        'drinks' : ['tea'     , 'coffee' , 'milk'  , 'beer'      , 'water' ],
        'smokes' : ['pallMall', 'dunhill', 'blends', 'blueMaster', 'prince'],
        'pets'   : ['dogs'    , 'birds'  , 'cats'  , 'horses'    , 'fish'  ]
    }

    # addVariables: each list gets numbered 1 - 5
    # addConstraint: apply exclusivity
    for values in variables.values():
        problem.addVariables(values, range(1,5+1))
        problem.addConstraint(AllDifferentConstraint(), values)

    # constraints: equal
    for i in (
        ["brit"      , "red"  ], ["swede" , "dogs"   ],
        ["dane"      , "tea"  ], ["green" , "coffee" ],
        ["pallMall"  , "birds"], ["yellow", "dunhill"],
        ["blueMaster", "beer" ], ["german", "prince" ]
    ):
        problem.addConstraint(lambda a, b: a == b, i)

    # constraints: next_to
    for i in (
        ["blends"   , "cats"], ["horses", "dunhill"],
        ["norwegian", "blue"], ["blends", "water"  ]
    ):
        problem.addConstraint(lambda a, b: a == b - 1 or a == b + 1, i)

    # constraints: left_of, middle, first
    problem.addConstraint(lambda a, b: a == b - 1, ["green"    , "white"])
    problem.addConstraint(lambda a: a == 3       , ["milk"              ])
    problem.addConstraint(lambda a: a == 1       , ["norwegian"         ])

    solution = problem.getSolution()

    def order(key):
        for position, array in enumerate(variables.values()):
            if key in array:
                return position

    ordered = [ 
        sorted([ k for k,v in solution.items() if v == i], key=lambda x: order(x) ) 
            for i in range(1, max(solution.values())+1)
    ]

    # transpose & format output
    for i in map(list, zip(*ordered)):
        print("{:10s} {:10s} {:10s} {:10s} {:10s}".format(*i))


if __name__ == "__main__":
    main()