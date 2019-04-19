# Python101 - Environment Setup

Welcome! Before jumping into projects with Failure Enthusiasts, let's get some basic setup out of the way. Here's what we'll do:

- First, we'll create a Project folder
- We'll pull down our Failure Enthusiasts directory (so we can all share these project setup files) 
- We'll install Python3 (Python 2 is deprecated soon) and a package manager. 

### Step 1: Create a "Projects" folder
First, we'll want directory to keep the files we work on for Projects. I'd recommend creating this in your Home directory, but that's up to you. Feel free to create your Projects folder elsewhere!

First, open a MacOS Terminal window, and change directory to Home:

`cd ~`

If you run a `pwd`, you'll see you're now in `/Users/firstname.lastname`.

Then, create a "Projects" folder, and change directory into it:

```
mkdir Projects
cd Projects
```

### Step 2: Clone this Repo
We'll use a `git clone` to pull the Failure Enthusiasts directory down from github to your local machine. That will let us collaborate, allow access to base project setup files, and so on. 

Run this command from your "Projects" folder:

`git clone git@github.com:bradleyjay/failure_enthusiasts.git`

Once complete, let's hop into this new directory, then this repo's folder:

```
cd failure_enthusiasts
cd python101-environment-setup
```

Ok! Now we're ready to setup our system.

### Step 3: Install Homebrew
We'll need a basic package manager to install Python3. Let's use `homebrew`. Start in your Mac OSX terminal, and run this command:

`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

### Step 2: Install Python3
Now, install Python 3 with the command:

`brew install python3`

### Step 4: 
Finally, for each project we work on, we'll want to create a Virtual Environment. Once created, installing Python packages will *only* install the package for that project enviornment. 

This is important because each project will require different tools and packages, and new versions of various tools may break each other. Creating an enviornment means that all those versions stay static for that particular project alone, unless we change them ourselves. 

Plus, it keeps our system's general Python installation clean and free of whatever packages we install for one-off projects - win-win!

**We'll create a Virtual Environment for each project we do. That project's enviroment lives in its "env" folder, and keeps track of what's installed in that environment. Let's practice by creating one now:**

Create the Virtual Environment:
```
python3 -m venv venv
```    
Then, to activate the enviornment (do this before working on a given project, each time you start working on it):
```
. venv/bin/activate
```
You'll see `(venv)` next to your command prompt - that means you're in the Virtual Environment!

To get out of that enviornment (for instance, when you'll switch to a new project, etc), run this command:

```
deactivate
```

`(venv)` now disappears from your command prompt, and you're back in your general system. Congrats! You're done.