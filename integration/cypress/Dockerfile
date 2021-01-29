FROM cypress/included:6.2.0

WORKDIR /usr/src/tests

COPY package.json package-lock.json cypress.json /usr/src/tests/

RUN npm install --no-save cypress-cucumber-preprocessor@^2.5.4 cypress-mailhog@^1.3.0
