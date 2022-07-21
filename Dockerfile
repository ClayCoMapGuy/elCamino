# Install Docker Extension, hover INSTRUCTION, to get information
FROM node:16
ENV NODE_ENV=development
WORKDIR /home/node/elCamino
COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]
RUN npm install --development --silent && mv node_modules ../
COPY . .
EXPOSE 3000
RUN chown -R node /home/node/elCamino
USER node
CMD ["npm", "start"]
