## Create Task Ideas
Complex interactive quiz game called "Which BLACKPINK Member Are You?" that can be implemented into the Break Time portion of our website and contains multiple features which expresses creativity. There is a total of 4 questions that contains 4 different options. A numerical value (1, 2, 3 or 4) will be assigned to each of the options, and different ranges of ending point values will correspond to different BLACKPINK members.

Feature ideas: random BLACKPINK fact generator, display BLACKPINK's top YouTube mvs, changeable backgrounds using buttons <br> 


## Requirements
- Requirements   |  Implementation 
- Program Purpose and Function - | Input will come from user clicking his/her choice under the questions. Program output will return based on which member's number range did the total score of user fells within.     
-  Data Abstraction -  | A list of facts in random BLACKPINK fact generator. A random math function will generate an index for this list to select a random fact and display it on the page.   
- Managing Complexity - | The code will be strictly organized. Instead of the facts being stored in individual variables, they are stored in a single list. Without this list the code will be unorganized and the list allows the fact to be called easier. The list containing the word that the user guessed will be called in multiple places to see if any of the letters match any of the corresponding letters in the real word list.   
- Procedural Abstraction -  | Functions in js file will be called multiple times in different places. For example, a function to display facts and change background will be in a seperate js file and be called in the html file using functionName().   
- Algorithm Implementation -  | There will be an algorithm that tallies up the users’ answers to the quiz and determines which member their personality is the most like. A numerical value will be assigned to each of the options, and different ranges of ending point values will correspond to different BLACKPINK members.    


