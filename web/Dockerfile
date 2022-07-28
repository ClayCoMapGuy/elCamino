# Install Docker Extension, then hover the instruction to get information
FROM node:16
ENV NODE_ENV=development
WORKDIR /home/node/elCamino
COPY --chown=node:node . .
EXPOSE 3000
RUN npm install
USER node
CMD ["npm", "start"]
