import requests
import simplejson as json
#as there is no good way to declare anonymous functions, nor to compile new
#functions dynamicallly in python, we will import a module that will act
#as our instance-specific config object, as the necessary functions that are
#unique to a given Directed_Crawler
#instance can be composed using expected method names. E.g:
#   Directed_Crawler_Instance.increment = crawler_config.increment
#   where increment is simply a function defined in the top-level namespace
#   of the crawler_config module
#if a better method can be devised in the future, it should replace
#this methodology
import crawler_config

class Directed_Crawler():
    def __init__(self):
        self.last_result = None
        self.previous_increment = None
        self.current_increment = None
        self.template = crawler_config.template()
        self._make_increment_rules()
        #could easily be inlined without the class method call, but am not
        #currently refactoring incase future requirements necessitate an
        #increase in complexity that would be better encapsulated within
        #a function
        self._make_stop_iteration_tests()
        self._make_processing_handlers()

    def _make_increment_rules(self):
        self._increment_rules = crawler_config.increment_rules()
        #crawler_config.increment_rules should be a list of functions that are
        #defined in the crawler_config module these function should take two
        #arguments, the result of the previous function (or the previous
        #increment value if it is the first function) and
        #a reference to the Directed_Crawler instance
        #e.g.:
        #def a():
        #   passs
        #def b():
        #   pass
        #def c():
        #   pass
        #def increment_rules():
        #   return [a, b, c]

    def _make_processing_handlers(self):
        self._process_handlers = crawler_config.process_resource()
        #see comments accompanying _make_increment_rules,
        #most of that applies here

    def _make_stop_iteration_tests(self):
        self._stop_iteration_tests = crawler_config.stop_iteration_tests()
        #see _make_increment_rules for details, except tests should only
        #receive a single argument, a reference the instance's self obj

    def advance(self):
        for test in self._stop_iteration_tests:
            if test(self):
                pass #because we just want to go to the next test if it passed
            else:
                return False
        return True

    def increment(self):
        _cur = _prev = self.current_increment
        for rule in self._increment_rules:
            #we pass self so that the rule can operate upon all
            #declared attributes
            _cur = rule(_cur, self)
        self.previous_increment = _prev
        self.current_increment = _cur

    def fetch_next(self):
        return requests.get(self.current_increment)

    def process_resource(self):
        #this is another method that will vary completely depending on what
        #we want to do with the results of a valid resource and hence will
        #needed to be defined almost exclusively in the config file
        resp = self.last_reponse
        for handler in self._process_handlers:
            resp = handler(resp)

    def validate_resource(self):
        return crawler_config.is_valid_resource(self.last_response)

    def start(self):
        if crawler_config.template_is_valid_increment:
            self.current_increment = self.template
        else:
            self.increment()
        while self.advance():
            self.last_response = self.fetch_next()
            self.validate_resource()
            if self.last_validation_result():
                self.process_resource()
            self.increment()
