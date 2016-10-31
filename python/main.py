

import requests
import simplejson as json

class Directed_Crawler():
    def __init__(self, init_obj):
        self.last_result = None
        self.previous_increment = None
        self.response_test = self._make_response_test(init_obj['response_test'])
        self.template = init_obj['template']
        self.incremenent_rule = self._make_increment_rule(init_obj['increment_rule'])
        
    def _make_increment_rule(self, rules):
        #need to solve problem of treating this similar to anonymous function in javascript
        for rule in rules:
            #rule.pre_test
            if rule.antecedent:
                pass
            
    
    def _make_reponse_test(self, rule):
        pass


#the following stateful properties must be included:
#self.template
#self.last_result
#self.increment_rule
#self.response_test
#self.stop_iteration_test
#self.previous_increment
