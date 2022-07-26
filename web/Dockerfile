# Install Docker Extension, then hover the instruction to get information
FROM node:16
ENV NODE_ENV=development
WORKDIR /home/docker/elCamino/web
COPY ["package.json", "package-lock.json*", "npm-shrinkwrap.json*", "./"]
RUN npm install
COPY . .
EXPOSE 3000
RUN chown -R node /home/docker/elCamino/web
RUN npm install
USER node
CMD ["npm", "start"]
