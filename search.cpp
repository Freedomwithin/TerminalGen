#include "search.hpp"
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cctype>
#include <sstream>

// Helper to lowercase string
std::string to_lower(const std::string& s) {
    std::string data = s;
    std::transform(data.begin(), data.end(), data.begin(),
        [](unsigned char c){ return std::tolower(c); });
    return data;
}

// Split string into words
std::vector<std::string> split_words(const std::string& s) {
    std::vector<std::string> words;
    std::stringstream ss(s);
    std::string word;
    while (ss >> word) {
        words.push_back(to_lower(word));
    }
    return words;
}

bool CommandRepository::LoadCommands(const std::string& path) {
    try {
        std::ifstream file(path);
        if (!file.is_open()) return false;
        json j;
        file >> j;
        commands = j.get<std::vector<CommandResult>>();

        for (auto& cmd : commands) {
            cmd.NameLower = to_lower(cmd.Name);
            cmd.DescriptionLower = to_lower(cmd.Description);
            cmd.UsageLower = to_lower(cmd.Usage);
            cmd.LanguageLower = to_lower(cmd.Language);
            cmd.KeywordsLower = to_lower(cmd.Keywords);
        }
        return true;
    } catch (...) {
        return false;
    }
}

std::vector<CommandResult> CommandRepository::Search(const std::string& query) {
    std::vector<CommandResult> results;
    std::string lowerQuery = to_lower(query);
    std::vector<std::string> queryWords = split_words(query);

    for (const auto& cmd : commands) {
        // 1. Exact substring match (Original behavior - High priority)
        if (cmd.NameLower.find(lowerQuery) != std::string::npos ||
            cmd.DescriptionLower.find(lowerQuery) != std::string::npos ||
            cmd.KeywordsLower.find(lowerQuery) != std::string::npos) {
            results.push_back(cmd);
            continue;
        }

        // 2. Multi-word "Smart" Match (New behavior)
        // If ALL words in the query are found SOMEWHERE in the command's name, description, or keywords
        bool allWordsMatch = true;
        for (const auto& word : queryWords) {
            if (word.length() < 3) continue; // Skip short words like "to", "in", "a"
            
            if (cmd.NameLower.find(word) == std::string::npos &&
                cmd.DescriptionLower.find(word) == std::string::npos &&
                cmd.KeywordsLower.find(word) == std::string::npos) {
                allWordsMatch = false;
                break;
            }
        }

        if (allWordsMatch && !queryWords.empty()) {
            results.push_back(cmd);
        }
    }
    return results;
}

std::vector<CommandResult> CommandRepository::GetAll() {
    return commands;
}
