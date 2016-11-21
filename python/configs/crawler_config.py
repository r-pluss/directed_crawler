#this is an example of the crawler_config file format that is used as a config
#file for an instance of the Directed_Crawler class
#this config file can and should be changed for each project and is only used
#here as prototyping example

#remember to structure the file so that all functions referenced by expected
#methods are declared first, as python does not have hoisting à la javascript

import bs4
import requests

#module level properties
template_is_valid_increment = True

#root for img resource is http://www.squidi.net/comic/amd/
#parse successful responses by appending relative path to the end
def find_image(response):
    html = bs4.BeautifulSoup(response.content, 'lxml')
    return html.find('img', alt = 'All comics: Copyright 2001-2008 Sean Howard')

def strip_attrs(img_tag):
    return {attr: val for attr, val in img_tag.attrs.items() if attr != 'alt'}

def download_image(img_data):
    return {
        'img': requests.get('http://www.squidi.net/comic/amd{0}'.format(
            img_data['src'])),
        'attributes': img_data
    }


def inc_id(url, crawler):
    numerics = []
    current_position = len(url) - 1
    if crawler.last_result:
        while url[current_position].isdigit():
            numerics.insert(0, url[current_position])
            current_position -= 1
        setattr(crawler.last_response, 'changed_ep', False)
        return url[0 : current_position + 1] + str(int(''.join(numerics)) + 1)
    else:
        query_string_chars = []
        while url[current_position].isdigit():
            current_position -= 1
            #get through the ids
        while not url[current_position].isdigit():
            query_string_chars.insert(0, url[current_position])
            current_position -= 1
            #get through all the crap after the ids
        while url[current_position].isdigit():
            numerics.insert(0, url[current_position])
            current_position -= 1
            #collect the ep
        setattr(crawler.last_response, 'changed_ep', True)
        return url[0: current_position + 1] + str(int(''.join(numerics)) + 1 ) + ''.join(query_string_chars) + '1'
        

def save_content(response):
    #persist the resource to disk
    return response

def fail_after_ep_change(crawler):
    if getattr(crawler.last_response, 'changed_ep') and not crawler.last_result:
        return False
    else:
        return True

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
    return [find_image, strip_attrs, download_image, save_content]

def stop_iteration_tests():
    return [fail_after_ep_change]

def template():
    #the initial value of the url that will be mutated via the increment method
    return 'http://www.squidi.net/comic/amd/view.php?series=amd&ep=1&id=1'
