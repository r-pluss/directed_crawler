#this is an example of the crawler_config file format that is used as a config
#file for an instance of the Directed_Crawler class
#this config file can and should be changed for each project and is only used
#here as prototyping example

#remember to structure the file so that all functions referenced by expected
#methods are declared first, as python does not have hoisting à la javascript

import bs4


#module level properties
template_is_valid_increment = True

#root for img resource is http://www.squidi.net/comic/amd/
#parse successful responses by appending relative path to the end
def find_image(response):
    html = bs4.BeautifulSoup(response.content, 'lxml')
    return html.find('img', alt = 'All comics: Copyright 2001-2008 Sean Howard')

def download_image(img_data):
    pass


def inc_id(url, crawler):
    numerics = []
    current_position = len(url) - 1
    while url[current_position].isdigit():
        numerics.insert(0, url[current_position])
    return url[0 : current_position + 1] + str(int(''.join(numerics)) + 1)
        

def save_content(response):
    #persist the resource to disk
    return response

def increment_rules():
    return [inc_id]

def is_valid_resource(response):
    if not response.ok:
        return False
    html = bs4.BeautifulSoup(response.content, 'lxml')
    if html.find(string = 'An error has occurred - Invalid Page') is not None:
        return False
    return True

def process_resource():
    #return a list of methods declared in this config module that be
    #chained to operate over the results of a successful request
    #all methods should return the resource to enable the chaining
    #it is acceptable to mutate the resource if latter methods in
    #the chain will operate upon said mutations
    return [find_image, save_content]

def stop_iteration_tests():
    return []


def template():
    #the initial value of the url that will be mutated via the increment method
    return 'http://www.squidi.net/comic/amd/view.php?series=amd&ep=1&id=1'
