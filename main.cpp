#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cstdlib>
#include "include/nlohmann/json.hpp"

using json = nlohmann::json;

// Function to load commands from JSON
json loadCommands(const std::string& filename) {
    std::ifstream file(filename);
    if (!file.is_open()) {
        std::cerr << "Error: Could not open " << filename << std::endl;
        return nullptr;
    }

    json data;
    try {
        file >> data;
    } catch (json::parse_error& e) {
        std::cerr << "Error parsing JSON: " << e.what() << std::endl;
        return nullptr;
    }

    if (!data.is_array()) {
        std::cerr << "Error: JSON data is not an array." << std::endl;
        return nullptr;
    }
    return data;
}

// Function to execute a command
void executeCommand(const std::string& command) {
    std::cout << "Executing: " << command << std::endl;
    std::string zshCommand = "zsh -c \"" + command + "\"";
    int result = system(zshCommand.c_str());
    if (result == 0) {
        std::cout << "Command executed successfully." << std::endl;
    } else {
        std::cerr << "Command execution failed." << std::endl;
    }
}

// Function to find commands by name
std::vector<json> findCommandsByName(const json& commands, const std::string& commandName) {
    std::vector<json> foundCommands;
    for (const auto& command : commands) {
        if (command.contains("name") && command["name"] == commandName) {
            foundCommands.push_back(command);
        }
    }
    return foundCommands;
}

// Function to find commands by search term
std::vector<json> findCommandsBySearchTerm(const json& commands, const std::string& searchTerm) {
    std::vector<json> foundCommands;
    for (const auto& command : commands) {
        if (command.contains("name") && command["name"].get<std::string>().find(searchTerm) != std::string::npos) {
            foundCommands.push_back(command);
        } else if (command.contains("description") && command["description"].get<std::string>().find(searchTerm) != std::string::npos) {
            foundCommands.push_back(command);
        } else if (command.contains("usage") && command["usage"].get<std::string>().find(searchTerm) != std::string::npos) {
            foundCommands.push_back(command);
        } else if (command.contains("language") && command["language"].get<std::string>().find(searchTerm) != std::string::npos) {
            foundCommands.push_back(command);
        }
    }
    return foundCommands;
}

int main(int argc, char *argv[]) {
    json commands = loadCommands("data/commands.json");
    if (commands == nullptr) {
        return 1;
    }

    if (argc > 1) { // Check for command-line arguments (search term)
        std::string searchTerm = argv[1];
        std::vector<json> foundCommands = findCommandsBySearchTerm(commands, searchTerm);
        if (foundCommands.empty()) {
            std::cout << "No commands found." << std::endl;
        } else {
            for (const auto& command : foundCommands) {
                std::cout << "Name: " << command["name"] << std::endl;
                std::cout << "Description: " << command["description"] << std::endl;
                std::cout << "Usage: " << command["usage"] << std::endl;
                std::cout << "Language: " << command["language"] << std::endl;
                std::cout << "----------------------" << std::endl;
            }
        }
    } else {
        while (true) {
            std::cout << "Enter command name (l/list, h/help, s/search, exit): ";
            std::string commandName;
            std::getline(std::cin, commandName);

            if (commandName == "exit") {
                break;
            } else if (commandName == "list" || commandName == "l") {
                for (const auto& command : commands) {
                    if (command.contains("name")) {
                        std::cout << command["name"] << std::endl;
                    }
                }
            } else if (commandName == "help" || commandName == "h") {
                std::cout << "Enter the name of a command to see its description and usage." << std::endl;
                std::cout << "Type 'list' or 'l' to see all available commands." << std::endl;
                std::cout << "Type 'search' or 's' to search for commands." << std::endl;
                std::cout << "Type 'exit' to quit." << std::endl;
            } else if (commandName == "search" || commandName == "s") {
                std::cout << "Enter search term: ";
                std::string searchTerm;
                std::getline(std::cin, searchTerm);
                std::vector<json> foundCommands = findCommandsBySearchTerm(commands, searchTerm);
                if (foundCommands.empty()) {
                    std::cout << "No commands found." << std::endl;
                } else {
                    for (const auto& command : foundCommands) {
                        std::cout << "Name: " << command["name"] << std::endl;
                        std::cout << "Description: " << command["description"] << std::endl;
                        std::cout << "Usage: " << command["usage"] << std::endl;
                        std::cout << "Language: " << command["language"] << std::endl;
                        std::cout << "----------------------" << std::endl;
                    }
                }
            } else {
                std::vector<json> foundCommands = findCommandsByName(commands, commandName);
                if (foundCommands.empty()) {
                    std::cout << "Command not found." << std::endl;
                } else {
                    for (const auto& command : foundCommands) {
                        std::cout << "Description: " << command["description"] << std::endl;
                        std::cout << "Usage: " << command["usage"] << std::endl;

                        std::cout << "Execute command? (y/n): ";
                        char execute;
                        std::cin >> execute;
                        std::cin.ignore();

                        if (execute == 'y' || execute == 'Y') {
                            executeCommand(command["usage"].get<std::string>());
                        }
                    }
                }
            }
        }
    }

    return 0;
}