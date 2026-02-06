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
    for (int i = 1; i < argc; ++i) {
        std::string arg = argv[i];
        if ((arg == "--data" || arg == "-d") && i + 1 < argc) {
            dataPath = argv[++i];
        } else {
            query = arg;
        }
    }

    if (query.empty()) {
        // If no query, output usage or empty JSON?
        // README says "./terminal_commands list" for all.
        // If really empty arguments, maybe just return empty JSON to be safe for GUI consumers.
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
