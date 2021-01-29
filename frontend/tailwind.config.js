const forms = require('@tailwindcss/forms')

module.exports = {
  purge: [
    './src/js/**/*.js',
    './src/js/**/*.ts',
    '../backend/**/*.html'
  ],
  darkMode: false,
  variants: {
    extend: {
      ringColor: ['hover'],
      ringOffsetColor: ['hover'],
      ringOffsetWidth: ['hover'],
      ringWidth: ['hover']
    }
  },
  plugins: [
    forms
  ]
}
