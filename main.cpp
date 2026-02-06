#include "search.hpp"
#include <iostream>
#include <vector>
#include <cstdlib> // for getenv

int main(int argc, char* argv[]) {
    // Determine data path
    std::string dataPath = "data/commands.json";

    // Check environment variable
    const char* envPath = std::getenv("TERMINAL_GEN_DATA");
    if (envPath) {
        dataPath = envPath;
    }

    // Parse CLI arguments
    std::string query;
    bool endOfFlags = false;

    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];

        if (!endOfFlags) {
            if (arg == "--") {
                endOfFlags = true;
                continue;
            }
            if (arg == "--data" || arg == "-d") {
                if (i + 1 < argc) {
                    dataPath = argv[++i];
                }
                continue;
            }
        }
        query = arg;
    }

    // Strip quotes if present (handling shlex.quote from python)
    if (query.size() >= 2) {
        if ((query.front() == '"' && query.back() == '"') ||
            (query.front() == '\'' && query.back() == '\'')) {
            query = query.substr(1, query.size() - 2);
        }
    }

    if (query.empty()) {
        std::cout << "[]" << std::endl;
        return 0;
    }

    CommandRepository repo;
    if (!repo.LoadCommands(dataPath)) {
        return 1; // Exit with error code if loading fails
    }

    std::vector<CommandResult> results;
    if (query == "list") {
        results = repo.GetAll();
    } else {
        results = repo.Search(query);
    }

    // Convert results to JSON
    json j = results;
    std::cout << j.dump() << std::endl;

    return 0;
}
