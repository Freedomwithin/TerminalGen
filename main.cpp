#include "search.hpp"
#include <iostream>
#include <vector>
#include <cstdlib> // for getenv
#include <filesystem> // for smarter pathing

namespace fs = std::filesystem;

int main(int argc, char* argv[]) {
    // Determine data path
    std::string dataPath = "data/commands.json";

    // 1. Check environment variable
    const char* envPath = std::getenv("TERMINAL_GEN_DATA");
    if (envPath) {
        dataPath = envPath;
    } else {
        // 2. If default doesn't exist, check relative to executable
        if (!fs::exists(dataPath)) {
            try {
                fs::path exePath = fs::canonical(fs::path(argv[0]).parent_path());
                fs::path potentialPath = exePath / "data" / "commands.json";
                if (fs::exists(potentialPath)) {
                    dataPath = potentialPath.string();
                }
            } catch (...) {}
        }
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
