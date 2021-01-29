/** @type {import("snowpack").SnowpackUserConfig } */
module.exports = {
  mount: {
    'src/': '/'
  },
  plugins: [
    '@snowpack/plugin-postcss',
    '@snowpack/plugin-babel',
    '@snowpack/plugin-optimize'
  ],
  buildOptions: {
    out: '../backend/assets'
  }
}
