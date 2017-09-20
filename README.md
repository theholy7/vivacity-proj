# Vivacity Labs Coding Challenge - Python

Please read the [challenge specification](VivacityCodingChallenge.pdf) before this.

This is the Python coding challenge for Vivacity Labs. We have given you some skeleton code for the basic structure of the each part. When you have completed the challenge we should be able to run the the tests we have provided. Please refrain from adding any additional unit tests.

## Install

This is written in [python](https://www.python.org/). You can complete the challenge in python 2.7 or python 3. Whatever you prefer, please provide a virtual environment and instructions on how to run your code.

## Coding

When coding please feel free to use external libraries if you feel they fit well or are needed.

You may add extra files with additional functions to call or add functions to the files we have given you but keeping the original function calls the same.

## Running

To run the code, please run in your preferred method may that be importing the file in python cli or creating main file to run. Please just make sure that this process is easily emulated on other machines and there is no IDE specific commitments.

## Testing

We have added some very basic unit tests, these basically take the examples from the specification file and turn them into [unit tests](https://docs.python.org/2/library/unittest.html). You do not need experience with unit tests, just run the provided command:

```
$ python -m unittest tests
```

Initially all these tests will fail but as you complete each part you should see these tests passing.

**N.B.**
As you are progressing through each section, some tests might take some time to complete. In order to speed up testing on certain sections you can choose to run only some of the tests. For example if you want to run just the hash collision tests you could do:

```
$ python -m unittest tests.HashIteratorTests
```

This will only run this test class, you can also do:

```
$ python -m unittest tests.HashIteratorTests.test_codequality_3
```

This will run just the code quality salt test for this class.

### Coordinate System

There is also a coordinate system folder, you can use this to really stress test your code as it gives valid files to build a large map from multiple files. You can then use this to see how your system behaves with multiple files, large maps and deep path finding.

**Good Luck**

