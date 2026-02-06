#include "search.hpp"
#include <iostream>
#include <vector>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        // No query provided, maybe list help or all commands?
        // The GUI calls it with a query.
        // ./terminal_commands list -> "All 1,024+ commands" according to README
        // Let's assume if "list" or empty, return all?
        // But README says ./terminal_commands "list" -> All commands
        // If no args, just return empty list or usage.
        std::cout << "[]" << std::endl;
        return 0;
    }

    std::string query = argv[1];

    CommandRepository repo;
    repo.LoadCommands("data/commands.json");

    std::vector<CommandResult> results;
    if (query == "list") {
        results = repo.Search(""); // Search with empty string should return all if logic permits
        // My current logic: find("") in any string returns 0 (found). So yes.
    } else {
        results = repo.Search(query);
    }

    // Convert results to JSON
    json j = results;
    std::cout << j.dump() << std::endl;

    return 0;
}
