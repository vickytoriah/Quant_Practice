# Hi and welcome to my Quant_Practice repo!

This repo is mainly meant for personal tracking of my OOP learning process in Python and C++ (will add later on). 

During my MSc Finance at Imperial College London, where I did additional courses, including Computational Finance in C++ 17 and 20 (Certified), and VBA in Excel, as well as various personal projects in Python 3.x, I became more keen on a career path as a quantitative analyst. 

So I want to advance my applicable skillsets by developing and practicing my coding skills through continuous projects, and will use this repo to track my process. 

Therefore, I am more than willing to receive feedback, comments and suggestions from (more) experienced programmers. [^1]


<details>
  <summary>Structure of Repo Contents</summary>
  
_I plan on making a core package that all packages will have access to, as they will be utility tools and functions that may be applicable to many cases._
  
Each package will relate/refer to a (popular) quantitative finance question, which I will provide details for. They will each have 4 versions of my solution, all of which will be object-oriented programming. The solution will solely reflect my understanding of   the problem, my intuition and thought process when solving it. 
  
*Please note: not all 4 versions will be out, as I started this in September 2023, and am not doing this full-time*

</details>

<details>
  <summary>Purpose of Repo</summary>
  
  ## What are the 4 versions? And, why 4 versions of the same solution?
  
  The 4 versions will be referred to in this fixed order and are the following:
  1. Python: OOP (standard, e.g., dynamic, classes, etc.)
  2. Python: OOP (standard + more advanced methods, e.g., decorators and or other concepts I learn later on)
  3. Python: OOP (standard + ABC)
  4. C++: OOP (standard)

## Reason for 4 versions
  
I learn best through practical applications, and whilst the answer and my interpretations may require self-study as well, the focus of this repo is to convey my understandings in a quantitative manner. 

Since my answer will be consistent between the 4 versions, it will be the easy factor to keep constant as I learn how to apply advanced programming methods and convey my thought-process. Therefore, if I can re-iterate my answer in all 4 versions, then I will be able to learn the systematic logic for each version type, and improve my computing, programming, and quantitative skills simultaneously.  

As I am really interested in learning the in-depth computer science rather than just the simple syntax differences between languages, I am focusing on OOP and C++ to further develop the skills' depth.
  
I am a multilinguist (native fluency in English, German and Chinese, conversational fluency in French), and easily pick up new subjects, languages and concepts, thus I do not find functional programming too difficult to learn within a few weeks or shorter. I learned SQL, R, Python, and VBA within a few hours for certain projects.

This is also why I decided to learn computational finance in C++, and became certified at Imperial College London. 
  
</details>

<details>
  <summary>Questions Answered & Versions Completed

   _This list will be continuously updated over time_
  </summary>
  
1. [Anthill_Food_Finding](https://github.com/vickytoriah/Quant_Practice/tree/main/Anthill_Food_Finding/)
  
    - Python: 1st Version
    - Python: 2nd Version
  
      - Upcoming versions:
							- Python 3rd version
							- [C++ version](https://github.com/vickytoriah/Quant_Practice/tree/main/Anthill_Food_Finding/anthill/c%2B%2B)[^2]
      
2. Systematic Trading Model [^3]

[^1]: Please also let me know if my repo has security issues, as I am still relatively new to the more advanced settings on GitHub.
[^2]: Please see the next section for details. 
[^3]: This is ready in another repo, however due to MNPI, I will slowly upload my IP for various segments of my model and its utility and core functions in this repo
</details>

<details>
	<summary>Next steps: Monte Carlo Implementation Using Matrix in C++</summary>

	### Overview

The [C++ folder in this repository]() is a work-in-progress implementation of Monte Carlo simulation using matrices in C++. The code is organized into separate files, each with its own `main` function, to facilitate unit testing and modular development.

	### Project Structure

-`monte_carlo.cpp`: Core implementation of the Monte Carlo simulation using matrices.

-`anthill.cpp`: Entry points for running sample simulations and testing individual components. It will import `anthill.h`, `monte_carlo.h`, and `coordsMatrix.h`. 

-`coordsMatrix`.cpp: Matrix constructor and extender that generates a Random Walk and determines the movement based on defined objects of class CoordsMatrix in `CoordsMatrix.h`. 

-`*.h`: Each Header file will define the objects and variables for it's respective *.cpp. 
	- `anthill.h`: defines the class Anthill and its objects and methods.

	- `*.h`: Most of these will be combined into a utility.cpp once everything is tested and structured efficiently. Currently, they are kept separate for testing and learning purposes. 


**Please note**

*The code is currently a preliminary draft and is divided into separate files for testing purposes.*

The goal is to create optimal functions for Monte Carlo simulations and various utility functions that future Quant Fin problems can use to solve a wide range of applications.

As I work towards the solutions in C++, it is likely that different versions of the solution will exist and be kept (like in Python).

As the solutions for each function become functional, the files will be edited and linked accordingly.	

Please kindly understand that this is a learning process, and an interest-driven personal project, so the commits are to track my progress and solutions rather than just the complete solutions on my first tries. 

Thank you! 

_I will most likely restructure this folder in a similar way to the Python ones, where several versions of a solution will exist in C++._

</details>