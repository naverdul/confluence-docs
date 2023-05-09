# How to upload docs and diagrams to Confluence using GitHub Actions

## Context
I’m not alone when I say that one of my least favorite things to do is to create documentation. I’m not a big fan of essays describing a situation, I much prefer bullet points describing steps I need to take combined with clear and useful visuals. However, I notice that often those visuals are outdated, resulting in me looking in the wrong place and drinking my coffee with frustration while I try to make sense of this application in front of me. 

In this blog I want to take you through my solution that has saved me (and my teammates) a lot of frustration on a daily basis. How cool would it be if we could create all our architecture diagrams and what not in python code (with version control) and automatically push the changes to Confluence?! I thought so too 😉 Let me show you how. 

It all started when I was checking out this [this python library called Diagrams](https://github.com/mingrammer/diagrams). It uses graphviz and cloud native icons which you can use to create your architecture diagrams in Python. Next, I was inspired by [this GitHub action](https://github.com/cupcakearmy/confluence-markdown-sync) which uploads the changes in your markdown file to Confluence. Trying to puzzle things together  there were a couple of problems to solve and challenges to overcome. Hope this article is helpful and please let me know if you have any ideas and/or improvements!  

## My goal:
Update our high-level documentation pages to Confluence

## My approach explained: 
Please find the setup and files in [GitHub](https://github.com/naverdul/confluence-docs) for your illustration. 
1.	Step 1: Create a diagram using [Diagrams](https://github.com/mingrammer/diagrams). 
    * In a docs folder, I added the diagrams folder where I included my python file. The documentation for the library is very explanatory which helps when creating your first diagram. It also provides you with the option to add your own icons. As an example, I added a few to show how. 
2.	Step 2: Create a markdown file which you want to upload to Confluence. 
    * In the same docs folder I created a high_level_architecture markdown file. 
3.	Step 3: Create a config file that explains which file needs to be uploaded. This solves the puzzle of having to specify the page id in the code itself and you have one list of all your diagrams and markdown files available. This can scale and is easily maintaiable. 
    * To upload content to confluence you need to provide a page id. To keep it simple for now, I created a csv file that maps the type of content, the content itself to the right page. I think this step can be improved, but for now this is how I solved it. 
    * This file also tackles the different approach for content vs images.
4.	Step 4: Create a confluence test page and get the id of the page
    * [This](https://confluence.atlassian.com/doc/create-and-edit-pages-139476.html) explains how in case you are not familiar
    * You can also do this using the Confluence API of course 😊 
    * Get the page id. Your URL will look something like this: https://{cloudid}.atlassian.net/wiki/ pages/{page_id}
5.	Step 5: Create a token in Confluence that you can use in your GitHub Action
    * [This page](https://confluence.atlassian.com/doc/view-and-revoke-oauth-access-tokens-208961965.html) describes how you can create the token 
    * Next you need to upload it as secrets on GitHub. [This page](https://docs.github.com/en/actions/security-guides/encrypted-secrets) describes how you can do that
6.	Step 6: Create the GitHub Actions
    * As I mentioned in the introduction, I was inspired by [this GitHub Action](https://github.com/cupcakearmy/confluence-markdown-sync). The only thing that was missing was that it didn’t support images yet. I altered the code and used the confluence wrapper to upload the image to Confluence. From there you can reference it in your md file. 
    * Create a deploy-docs.yml file. Here you can find my example with the python code that uploads your documentation to Confluence. 
    * As you can see this Actions will run with the main branch or docs branches. 
7.	Step 7: push your changes and have fun reading your documentation (: 

Hopefully you find this information useful and inspired you to automate your documentation. 