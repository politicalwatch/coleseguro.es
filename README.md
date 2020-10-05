ColeSeguro
==========

## Development notes

To compile SCSS file,run:

```
scss --watch sass/style.scss:css/style.css
```

### Avoid 3rd party software locally

#### SASS
```
docker run --rm -v $(pwd):/data codycraven/sassc sass/style.scss > css/style.css
```

#### HTTP SERVER
```
docker run -it --rm -p 8080:8080 -v $(pwd):/public danjellz/http-server
```
