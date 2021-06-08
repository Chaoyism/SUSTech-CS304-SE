# Suggestion on the Final Exam

## FYI
@Author Chaoyi
@Email wangcy2018@mail.sustech.edu.cn

## Basics
In 2021Spring, the exam has multiple-choice (about 27 questions) and essay questions (about 5 questions).
The time should be sufficient, don't worry about that.
The exam designer must be a fan of Pokemon-Go (a game), so it would be good if you have some background knowledge on the game. In 2021Spring and 2020Spring, the exams were both full of Pokemon-related things.

## Multiple Choice
I cannot remember much on this part. 

A good advice would be: read slides on both lec and lab carefully and try to memorize all the mentioned programs. For instance:
- JaCoCo
- Prapr
- PIT
- PMD
- Dex2Jar
There are at least 4 questions are asking you which of the four given choices is used for some goal. For example, which is NOT used to decompile a Java program?

And you'd better know what the three components in PMD are specifically responsible for. For example, there were two questions like: what kinds of code norm (unused method, weird naming...) would NOT be checked by PMD?

A question asked what is the step after Continuous Integration (mentioned in a picture in the slides of CI).

A question asked which one is NOT included in the 10 principles of designing a UI (very obvious in fact).

A question asked some details about Mutation Test. Read the text carefully.

## Essay Question
There were 5 essay questions in 2021Spring. They are (may not be in order):
1. Smoke Test
    1. Briefly explain what Smoke Test is.
    2. If you are given a Pokemon Ball (the usage is explained in the text), describe how you are going to apply Smoke Test to the ball.

2. Re-engineering (I think this should be reverse engineering, but not sure. The original word used here is re-engineering.)
    1. If you are given a source code of an Android app (about 10,000 lines of code), what re-engineering pattern would you apply to the code?
    2. Why?

3. You are given a part of a Java code, it would be like this:
```
import ...
public class A() {
    public static void B(String str) {
        if (D) {
            ...
        } else {
            str = C(str);
        }
        ...
        return str;
    }
    private static void C(String str) {
        if (E) {
            ...
        }
        return str;
    }
}
```

    1. Write two JUnit test methods to test method B. The first test should enter the "if" branch while the second test should not. The code written should be able to compile.
    2. Write JavaDoc for the method. The JavaDoc should include a brief description and what parameter and return value is.
    3. There was question 3 but I cannot remember...

4. Extreme Programming (XP)
    1. Describe two practices of XP.
    2. Give two examples of the tools which can build Java program.

5. Git
    1. If you want to commit something to Git with message "lol", what is the command?
    2. If you want to push something to a remote repo which is the origin, what is the command?