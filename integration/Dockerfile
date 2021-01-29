FROM cypress/base:12.18.4

ENV CI=1

ENV CYPRESS_CACHE_FOLDER=/root/.cache/Cypress

WORKDIR /usr/src/app

COPY integration .

RUN npm install

RUN npm run test:e2e:verify

ENTRYPOINT ["npm", "run", "test:e2e"]
