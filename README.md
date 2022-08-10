# Test Driven Development

### What is it?

 Test Driven Development (TDD) is a software development practice that focuses on creating unit
 test cases before developing the actual code. It is an iterative approach that combines
 programming, the creation of unit tests, and refactoring.
- Tiny mistakes have big impacts (AGILE)

TDD allows us to express intent in the form of a test
1) Create the tests
2) Test the test by running and seeing it fail
   (Now we know it is testing something useful)
3) Create the minimum code to meet the needs of the test. Run it and see it pass.
4) Stable state or passing state, (refactor test and code for quality and generality)
5) Repeat

- Red, Green, Refactor

Unit testing is about testing
TDD is about design

### Benefits of TDD
- it works
- easy to read
- testable
- easy to change
- simple
- efficient


### Attributes of TDD
- Modular 
- Loosely coupled
- Cohesive
- Separation of Concerns
- Information Hiding

### How to use Pytest

- pip install pytest
- call `pytest "filename"` in terminal
