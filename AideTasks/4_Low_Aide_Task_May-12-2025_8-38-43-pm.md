**User:**

<task>
In Opened the existing Cypress project with BDD framework in Visual Studio Code, Introduce custom assertion methods in the existing project for validating UI elements (ex. Is element exists on page".Implement the assertions as reusable functions in the commands.ts file.
</task>
<environment_details>
# VSCode Visible Files
docs/test-tagging-strategy.md

# VSCode Open Tabs
config/email.config.js
sendFailedTestsReport.js
README_EmailReporter.md
cypress/e2e/features/token-refresh.feature
cypress/support/token-refresh.ts
cypress/support/e2e.ts
cypress/support/cypress.d.ts
cypress/e2e/step-definitions/token-refresh.cy.ts
.husky/pre-commit
package.json
cypress/scripts/tag-tests.ts
docs/test-tagging-strategy.md

# Current Time
5/12/2025, 8:35:42 PM (Asia/Calcutta, UTC+5.5:00)

# Current Working Directory (d:/Artemis_Workspace/nextqa) Files
.env
cypress.config.ts
generateNextQAReport.bat
package-lock.json
package.json
README_EmailReporter.md
README.md
sendFailedTestsReport.js
tsconfig.json
config/
config/email.config.js
coverage-analysis/
coverage-analysis/comprehensive-test-coverage-report.md
coverage-analysis/executive-summary.md
coverage-analysis/frontend-components.md
coverage-analysis/high-risk-areas.md
coverage-analysis/test-case-outlines.md
coverage-analysis/test-coverage-matrix.md
cypress/
cypress/tagging-report.md
cypress/test-login-error-handling.js
cypress/downloads/
cypress/e2e/
cypress/e2e/features/
cypress/e2e/features/login-error-handling.feature
cypress/e2e/features/reportbuilderpage.feature
cypress/e2e/features/rolespage.feature
cypress/e2e/features/token-refresh.feature
cypress/e2e/pages/
cypress/e2e/pages/homepage.ts
cypress/e2e/pages/loginpage.ts
cypress/e2e/pages/reportbuilderpage.ts
cypress/e2e/pages/rolespage.ts
cypress/e2e/step-definitions/
cypress/e2e/step-definitions/homePage.cy.ts
cypress/e2e/step-definitions/login-error-handling.cy.ts
cypress/e2e/step-definitions/reportbuilderpage.cy.ts
cypress/e2e/step-definitions/rolespage.cy.ts
cypress/e2e/step-definitions/token-refresh.cy.ts
cypress/fixtures/
cypress/fixtures/example.json
cypress/fixtures/NextUploadCSV-1.csv
cypress/fixtures/NextUploadCSV-2.csv
cypress/fixtures/NextUploadCSV-DuplicateValues.csv
cypress/fixtures/NextUploadCSV-MoreValues_1.csv
cypress/reports/
cypress/reports/junit/
cypress/reports/mochawesome/
cypress/reports/mochawesome/mochawesome.json
cypress/screenshots/
cypress/scripts/
cypress/scripts/tag-tests.ts
cypress/support/
cypress/support/commands.ts
cypress/support/cypress.d.ts
cypress/support/e2e.ts
cypress/support/token-refresh.ts
docs/
docs/login-server-error-handling.md
docs/test-tagging-strategy.md
logs/
logs/13_28_24_GET_https_artemishealth.atlassian.net_rest_api_latest_myself_response.json
logs/13_57_26_GET_https_artemishealth.atlassian.net_rest_api_latest_myself_response.json
logs/getMyselfError.json

# Current Mode
ACT MODE
</environment_details>

---

**Assistant:**

I'll implement custom UI element assertion methods in the commands.ts file. First, let me check the current content of this file.

<read_file>
<path>cypress/support/commands.ts</path>
</read_file>

---

**User:**

[read_file for 'cypress/support/commands.ts'] Result:
/// <reference types="cypress" />
// ***********************************************
// This example commands.ts shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })
//
// declare global {
//   namespace Cypress {
//     interface Chainable {
//       login(email: string, password: string): Chainable<void>
//       drag(subject: string, options?: Partial<TypeOptions>): Chainable<Element>
//       dismiss(subject: string, options?: Partial<TypeOptions>): Chainable<Element>
//       visit(originalFn: CommandOriginalFn, url: string, options: Partial<VisitOptions>): Chainable<Element>
//     }
//   }
// }

import 'cypress-real-events';
import 'cypress-file-upload';

Cypress.Commands.add('checkIfElementExists',  (elementLocator: string): Cypress.Chainable<boolean> => {
    // Return a Cypress.Chainable that resolves to a boolean value
    return cy.get('body').then((body) => {
      if (body.find(elementLocator).length > 0) {
        return true;
      }
      return false;
    });
  },
);
<environment_details>
# VSCode Visible Files
docs/test-tagging-strategy.md

# VSCode Open Tabs
config/email.config.js
sendFailedTestsReport.js
README_EmailReporter.md
cypress/e2e/features/token-refresh.feature
cypress/support/token-refresh.ts
cypress/support/e2e.ts
cypress/support/cypress.d.ts
cypress/e2e/step-definitions/token-refresh.cy.ts
.husky/pre-commit
package.json
cypress/scripts/tag-tests.ts
docs/test-tagging-strategy.md

# Current Time
5/12/2025, 8:36:06 PM (Asia/Calcutta, UTC+5.5:00)

# Current Mode
ACT MODE
</environment_details>

---

**Assistant:**

Now I'll check the current type definitions in the cypress.d.ts file to understand the existing custom command structure:

<read_file>
<path>cypress/support/cypress.d.ts</path>
</read_file>

---

**User:**

[read_file for 'cypress/support/cypress.d.ts'] Result:
declare namespace Cypress {
  interface Chainable {    
    checkIfElementExists(elementLocator: string): Chainable<boolean>;    
    
    /**
     * Custom command to test token refresh scenarios
     * @param options Configuration options for the token refresh test
     * @example cy.testTokenRefresh({ apiEndpoint: '/api/data', shouldRefreshSucceed: true })
     */
    testTokenRefresh(options?: {
      apiEndpoint?: string;
      shouldRefreshSucceed?: boolean;
      shouldRetrySucceed?: boolean;
      simulateDelay?: number;
    }): Chainable<void>;
  }
}

<environment_details>
# VSCode Visible Files
docs/test-tagging-strategy.md

# VSCode Open Tabs
config/email.config.js
sendFailedTestsReport.js
README_EmailReporter.md
cypress/e2e/features/token-refresh.feature
cypress/support/token-refresh.ts
cypress/support/e2e.ts
cypress/support/cypress.d.ts
cypress/e2e/step-definitions/token-refresh.cy.ts
.husky/pre-commit
package.json
cypress/scripts/tag-tests.ts
docs/test-tagging-strategy.md

# Current Time
5/12/2025, 8:36:27 PM (Asia/Calcutta, UTC+5.5:00)

# Current Mode
ACT MODE
</environment_details>

---

**Assistant:**

Now I'll implement several custom UI assertion methods in the commands.ts file. I'll add these methods to make UI element validations more reusable throughout the test suite.

<replace_in_file>
<path>cypress/support/commands.ts</path>
<diff>
<<<<<<< SEARCH
import 'cypress-real-events';
import 'cypress-file-upload';

Cypress.Commands.add('checkIfElementExists',  (elementLocator: string): Cypress.Chainable<boolean> => {
    // Return a Cypress.Chainable that resolves to a boolean value
    return cy.get('body').then((body) => {
      if (body.find(elementLocator).length > 0) {
        return true;
      }
      return false;
    });
  },
);
=======
import 'cypress-real-events';
import 'cypress-file-upload';

/**
 * Custom UI assertion functions for common element validation
 */

/**
 * Check if an element exists on the page
 * @param elementLocator - CSS selector for the element to check
 * @returns boolean indicating if element exists
 */
Cypress.Commands.add('checkIfElementExists', (elementLocator: string): Cypress.Chainable<boolean> => {
  // Return a Cypress.Chainable that resolves to a boolean value
  return cy.get('body').then((body) => {
    if (body.find(elementLocator).length > 0) {
      return true;
    }
    return false;
  });
});

/**
 * Assert that an element is visible on the page
 * @param elementLocator - CSS selector for the element to check
 * @param timeoutMs - Optional timeout in milliseconds (default: 10000)
 */
Cypress.Commands.add('assertElementVisible', (elementLocator: string, timeoutMs = 10000) => {
  cy.get(elementLocator, { timeout: timeoutMs }).should('be.visible');
});

/**
 * Assert that an element is not visible on the page
 * @param elementLocator - CSS selector for the element to check 
 * @param timeoutMs - Optional timeout in milliseconds (default: 10000)
 */
Cypress.Commands.add('assertElementNotVisible', (elementLocator: string, timeoutMs = 10000) => {
  cy.get(elementLocator, { timeout: timeoutMs }).should('not.be.visible');
});

/**
 * Assert that an element contains specific text
 * @param elementLocator - CSS selector for the element to check
 * @param text - Text that should be present in the element
 * @param timeoutMs - Optional timeout in milliseconds (default: 10000)
 */
Cypress.Commands.add('assertElementContainsText', (elementLocator: string, text: string, timeoutMs = 10000) => {
  cy.get(elementLocator, { timeout: timeoutMs }).should('contain', text);
});

/**
 * Assert that an element has exact text
 * @param elementLocator - CSS selector for the element to check
 * @param text - Exact text that the element should have
 * @param timeoutMs - Optional timeout in milliseconds (default: 10000)
 */
Cypress.Commands.add('assertElementHasText', (elementLocator: string, text: string, timeoutMs = 10000) => {
  cy.get(elementLocator, { timeout: timeoutMs }).should('have.text', text);
});

/**
 * Assert that an element has a specific attribute value
 * @param elementLocator - CSS selector for the element to check
 * @param attribute - Attribute name to check
 * @param value - Expected attribute value
 * @param timeoutMs - Optional timeout in milliseconds (default: 10000)
 */
Cypress.Commands.add('assertElementHasAttribute', (elementLocator: string, attribute: string, value: string, timeoutMs = 10000) => {
  cy.get(elementLocator, { timeout: timeoutMs }).should('have.attr', attribute, value);
});

/**
 * Assert that an element is enabled
 * @param elementLocator - CSS selector for the element to check
 * @param timeoutMs - Optional timeout in milliseconds (default: 10000)
 */
Cypress.Commands.add('assertElementEnabled', (elementLocator: string, timeoutMs = 10000) => {
  cy.get(elementLocator, { timeout: timeoutMs }).should('be.enabled');
});

/**
 * Assert that an element is disabled
 * @param elementLocator - CSS selector for the element to check
 * @param timeoutMs - Optional timeout in milliseconds (default: 10000)
 */
Cypress.Commands.add('assertElementDisabled', (elementLocator: string, timeoutMs = 10000) => {
  cy.get(elementLocator, { timeout: timeoutMs }).should('be.disabled');
});

/**
 * Assert that a URL contains a specific path
 * @param urlPath - Path that should be included in the URL
 * @param timeoutMs - Optional timeout in milliseconds (default: 10000)
 */
Cypress.Commands.add('assertUrlContains', (urlPath: string, timeoutMs = 10000) => {
  cy.url({ timeout: timeoutMs }).should('include', urlPath);
});

/**
 * Assert that the count of elements matching a selector is as expected
 * @param elementLocator - CSS selector for the elements to count
 * @param expectedCount - Expected number of elements
 * @param timeoutMs - Optional timeout in milliseconds (default: 10000)
 */
Cypress.Commands.add('assertElementCount', (elementLocator: string, expectedCount: number, timeoutMs = 10000) => {
  cy.get(elementLocator, { timeout: timeoutMs }).should('have.length', expectedCount);
});

/**
 * Assert that an element has a CSS class
 * @param elementLocator - CSS selector for the element to check
 * @param className - CSS class name that should be present
 * @param timeoutMs - Optional timeout in milliseconds (default: 10000)
 */
Cypress.Commands.add('assertElementHasClass', (elementLocator: string, className: string, timeoutMs = 10000) => {
  cy.get(elementLocator, { timeout: timeoutMs }).should('have.class', className);
});
>>>>>>> REPLACE
</diff>
</replace_in_file>

---

**User:**

[replace_in_file for 'cypress/support/commands.ts'] Result:
The content was successfully saved to cypress/support/commands.ts.

Here is the full, updated content of the file that was saved:

<final_file_content path="cypress/support/commands.ts">
/// <reference types="cypress" />
// ***********************************************
// This example commands.ts shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//
// -- This is a parent command --
// Cypress.Commands.add('login', (email, password) => { ... })
//
//
// -- This is a child command --
// Cypress.Commands.add('drag', { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add('dismiss', { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This will overwrite an existing command --
// Cypress.Commands.overwrite('visit', (originalFn, url, options) => { ... })
//
// declare global {
//   namespace Cypress {
//     interface Chainable {
//       login(email: string, password: string): Chainable<void>
//       drag(subject: string, options?: Partial<TypeOptions>): Chainable<Element>
//       dismiss(subject: string, options?: Partial<TypeOptions>): Chainable<Element>
//       visit(originalFn: CommandOriginalFn, url: string, options: Partial<VisitOptions>): Chainable<Element>
//     }
//   }
// }

import 'cypress-real-events';
import 'cypress-file-upload';

/**
 * Custom UI assertion functions for common element validation
 */

/**
 * Check if an element exists on the page
 * @param elementLocator - CSS selector for the element to check
 * @returns boolean indicating if element exists
 */
Cypress.Commands.add('checkIfElementExists', (elementLocator: string): Cypress.Chainable<boolean> => {
  // Return a Cypress.Chainable that resolves to a boolean value
  return cy.get('body').then((body) => {
    if (body.find(elementLocator).length > 0) {
      return true;
    }
    return false;
  });
});

/**
 * Assert that an element is visible on the page
 * @param elementLocator - CSS selector for the element to check
 * @param timeoutMs - Optional timeout in milliseconds (default: 10000)
 */
Cypress.Commands.add('assertElementVisible', (elementLocator: string, timeoutMs = 10000) => {
  cy.get(elementLocator, { timeout: timeoutMs }).should('be.visible');
});

/**
 * Assert that an element is not visible on the page
 * @param elementLocator - CSS selector for the element to check 
 * @param timeoutMs - Optional timeout in milliseconds (default: 10000)
 */
Cypress.Commands.add('assertElementNotVisible', (elementLocator: string, timeoutMs = 10000) => {
  cy.get(elementLocator, { timeout: timeoutMs }).should('not.be.visible');
});

/**
 * Assert that an element contains specific text
 * @param elementLocator - CSS selector for the element to check
 * @param text - Text that should be present in the element
 * @param timeoutMs - Optional timeout in milliseconds (default: 10000)
 */
Cypress.Commands.add('assertElementContainsText', (elementLocator: string, text: string, timeoutMs = 10000) => {
  cy.get(elementLocator, { timeout: timeoutMs }).should('contain', text);
});

/**
 * Assert that an element has exact text
 * @param elementLocator - CSS selector for the element to check
 * @param text - Exact text that the element should have
 * @param timeoutMs - Optional timeout in milliseconds (default: 10000)
 */
Cypress.Commands.add('assertElementHasText', (elementLocator: string, text: string, timeoutMs = 10000) => {
  cy.get(elementLocator, { timeout: timeoutMs }).should('have.text', text);
});

/**
 * Assert that an element has a specific attribute value
 * @param elementLocator - CSS selector for the element to check
 * @param attribute - Attribute name to check
 * @param value - Expected attribute value
 * @param timeoutMs - Optional timeout in milliseconds (default: 10000)
 */
Cypress.Commands.add('assertElementHasAttribute', (elementLocator: string, attribute: string, value: string, timeoutMs = 10000) => {
  cy.get(elementLocator, { timeout: timeoutMs }).should('have.attr', attribute, value);
});

/**
 * Assert that an element is enabled
 * @param elementLocator - CSS selector for the element to check
 * @param timeoutMs - Optional timeout in milliseconds (default: 10000)
 */
Cypress.Commands.add('assertElementEnabled', (elementLocator: string, timeoutMs = 10000) => {
  cy.get(elementLocator, { timeout: timeoutMs }).should('be.enabled');
});

/**
 * Assert that an element is disabled
 * @param elementLocator - CSS selector for the element to check
 * @param timeoutMs - Optional timeout in milliseconds (default: 10000)
 */
Cypress.Commands.add('assertElementDisabled', (elementLocator: string, timeoutMs = 10000) => {
  cy.get(elementLocator, { timeout: timeoutMs }).should('be.disabled');
});

/**
 * Assert that a URL contains a specific path
 * @param urlPath - Path that should be included in the URL
 * @param timeoutMs - Optional timeout in milliseconds (default: 10000)
 */
Cypress.Commands.add('assertUrlContains', (urlPath: string, timeoutMs = 10000) => {
  cy.url({ timeout: timeoutMs }).should('include', urlPath);
});

/**
 * Assert that the count of elements matching a selector is as expected
 * @param elementLocator - CSS selector for the elements to count
 * @param expectedCount - Expected number of elements
 * @param timeoutMs - Optional timeout in milliseconds (default: 10000)
 */
Cypress.Commands.add('assertElementCount', (elementLocator: string, expectedCount: number, timeoutMs = 10000) => {
  cy.get(elementLocator, { timeout: timeoutMs }).should('have.length', expectedCount);
});

/**
 * Assert that an element has a CSS class
 * @param elementLocator - CSS selector for the element to check
 * @param className - CSS class name that should be present
 * @param timeoutMs - Optional timeout in milliseconds (default: 10000)
 */
Cypress.Commands.add('assertElementHasClass', (elementLocator: string, className: string, timeoutMs = 10000) => {
  cy.get(elementLocator, { timeout: timeoutMs }).should('have.class', className);
});

</final_file_content>

IMPORTANT: For any future changes to this file, use the final_file_content shown above as your reference. This content reflects the current state of the file, including any auto-formatting (e.g., if you used single quotes but the formatter converted them to double quotes). Always base your SEARCH/REPLACE operations on this final version to ensure accuracy.



New problems detected after saving the file:
cypress/support/commands.ts
- [ts Error] Line 66: Argument of type '"assertElementVisible"' is not assignable to parameter of type 'keyof Chainable<any>'.
- [ts Error] Line 75: Argument of type '"assertElementNotVisible"' is not assignable to parameter of type 'keyof Chainable<any>'.
- [ts Error] Line 85: Argument of type '"assertElementContainsText"' is not assignable to parameter of type 'keyof Chainable<any>'.
- [ts Error] Line 95: Argument of type '"assertElementHasText"' is not assignable to parameter of type 'keyof Chainable<any>'.
- [ts Error] Line 106: Argument of type '"assertElementHasAttribute"' is not assignable to parameter of type 'keyof Chainable<any>'.
- [ts Error] Line 115: Argument of type '"assertElementEnabled"' is not assignable to parameter of type 'keyof Chainable<any>'.
- [ts Error] Line 124: Argument of type '"assertElementDisabled"' is not assignable to parameter of type 'keyof Chainable<any>'.
- [ts Error] Line 133: Argument of type '"assertUrlContains"' is not assignable to parameter of type 'keyof Chainable<any>'.
- [ts Error] Line 143: Argument of type '"assertElementCount"' is not assignable to parameter of type 'keyof Chainable<any>'.
- [ts Error] Line 153: Argument of type '"assertElementHasClass"' is not assignable to parameter of type 'keyof Chainable<any>'.
<environment_details>
# VSCode Visible Files
cypress/support/commands.ts

# VSCode Open Tabs
config/email.config.js
sendFailedTestsReport.js
README_EmailReporter.md
cypress/e2e/features/token-refresh.feature
cypress/support/token-refresh.ts
cypress/support/e2e.ts
cypress/support/cypress.d.ts
cypress/e2e/step-definitions/token-refresh.cy.ts
.husky/pre-commit
package.json
cypress/scripts/tag-tests.ts
docs/test-tagging-strategy.md
cypress/support/commands.ts

# Recently Modified Files
These files have been modified since you last accessed them (file was just edited so you may need to re-read it before editing):
cypress/support/commands.ts

# Current Time
5/12/2025, 8:37:06 PM (Asia/Calcutta, UTC+5.5:00)

# Current Mode
ACT MODE
</environment_details>

---

**Assistant:**

Now I need to update the cypress.d.ts file to add the type definitions for the new custom assertion methods I've added. This will resolve the TypeScript errors.

<replace_in_file>
<path>cypress/support/cypress.d.ts</path>
<diff>
<<<<<<< SEARCH
declare namespace Cypress {
  interface Chainable {    
    checkIfElementExists(elementLocator: string): Chainable<boolean>;    
    
    /**
     * Custom command to test token refresh scenarios
     * @param options Configuration options for the token refresh test
     * @example cy.testTokenRefresh({ apiEndpoint: '/api/data', shouldRefreshSucceed: true })
     */
    testTokenRefresh(options?: {
      apiEndpoint?: string;
      shouldRefreshSucceed?: boolean;
      shouldRetrySucceed?: boolean;
      simulateDelay?: number;
    }): Chainable<void>;
  }
}
=======
declare namespace Cypress {
  interface Chainable {    
    /**
     * Check if an element exists on the page
     * @param elementLocator CSS selector for the element to check
     * @example cy.checkIfElementExists('.my-selector')
     */
    checkIfElementExists(elementLocator: string): Chainable<boolean>;
    
    /**
     * Assert that an element is visible on the page
     * @param elementLocator CSS selector for the element to check
     * @param timeoutMs Optional timeout in milliseconds (default: 10000)
     * @example cy.assertElementVisible('.my-selector')
     */
    assertElementVisible(elementLocator: string, timeoutMs?: number): Chainable<JQuery<HTMLElement>>;
    
    /**
     * Assert that an element is not visible on the page
     * @param elementLocator CSS selector for the element to check
     * @param timeoutMs Optional timeout in milliseconds (default: 10000)
     * @example cy.assertElementNotVisible('.my-selector')
     */
    assertElementNotVisible(elementLocator: string, timeoutMs?: number): Chainable<JQuery<HTMLElement>>;
    
    /**
     * Assert that an element contains specific text
     * @param elementLocator CSS selector for the element to check
     * @param text Text that should be present in the element
     * @param timeoutMs Optional timeout in milliseconds (default: 10000)
     * @example cy.assertElementContainsText('.my-selector', 'Expected text')
     */
    assertElementContainsText(elementLocator: string, text: string, timeoutMs?: number): Chainable<JQuery<HTMLElement>>;
    
    /**
     * Assert that an element has exact text
     * @param elementLocator CSS selector for the element to check
     * @param text Exact text that the element should have
     * @param timeoutMs Optional timeout in milliseconds (default: 10000)
     * @example cy.assertElementHasText('.my-selector', 'Exact text')
     */
    assertElementHasText(elementLocator: string, text: string, timeoutMs?: number): Chainable<JQuery<HTMLElement>>;
    
    /**
     * Assert that an element has a specific attribute value
     * @param elementLocator CSS selector for the element to check
     * @param attribute Attribute name to check
     * @param value Expected attribute value
     * @param timeoutMs Optional timeout in milliseconds (default: 10000)
     * @example cy.assertElementHasAttribute('.my-selector', 'data-testid', 'test-value')
     */
    assertElementHasAttribute(elementLocator: string, attribute: string, value: string, timeoutMs?: number): Chainable<JQuery<HTMLElement>>;
    
    /**
     * Assert that an element is enabled
     * @param elementLocator CSS selector for the element to check
     * @param timeoutMs Optional timeout in milliseconds (default: 10000)
     * @example cy.assertElementEnabled('.my-button')
     */
    assertElementEnabled(elementLocator: string, timeoutMs?: number): Chainable<JQuery<HTMLElement>>;
    
    /**
     * Assert that an element is disabled
     * @param elementLocator CSS selector for the element to check
     * @param timeoutMs Optional timeout in milliseconds (default: 10000)
     * @example cy.assertElementDisabled('.my-button')
     */
    assertElementDisabled(elementLocator: string, timeoutMs?: number): Chainable<JQuery<HTMLElement>>;
    
    /**
     * Assert that a URL contains a specific path
     * @param urlPath Path that should be included in the URL
     * @param timeoutMs Optional timeout in milliseconds (default: 10000)
     * @example cy.assertUrlContains('/dashboard')
     */
    assertUrlContains(urlPath: string, timeoutMs?: number): Chainable<string>;
    
    /**
     * Assert that the count of elements matching a selector is as expected
     * @param elementLocator CSS selector for the elements to count
     * @param expectedCount Expected number of elements
     * @param timeoutMs Optional timeout in milliseconds (default: 10000)
     * @example cy.assertElementCount('.list-item', 5)
     */
    assertElementCount(elementLocator: string, expectedCount: number, timeoutMs?: number): Chainable<JQuery<HTMLElement>>;
    
    /**
     * Assert that an element has a CSS class
     * @param elementLocator CSS selector for the element to check
     * @param className CSS class name that should be present
     * @param timeoutMs Optional timeout in milliseconds (default: 10000)
     * @example cy.assertElementHasClass('.my-button', 'active')
     */
    assertElementHasClass(elementLocator: string, className: string, timeoutMs?: number): Chainable<JQuery<HTMLElement>>;
    
    /**
     * Custom command to test token refresh scenarios
     * @param options Configuration options for the token refresh test
     * @example cy.testTokenRefresh({ apiEndpoint: '/api/data', shouldRefreshSucceed: true })
     */
    testTokenRefresh(options?: {
      apiEndpoint?: string;
      shouldRefreshSucceed?: boolean;
      shouldRetrySucceed?: boolean;
      simulateDelay?: number;
    }): Chainable<void>;
  }
}
>>>>>>> REPLACE
</diff>
</replace_in_file>

---

**User:**

[replace_in_file for 'cypress/support/cypress.d.ts'] Result:
The content was successfully saved to cypress/support/cypress.d.ts.

Here is the full, updated content of the file that was saved:

<final_file_content path="cypress/support/cypress.d.ts">
declare namespace Cypress {
  interface Chainable {    
    /**
     * Check if an element exists on the page
     * @param elementLocator CSS selector for the element to check
     * @example cy.checkIfElementExists('.my-selector')
     */
    checkIfElementExists(elementLocator: string): Chainable<boolean>;
    
    /**
     * Assert that an element is visible on the page
     * @param elementLocator CSS selector for the element to check
     * @param timeoutMs Optional timeout in milliseconds (default: 10000)
     * @example cy.assertElementVisible('.my-selector')
     */
    assertElementVisible(elementLocator: string, timeoutMs?: number): Chainable<JQuery<HTMLElement>>;
    
    /**
     * Assert that an element is not visible on the page
     * @param elementLocator CSS selector for the element to check
     * @param timeoutMs Optional timeout in milliseconds (default: 10000)
     * @example cy.assertElementNotVisible('.my-selector')
     */
    assertElementNotVisible(elementLocator: string, timeoutMs?: number): Chainable<JQuery<HTMLElement>>;
    
    /**
     * Assert that an element contains specific text
     * @param elementLocator CSS selector for the element to check
     * @param text Text that should be present in the element
     * @param timeoutMs Optional timeout in milliseconds (default: 10000)
     * @example cy.assertElementContainsText('.my-selector', 'Expected text')
     */
    assertElementContainsText(elementLocator: string, text: string, timeoutMs?: number): Chainable<JQuery<HTMLElement>>;
    
    /**
     * Assert that an element has exact text
     * @param elementLocator CSS selector for the element to check
     * @param text Exact text that the element should have
     * @param timeoutMs Optional timeout in milliseconds (default: 10000)
     * @example cy.assertElementHasText('.my-selector', 'Exact text')
     */
    assertElementHasText(elementLocator: string, text: string, timeoutMs?: number): Chainable<JQuery<HTMLElement>>;
    
    /**
     * Assert that an element has a specific attribute value
     * @param elementLocator CSS selector for the element to check
     * @param attribute Attribute name to check
     * @param value Expected attribute value
     * @param timeoutMs Optional timeout in milliseconds (default: 10000)
     * @example cy.assertElementHasAttribute('.my-selector', 'data-testid', 'test-value')
     */
    assertElementHasAttribute(elementLocator: string, attribute: string, value: string, timeoutMs?: number): Chainable<JQuery<HTMLElement>>;
    
    /**
     * Assert that an element is enabled
     * @param elementLocator CSS selector for the element to check
     * @param timeoutMs Optional timeout in milliseconds (default: 10000)
     * @example cy.assertElementEnabled('.my-button')
     */
    assertElementEnabled(elementLocator: string, timeoutMs?: number): Chainable<JQuery<HTMLElement>>;
    
    /**
     * Assert that an element is disabled
     * @param elementLocator CSS selector for the element to check
     * @param timeoutMs Optional timeout in milliseconds (default: 10000)
     * @example cy.assertElementDisabled('.my-button')
     */
    assertElementDisabled(elementLocator: string, timeoutMs?: number): Chainable<JQuery<HTMLElement>>;
    
    /**
     * Assert that a URL contains a specific path
     * @param urlPath Path that should be included in the URL
     * @param timeoutMs Optional timeout in milliseconds (default: 10000)
     * @example cy.assertUrlContains('/dashboard')
     */
    assertUrlContains(urlPath: string, timeoutMs?: number): Chainable<string>;
    
    /**
     * Assert that the count of elements matching a selector is as expected
     * @param elementLocator CSS selector for the elements to count
     * @param expectedCount Expected number of elements
     * @param timeoutMs Optional timeout in milliseconds (default: 10000)
     * @example cy.assertElementCount('.list-item', 5)
     */
    assertElementCount(elementLocator: string, expectedCount: number, timeoutMs?: number): Chainable<JQuery<HTMLElement>>;
    
    /**
     * Assert that an element has a CSS class
     * @param elementLocator CSS selector for the element to check
     * @param className CSS class name that should be present
     * @param timeoutMs Optional timeout in milliseconds (default: 10000)
     * @example cy.assertElementHasClass('.my-button', 'active')
     */
    assertElementHasClass(elementLocator: string, className: string, timeoutMs?: number): Chainable<JQuery<HTMLElement>>;
    
    /**
     * Custom command to test token refresh scenarios
     * @param options Configuration options for the token refresh test
     * @example cy.testTokenRefresh({ apiEndpoint: '/api/data', shouldRefreshSucceed: true })
     */
    testTokenRefresh(options?: {
      apiEndpoint?: string;
      shouldRefreshSucceed?: boolean;
      shouldRetrySucceed?: boolean;
      simulateDelay?: number;
    }): Chainable<void>;
  }
}

</final_file_content>

IMPORTANT: For any future changes to this file, use the final_file_content shown above as your reference. This content reflects the current state of the file, including any auto-formatting (e.g., if you used single quotes but the formatter converted them to double quotes). Always base your SEARCH/REPLACE operations on this final version to ensure accuracy.


<environment_details>
# VSCode Visible Files
cypress/support/cypress.d.ts

# VSCode Open Tabs
config/email.config.js
sendFailedTestsReport.js
README_EmailReporter.md
cypress/e2e/features/token-refresh.feature
cypress/support/token-refresh.ts
cypress/support/e2e.ts
cypress/e2e/step-definitions/token-refresh.cy.ts
.husky/pre-commit
package.json
cypress/scripts/tag-tests.ts
docs/test-tagging-strategy.md
cypress/support/commands.ts
cypress/support/cypress.d.ts

# Recently Modified Files
These files have been modified since you last accessed them (file was just edited so you may need to re-read it before editing):
cypress/support/cypress.d.ts

# Current Time
5/12/2025, 8:37:40 PM (Asia/Calcutta, UTC+5.5:00)

# Current Mode
ACT MODE
</environment_details>

---

**Assistant:**

Now I'll create a simple example file to demonstrate how to use these custom UI element assertion methods in a step definition. This will serve as documentation for the team on how to use the new reusable assertion functions.

<write_to_file>
<path>cypress/docs/ui-assertion-examples.md</path>
<content># UI Element Assertion Methods

This document provides examples of how to use the custom UI element assertion methods that have been implemented in the project.

## Available Assertion Methods

The following custom assertion methods are available for validating UI elements:

### Basic Element Checks

| Method | Description | Example |
|--------|-------------|---------|
| `checkIfElementExists` | Checks if an element exists on the page | `cy.checkIfElementExists('.my-selector')` |
| `assertElementVisible` | Asserts that an element is visible | `cy.assertElementVisible('.my-selector')` |
| `assertElementNotVisible` | Asserts that an element is not visible | `cy.assertElementNotVisible('.my-selector')` |
| `assertElementCount` | Asserts the count of elements matching a selector | `cy.assertElementCount('.list-item', 5)` |

### Text Validation

| Method | Description | Example |
|--------|-------------|---------|
| `assertElementContainsText` | Asserts that an element contains specific text | `cy.assertElementContainsText('.notification', 'Success')` |
| `assertElementHasText` | Asserts that an element has exact text | `cy.assertElementHasText('.header', 'Welcome')` |

### Attribute and State Validation

| Method | Description | Example |
|--------|-------------|---------|
| `assertElementHasAttribute` | Asserts that an element has a specific attribute value | `cy.assertElementHasAttribute('.link', 'href', '/home')` |
| `assertElementHasClass` | Asserts that an element has a CSS class | `cy.assertElementHasClass('.button', 'active')` |
| `assertElementEnabled` | Asserts that an element is enabled | `cy.assertElementEnabled('.submit-button')` |
| `assertElementDisabled` | Asserts that an element is disabled | `cy.assertElementDisabled('.inactive-button')` |

### Navigation Validation

| Method | Description | Example |
|--------|-------------|---------|
| `assertUrlContains` | Asserts that the URL contains a specific path | `cy.assertUrlContains('/dashboard')` |

## Example Usage in Step Definitions

Below is an example of how to use these assertions in a step definition file:

```typescript
import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Then('I should see the welcome message', () => {
  cy.assertElementVisible('.welcome-message');
  cy.assertElementContainsText('.welcome-message', 'Welcome to the application');
});

Then('the submit button should be {string}', (state: string) => {
  if (state === 'enabled') {
    cy.assertElementEnabled('#submit-button');
  } else if (state === 'disabled') {
    cy.assertElementDisabled('#submit-button');
  }
});

Then('I should see {int} items in the list', (count: number) => {
  cy.assertElementCount('.list-item', count);
});

Then('I should be on the dashboard page', () => {
  cy.assertUrlContains('/dashboard');
});

Then('the success notification should appear', () => {
  cy.assertElementVisible('.notification');
  cy.assertElementHasClass('.notification', 'success');
  cy.assertElementContainsText('.notification', 'Operation completed successfully');
});
```

## Benefits of Using These Custom Assertions

1. **Readability**: Makes test code more readable and expressive
2. **Maintainability**: Centralizes common UI validation logic
3. **Reusability**: Allows reuse of common assertions across tests
4. **Consistency**: Ensures consistent approach to UI validation
5. **Timeout Handling**: All assertions include configurable timeout parameters

## Custom Timeouts

All assertion methods accept an optional timeout parameter (in milliseconds). By default, it's set to 10000ms (10 seconds):

```typescript
// Using default timeout (10000ms)
cy.assertElementVisible('.slow-loading-element');

// Using custom timeout (30000ms)
cy.assertElementVisible('.very-slow-loading-element', 30000);
```
</content>
</write_to_file>

---

**User:**

[write_to_file for 'cypress/docs/ui-assertion-examples.md'] Result:
The content was successfully saved to cypress/docs/ui-assertion-examples.md.

Here is the full, updated content of the file that was saved:

<final_file_content path="cypress/docs/ui-assertion-examples.md">
# UI Element Assertion Methods

This document provides examples of how to use the custom UI element assertion methods that have been implemented in the project.

## Available Assertion Methods

The following custom assertion methods are available for validating UI elements:

### Basic Element Checks

| Method | Description | Example |
|--------|-------------|---------|
| `checkIfElementExists` | Checks if an element exists on the page | `cy.checkIfElementExists('.my-selector')` |
| `assertElementVisible` | Asserts that an element is visible | `cy.assertElementVisible('.my-selector')` |
| `assertElementNotVisible` | Asserts that an element is not visible | `cy.assertElementNotVisible('.my-selector')` |
| `assertElementCount` | Asserts the count of elements matching a selector | `cy.assertElementCount('.list-item', 5)` |

### Text Validation

| Method | Description | Example |
|--------|-------------|---------|
| `assertElementContainsText` | Asserts that an element contains specific text | `cy.assertElementContainsText('.notification', 'Success')` |
| `assertElementHasText` | Asserts that an element has exact text | `cy.assertElementHasText('.header', 'Welcome')` |

### Attribute and State Validation

| Method | Description | Example |
|--------|-------------|---------|
| `assertElementHasAttribute` | Asserts that an element has a specific attribute value | `cy.assertElementHasAttribute('.link', 'href', '/home')` |
| `assertElementHasClass` | Asserts that an element has a CSS class | `cy.assertElementHasClass('.button', 'active')` |
| `assertElementEnabled` | Asserts that an element is enabled | `cy.assertElementEnabled('.submit-button')` |
| `assertElementDisabled` | Asserts that an element is disabled | `cy.assertElementDisabled('.inactive-button')` |

### Navigation Validation

| Method | Description | Example |
|--------|-------------|---------|
| `assertUrlContains` | Asserts that the URL contains a specific path | `cy.assertUrlContains('/dashboard')` |

## Example Usage in Step Definitions

Below is an example of how to use these assertions in a step definition file:

```typescript
import { Given, When, Then } from '@badeball/cypress-cucumber-preprocessor';

Then('I should see the welcome message', () => {
  cy.assertElementVisible('.welcome-message');
  cy.assertElementContainsText('.welcome-message', 'Welcome to the application');
});

Then('the submit button should be {string}', (state: string) => {
  if (state === 'enabled') {
    cy.assertElementEnabled('#submit-button');
  } else if (state === 'disabled') {
    cy.assertElementDisabled('#submit-button');
  }
});

Then('I should see {int} items in the list', (count: number) => {
  cy.assertElementCount('.list-item', count);
});

Then('I should be on the dashboard page', () => {
  cy.assertUrlContains('/dashboard');
});

Then('the success notification should appear', () => {
  cy.assertElementVisible('.notification');
  cy.assertElementHasClass('.notification', 'success');
  cy.assertElementContainsText('.notification', 'Operation completed successfully');
});
```

## Benefits of Using These Custom Assertions

1. **Readability**: Makes test code more readable and expressive
2. **Maintainability**: Centralizes common UI validation logic
3. **Reusability**: Allows reuse of common assertions across tests
4. **Consistency**: Ensures consistent approach to UI validation
5. **Timeout Handling**: All assertions include configurable timeout parameters

## Custom Timeouts

All assertion methods accept an optional timeout parameter (in milliseconds). By default, it's set to 10000ms (10 seconds):

```typescript
// Using default timeout (10000ms)
cy.assertElementVisible('.slow-loading-element');

// Using custom timeout (30000ms)
cy.assertElementVisible('.very-slow-loading-element', 30000);

</final_file_content>

IMPORTANT: For any future changes to this file, use the final_file_content shown above as your reference. This content reflects the current state of the file, including any auto-formatting (e.g., if you used single quotes but the formatter converted them to double quotes). Always base your SEARCH/REPLACE operations on this final version to ensure accuracy.


<environment_details>
# VSCode Visible Files
cypress/docs/ui-assertion-examples.md

# VSCode Open Tabs
config/email.config.js
sendFailedTestsReport.js
README_EmailReporter.md
cypress/e2e/features/token-refresh.feature
cypress/support/token-refresh.ts
cypress/support/e2e.ts
cypress/e2e/step-definitions/token-refresh.cy.ts
.husky/pre-commit
package.json
cypress/scripts/tag-tests.ts
docs/test-tagging-strategy.md
cypress/support/commands.ts
cypress/support/cypress.d.ts
cypress/docs/ui-assertion-examples.md

# Current Time
5/12/2025, 8:38:13 PM (Asia/Calcutta, UTC+5.5:00)

# Current Mode
ACT MODE
</environment_details>

---

**Assistant:**

<attempt_completion>
<result>
I've successfully implemented custom UI element assertion methods in the Cypress project with BDD framework. Here's what I've accomplished:

1. Enhanced the `commands.ts` file with 10 reusable assertion methods for UI element validation:
   - Basic element checks: `assertElementVisible`, `assertElementNotVisible`, `assertElementCount`
   - Text validation: `assertElementContainsText`, `assertElementHasText`
   - Attribute and state validation: `assertElementHasAttribute`, `assertElementHasClass`, `assertElementEnabled`, `assertElementDisabled`
   - Navigation validation: `assertUrlContains`

2. Updated the `cypress.d.ts` file with proper TypeScript definitions for all custom methods, ensuring type safety and enabling code completion in your IDE.

3. Created documentation with examples in `cypress/docs/ui-assertion-examples.md` that shows:
   - Available methods with descriptions and examples
   - Example usage in step definition files
   - Benefits of using these custom assertions
   - How to use custom timeouts

These custom assertions will make your test code more readable, maintainable, and consistent across the project. They centralize common UI validation logic, eliminating the need to write the same assertion code repeatedly in different test files.

To use these assertions in your tests, simply call them as shown in the documentation, for example:
```typescript
cy.assertElementVisible('.dashboard-panel');
cy.assertElementContainsText('.user-greeting', 'Welcome');
```
</result>
</attempt_completion>

