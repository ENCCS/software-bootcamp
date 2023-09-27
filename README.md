# RISE Software Bootcamp

> [!NOTE]
> - Online via Zoom
> - Dates: November 6-10 and 13-17
> - Time: 10:00-12:00 and 13:00-15:00 every day

## Target audience

The *RISE Software Development Bootcamp* is a practical training program meant for both new and experienced RISE team members. It's meant to help newcomers understand programming and good software practices, and for our seasoned researchers to gain new skills to solve new types of problems.

The bootcamp covers several topics: we start with the basics of the Unix shell and move on to beginner and intermediate programming in Python or Julia (in parallel tracks). We also teach how to use Git for version control, especially when working with a team. We moreover focus on good practices in software testing, writing documentation, developing modular code, and understanding licensing. These skills will help you make software that's easy to maintain, reuse, and share - what we call [FAIR software](https://www.nature.com/articles/s41597-022-01710-x).

 
Our bootcamp offers a welcoming and useful environment for learning many necessary practical skills that are typically not taught in university education. We're looking forward to having you with us!

## Prerequisites

- You should be prepared to install software on your own laptop and bring it to the bootcamp - see below.
- Some previous experience with programming is advantageous but not mandatory - the first day is devoted to introductory topics.

## Before the bootcamp

Before attending the bootcamp, please follow carefully the installation instructions below (click the arrow) to make sure that all tools and packages that will be needed during the bootcamp are installed correctly on your computer.

<details>
  <summary>Installation instructions</summary>
 
You will need the following tools installed on the computer you will use during the bootcamp. Please go through this list carefully and make 
sure to install everything that you don't already have installed. The links take you to external installation instructions for different operating systems.
- Shell and Git - [instructions](https://coderefinery.github.io/installation/shell-and-git/)
- A GitHub account - [instructions](https://coderefinery.github.io/installation/github/)
- SSH connection to GitHub - [instructions](https://coderefinery.github.io/installation/ssh/)
- A text editor - [instructions](https://coderefinery.github.io/installation/editors/)
   - **Sublime Text** is also a good text-based code editor to use for Win, Linux, and Mac OS - [instruction](https://www.sublimetext.com/download)
- Python via one of two ways:
   - through the Anaconda distribution - [instructions](https://carpentries.github.io/workshop-template/install_instructions/#python-1)
   - or if you already have a Python installation and the `conda` package manager on your computer, make sure to install the required packages listed in the following yaml file by saving it to a file `env.yml` and then run `conda env create -f env.yml`:
     ```yaml
        name: bootcamp
        channels:
          - conda-forge
          - defaults
          - bioconda
        dependencies:
          - python>3.9
          - click
          - ipywidgets
          - jupyterlab
          - jupyterlab-git
          - matplotlib
          - myst-parser
          - nbdime
          - numpy
          - pandas
          - pytest
          - pytest-cov
          - snakemake-minimal
          - sphinx
          - sphinx-autobuild
          - sphinx_rtd_theme
          - jsonlines
          - notebook
          - requests
          - seaborn
          - mpi4py
          - dask
          - setuptools
          - twine
          - poetry
          - flit
     ```

</details>

## Learning objectives

By attending this bootcamp, you will:

- Gain confidence in developing software and using modern tools for collaborative software engineering.
- Become comfortable with working in the Unix terminal.
- Understand how Git enables transformative workflows for collaborative software development.
- Understand the importance of good software development practices such as testing, documentation and dependency management.
- Reflect on how FAIR principles can be applied to software.
- Know which factors contribute to reproducible and reusable software.
- Obtain hands-on experience in using modern software development tools and practices.
- Know where to go next to further develop your skills.

After attending the bootcamp and completing all hands-on exercises, you will be well equipped to contribute to programming tasks in your projects at RISE.  

## Course leaders

- Anastasiia Andriievska
- Martin Simonsson
- Yonglei Wang
- Thor Wikfeldt

## Schedule

**Day 1 - Unix and Python introduction**

- 10:00-10:30 Welcome and general introduction (Everyone)
- 10:30-12:00 Unix basics
  - 10:30-10:35 [Introducing the Shell](https://swcarpentry.github.io/shell-novice/instructor/01-intro.html) (AA and TW)
  - 10:35-11:10 [Navigating Files and Directories](https://swcarpentry.github.io/shell-novice/instructor/02-filedir.html) (AA and TW)
  - 11:10-11:40 [Working With Files and Directories](https://swcarpentry.github.io/shell-novice/instructor/03-create.html) (AA and TW)
  - 11:40-12:00 Where to go from here: pipes, filters, loops, shell scripts, finding things.
- 13:00-15:00 Python intro
  - 13:00-13:30 [Writing Python in Jupyter](https://aaltoscicomp.github.io/python-for-scicomp/jupyter/) (AA and YW)
  - 13:30-14:00 [Writing Python in VSCode](https://code.visualstudio.com/docs/introvideos/basics) (AA and YW)
  - 14:00-14:30 [Basic introduction to Python](https://aaltoscicomp.github.io/python-for-scicomp/python/) (YW and AA) 
  - 14:30-15:00 [Python scripts](https://aaltoscicomp.github.io/python-for-scicomp/scripts/) (YW and AA)


**Day 2 - Python intermediate**

- 10:00-10:10 Recap of what we learned yesterday
- 10:10-12:00 Python intermediate
    - 10:10-11:00 [Numpy](https://aaltoscicomp.github.io/python-for-scicomp/numpy/) (MS and YW)
    - 11:00-12:00 [Pandas](https://aaltoscicomp.github.io/python-for-scicomp/pandas/) (MS and YW)
- 13:00-15:00 Python intermediate
    - 13:00-13:50 [Visualisation with Matplotlib](https://aaltoscicomp.github.io/python-for-scicomp/data-visualization/) (YW and MS)
    - 13:50-14:20 [Data formats with Numpy and Pandas](https://aaltoscicomp.github.io/python-for-scicomp/data-formats/) (YW and MS)
    - 14:20-14:50 [Web APIs with Python](https://aaltoscicomp.github.io/python-for-scicomp/web-apis/) (AA and TW)
    - 14:50-15:00 Where to go from here: [advanced Numpy](https://aaltoscicomp.github.io/python-for-scicomp/numpy-advanced/)

    
**Day 3 - Python intermediate**

- 10:00-10:15 Recap of what we learned yesterday
- 10:15-12:00 Python intermediate
    - 10:15-10:30 [Scipy](https://aaltoscicomp.github.io/python-for-scicomp/scipy/) (MS and)
    - 10:30-11:00 [Library ecosystem](https://aaltoscicomp.github.io/python-for-scicomp/libraries/) (MS and)
- 13:00-15:00 Python intermediate
    - 13:00-13:30 [Parallel programming](https://aaltoscicomp.github.io/python-for-scicomp/parallel/) (TW and YW)
    - 13:30-14:00 [Dependency management](https://aaltoscicomp.github.io/python-for-scicomp/dependencies/) (AA and TW)
    - 14:00-14:50 [Packaging](https://aaltoscicomp.github.io/python-for-scicomp/packaging/) (AA and TW)
    - 14:50-15:00 Where to go from here: [Accelerating Python, porting to GPUs](https://enccs.github.io/hpda-python/).

**Day 4 - Python intermediate, more Unix, and HPC**

- 10:00-11:00 Buffer time, Q&A session and discussions.
- 11:00-12:00 Unix intermediate:
   - 11:00-11:35 [Pipes and filters](https://swcarpentry.github.io/shell-novice/instructor/04-pipefilter.html) (AA and TW)
   - 11:35-12:00 [Loops](https://swcarpentry.github.io/shell-novice/instructor/05-loop.html) (AA and TW)
- 13:00-15:00 Intermediate Unix
    - 13:00-13:25 [Loops contd.](https://swcarpentry.github.io/shell-novice/instructor/05-loop.html) (AA and TW)
    - 13:25-14:10 [Shell scripts](https://swcarpentry.github.io/shell-novice/instructor/06-script.html) (YW and AA)
    - 14:10-14:50 [Finding things](https://swcarpentry.github.io/shell-novice/instructor/07-find.html) (YW and AA)
    - 14:50-15:00 Where to go from here: [awk](https://pmitev.github.io/to-awk-or-not/) etc.


**Day 5 - HPC and Cloud**

- 10:00-12:00 High performance computing
   - 10:00-10:20 [Why use a cluster?](https://carpentries-incubator.github.io/hpc-intro/10-hpc-intro/index.html) (YW and TW)
   - 10:20-10:55 [Connecting to a remote HPC system - using LUMI](https://carpentries-incubator.github.io/hpc-intro/11-connecting/index.html) (YW and TW)
   - 10:55-11:20 [Exploring Remote Resources](https://carpentries-incubator.github.io/hpc-intro/12-cluster/index.html) (YW and AA)
   - 11:20-11:50 [Scheduler fundamentals](https://carpentries-incubator.github.io/hpc-intro/13-scheduler/index.html) - [Interactive SLURM playground](http://slurmlearning.deic.dk/) (TW and AA)
   - 11:50-12:00 Where to go from here: Getting EuroHPC access via ENCCS, [Module systems](https://carpentries-incubator.github.io/hpc-intro/14-modules/index.html), [Running parallel jobs](https://carpentries-incubator.github.io/hpc-intro/16-parallel/index.html), [Transferring files to remote computers](https://carpentries-incubator.github.io/hpc-intro/15-transferring-files/index.html) (TW)
- 13:00-15:00 Cloud
   - 13:00-15:00 ICE data center (Johan Kristiansson)

**Day 6 - Introduction to Git**

- 10:00-12:00 Git introduction
   - 10:00-10:15 [Motivation](https://coderefinery.github.io/git-intro/motivation/) (AA and MS)
   - 10:15-11:10 [Basics](https://coderefinery.github.io/git-intro/basics/) (AA and MS)
   - 11:10-12:00 [Branching and merging](https://coderefinery.github.io/git-intro/branches/) (MS and AA)
- 13:00-15:00 
    - 13:00-13:30 [Conflict resolution](https://coderefinery.github.io/git-intro/conflicts/) (MS and TW)
    - 13:30-14:00 [Sharing repositories online](https://coderefinery.github.io/git-intro/remotes/) (TW and MS)
    - 14:00-14:45 [Inspecting history](https://coderefinery.github.io/git-intro/archaeology/) (TW and AA)
    - 14:45-15:00 [How much Git is necessary?](https://coderefinery.github.io/git-intro/level/) (TW and AA)

**Day 7 - Introductory and intermediate Git**

- 10:00-12:00 Git introduction
   - 10:00-10:10 [What to avoid](https://coderefinery.github.io/git-intro/what-to-avoid/) (YW and AA)
   - 10:10-10:30 [Using the Git staging area](https://coderefinery.github.io/git-intro/staging-area/) (YW and AA)
   - 10:30-11:00 Where to go from here: [Undoing and recovering](https://coderefinery.github.io/git-intro/recovering/), [Interupted work](https://coderefinery.github.io/git-intro/interrupted/), [Aliases and configuration](https://coderefinery.github.io/git-intro/aliases/), [Git under the hood](https://coderefinery.github.io/git-intro/under-the-hood/) (AA and YW)
   - 11:00-12:00 [Social coding and open software](https://coderefinery.github.io/social-coding/) (MS and YW)
- 13:00-15:00 Git intermediate
    - 13:00-13:15 [Concepts around collaboration](https://coderefinery.github.io/git-collaborative/remotes/) (TW and MS)
    - 13:15-14:15 [Centralised workflow](https://coderefinery.github.io/git-collaborative/centralized/) (TW and MS)
    - 14:10-15:00 [Distributed version control and forking workflow I](https://coderefinery.github.io/git-collaborative/distributed/) (TW and MS)

**Day 8 - Intermediate Git, Jupyter, Reproducibility**

- 10:00-12:00 Git intermediate
   - 10:00-10:30 [Distributed version control and forking workflow II](https://coderefinery.github.io/git-collaborative/distributed/) (TW and YW)
   - 10:30-11:00 [How to contribute changes to somebody else’s project](https://coderefinery.github.io/git-collaborative/contributing/) (TW and YW)
   - 11:00-12:00 Buffer time, Q&A session, discussions and where to go from here: [Git cheatsheet](https://aaltoscicomp.github.io/cheatsheets/git-the-way-you-need-it-cheatsheet.pdf).
- 13:00-15:00 Jupyter and Reproducibility
    - 13:00-13:20 [Notebooks and version control](https://coderefinery.github.io/jupyter/version-control/) (AA and TW)
    - 13:20-13:50 [Sharing notebooks](https://coderefinery.github.io/jupyter/sharing/) (AA and TW)
    - 13:50-14:00 [Reproducible research - Motivation](https://coderefinery.github.io/reproducible-research/motivation/) (TW)
    - 14:00-14:10 [Organising your projects](https://coderefinery.github.io/reproducible-research/organizing-projects/) (AA and TW)
    - 14:10-14:40 [Recording computational steps](https://coderefinery.github.io/reproducible-research/workflow-management/) (AA and TW)
    - 14:40-15:00 Buffer time, Q&A session and discussions.


Day 9 - Reproducibility and Documentation

- 10:00-12:00 Reproducibility
   - 10:00-10:30 [Recording dependencies](https://coderefinery.github.io/reproducible-research/dependencies/) (TW and AA)
   - 10:30-11:00 [Recording environments - containers](https://coderefinery.github.io/reproducible-research/environments/) (TW and AA)
   - 11:00-11:30 Q&A, where to go from here: [More on containers](https://enccs.github.io/containers/).
   - 11:30-11:45 [Documentation - motivation and wish list](https://coderefinery.github.io/documentation/wishlist/) (TW and AA)
   - 11:45-12:00 [Documentation - Popular tools and solutions](https://coderefinery.github.io/documentation/tools/) (TW and AA)
- 13:00-15:00 Documentation
    - 13:00-13:20 [In-code documentation](https://coderefinery.github.io/documentation/in-code-documentation/) (TW and AA)
    - 13:20-13:50 [Writing good README files](https://coderefinery.github.io/documentation/writing-readme-files/) (TW and AA)
    - 13:50-14:20 [Sphinx and Markdown](https://coderefinery.github.io/documentation/sphinx/) (TW and AA)
    - 14:20-14:50 [Deploying Sphinx documentation to GitHub Pages](https://coderefinery.github.io/documentation/gh_workflow/) (TW and AA)
    - 14:50-15:00 Where to go from here: [Hosting websites/homepages on GitHub Pages](https://coderefinery.github.io/documentation/gh-pages/)

**Day 10 - Testing and Modular code development**

- 10:00-12:00 Software testing
   - 10:00-10:15 [Motivation](https://coderefinery.github.io/testing/motivation/)  (TW and MS)
   - 10:15-10:40 [Testing locally](https://coderefinery.github.io/testing/pytest/) (TW and MS)
   - 10:40-11:10 [Automated testing](https://coderefinery.github.io/testing/continuous-integration/) (TW and MS)
   - 11:10-11:40 [Test design](https://coderefinery.github.io/testing/test-design/) (TW and MS)
   - 11:40-11:50 [Conclusions and recommendations](https://coderefinery.github.io/testing/conclusions/) (TW and MS)
   - 11:50-12:00 Where to go from here: [full-cycle collaborative workflow](https://coderefinery.github.io/testing/full-cycle-ci/)
- 13:00-15:00 Modular code development and wrap-up
    - 13:00-14:00 [Slides](http://cicero.xyz/v3/remark/0.14.0/github.com/coderefinery/modular-code-development/master/talk.md/#1) or [Type-along](https://coderefinery.github.io/modular-type-along/) (TW and MS)
    - 14:00-15:00 Q&A, discussion, final words.




