import { When, Then } from 'cypress-cucumber-preprocessor/steps'

const randomString = () => Math.random().toString(36).substring(2, 7)

let userEmail,
  userPassword

When('a visitor creates a new account with:', (dataTable) => {
  const data = dataTable.hashes()[0]
  const { name, password, 'last name': lastName } = data
  const email = `${name.toLowerCase()}.${lastName.toLowerCase()}+${randomString()}@example.com`
  userEmail = email
  userPassword = password

  cy.visit('/crear-cuenta/')
  cy.get('#id_first_name').type(name)
  cy.get('#id_last_name').type(lastName)
  cy.get('#id_email').type(email)
  cy.get('#id_password1').type(password)
  cy.get('button').click()
})

When('the user verifies its email', () => {
  const urlRegex = new RegExp(`${Cypress.config().baseUrl}([-a-zA-Z0-9()@:%_+.~#?&/=]+)`, 'gi')

  cy.mhGetAllMails().mhFirst().mhGetBody().then((mailBody) => {
    const confirmationUrl = urlRegex.exec(mailBody)[1]
    cy.visit(confirmationUrl)
    cy.get('form > button').click()
    cy.get('.js-notification').contains(`Has confirmado ${userEmail}`)
  })
})

When('the user logins', () => {
  cy.visit('/iniciar-sesion/')

  cy.get('#id_login').type(userEmail)
  cy.get('#id_password').type(userPassword)
  cy.get('button').click()
})

Then('a verify email message is displayed', () => {
  cy.get('h1').contains('Verifica tu dirección de correo electrónico')
})

Then('the user is redirected to the login page', () => {
  cy.location().should((location) => {
    expect(location.pathname).to.eq('/iniciar-sesion/')
  })
})

Then(/the user has (\d+) emails? with the confirmation code/, (emailsCount) => {
  cy.mhGetMailsByRecipient(userEmail).should('have.length', emailsCount)
  cy.mhGetAllMails().mhFirst().mhGetSubject()
    .should('contain', 'Por_favor_confirmar_direcci=C3=B3n_de_correo')
})
