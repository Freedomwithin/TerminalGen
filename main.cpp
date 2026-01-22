#include <emscripten.h>
#include <string.h>

extern "C" {
    EMSCRIPTEN_KEEPALIVE
    char* search_commands(char* query) {
        static char result[4096];
        
        if (strstr(query, "git")) {
            strcpy(result, "[{\"name\":\"git status\",\"desc\":\"repo status\",\"usage\":\"git status\",\"lang\":\"GIT\"},{\"name\":\"git commit\",\"desc\":\"commit changes\",\"usage\":\"git commit -m msg\",\"lang\":\"GIT\"}]");
        } else if (strstr(query, "docker")) {
            strcpy(result, "[{\"name\":\"docker ps\",\"desc\":\"list containers\",\"usage\":\"docker ps\",\"lang\":\"DOCKER\"}]");
        } else {
            strcpy(result, "[]");
        }
        return result;
    }
}

int main() {}
