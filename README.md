# pyGitHub_API

Set of functions that integrate with GitHub's own API, in an efford to simplify it's aplication in python projects.

# What is this?

This is an attempt at writting an API [(what's an API?)](https://en.wikipedia.org/wiki/Application_programming_interface) for compatibility with
python bots. It contains a set of functions that can fetch JSON data from GitHub's own API.

This is a work in progress, so there might be (definitely are) some bugs out there. You are welcome to open
an issue mentioning this. All I ask is for you to start it with [BUG], just to help me sort most stuff.

# What is this not?

This is not a GitHub bot of any sort, or part of any source of such.

Please read the instructions, it also does not work on it's own. It is an API.

# How can I use it then?

As you use Telegram's API: as an API. You import this module in your script and call functions directly from it.

`import project.modules.functions.git_api as git`

If you do it like this, all you need to do to call a function from it is:

`git.function()`

That's pretty much it. Enjoy.

# Extra info:

I reserve the rights to take down this project, change any of these information/disclaimer files, and to revoke
or change the license under which the project is built, if needed.

# References:

All the methods here created were developed by myself, so the code belongs to me. It is licensed under GPL-3.0, 
which means you are free to use it, even for commercial purposes, as long as it stays open source. For the development
process (past, present and future), I used the [GitHub REST API v3 manual](https://developer.github.com/v3/) as a reference. 
The GitHub API and all it's data, services and products provided do not belong to me in any way, shape or form.
