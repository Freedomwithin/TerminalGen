#include "search.hpp"
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cctype>

// Helper to lowercase string for case-insensitive search
std::string to_lower(const std::string& s) {
    std::string data = s;
    std::transform(data.begin(), data.end(), data.begin(),
        [](unsigned char c){ return std::tolower(c); });
    return data;
}

bool CommandRepository::LoadCommands(const std::string& path) {
    try {
        std::ifstream file(path);
        if (!file.is_open()) {
            std::cerr << "Failed to open commands file: " << path << std::endl;
            return false;
        }
        json j;
        file >> j;
        commands = j.get<std::vector<CommandResult>>();

        // Pre-compute lowercase fields
        for (auto& cmd : commands) {
            cmd.NameLower = to_lower(cmd.Name);
            cmd.DescriptionLower = to_lower(cmd.Description);
            cmd.UsageLower = to_lower(cmd.Usage);
            cmd.LanguageLower = to_lower(cmd.Language);
        }
        return true;
    } catch (const std::exception& e) {
        std::cerr << "Error loading commands: " << e.what() << std::endl;
        return false;
    }
}

std::vector<CommandResult> CommandRepository::Search(const std::string& query) {
    std::vector<CommandResult> results;
    std::string lowerQuery = to_lower(query);

    for (const auto& cmd : commands) {
        // Optimized fuzzy search using pre-computed lowercase fields
        if (cmd.NameLower.find(lowerQuery) != std::string::npos ||
            cmd.DescriptionLower.find(lowerQuery) != std::string::npos ||
            cmd.UsageLower.find(lowerQuery) != std::string::npos ||
            cmd.LanguageLower.find(lowerQuery) != std::string::npos) {
            results.push_back(cmd);
        }
    }
    return results;
}

std::vector<CommandResult> CommandRepository::GetAll() {
    return commands;
}
