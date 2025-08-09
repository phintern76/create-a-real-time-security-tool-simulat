import time
import random
import threading

class SecurityToolSimulator:
    def __init__(self):
        self.system_status = "SECURE"
        self.alert_level = "LOW"
        self.system_components = ["NETWORK", "SYSTEM_FILES", "USER_ACCOUNTS"]
        self.threads = []

    def monitor_system(self):
        while True:
            time.sleep(1)
            self.check_for_intrusions()

    def check_for_intrusions(self):
        component = random.choice(self.system_components)
        intrusion_chance = random.random()

        if intrusion_chance > 0.7:
            self.raise_alert(component)
        else:
            print(f"System {component} is secure.")

    def raise_alert(self, component):
        self.system_status = "INSECURE"
        self.alert_level = "HIGH"
        print(f"ALERT: Possible intrusion detected in {component}!")

    def respond_to_alert(self, component):
        response_time = random.randint(1, 5)
        time.sleep(response_time)
        print(f"Responding to alert in {component}... (took {response_time} seconds)")
        self.system_status = "SECURE"
        self.alert_level = "LOW"

    def run(self):
        monitoring_thread = threading.Thread(target=self.monitor_system)
        monitoring_thread.start()
        self.threads.append(monitoring_thread)

        while True:
            user_input = input("Enter 'quit' to exit or 'alert' to simulate an alert response: ")

            if user_input.lower() == 'quit':
                break
            elif user_input.lower() == 'alert':
                component = random.choice(self.system_components)
                self.respond_to_alert(component)

        for thread in self.threads:
            thread.join()

if __name__ == "__main__":
    simulator = SecurityToolSimulator()
    simulator.run()