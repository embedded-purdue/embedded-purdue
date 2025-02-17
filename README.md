# Embedded Systems @ Purdue Website

This repository contains the code for the Embedded Purdue website, custom built using [Astro](https://astro.build/).

## Maintenance
This webiste reflects the current state of ES@P, so should reflect all recent work. Update with new photos, projects, and members regularly. Maintenance is assigned to the president, although any member may contribute. Basic knowledge of HTML/CSS/JS and Astro recommended.
# Data Management Instructions

## Steps
1. Update Data in Excel File
   - Open the `data.xlsx` file located in the `data` folder.
   - Update the following fields manually: Name, Role, Image, MajorYear, LinkedIn

2. Upload Images
   - Upload the updated images to the `public/media` folder.

3. Generate JSON Data
   - Run the following command to load the data into JSON format:
     npm run generate-data

This will unpack the data and make it ready for use.

## Contributions

Contributions are welcome! Check the Issues tab for pending tasks. Follow these steps to contribute:

1. Fork the repository on GitHub.
2. Create a new branch for your changes: `git checkout -b feature-branch-name`
3. Make your changes and commit them: `git commit -m "Description of changes"`
4. Push your changes to your fork: `git push origin feature-branch-name`
5. Submit a pull request to the main repository.

## Installation

1. Clone the repository
2. Install dependencies using npm: `npm install`
3. Start the development server: `npm run dev`
4. Open the local development environment: The website should be available at http://localhost:4321/ (or as indicated in the terminal output).

## License

This project is licensed under the MIT License. See the LICENSE file for details.