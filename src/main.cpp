#include <string>
#include <emscripten/emscripten.h>

int global_var{ 0 };

extern "C" {
	EMSCRIPTEN_KEEPALIVE
		const char* say_hello() {
		++global_var;
		std::string* test = new std::string("sayhello");
		const char* result = test->c_str();
		delete test; // 在调用方负责释放内存
		return result;
	};

	EMSCRIPTEN_KEEPALIVE
		int reversenumber(int n) {
		++global_var;
		int reverse = 0, rem;
		while (n != 0) {
			rem = n % 10; reverse = reverse * 10 + rem; n /= 10;
		}
		return reverse;
	};

	EMSCRIPTEN_KEEPALIVE
		int get_callcount() {
		++global_var;
		return global_var;
	};
}

int main() {
	emscripten_exit_with_live_runtime(); // 保持运行时活跃
	return 0;
}