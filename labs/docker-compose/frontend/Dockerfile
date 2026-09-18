# Historical React development server, not a production image.
FROM node:18.12.0
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci --no-audit --no-fund
COPY . .
ENV NODE_OPTIONS=--openssl-legacy-provider
EXPOSE 3000
CMD ["npm", "start"]
