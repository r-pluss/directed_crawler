

import requests
import simplejson as json
#as there is no good way to declare anonymous functions, nor to compile new functions
#dynamicallly in python, we will import a module that will act as our instance-specific
#config object, as the necessary functions that are unique to a given Directed_Crawler
#instance can be composed using expected method names. E.g: 
#   Directed_Crawler_Instance.increment = crawler_config.increment
#   where increment is simply a function defined in the top-level namespace of the 
#   crawler_config module
#if a better method can be devised in the future, it should replace this methodology
import crawler_config

class Directed_Crawler():
    def __init__(self, init_obj):
        self.last_result = None
        self.previous_increment = None
        #self.response_test = self._make_response_test(init_obj['response_test'])
        #self.template = init_obj['template']
        #self._make_increment_rules(init_obj['increment_rules'])
        
    def _make_increment_rules(self):
        self._increment_rules = crawler_config.increment_rules
        #crawler_config.increment_rules should be a list of functions that are defined in the crawler_config module
        #these function should take two arguments, the result of the previous function (or the previous increment
        #value if it is the first function) and a reference to the Directed_Crawler instance
        #e.g.:
        #def a():
        #   passs
        #def b():
        #   pass
        #def c():
        #   pass
        #def increment_rules():
        #   return [a, b, c]
        
        
    def increment(self):
        _ = self.previous_increment
        for rule in self._increment_rules:
            #we pass self so that the rule can operate upon all declared attributes
            _ = rule(_, self)
        self.current_increment = _
            
    
    def _make_reponse_test(self, rule):
        pass


#the following stateful properties must be included:
#self.template
#self.last_result
#self.increment_rule
#self.response_test
#self.stop_iteration_test
#self.previous_increment
