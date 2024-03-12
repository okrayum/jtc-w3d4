# W3D4 After Class Assignment

## Task Description

- Design a simple database schema for a blogging platform, considering the relationships between users, posts, and comments.
- Implement the defined schema in both JavaScript and Python.
- Use appropriate technologies and frameworks for connecting applications to databases, showcasing the versatility of integration.
- Test your implementations to ensure seamless interaction between the application and the database.

## Getting Started

- For the JavaScript example, navigate to the 'JavaScript' directory and run `npm install` to install the required dependencies.
- The Python example is ready to use.

## Test Script Images

- JavaScript

![CRUD Tests](/JavaScript/testJS.png)

- Python

![CRUD Tests](/Python/testPy.png)

## Reflection

My main challenge was never having used SQL databases until this lesson. It was alot to learn. I based these examples off of what we covered in class. I was unfamiliar with the command-line interface for SQLite, so I focused on working entirely within VS Code. I like the simplicity that SQL can work with JavaScript and Python similarly. There weren't many differences in the syntax going from Python to JavaScript. My previous experience has been with MongoDB/Express, where referencing another ID is done by using `ref:`. It was interesting to learn that it works the same as `FOREIGN KEY` in SQLite. This realization helped to understand the relationship between foreign keys much better. Overall I guess the biggest problem I ran into, which took several days to fix. Is that I could not get the `DELETE ON CASCADE` to work. At first I would get no erors or messages, but also no deletion of related data. Then I finally got it to give an error about foreign_keys contraints. I still am not really sure how I fixed it, but I ended up specifically declaring `"PRAGMA foreign_keys = ON;"` then deleting the databases and starting over. That seemed to work. I wish I knew exactly what it was but I think I know the steps to try the next time I do this. 
