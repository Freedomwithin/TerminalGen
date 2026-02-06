#include "search.hpp"
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cctype>

void CommandRepository::LoadCommands(const std::string& path) {
    try {
        std::ifstream file(path);
        if (!file.is_open()) {
            std::cerr << "Failed to open commands file: " << path << std::endl;
            return;
        }
        json j;
        file >> j;
        commands = j.get<std::vector<CommandResult>>();
    } catch (const std::exception& e) {
        std::cerr << "Error loading commands: " << e.what() << std::endl;
    }
}

// Helper to lowercase string for case-insensitive search
std::string to_lower(const std::string& s) {
    std::string data = s;
    std::transform(data.begin(), data.end(), data.begin(),
        [](unsigned char c){ return std::tolower(c); });
    return data;
}

std::vector<CommandResult> CommandRepository::Search(const std::string& query) {
    std::vector<CommandResult> results;
    std::string lowerQuery = to_lower(query);

    for (const auto& cmd : commands) {
        // Simple fuzzy search: check if query is substring of any field
        if (to_lower(cmd.Name).find(lowerQuery) != std::string::npos ||
            to_lower(cmd.Description).find(lowerQuery) != std::string::npos ||
            to_lower(cmd.Usage).find(lowerQuery) != std::string::npos ||
            to_lower(cmd.Language).find(lowerQuery) != std::string::npos) {
            results.push_back(cmd);
        }
    }
    return results;
}
