# Use nginx to serve the static site
FROM nginx:stable-alpine
LABEL maintainer="Sumit <noreply@example.com>"

# Copy site files into nginx html root
WORKDIR /usr/share/nginx/html
COPY . /usr/share/nginx/html

# Replace default nginx config with our SPA-friendly config
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Ensure proper permissions
RUN chmod -R 755 /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
