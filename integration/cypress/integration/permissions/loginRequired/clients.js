import { When } from 'cypress-cucumber-preprocessor/steps'

When('I open the clients list', () => {
  cy.visit('/companias/')
})
