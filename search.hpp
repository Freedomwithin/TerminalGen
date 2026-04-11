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
    std::string Keywords;

    // Pre-computed lowercase fields for efficiency
    std::string NameLower;
    std::string DescriptionLower;
    std::string UsageLower;
    std::string LanguageLower;
    std::string KeywordsLower;
};

inline void to_json(json& j, const CommandResult& c) {
    j = json{
        {"name", c.Name},
        {"description", c.Description},
        {"usage", c.Usage},
        {"language", c.Language},
        {"keywords", c.Keywords}
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
    
    if (j.contains("keywords"))
        j.at("keywords").get_to(c.Keywords);
    else
        c.Keywords = "";
}

class ICommandRepository {
public:
    virtual ~ICommandRepository() = default;
    virtual bool LoadCommands(const std::string& path) = 0;
    virtual std::vector<CommandResult> Search(const std::string& query) = 0;
    virtual std::vector<CommandResult> GetAll() = 0;
};

class CommandRepository : public ICommandRepository {
private:
    std::vector<CommandResult> commands;
public:
    bool LoadCommands(const std::string& path) override;
    std::vector<CommandResult> Search(const std::string& query) override;
    std::vector<CommandResult> GetAll() override;
};
