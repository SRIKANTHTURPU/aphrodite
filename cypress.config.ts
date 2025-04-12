const { defineConfig } = require('cypress');
const { beforeRunHook, afterRunHook } = require('cypress-mochawesome-reporter/lib');
const { rm } = require('fs');
require('dotenv').config();

module.exports = defineConfig({
  projectId: process.env.CYPRESS_PROJECT_ID || 'r8uvx7',
  defaultCommandTimeout: 60000,
  pageLoadTimeout: 60000,
  numTestsKeptInMemory: 5, // Reduce memory usage

  e2e: {
    testIsolation: false,
    watchForFileChanges: false,
    downloadsFolder: "cypress/downloads",
    screenshotsFolder: 'cypress/screenshots',
    videosFolder: 'cypress/videos',
    video: false,
    experimentalMemoryManagement: true,
    experimentalInteractiveRunEvents: true,
    specPattern: 'cypress/e2e/**/*.cy.{js,ts}',

    retries: {
      runMode: 1,
      openMode: 0
    },

    reporter: 'cypress-mochawesome-reporter',
    reporterOptions: {
      reportDir: 'cypress/reports',
      charts: true,
      reportPageTitle: 'Automation Test Results',
      embeddedScreenshots: true,
      inline: true,
      reportFilename: generateReportFilename(),
      cdn: true,
      overwrite: false,
    },

    env: {
      ...process.env,
      companyName: 'Advocate Health - Midwest',
      contractstartyear: '2022',
      contractstartmonth: 'January',
      contractstartdate: 'Jan 1',
      elementInteractionTimeout: 2500,
    },

    setupNodeEvents(on, config) {
      on('before:run', async (details) => {
        console.log('Override before:run');
        await beforeRunHook(details);
      });

      on('after:run', async () => {
        console.log('Override after:run');
        await afterRunHook();
      });

      on('task', {
        deleteFile(fileName) {
          return new Promise((resolve, reject) => {
            rm(fileName, { maxRetries: 2, recursive: true }, (err) => {
              if (err) {
                console.error(`Error deleting file: ${fileName}`, err);
                reject(err);
              } else {
                console.log(`File deleted: ${fileName}`);
                resolve(null);
              }
            });
          });
        },
      });

      return config;
    },
  },
});

function generateReportFilename() {
  const projectName = process.env.projectName;
  const currentDate = new Date();

  const monthNames = [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
  ];

  const year = currentDate.getFullYear();
  const month = monthNames[currentDate.getMonth()];
  const day = currentDate.getDate();
  const hour = currentDate.getHours();
  const minutes = String(currentDate.getMinutes()).padStart(2, '0');
  const ampm = hour >= 12 ? 'PM' : 'AM';
  const formattedHour = hour % 12 || 12;

  switch (projectName) {
    case 'perspectives':
      return `Perspectives-Report-${year}-${month}-${day}-${formattedHour}-${minutes}-${ampm}`;
    case 'cost_advisor':
      return `Cost-Advisor-Report-${year}-${month}-${day}-${formattedHour}-${minutes}-${ampm}`;
    default:
      return `CFA-Report-${year}-${month}-${day}-${formattedHour}-${minutes}-${ampm}`;
  }
}