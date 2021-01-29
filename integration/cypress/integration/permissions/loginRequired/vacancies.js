import { When } from 'cypress-cucumber-preprocessor/steps'

When('I open the vacancies list', () => {
  cy.visit('/vacantes/')
})
