#pragma once
#include <string>
#include <vector>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

class CommandResult {
public:
    std::string Name;
    std::string Description;
    std::string Usage;
    std::string Language;

    // Serialization mapping matching JSON keys (lowercase) to C++ properties (PascalCase)
    // Actually, nlohmann macro maps to the member name.
    // The JSON file has lowercase keys: "name", "description", "usage", "language".
    // I want the C++ class to have PascalCase properties: Name, Description, Usage, Language.
    // So I need to customize the to_json/from_json.
};

inline void to_json(json& j, const CommandResult& c) {
    j = json{
        {"name", c.Name},
        {"description", c.Description},
        {"usage", c.Usage},
        {"language", c.Language}
    };
}

inline void from_json(const json& j, CommandResult& c) {
    j.at("name").get_to(c.Name);
    j.at("description").get_to(c.Description);
    j.at("usage").get_to(c.Usage);
    if (j.contains("language"))
        j.at("language").get_to(c.Language);
    else
        c.Language = "Unknown";
}

class ICommandRepository {
public:
    virtual ~ICommandRepository() = default;
    virtual void LoadCommands(const std::string& path) = 0;
    virtual std::vector<CommandResult> Search(const std::string& query) = 0;
};

class CommandRepository : public ICommandRepository {
private:
    std::vector<CommandResult> commands;
public:
    void LoadCommands(const std::string& path) override;
    std::vector<CommandResult> Search(const std::string& query) override;
};
