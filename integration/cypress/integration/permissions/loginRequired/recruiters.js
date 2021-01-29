import { When } from 'cypress-cucumber-preprocessor/steps'

When('I open the recruiters list', () => {
  cy.visit('/reclutadores/')
})
