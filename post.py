## Tristan Potter
## This allows for a user to post to the blog. It will modify
##     the blog.html file while creating a new file in the blog folder
##     that cooresponds to the post.

## temporary blog file that is created by this script
##     This file is created at the start of the script
##     Renamed once everything is written, and the old file's name is changed
##     new_blog.html -> blog.html && blog.html -> old_blog.html
new_blog = open("new_blog.html", "w")

## The original blog file. Data is read from this file to create new_blog
blog = open("blog.html", "r")

## The template of what a preview post looks like in the blog. Read and never changed.
template_blog = open("blog/blog_template.html", "r")

## The template of what a blog post looks like. Read and never changed.
template_post = open("blog/post_template.html", "r")

## writeBlog : String, File -> Void
## Purpose: Adds a string title, a date (determined by time of running) and a
##     File body (representing the body of the blog post) to the blog page
def writeBlog(title, body):
    for line in blog:
        if "<!--PostNumber:" in line:
            postNumber = line[line.find(":")+1:line.find(";")] + 1 #find the previous post number ##WARN: Error location
            new_blog.write("<!--PostNumber:" + postNumber + ";-->") #write the current post number
        else if "<!--NewPost-->"in line:
            post_preview(title, body)#ADD NEW POST LINK
        else:
            new_blog.write(line)
    return 0;

## post_preview : String File -> Void
## Purpose: Reads from template_blog, filling in the required information and writing to
##     the new_blog to create the preview for this post.
def post_preview(title, body):
    for line in template_blog:
        if "<!--title-->" in line:
            new_blog.write(title)
        else if "<!--date-->" in line:
            new_blog.write() ##TODO: date
        else if "<!--body-->" in line:
            new_blog.write(body)
        else:
            new_blog.write(line)
    return 0;

## write_body : File -> String
## Purpose: Reads a given body file representing the content of the post and creates an html version as a string.
def parse_body(body):
    final = ""
    for line in body:
        final.append("<p>&emsp;&emsp;"  + line "</p>\n")
    return final

## preview_body : File -> String
def preview_body(body):
    return = "<p>&emsp;&emsp;" + body.readline() " </p>\n"


## writePost : String File -> Void
## Purpose: Creates the file for this blog post from template_post using the given information.
def writePost(title, body, post):
    for line in template_post:
        if "{{title}}" in line:
            post.write(title)
        else if "{{date}}" in line:
            ##TODO Write date
        else if "{{body}}" in line:
            post.write(body)
        else
            post.write(line)
    return 0


with open("blog.html", "r") as blog:
    prev_postNumber = findBlogNumber(blog)
    postNumber = prev_postNumber + 1


    body = parse_body() ##TODO parse body? ie parse_body(body file)
    title = ##TODO parse title?
    preview = preview_body() ##TODO parse body preview?

    writeBlog(title, body) ##WARN is this how things should be transfered? not using preview_body...
    ##TODO rename old file
    ##TODO rename new file

    with open(postnumber + ".txt") as new_post:
        writePost(title, body, new_post)



