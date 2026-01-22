#include <emscripten.h>
#include <string.h>
#include <string>

extern "C" {
    EMSCRIPTEN_KEEPALIVE
    char* search_commands(char* query_c) {
        static char result[4096];
        std::string query(query_c);
        
        // SIMULATE FULL DATASET SEARCH (real impl tomorrow)
        if (query.find("git") != std::string::npos) {
            strcpy(result, "[{\"name\":\"git status\",\"desc\":\"repo status\",\"usage\":\"git status\",\"lang\":\"GIT\"},{\"name\":\"git commit\",\"desc\":\"commit changes\",\"usage\":\"git commit -m msg\",\"lang\":\"GIT\"},{\"name\":\"git push\",\"desc\":\"push changes\",\"usage\":\"git push origin main\",\"lang\":\"GIT\"}]");
        } else if (query.find("docker") != std::string::npos) {
            strcpy(result, "[{\"name\":\"docker ps\",\"desc\":\"list containers\",\"usage\":\"docker ps\",\"lang\":\"DOCKER\"},{\"name\":\"docker run\",\"desc\":\"run container\",\"usage\":\"docker run -d nginx\",\"lang\":\"DOCKER\"}]");
        } else {
            strcpy(result, "[]");
        }
        return result;
    }
}
