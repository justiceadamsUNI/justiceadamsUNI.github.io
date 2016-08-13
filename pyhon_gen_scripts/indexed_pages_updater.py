## Created by Justice Adams

## Update and index page to navigate the directory correctly once its bucketed.
## In other words, replace folder references with parent folders, and add "newer"
## or "older" buttons when necessary.

import os
import webbrowser
import time
import re

def promptForFileToUpdate():
    print(" This script will update an index file to work properly once it's outside the parent directory.")
    print(" All you must do is tell us which file to update. And what to link it to.")
    print(" * Please note this script assumes 4 post teasers per index *")
    input("\n Press Enter to start, or stop script with CNTRL+C: ")

    return getIndexFile("\n Index File (leave empty to see all files in indexed_homepages folder): ")


def getIndexFile(message):
    indexDirectory = os.path.dirname(__file__) + "/../html_bucket_indexed_homepages/"

    while(True):
        indexFile = input(message)
        indexPath = indexDirectory + indexFile
        if os.path.isfile(indexPath) and os.access(indexPath, os.R_OK):
            return indexPath
        else:
           print(" Not a valid file. Try again.")
           print("\n All files in folder: \n")
           print(os.listdir(indexDirectory))


def promptForValidNumber(message):
    while(True):
        userResponse = input("\n" + message + " : ")
        if userResponse.isdigit():
            break
        else:
            print("\n Invlid input.Please enter a valid integer!")

    return int(userResponse)


def generateHtmlFromIndexFile(indexFile, index):
    file = open(indexFile, "r")
    html = file.read()
    file.close()

    html = replaceDirectoryStructure(html)
    html = updateNavigationButtons(html, index)

    return html


def replaceDirectoryStructure(html):
    href_nodeModulesFolder = "href=\"node_modules/"
    href_cssFolder = "href=\"css/"
    href_imageFolder = "href=\"img/"
    href_modulesFolder = "href=\"modules/"
    href_indexFile = "href=\"index.html"
    href_recapsPageFile = "href=\"recaps-page.html"
    href_eventsPageFile = "href=\"events-page.html"
    href_resourcesPageFile = "href=\"resources-page.html"
    href_html_bucket_class_recaps = "href=\"html_bucket_class_recaps"
    href_html_bucket_other_posts = "href=\"html_bucket_other_posts"
    href_html_bucket_indexed_homepages = "href=\"html_bucket_indexed_homepages"

    src_nodeModulesFolder = "src=\"node_modules/"
    src_cssFolder = "src=\"css/"
    src_imageFolder = "src=\"img/"
    src_modulesFolder = "src=\"modules/"
    src_indexFile = "src=\"index.html"
    src_recapsPageFile = "src=\"recaps-page.html"
    src_eventsPageFile = "src=\"events-page.html"
    src_resourcesPageFile = "src=\"resources-page.html"
    src_html_bucket_class_recaps = "src=\"html_bucket_class_recaps"
    src_html_bucket_other_posts = "src=\"html_bucket_other_posts"
    src_html_bucket_indexed_homepages = "src=\"html_bucket_indexed_homepages"


    html = (html.replace(href_nodeModulesFolder, href_nodeModulesFolder.replace("node_modules","../node_modules"))
            .replace(href_cssFolder, href_cssFolder.replace("css", "../css"))
            .replace(href_imageFolder, href_imageFolder.replace("img", "../img"))
            .replace(href_modulesFolder, href_modulesFolder.replace("modules", "../modules"))
            .replace(href_indexFile, href_indexFile.replace("index", "../css"))
            .replace(href_recapsPageFile, href_recapsPageFile.replace("recaps-page", "../recaps-page"))
            .replace(href_eventsPageFile, href_eventsPageFile.replace("events-page", "../events-page"))
            .replace(href_resourcesPageFile, href_resourcesPageFile.replace("resources-page", "../resources-page"))
            .replace(href_html_bucket_class_recaps, href_html_bucket_class_recaps.replace("html_bucket_class_recaps", "../html_bucket_class_recaps"))
            .replace(href_html_bucket_other_posts, href_html_bucket_other_posts.replace("html_bucket_other_posts", "../html_bucket_other_posts"))
            .replace(href_html_bucket_indexed_homepages, href_html_bucket_indexed_homepages.replace("html_bucket_indexed_homepages", "../html_bucket_indexed_homepages")))

    html = (html.replace(src_nodeModulesFolder, src_nodeModulesFolder.replace("node_modules","../node_modules"))
            .replace(src_cssFolder, src_cssFolder.replace("css", "../css"))
            .replace(src_imageFolder, src_imageFolder.replace("img", "../img"))
            .replace(src_modulesFolder, src_modulesFolder.replace("modules", "../modules"))
            .replace(src_indexFile, src_indexFile.replace("index", "../css"))
            .replace(src_recapsPageFile, src_recapsPageFile.replace("recaps-page", "../recaps-page"))
            .replace(src_eventsPageFile, src_eventsPageFile.replace("events-page", "../events-page"))
            .replace(src_resourcesPageFile, src_resourcesPageFile.replace("resources-page", "../resources-page"))
            .replace(src_html_bucket_class_recaps, src_html_bucket_class_recaps.replace("html_bucket_class_recaps", "../html_bucket_class_recaps"))
            .replace(src_html_bucket_other_posts, src_html_bucket_other_posts.replace("html_bucket_other_posts", "../html_bucket_other_posts"))
            .replace(src_html_bucket_indexed_homepages, src_html_bucket_indexed_homepages.replace("html_bucket_indexed_homepages", "../html_bucket_indexed_homepages")))
        
    return html


def updateNavigationButtons(html, index):
    previousIndexPath = os.path.dirname(__file__) + "/../html_bucket_indexed_homepages/index-posts-" + str(index-4) + "-" + str(index-1) + ".html"

    if os.path.isfile(previousIndexPath) and os.access(previousIndexPath, os.R_OK):
        navSetup = (" <div class=\"paging\">" +
                   " <a href=\"..\index.html\" class=\"newer\"><i class=\"fa fa-long-arrow-left\">" +
                   " </i> Newer</a>" + 
                   " <span>&bull;</span> " +
                   " <a href=\"" + previousIndexPath + "\" class=\"older\">Older <i class=\"fa fa-long-arrow-right\"></i></a>" + 
                   " </div>")

        
        return re.sub("<!-- NAV-BUTTON-FLAG -->.*?<!-- NAV-BUTTON-FLAG -->", navSetup, html, flags=re.DOTALL)

    else:
        navSetup = (" <div class=\"paging\">" +
                   " <a href=\"..\index.html\" class=\"newer\"><i class=\"fa fa-long-arrow-left\">" +
                   " </i> Newer</a>" +
                    " </div>")
        
        return re.sub("<!-- NAV-BUTTON-FLAG -->.*?<!-- NAV-BUTTON-FLAG -->", navSetup, html, flags=re.DOTALL)
    



def saveUpdatedFile(html, index):
    newFilePath = os.path.dirname(__file__) + "/../html_bucket_indexed_homepages/index-posts-" + str(index) + "-" + str(index + 3) + ".html"

    file = open(newFilePath, "w")
    file.write(html)
    file.close()

    return newFilePath

def reviewPost(filename):
    print("\n Script Over. Opening File for review...")
    time.sleep(.5)
    webbrowser.open_new(filename)

indexFile = promptForFileToUpdate()
index = promptForValidNumber("\n What is the starting index. (This assumes there are 4 post on the page)")
updatedHtml = generateHtmlFromIndexFile(indexFile, index)
newPost = saveUpdatedFile(updatedHtml, index)
reviewPost(newPost)
