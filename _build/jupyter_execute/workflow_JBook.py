#!/usr/bin/env python
# coding: utf-8

# # Workflow to build the book
# 
# Assuming that you have created the folder of a Jupyter Book, and done the setting of the github Pages such as the main and gh-pages beanches. For initilizing a book and publishing the content,
# 
# -   to create a JB book
# -   to make a github repository
# -   to initial the git of the folder
# -   main branch is used for storing the sources
# -   to create a gh-pahges branch, where the content is published here.
# 
# ```{note}
# To build and to create the content, stay in the main branch.
# ```
# ```{warning}
# Version of the jupyter-book seems an issue.
# It is better to create a virtual environment 
# by conda create. 
# The current version info is 
# 
# * Jupyter Book      : 0.13.0
# * External ToC      : 0.2.4
# * MyST-Parser       : 0.15.2
# * MyST-NB           : 0.13.2
# * Sphinx Book Theme : 0.3.2
# * Jupyter-Cache     : 0.4.3
# * NbClient          : 0.5.13
# 
# ```
# ## Build the HTML from source
# 
# A book is created in a foler named “jbook”. You can build the HTML with the command. Excute the following command at the place containing the “jbook” folder, i.e., outside “jbook”
# 
# ``` bash
# jupyter-book build jbook/
# ```
# 
# ## Create your file and add content to it
# 
# In the book folder, create a new file called `mymarkdownfile.md`. Put the following content in it:
# 
# ``` md
# # Here's my sample title
# 
# This is some sample text.
# 
# (section-label)=
# ## Here's my first section
# 
# Here is a [reference to the intro](intro.md). Here is a reference to [](section-label).
# ```
# 
# We’ve added two new pieces of markdown syntax, both of them are related to **cross-references**.
# 
# -   `(section-label)=` is a label that’s attached to a section header. It refers to whatever header follows, and allows you to refer to this label later on in your text.
# -   `[link text](link-target)` syntax is how you specify a link in markdown. Here we’ve linked to another page, as well as to the label we created above.
# 
# When you build your book, you’ll see how these links resolve in the output.
# 
# ## Add it to your Table of Contents
# 
# Now that you’ve got a new file, we need to add it to your `_toc.yml` file so that Jupyter Book knows where it fits with your book’s structure.
# Add the a line to your `_toc.yml` file pointing to this new content, it should look something like this:
# 
# ``` yaml
# # In _toc.yml
# format: jb-book
# root: intro
# chapters:
# - file: markdown
# - file: notebooks
# - file: markdown-notebooks
# - file: mymarkdownfile
# ```
# 
# ## Re-build your book
# 
# Now that you’ve added the file to your `_toc.yml` file, you can re-run the build command:
# 
# ``` console
# $ jupyter-book build mybookname
# ```
# 
# This will re-build your book, and your new page will show up in the output.
# 
# ## Publish the content
# The web content is in the gh-pages branch.
# We have just pushed the *source files* for our book into our GitHub repository.
# This makes it publicly accessible for you or others to see.
# 
# Next, we'll publish the *build artifact* of our book online, so that it is rendered as a website.
# 
# 
# The easiest way to use GitHub Pages with your built HTML is to use the [`ghp-import`](https://github.com/davisp/ghp-import) package. `ghp-import` is a lightweight Python package that makes it easy to push HTML content to a GitHub repository.
# 
# `ghp-import` works by copying *all* of the contents of your built book (i.e., the `_build/html` folder) to a branch of your repository called `gh-pages`, and pushes it to GitHub. The `gh-pages` branch will be created and populated automatically for you by `ghp-import`. To use `ghp-import` to host your book online with GitHub Pages follow the steps below:
# 
# ```{note}
# Before performing the below steps, ensure that HTML has been built for each page of your book. There should be a collection of HTML
# files in your book's `_build/html` folder.
# ```
# 
# 1. Install `ghp-import`
# 
#    ```bash
#    pip install ghp-import
#    ```
# 2. Update the settings for your GitHub pages site: Use the `gh-pages` branch to host your website.
# 
# 3. From the `main` branch of your book's root directory (which should contain the `_build/html` folder) call `ghp-import` and point it to your HTML files, like so:
# 
#    ```bash
#    ghp-import -n -p -f _build/html
#    ```
# 
# ```{warning}
# Make sure that you included the `-n` - this tells GitHub *not* to build your book with
# [Jekyll](https://jekyllrb.com/), which we don't want because our HTML is already built!
# If you do not do this you may see **404 not found** for your deployed content.
# ```
