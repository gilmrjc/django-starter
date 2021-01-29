const postcssPresetEnv = require('postcss-preset-env')
const tailwindcss = require('tailwindcss')

module.exports = {
  plugins: [
    tailwindcss(),
    postcssPresetEnv({
      autprefixer: {}
    })
  ]
}
