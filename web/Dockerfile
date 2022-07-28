# Install Docker Extension, then hover the instruction to get information
FROM node:16
USER node
ENV NODE_ENV=development
WORKDIR /home/node/elCamino
COPY . .
RUN chown -R node /home/node/elCamino
RUN npm install
EXPOSE 3000
CMD ["npm", "start"]
