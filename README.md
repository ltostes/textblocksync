# textblocksync
Python code to sync text blocks across multiple files.

## Getting Started

Python script file must be placed in the root folder of the project, together with the syncblock.json file that has the parameters for block syncing.

### Prerequisites

You must have python 3.x installed.

### Configuring

First you must specify the parameters inside the syncblock.json to let the script know what are the *base code blocks* and what are the *block start* and *block end* parameters so that it will be copied into the specified files that will use it. Then run the script and voila!

In this example, we are using code blocks inside *baseblock1.txt* and *baseblock2.txt*

Configuration file is as follows:

```json
{
    "base_blocks" : {
        "Block1": {
            "file": "./example/baseblock1.txt",
            "block_start": "-- Beginning of block 1",
            "block_end": "-- End of block 1"
        },
        "Block2": {
            "file": "./example/baseblock2.txt",
            "block_start": "** Block 2 start",
            "block_end": "** Block 2 end"
        },
        "File1": {
            "file": "./example/file1.txt",
            "block_start": "+ F1S",
            "block_end": "+ F1E"
        }
    },
    "use_blocks" : [
        {
            "blocks": ["Block1"],
            "file": "./example/file1.txt"
        },
        {
            "blocks": ["File1","Block2"],
            "file": "./example/file2.txt"
        }
    ]
}
```

An example file that has a code block in it:

```
This is the file that contains base block 1.
-- Beginning of block 1
this is block 1
it contains a lot of content
...
or not
-- End of block 1
This is the rest of the file
We don't care about it
```

And this is a file that receives a codeblock and has a codeblock (with the other codeblock inside)

```
This is file 1.
This is where we start using the code blocks. We also might reuse it inside others (file 2 for instance).
+ F1S
This is where block 1 should go in. With header, end and all.
-- Beginning of block 1
you should not read this.
-- End of block 1
We will also use a block that contains another block unblocking everything or blocking I'm lost.
+ F1E
Don't care.
``` 

## Important

Pay attention to the order in which the use_blocks are configured (to avoid inconsistencies and erroneous block sync).

## Author

* **Lucas Tostes** - *Initial work* - [ltostes](https://github.com/ltostes)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Wohoo
