# Trevor's Personal Website

Hello!

This is the home of my personal website. The repository name might seem random, but it was a suggestion by GitHub that stuck.

## Overview

This repository contains the source code for my personal site, structured in TTL (Template Transformation Language) files. A unique aspect of this project is the use of GitHub Actions to automatically render the website from TTL files into HTML, which are then deployed to a DigitalOcean App for hosting.

## Project Structure

- `src/`: Contains the TTL files that define the structure and content of my website.
- `parser/`: Houses the custom Parser class responsible for interpreting TTL files and generating an intermediate representation.
- `renderer/`: Contains the Renderer module, which converts the intermediate representation into HTML files.
- `actions/`: Defines the GitHub Actions workflows that automate the parsing and rendering process.
- `public/`: The output directory where the rendered HTML files are placed. (This directory might be in a separate branch or repository, depending on the deployment strategy.)

## Workflow

1. **Content Update**: Whenever I update the TTL files in the `src/` directory, I push the changes to the repository.
2. **GitHub Actions**: On every push to the main branch, a GitHub Action is triggered that executes the following steps:
   - **Parse**: The TTL files are parsed into an intermediate representation using the custom Parser.
   - **Render**: The Renderer module transforms the intermediate representation into static HTML files.
   - **Deploy**: The rendered files are either pushed to a specific directory within this repository, to another branch, or even to a separate repository, based on the configured deployment strategy.
3. **DigitalOcean Deployment**: A DigitalOcean App monitors the directory or repository where the rendered HTML files are stored. Upon detecting changes, it automatically deploys the new version of the site.

## Deployment

This site is deployed using DigitalOcean Apps. The deployment process is designed to be seamless and automatic, leveraging the power of GitHub Actions for continuous integration and continuous deployment (CI/CD).

- **Source**: The source for deployment is set to the directory or repository that contains the rendered HTML files.
- **Configuration**: The DigitalOcean App is configured to automatically pull changes from this source, ensuring that the live site is always up-to-date with the latest versions of the HTML files.

## Contributing

Feel free to fork this project if you're interested in creating your own site using a similar setup. If you have suggestions for improvements or encounter any issues, please open an issue or submit a pull request.

Thank you for visiting my personal website repository!
