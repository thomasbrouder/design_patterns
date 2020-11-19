import yaml
import json
import os


class UsualService():
    """
    Third party library returning a yaml file
    """
    def __init__(self, output_path):
        self.output_path = output_path

    def save_output(self) -> None:
        rules_dict = {
            0: "Je pense puis je code",
            1: "Je merge puis je code",
            2: "Je ne merge que sur Master",
            3: "Je ne rebase que sur Master",
            4: "Je ne valide que sur Master",
            5: "Je conserve mes branches jusqu'au merge",
        }
        with open(self.output_path, "w") as handle:
            json.dump(rules_dict, handle)


class NewService():
    """
    Third party library returning a json file
    """

    def __init__(self, output_path):
        self.output_path = output_path

    def new_save_output(self) -> None:
        rules_dict = {
            0: "Je pense puis je code",
            1: "Je merge puis je code",
            2: "Je ne merge que sur Master",
            3: "Je ne rebase que sur Master",
            4: "Je ne valide que sur Master",
            5: "Je conserve mes branches jusqu'au merge",
        }
        with open(self.output_path, "w") as handle:
            yaml.dump(rules_dict, handle)


class Adapter(UsualService, NewService):
    """"""
    def save_output(self):
        self.new_save_output()
        yaml_output_path = self.output_path
        self.output_path = self.output_path.replace(".yml", ".json")

        with open(yaml_output_path, "r") as handle:
            yaml_input = yaml.load(handle)

        with open(self.output_path, "w") as handle:
            json.dump(yaml_input, handle)


def client_code(service: "UsualService") -> None:
    """Open third party service output"""
    service.save_output()
    with open(service.output_path, "r") as handle:
        service_output = json.load(handle)
    print("service_output: ", service_output)


if __name__ == '__main__':
    output_folder = "output/"
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    # output_path = os.path.join(output_folder, "usual_service_output.json")
    # usual_service = UsualService(output_path)
    # client_code(usual_service)

    # output_path = os.path.join(output_folder, "usual_service_output.yml")
    # new_service = NewService(output_path)
    # client_code(new_service)
    
    output_path = os.path.join(output_folder, "usual_service_output.yml")
    adapter = Adapter(output_path)
    client_code(adapter)

