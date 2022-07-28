# Install Docker Extension, then hover the instruction to get information
FROM node:16
USER node
ENV NODE_ENV=development
WORKDIR /home/node/elCamino
COPY --chown=node:node . .
RUN sudo npm install
EXPOSE 3000
CMD ["npm", "start"]
