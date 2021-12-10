安装依赖
npm i lib-flexible -S

npm i px2rem-loader -D

改\node_modules\lib-flexible\flexible.js（或者在其它地方找到这个.js文件） ：
ctrl+F: 
if (width / dpr > 540) {
            width = 540 * dpr;
        }

改为：
if (width / dpr > 540) {
            width = width * dpr;
        }