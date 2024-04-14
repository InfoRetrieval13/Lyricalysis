# Build stage
FROM node:lts-alpine AS build-stage 

WORKDIR /app

COPY package*.json ./
COPY . .
RUN npm install --only=production
RUN npm install --only=development
RUN npm run build 

# Production stage
FROM nginx:stable-alpine

COPY --from=build-stage /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]