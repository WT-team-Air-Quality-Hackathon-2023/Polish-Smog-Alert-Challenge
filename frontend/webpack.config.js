const path = require('path')

module.exports = {
	entry: {
		app: './source/js/app.js',
	},
	output: {
		filename: '[name].min.js',
		path: path.resolve(__dirname, 'js'),
	},
	module: {
		rules: [
			{
				test: /\.js$/,
				exclude: /node_modules/,
				loader: 'babel-loader',
				options: {
					presets: ['@babel/preset-env'],
				},
			},
		],
	},
	mode: process.env.NODE_ENV == 'production' ? 'production' : 'development',
}