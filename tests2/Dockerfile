FROM nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY ./home/ivan/project1/djangogirls /usr/share/nginx/app
CMD ["nginx", "-g", "daemon off; "]
