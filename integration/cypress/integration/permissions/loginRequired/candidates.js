import { When } from 'cypress-cucumber-preprocessor/steps'

When('I open the candidates list', () => {
  cy.visit('/candidatos/')
})
