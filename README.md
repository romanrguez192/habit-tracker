# Habit Tracker

## Description

A habit tracker console application based on [Thomas Frank's method](https://collegeinfogeek.com/paper-habit-tracker/), called the Martin method, which divides every month of the week into two cycles.

The application is build using Python and SQLite database for storing data.

## Languages

The application supports languages such as English and Spanish, with capabilities to add more easily.

## Input

Generally, the application prompts the user with a series of options, each one with a number to insert as input. When being asked to insert the days of a specific habit while creating it, the user depending on the language should use the following format, which uses the first two letters of every day of the week, for instance:

```
Mo We-Fr Su
```

It means that the habit should be executed on Monday, Wednesday, Thursday, Friday and Sunday.

An example in Spanish could be:

```
Lu-Vi Do
```

Which makes the habit go from Monday to Friday and Sunday.

If the user wants to make it a daily habit, writing `D` is enough (both in English and Spanish).
