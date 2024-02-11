# Trevor's Website

Hello!

This is the home of my personal website. 

## Overview

This repository contains the source code for my personal site, structured in TTL.

Example:
```yaml
section [
   title: formatted: code {print("Hello, World! 👋")}}
   body {
      I'm a multi-line string.
   }
]
```

## Project Structure

1. I manually create the `.ttl` files for each page on the website (along with the corresponding `/templates`. 
2. On GH push, a GH action executes the TTL.py on all the `.ttl` files in the root directiory to generate the HTML.
3. When the HTML is commited to the production branch (by the GH action), my webserver is re-started using the new HTML.

## Deployment

This site is deployed using DigitalOcean Apps. The deployment process is designed to be seamless and automatic, leveraging the power of GitHub Actions for continuous integration and continuous deployment (CI/CD).

- **Source**: The source for deployment is set to the directory or repository that contains the rendered HTML files.
- **Configuration**: The DigitalOcean App is configured to automatically pull changes from this source, ensuring that the live site is always up-to-date with the latest versions of the HTML files.

## Contributing

Feel free to fork this project if you're interested in creating your own site using a similar setup. If you have suggestions for improvements or encounter any issues, please open an issue or submit a pull request.

Thank you for visiting my personal website repository!
