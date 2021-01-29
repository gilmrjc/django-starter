import { When } from 'cypress-cucumber-preprocessor/steps'

When('I open the homepage', () => {
  cy.visit('/')
})
