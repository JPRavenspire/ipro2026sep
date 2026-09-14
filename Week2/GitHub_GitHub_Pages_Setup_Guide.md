# GitHub & GitHub Pages Setup Guide (Beginner)

A complete guide for creating your first GitHub repository and
publishing a static website with GitHub Pages.

## Goal

By the end of this guide you will have:

-   A GitHub account.
-   Git installed on your computer.
-   Your first repository on GitHub.
-   Your existing website uploaded.
-   A live website hosted with GitHub Pages.

------------------------------------------------------------------------

## Step 1 --- Create a GitHub Account

1.  Go to https://github.com
2.  Click **Sign up**.
3.  Choose:
    -   Username
    -   Email address
    -   Password
4.  Verify your email address.

> Your username becomes part of your GitHub Pages URL.

Example:

    https://yourusername.github.io

------------------------------------------------------------------------

## Step 2 --- Install Git

Download **Git for Windows** from:

https://git-scm.com/downloads

Install using the default settings.

Verify the installation:

``` bash
git --version
```

Expected output:

``` text
git version 2.xx.x.windows.x
```

------------------------------------------------------------------------

## Step 3 --- Configure Git (One Time Only)

Tell Git who you are.

``` bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Verify:

``` bash
git config --global --list
```

You should see your name and email.

------------------------------------------------------------------------

## Step 4 --- Create Your Website Folder

Example structure:

``` text
my-website/
├── index.html
├── style.css
├── script.js
└── images/
```

Your `index.html` should be in the root folder.

------------------------------------------------------------------------

## Step 5 --- Create an Empty GitHub Repository

On GitHub:

1.  Click **New Repository**.
2.  Repository name: `my-website`
3.  Visibility: **Public**
4.  **Do NOT** check:
    -   Add a README
    -   Add a .gitignore
    -   Add a License

Click **Create Repository**.

> Leaving it empty prevents merge conflicts on the first push.

------------------------------------------------------------------------

## Step 6 --- Initialize Git in Your Existing Folder

Open a terminal inside your website folder.

``` bash
cd path/to/my-website
```

Initialize Git:

``` bash
git init
```

Check status:

``` bash
git status
```

------------------------------------------------------------------------

## Step 7 --- Stage Your Files

Add everything to Git.

``` bash
git add .
```

Check status again:

``` bash
git status
```

Files should appear under **Changes to be committed**.

------------------------------------------------------------------------

## Step 8 --- Create Your First Commit

``` bash
git commit -m "Initial website"
```

This creates your first local snapshot.

------------------------------------------------------------------------

## Step 9 --- Connect the Repository to GitHub

Copy the repository URL from GitHub.

Example:

``` text
https://github.com/YOUR_USERNAME/my-website.git
```

Connect it:

``` bash
git remote add origin https://github.com/YOUR_USERNAME/my-website.git
```

Verify:

``` bash
git remote -v
```

------------------------------------------------------------------------

## Step 10 --- Authenticate with GitHub

Modern GitHub does **not** use your GitHub password for `git push`.

If Git Credential Manager is installed (default on Windows):

Run:

``` bash
git push -u origin main
```

Git will:

1.  Open a browser window.
2.  Ask you to sign into GitHub.
3.  Ask you to authorize Git Credential Manager.
4.  Store your credentials securely.

Check it's enabled:

``` bash
git config --global credential.helper
```

Expected output:

``` text
manager
```

------------------------------------------------------------------------

## Step 11 --- Push Your Website

Rename the default branch:

``` bash
git branch -M main
```

Push to GitHub:

``` bash
git push -u origin main
```

The `-u` option links your local branch with GitHub's `main` branch.

Future pushes only require:

``` bash
git push
```

------------------------------------------------------------------------

## Step 12 --- Enable GitHub Pages

In your repository:

1.  **Settings**
2.  **Pages**
3.  **Source:** Deploy from a branch
4.  **Branch:** `main`
5.  **Folder:** `/ (root)`
6.  Click **Save**.

------------------------------------------------------------------------

## Step 13 --- Visit Your Website

After 30--60 seconds GitHub Pages publishes your site.

Project website:

``` text
https://YOUR_USERNAME.github.io/my-website/
```

Personal website repository (`YOUR_USERNAME.github.io`):

``` text
https://YOUR_USERNAME.github.io
```

------------------------------------------------------------------------

# Updating Your Website

Whenever you change files:

``` bash
git status
git add .
git commit -m "Describe your changes"
git push
```

GitHub Pages automatically redeploys after each push.

------------------------------------------------------------------------

# Git Workflow Cheat Sheet

  Command                     Purpose
  --------------------------- -------------------------------
  `git status`                Show changed files.
  `git add .`                 Stage all changes.
  `git commit -m "message"`   Save a local snapshot.
  `git push`                  Upload commits to GitHub.
  `git pull`                  Download changes from GitHub.

------------------------------------------------------------------------

# Common Beginner Mistakes

  ------------------------------------------------------------------------------------
  Problem                                     Fix
  ------------------------------------------- ----------------------------------------
  `non-fast-forward` error on first push      Repository was initialized with a
                                              README. Use
                                              `git pull --allow-unrelated-histories`
                                              or create an empty repository.

  `fatal: destination path already exists`    Don't `git clone` into an existing
                                              project folder. Use `git init` instead.

  Website shows 404                           Make sure `index.html` is in the
                                              repository root and GitHub Pages is
                                              enabled.

  Changes don't appear online                 Run `git add`, `git commit`, and
                                              `git push`. GitHub Pages only updates
                                              after a push.
  ------------------------------------------------------------------------------------
