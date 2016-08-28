## Created by Justice Adams
## Populate a blog post with the user given information.

##Title
##Date
##Body
##Image
##Embedd a youtube Video or image/gif?
##Tags

import os.path
import os
import webbrowser
import time

def promptForBlogInfo():
    print(" Info needed to generate blog post."
         + "\n * TITLE \n * DATE \n * IMAGE"
         + "\n * EMBEDDED YOUTUBE OR IMAGE/GIF \n * TAGS")
    print(" Remember that the body of your post must live within blog-post-body.txt")

    input("\n Press Enter to start, or stop script with CNTRL+C: ")
    title = input("\n\n Title: ")
    date = input("\n Date: ")
    image = getImageFile("\n Image (header): ")

    mediaHtml = ""
    shouldEmbeddMedia = promptForValidBoolean(" Do you want to embedd a youtube video/gif/image?")

    if(shouldEmbeddMedia):
        mediaIsYoutube = promptForValidBoolean(" Is it a youTubeVideo?")
        if (mediaIsYoutube):
            mediaHtml = input("\n YouTube embedd code: ")
            mediaHtml = wrapYoutubeVideo(mediaHtml)
        else:
            mediaHtml = getImageFile("\n Embedd image/GIF file: ")
            mediaHtml = wrapEmbeddedImage(mediaHtml)

    tags = promptForTags()
    body = getBodyText()

    return BlogInfo(title, body, date, image, mediaHtml, tags)


def getBodyText():
    bodyTextFile = open("blog-post-body.txt", "r")
    blogBody =  bodyTextFile.read()
    bodyTextFile.close()

    return blogBody.replace("\n", "<br>")


def generateHtmlFromSkeleton(blogInfo):
    titlePlaceHolder = "<!-- TITLE-PLACEHOLDER -->"
    imagePlaceHolder = "<!-- IMAGE-PLACEHOLDER -->"
    datePlaceHolder = "<!-- DATE-PLACEHOLDER -->"
    bodyPlaceHolder = "<!-- BODY-PLACEHOLDER -->"
    mediaPlaceHolder = "<!-- EMBEDDED-MEDIA-PLACEHOLDER -->"
    tagsPlaceHolder = "<!-- TAGS-LIST-PLACEHOLDER -->"
    
    blogSkeletonFile = open("blog-post-skeleton.html", "r")
    blogHtml = blogSkeletonFile.read()
    blogSkeletonFile.close()

    blogHtml = (blogHtml.replace(titlePlaceHolder, blogInfo.title)
    .replace(imagePlaceHolder, blogInfo.headerImage)
    .replace(datePlaceHolder, blogInfo.date)
    .replace(bodyPlaceHolder, blogInfo.body)
    .replace(mediaPlaceHolder, blogInfo.embeddedMedia))

    tagHtmlList = ""
    for tag in blogInfo.tags:
        tagHtmlList += tag + " \n"

    blogHtml = blogHtml.replace(tagsPlaceHolder, tagHtmlList)

    return blogHtml


def promptForValidBoolean(message):
    while(True):
        userResponse = input("\n" + message + " (y)es or (n)o: ")
        if userResponse.lower().strip() in ("y", "n"):
            userResponse = (userResponse == "y")
            break
        else:
            print("\n Invlid input. Enter (y)es or (n)o")

    return userResponse


def promptForTags():
    print("\n Enter as many tags as needed. Enter an empty tag when finished")
    tags = []
    while(True):
        tag = input("\n Tag: ")
        if tag != "":
            tags.append("<li><a>" + tag + "</a></li>")
        else:
            break

    return tags


def getImageFile(message):
    imageDirectory = os.path.dirname(__file__) + "/../img/"

    while(True):
        imageFile = input(message)
        imagePath = imageDirectory + imageFile
        if os.path.isfile(imagePath) and os.access(imagePath, os.R_OK):
            return imageFile
        else:
           print(" Not a valid image. Try again")
           print("\n All images: \n")
           print(os.listdir(imageDirectory))


def wrapEmbeddedImage(imageFile):
   return "<img src=../img/" + imageFile + " class=\"img-responsive\"> "


def wrapYoutubeVideo(youtubeEmbeddURL):
    vid = ("<div class=\"auto-resizable-iframe\">"  + 
            "<div>" + 
            " <iframe frameborder=\"0\" allowfullscreen=\"\" src=\"" +  youtubeEmbeddURL + " \"></iframe>" +
            " </div>" + 
            "</div>"
            )
    return vid


def saveUpdatedFile(html, blogInfo):
    classRecapResponse = promptForValidBoolean(" Is this a clas recap? ")

    if (classRecapResponse):
        html = (html.replace("<!-- ACTIVE-BREADCRUMB-CLASS-PLACEHOLDER -->", "class=\"active\"")
                   .replace("<!-- ACTIVE-BREADCRUMB-PLACEHOLDER -->", "Recaps"))
        
        parentDirectory = '/../html_bucket_class_recaps/'
    else:
        html = (html.replace("<!-- ACTIVE-BREADCRUMB-CLASS-PLACEHOLDER -->", "")
                   .replace("<!-- ACTIVE-BREADCRUMB-PLACEHOLDER -->", ""))
        
        parentDirectory = '/../html_bucket_other_posts/'
    
    filename = blogInfo.title.replace(" ", "-").lower() + ".html"
    filename = parentDirectory + filename
    outFile = open(os.path.dirname(__file__) + filename, "w")
    outFile.write(html)
    outFile.close()

    return os.path.dirname(__file__) + filename


def reviewPost(filename):
    print("\n Script Over. Opening File for review...")
    time.sleep(.5)
    webbrowser.open_new(filename)
    

    
class BlogInfo(object):
    def __init__(self, title, body, date, headerImage, embeddedMedia, tags):
        self.title = title
        self.body = body
        self.date = date
        self.headerImage = headerImage
        self.embeddedMedia = embeddedMedia
        self.tags = tags


blogInfo = promptForBlogInfo()
updatedHtml = generateHtmlFromSkeleton(blogInfo)
newPost = saveUpdatedFile(updatedHtml, blogInfo)
reviewPost(newPost)


