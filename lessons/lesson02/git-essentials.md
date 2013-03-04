# git essentials

- - -
## git essentials

### create a new repository

create a new repository on github and follow instruction for the first push.

To clone it on your machine

```
> git clone username@host:/path/to/repository
```

- - -

## git essentials

### workflow

Your local repository consists of three "trees" maintained by git:

* your `Working Directory` which holds the actual files
* the `Index` which acts as a staging area
* the `HEAD` which points to the last commit you've made

![trees](https://github.com/cvdlab/git-crumbs/raw/master/git/images/trees.png "trees")

- - -

## git essentials

### workflow

#### add & commit

To propose changes (add it to the **Index**) use

```
> git add <filename>
```

```
> git add .
```

This is the first step in the basic git workflow.

- - -

## git essentials

### workflow

To actually commit these changes use

```
> git commit -m "Commit message"
```

Now the file is committed to the **HEAD**, but not in your remote repository yet.

- - -

## git essentials

### workflow


#### pushing changes

Your changes are now in the **HEAD** of your local working copy.
To send those changes to your remote repository, execute

```
> git push origin master
```

Now you are able to push your changes to the selected remote server.

- - -

## git essentials

### summarizing

create a repo on github and follow instruction

clone it:

```
> git clone username@host:/path/to/repository
```

add changes:

```
> git add .
```

commit changes:

```
> git commit -m "Commit message"
```

push changes

```
> git push origin master
```

- - -

## git essentials

### update

To update your local repository to the newest commit, execute

```
> git pull
```

in your working directory to fetch and merge remote changes.

git tries to auto-merge changes.
Unfortunately, this is not always possible and results in conflicts.
You are responsible to merge those conflicts manually by editing the files shown by git.

After changing, mark them as merged with

```
> git add <filename>
```

and then commit.
