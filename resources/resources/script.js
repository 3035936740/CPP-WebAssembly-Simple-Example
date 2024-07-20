        let reversenumber = null;
        let get_callcount = null;
        let moduleInitialized = false;

        // 当模块加载并初始化完成后执行
        Module.onRuntimeInitialized = function() {
            // 调用导出的函数
            const result1 = Module._say_hello();
            const number = 12345;
            reversenumber = Module.cwrap('reversenumber', 'number', ['number']);
			get_callcount = Module.cwrap('get_callcount', 'number', []);
            const result2 = get_callcount();

            const result3 = Module._get_callcount();
			
			console.log(result3);
			
            // 将结果显示在页面上
            const outputDiv = document.getElementById('output');
            outputDiv.innerHTML = `
                <p>Say Hello: ${result1}</p>
                <p>Reversed Number of ${number}: ${result2}</p>
            `;

            // 标记模块已初始化
            moduleInitialized = true;

            // 如果有延迟的函数调用，可以在这里处理
            if (delayedCall) {
                delayedCall();
            }
        };

        // 延迟的函数调用
        let delayedCall = null;

        // 尝试调用函数
        function tryCallReversenumber(value) {
            if (moduleInitialized) {
                console.log(reversenumber(value));
            } else {
                delayedCall = function() {
                    console.log(reversenumber(value));
                };
            }
        }

        // 示例调用
        tryCallReversenumber(20136);
		
		function addCount() {
			const res = get_callcount();
            alert(res);
        }