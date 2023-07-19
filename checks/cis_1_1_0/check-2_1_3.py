from checker import Checker

class Check_CIS_2_1_3(Checker):

    def __init__(self, firewall, display, verbose=False):
        
        super().__init__(firewall, display, verbose)

        self.id = "2.1.3"
        self.title = "Ensure timezone is properly configured"
        self.levels = [1]
        self.auto = False
        self.benchmark_version = "v1.1.0"
        self.benchmark_author = "CIS"

    def do_check(self):
        config_system_global = self.get_config("system global")

        if not "timezone" in config_system_global.keys():
            self.set_message("No timezone defined")
            return False

        timezone = config_system_global["timezone"]

        self.question_context = 'The configured timezone is ' + self.firewall.all_timezones[timezone]

        answer = self.ask("Is it correct? (Y/n)")
        
        if answer == 'n' or answer == 'N':
            self.set_message("Manually set to not compliant")
            return False
        else:
            self.set_message("Manually set to compliant")
            return True
