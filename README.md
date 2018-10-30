Assembler program written in python3.

main.py is a main driver code. There are several modules which are imported in main.py file.
To run code type,
        
            python3 main.py [action] [filename]

where,
    main.py is a driver code
    actions are (-s,-l,-i,-lst)
                -s   ->  For symbol table
                -l   ->  For literal table
                -i   ->  For intermediate table
                -lst ->  For lst file generation

When -i option is selected, additional 'intermediate.txt' file will be generated. This file contains the intermediate code.
