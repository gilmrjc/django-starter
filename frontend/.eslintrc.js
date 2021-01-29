module.exports = {
  env: {
    es6: true
  },
  extends: [
    'airbnb-base',
    'standard'
  ],
  globals: {
    APP: true
  },
  overrides: [
    {
      files: ['**/*.ts'],
      parser: '@typescript-eslint/parser',
      parserOptions: {
        sourceType: 'module',
        project: './tsconfig.json'
      },
      plugins: [
        '@typescript-eslint'
      ],
      extends: [
        'airbnb-typescript/base',
        'plugin:@typescript-eslint/recommended',
        'plugin:@typescript-eslint/recommended-requiring-type-checking',
        'standard',
        'standard-with-typescript'
      ],
      rules: {
        '@typescript-eslint/comma-dangle': [
          'off'
        ]
      }
    }
  ]
}
