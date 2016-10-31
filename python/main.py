

import requests
import simplejson as json

class Directed_Crawler():
    def __init__(self, init_obj):
        self.last_result = None
        self.previous_increment = None
        self.response_test = self._make_response_test(init_obj['response_test'])
        self.template = init_obj['template']
        self._make_increment_rules(init_obj['increment_rules'])
        
    def _make_increment_rules(self, rules):
        #need to solve problem of treating this similar to anonymous function in javascript
        #each rule should describe a single atomic change
        self._increment_rules = []
        for rule in rules:
            self._increment_rules.append(lambda x: x
        
    def increment(self):
        _ = self.previous_increment
        for rule in self._increment_rules:
            _ = rule(_)
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
