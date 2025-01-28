# Use the Nginx base image
FROM nginx:alpine

# Copy the static front-end files to the default Nginx directory
COPY . /usr/share/nginx/html

# Expose port 80 for HTTP
EXPOSE 80

# Start the Nginx server
CMD ["nginx", "-g", "daemon off;"]
