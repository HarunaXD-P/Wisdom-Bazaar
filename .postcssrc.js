// https://github.com/michael-ciniawsky/postcss-load-config

module.exports = {
  "plugins": {
    "postcss-import": {},
    "postcss-url": {},
    // to edit target browsers: use "browserslist" field in package.json
    "autoprefixer": {}
  },
  /*
	"plugins": {
	    "postcss-import": {},
	    "postcss-url": {},
	    // to edit target browsers: use "browserslist" field in package.json
	    // "autoprefixer": {},
	      "postcss-aspect-ratio-mini": {},
	      "postcss-write-svg": {
	          utf8: false
	      },
	      "postcss-cssnext": {},
	      "postcss-px-to-viewport": {
	        // 视窗的宽度，对应的是我们设计稿的宽度，移动端一般是750，如果是pc端那就是类似1920这样的尺寸
	          viewportWidth: 1920,
	          viewportHeight: 1080,    // 视窗的高度，也可以不配置
	          unitPrecision: 3,       // 指定`px`转换为视窗单位值的小数位数（很多时候无法整除）
	          viewportUnit: 'vw',    // 指定需要转换成的视窗单位，建议使用vw
	          // 过滤掉不转换为视窗单位的class类名，可以自定义，可以无限添加,建议定义一至两个通用的类名
	          selectorBlackList: ['.ignore', '.hairlines'],  
	          minPixelValue: 1,      // 小于或等于`1px`不转换为视窗单位，你也可以设置为你想要的值
	          mediaQuery: false      // 允许在媒体查询中转换`px`
	      },
	      <!--postcss-viewport-units":{} 官方建议-->"
	      <!--过滤掉::after ::before 的配置-->
	      "postcss-viewport-units":{
	          filterRule: rule => rule.selector.indexOf('::after') === -1 &&
	          rule.selector.indexOf('::before') === -1 &&
	          rule.selector.indexOf(':after') === -1 &&
	          rule.selector.indexOf(':before') === -1
	      },
	      "cssnano": {
	          preset: "default", // 设置成default将不会启用autoprefixer
	          "postcss-zindex": false
	      }
	  }*/
}
