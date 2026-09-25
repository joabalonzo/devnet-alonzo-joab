# Module 1 — Git & GitHub

**Student:** [Alonzo, Joab P.]
**Date:** [September 25, 2026]

---

## What is Git? What is GitHub? (explain like you're teaching a friend who's never used either)

[Git is a tool that help us to track or monitor our changes in our files. Git helps us to see what we changed and we can go back to the older version if we make a mistake.

Github is a website where we can save our work online. We can also share our work online to cooperate with other people. 

Overall, Git is the tool that tracks our changes, while Github is the website where we can store and share our projects online.]

---

## Key vocabulary (in your own words)

- repository: A folder for our project where the files and changes are kept.
- commit: A saved version of the changes that we made in our project. It records the changes we made.
- branch: Branch is a safe place to work with your project without making a mistake on the main file. It is a separate place for us.
- push / pull: Push means sending our saved changes to Github. Pull is the opposite of push it means getting the changes to our computer.
- pull request: A request to add our changes to another branch. This is very helpful because it lets other people to check if there is a mistake or a problem on the work before adding it.
- merge conflict: This is a problem that happens when two changes cannot be merge or cannot be joined. We need to check the changes and after we check it, we need to decide what to keep.

---

## Walking through what I did

[When we are making our project which is a Task Manager. I created a branch named edit-feature-joab so i could work on my own without affecting the main branch i made and saved my changes on that branch. After that. I pushed my changes in Github and created a pull request. The pull request allowed our leader to review our work before adding it to the main branch.]

```
git switch -c edit-feature-joab
git add .
git commit -m "edit featured task"
git push -u origin edit-feature-joabx
```

---

## A mistake I made (or one I want to avoid)

[One mistake I want to avoid is not checking which branch i am working on before making changes. If i work on the wrong branch and make a mistake the main branch could be a mess or it can cause a problem. To avoid the that. I should always check my current branch first using the command "git branch" before starting my work. This simple command helps me to check if i am working on the correct branch.]

---

## How this connects to something else

[Git and Github are useful when working on a group projects. We can work our own parts without changing the main project. It also helps us to keep tracking our changes and combine or merge our work when we are done.]
