#include <string>
#include <emscripten/emscripten.h>

extern "C" {
    EMSCRIPTEN_KEEPALIVE
    const char* say_hello() {
        std::string* test = new std::string("sayhello");
        const char* result = test->c_str();
        delete test; // 在调用方负责释放内存
        return result;
    };

    EMSCRIPTEN_KEEPALIVE
    int reversenumber(int n) {
        int reverse = 0, rem;
        while (n != 0) {
            rem = n % 10; reverse = reverse * 10 + rem; n /= 10;
        }
        return reverse;
    };
}
