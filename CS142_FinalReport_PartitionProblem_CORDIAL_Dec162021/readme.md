# NP-Complete Problem: Partition Problem

## **How to run demo**

- **NOTE:** The java program was created using `eclipse IDE`, might be better to use the same IDE to run.
- Download `Partition_Recursive` and `Partition_Recursive` inside `src_code` folder.
- Run the program.



## **Partition Problem**

The _Partition Problem_, or number partitioning, is the task of deciding whether a given multiset S of positive integers can be partitioned into two subsets S1 and S2 such that the sum of the numbers in S1 equals the sum of the numbers in S2.


## **Keypoints/Summary**

- The SUM of the set has to be EVEN
  - If it is ODD then the set CANNOT be divided into two subsets with equal sum
  - If there is a subset of integers that sum up to SUM/ 2 then the remaining integers in the set will also sum to
SUM/ 2
- Brute Force can be used to solve problems
with smaller values
- Dynamic Programming might be efficient with higher values (relative to brute force capacity) as long as the sum does not go near 2 ^n values (exponential sum)



### **How to solve?**
Following are the two main steps to solve this problem:

- Calculate the sum of the array. If the _sum_ is odd, there can no the two subsets with an equal sum, so return false.
- If the _sum_ of array elements is even, calculate _sum/2_ and call it the _target_. The goal now is to find a subset that has a total sum equal to _target_. We are sure that the remaining elements also sum up equal to _sum/2_ (_target_).
## **Sample Problem**

```
S[] = {3,1,1,2,2,1}
Output: true 
The array can be partitioned as A = {3, 1, 1} and B = {2, 2, 1}
Since, 

Sum of A = 3 + 1 + 1 = 5 and
Sum of B = 3 + 1 + 1 = 5

While, 
arr[] = {1, 5, 3}
Output: false 
The array cannot be partitioned into equal sum sets.
```



### **Algorithms: Recursive**

The goal is to determine each possible combination of elements in the array and calculate its corresponding sum and check whether a subset that has a sum equal to _target_ exist.

Let _isSubsetSum(arr, n, sum/2)_ be the function that returns true if 
there is a subset of arr[0..n-1] with a sum equal to sum/2

The isSubsetSum problem can be divided into two subproblems
-  isSubsetSum() without considering last element 
    (reducing n to n-1)
-  isSubsetSum considering the last element 
    (reducing sum/2 by arr[n-1] and n to n-1)

If any of the above subproblems return true, then return true. 
isSubsetSum (arr, n, sum/2) = isSubsetSum (arr, n-1, sum/2) ||
                              isSubsetSum (arr, n-1, sum/2 - arr[n-1])

<img src = "images/recursive_example.PNG">

#### **_How does this solve a Sudoku puzzle?_**

- Starting from the top-left square of the grid, find an empty square and fill in this square with a number from 1 to 9.
  - If the number adheres to the rules, then move on to the next empty square.
  - If the number has a duplicate in its row, column, or 3x3 grid, then choose the next number from 1 to 9.
  - If all choices from 1 to 9 were checked and contradicted, then go back to the previous square and fill in the next number from 1 to 9.
- Repeat steps until the bottom-right square is reached. (Solution is found)

### **STOCHASTIC SEARCH**

_Stochastic Search_ is an optimization algorithm that incorporates randomness. This is implemented with _Beam Search Algorithm_ that examines a graph by extending the most "promising" node at each level.

#### **_How does this solve a Sudoku puzzle?_**

- Create a series of 10 candidate grids by randomly filling in the empty squares in the puzzle.
- Check how many mistakes each board has.
  - If number is zero, the puzzle is solved
  - If there are mistakes, a set of 4 successors is generated from it by taking two squares in the same row (excluding squares from the original puzzle) and switching their labels
    - Successors are added to the set of candidate grids which is then sorted by the number of mistakes and the 10 grids with the least mistakes are taken
- The process is repeated with the new set of 10 grids until a solution is found.

### **CONSTRAINT PROGRAMMING**

A paradigm that identifies feasible solutions out of a set of candidates where the problem can be modeled in terms of arbitrary constraints.

#### **_How does this solve a Sudoku puzzle?_**

- Create a problem instance
  - Add sudoku input and their indices as variables
  - Add constraints to the problem
    1. No two number in a row should be the same
    2. No two numbers in a column should be the same
    3. No two numbers in a 3x3 grid shold be the same

## **Comparative Analysis**

|                                      | Backtracking                                         | Stochastic Search                            | Constraint Programming                                  |
| ------------------------------------ | ---------------------------------------------------- | -------------------------------------------- | ------------------------------------------------------- |
| **Time Complexity**                  | Ο(N<sup>n<sup>2</sup></sup>)                         | O(b\*n<sup>2</sup>)                          | Ο(N<sup>n<sup>2</sup></sup>)                            |
| **Method**                           | Depth-first search                                   | Breadth-first search                         | Depth-first search                                      |
| **No. of Solutions _(if possible)_** | 1                                                    | 1 or none                                    | At least 1                                              |
| **Advantage**                        | Would always find a solution if there is one         | Possibility of finding a solution right away | Finds all possible solutions                            |
| **Disadvantage**                     | May spend a long time assuming a value that is wrong | Unreliable and problematic                   | Higher run time than backtracking if multiple solutions |

## **Conclusion**

The most common algorithm used in solving a Sudoku puzzle is the backtracking algorithm because it is comparatively easier to implement. It is also best used if there is only one solution, because it is the most stable and is faster than constraint programming in this regard. However, it is best to use constraint programming if you are trying to find multiple solutions. It is best to avoid the stochastic search because this is the most unreliable and unstable. Additionally, this has more lines of code than the previous two.

## **References**

- Overall code: https://fse.studenttheses.ub.rug.nl/22745/1/bMATH_2020_HoexumES.pdf.pdf
- Backtracking: https://www.techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/
- Stochastic Search: https://github.com/ananthamapod/Sudoku
- Constraint Programming: https://gist.github.com/ksurya/3940679
- GeeksForGeeks. (2017, July 16). Sudoku (Explanation) | Backtracking | Set 7 | GeeksforGeeks [Video]. YouTube. https://www.youtube.com/watch?v=l7f9-GNH1j8
- Backtracking algorithm. Programiz. (n.d.). Retrieved from https://www.programiz.com/dsa/backtracking-algorithm.
- Neumann, F., & Witt, C. (2010). Stochastic Search Algorithms. Natural Computing Series, 21–32. doi:10.1007/978-3-642-16544-3_3
- Computerphile. (2020, February 13). Python Sudoku Solver - Computerphile [Video]. YouTube. https://www.youtube.com/watch?v=G_UYXzGuqvM
- What is stochastic search. IGI Global. (n.d.). Retrieved from https://www.igi-global.com/dictionary/stationary-density-stochastic-search-processes/28313.
- Introduction to beam search algorithm. GeeksforGeeks. (2021, July 18). Retrieved from https://www.geeksforgeeks.org/introduction-to-beam-search-algorithm/.
- Google. (n.d.). Constraint optimization. Google. Retrieved from https://developers.google.com/optimization/cp.
- Sudoku puzzles, constraint programming and graph theory. OpenSourc.ES. (n.d.). Retrieved from https://opensourc.es/blog/sudoku/.
- Sudoku: Backtracking-7. GeeksforGeeks. (2021, July 22). Retrieved from https://www.geeksforgeeks.org/sudoku-backtracking-7/.
- Sudoku solver. AfterAcademy. (n.d.). Retrieved from https://afteracademy.com/blog/sudoku-solver.
- Define Beam Search. Javatpoint. (n.d.). Retrieved from https://www.javatpoint.com/define-beam-search.