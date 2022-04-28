Welcome to the create_task_quiz repository!

### Contributors: Saathvika Ajith & Linda Liu

## Ideas
We have two unique and exciting personality quizzes that you can take to learn more about yourself! These interactive quiz games are called: "Which Blackpink Member Are You?" and "Which Greek Goddess Are You?" and they contain multiple features such as a card hover interaction in the homepage, pause and play music buttons, animated navigation buttons, header image changing buttons, a random Blackpink fact generator API, and finally the actual quizzes themselves which include unique questions and images to help you figure out who your personality is the most similar to. Our project expresses creativity and explores our personal interests through the topics of the quizzes, the formatting and CSS, and our own original quiz questions. In each quiz, there are a total of 4 questions that contain 4 different options. A numerical value (1, 2, 3 or 4) will be assigned to each of the options, and different ranges of ending point values will correspond to different Blackpink members or Greek Goddesses.

## Requirements
| Requirements       |  Implementation |
| :----:     |     :----:     |
| Program Purpose and Function |  Input will come from user clicking the user's choice under each of the questions. Program output will return based on which person's number range the total score of user falls within.     |
|  Data Abstraction  |  The list of facts in random BLACKPINK fact generator. A random math function will generate an index for this list to select a random fact and display it on the page.   |
| Managing Complexity   | The code will be strictly organized. The assets folder containing all the images for the quizzes is divided into 2, and the CSS for each quiz is located in the header to reduce the number of extra files. Each quiz is in it's own html separate from the main page and main.py is organized accordingly.  The numerous functions in our programs are always at the end in a script tag after the html code in the body tag. |
|  Procedural Abstraction  |  Functions in our program are written in Javascript in one location, and called one or more times in html in other locations.   |
| Algorithm Implementation|  There is an algorithm that tallies up the users’ answers to the quiz and determines which person their personality is the most like. A numerical value is assigned to each of the options, and different ranges of endpoint values will correspond to different BLACKPINK members/Greek Goddesses.    |
