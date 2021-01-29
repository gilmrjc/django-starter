import { Then } from 'cypress-cucumber-preprocessor/steps'

Then('I am redirected to the login page', () => {
  cy.url().should('include', 'iniciar-sesion')
})
